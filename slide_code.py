"""VS-style syntax-highlighted code blocks for slides and popups."""

from __future__ import annotations

import html
import re

_CODE_SNIPPETS: list[str] = []
_CODE_EXPECTED: dict[int, str] = {}
_CODE_MARKER = re.compile(r"<!--CODE:(\d+)-->")

_PY_KEYWORDS = {
    "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class",
    "continue", "def", "del", "elif", "else", "except", "finally", "for", "from",
    "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass",
    "raise", "return", "try", "while", "with", "yield",
}
_PY_BUILTINS = {
    "abs", "all", "any", "bin", "bool", "bytes", "chr", "dict", "enumerate", "filter",
    "float", "format", "frozenset", "getattr", "hasattr", "hash", "hex", "id", "input",
    "int", "isinstance", "issubclass", "iter", "len", "list", "map", "max", "min", "next",
    "object", "oct", "open", "ord", "pow", "print", "range", "repr", "reversed", "round",
    "set", "slice", "sorted", "str", "sum", "super", "tuple", "type", "zip",
}

_CS_KEYWORDS = {
    "abstract", "as", "async", "await", "base", "bool", "break", "byte", "case", "catch",
    "char", "checked", "class", "const", "continue", "decimal", "default", "delegate", "do",
    "double", "else", "enum", "event", "explicit", "extern", "false", "finally", "fixed",
    "float", "for", "foreach", "get", "goto", "if", "implicit", "in", "init", "int",
    "interface", "internal", "is", "lock", "long", "nameof", "namespace", "new", "nint",
    "nuint", "null", "object", "operator", "out", "override", "params", "private",
    "protected", "public", "readonly", "record", "ref", "required", "return", "sbyte",
    "sealed", "set", "short", "sizeof", "stackalloc", "static", "string", "struct", "switch",
    "this", "throw", "true", "try", "typeof", "uint", "ulong", "unchecked", "unsafe",
    "ushort", "using", "var", "virtual", "void", "volatile", "when", "while", "with", "yield",
}
_CS_TYPE_INTRO = {
    "class", "interface", "struct", "enum", "record", "new", "is", "as", "typeof",
}
_CS_BUILTIN_TYPES = {
    "bool", "byte", "char", "decimal", "double", "float", "int", "long", "nint", "nuint",
    "object", "sbyte", "short", "string", "uint", "ulong", "ushort", "void", "var",
}
_CS_LOOKS_LIKE = re.compile(
    r"(?m)^\s*(public|private|internal|protected|static)\s+"
    r"(class|interface|async|static|override|void|readonly|sealed)"
    r"|^\s*(public|private|internal)\s+interface\b"
    r"|\bbuilder\.Services\."
)


def _span(cls: str, text: str) -> str:
    return f'<span class="{cls}">{html.escape(text)}</span>'


def highlight_python_line(line: str) -> str:
    out: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        ch = line[i]
        if ch == "#":
            out.append(_span("t-cm", line[i:]))
            break
        if ch in "\"'":
            q = ch
            j = i + 1
            while j < n:
                if line[j] == "\\":
                    j += 2
                    continue
                if line[j] == q:
                    j += 1
                    break
                j += 1
            out.append(_span("t-str", line[i:j]))
            i = j
            continue
        if ch.isdigit() and (i == 0 or not (line[i - 1].isalnum() or line[i - 1] == "_")):
            j = i
            while j < n and (line[j].isdigit() or line[j] in "._"):
                j += 1
            out.append(_span("t-num", line[i:j]))
            i = j
            continue
        if ch.isalpha() or ch == "_":
            j = i
            while j < n and (line[j].isalnum() or line[j] == "_"):
                j += 1
            word = line[i:j]
            if word in _PY_KEYWORDS:
                cls = "t-kw"
            elif word in _PY_BUILTINS:
                cls = "t-bi"
            else:
                cls = "t-id"
            out.append(_span(cls, word))
            i = j
            continue
        out.append(_span("t-op", ch))
        i += 1
    return "".join(out) if out else "&#160;"


def _cs_skip_ws(line: str, i: int) -> int:
    n = len(line)
    while i < n and line[i] in " \t":
        i += 1
    return i


def _cs_after_generics(line: str, i: int) -> int:
    """Skip a `<...>` generic argument list, then whitespace."""
    n = len(line)
    i = _cs_skip_ws(line, i)
    if i >= n or line[i] != "<":
        return i
    depth = 0
    while i < n:
        if line[i] == "<":
            depth += 1
        elif line[i] == ">":
            depth -= 1
            i += 1
            if depth == 0:
                break
            continue
        i += 1
    return _cs_skip_ws(line, i)


def highlight_csharp_line(line: str) -> str:
    """VS 2022 Light: keyword blue, type teal, method gold, string maroon, comment green."""
    out: list[str] = []
    i = 0
    n = len(line)
    prev_was_dot = False
    prev_was_colon = False
    after_type_intro = False
    expect_name = False
    generic_depth = 0
    while i < n:
        if line[i:i + 2] == "//":
            out.append(_span("t-cm", line[i:]))
            break
        if line[i:i + 2] == "/*":
            end = line.find("*/", i + 2)
            if end < 0:
                out.append(_span("t-cm", line[i:]))
                break
            out.append(_span("t-cm", line[i : end + 2]))
            i = end + 2
            continue
        ch = line[i]
        if ch in "\"'":
            q = ch
            j = i + 1
            while j < n:
                if line[j] == "\\":
                    j += 2
                    continue
                if line[j] == q:
                    j += 1
                    break
                j += 1
            out.append(_span("t-str", line[i:j]))
            i = j
            prev_was_dot = False
            prev_was_colon = False
            after_type_intro = False
            continue
        if ch.isdigit() and (i == 0 or not (line[i - 1].isalnum() or line[i - 1] == "_")):
            j = i
            while j < n and (line[j].isdigit() or line[j] in "._"):
                j += 1
            out.append(_span("t-num", line[i:j]))
            i = j
            prev_was_dot = False
            prev_was_colon = False
            after_type_intro = False
            continue
        if ch.isalpha() or ch == "_":
            j = i
            while j < n and (line[j].isalnum() or line[j] == "_"):
                j += 1
            word = line[i:j]
            if word in _CS_KEYWORDS:
                cls = "t-kw"
                after_type_intro = word in _CS_TYPE_INTRO
                expect_name = word in _CS_BUILTIN_TYPES
                prev_was_dot = False
                prev_was_colon = False
            else:
                nxt = _cs_after_generics(line, j)
                is_call = nxt < n and line[nxt] == "("
                if generic_depth > 0:
                    cls = "t-type" if word[:1].isupper() else "t-id"
                elif after_type_intro or prev_was_colon:
                    cls = "t-type"
                    expect_name = True
                elif expect_name:
                    cls = "t-fn" if is_call else "t-id"
                    expect_name = False
                elif prev_was_dot:
                    cls = "t-fn" if is_call else "t-id"
                    expect_name = False
                elif is_call:
                    cls = "t-fn"
                    expect_name = False
                elif word[:1].isupper():
                    cls = "t-type"
                    expect_name = True
                else:
                    cls = "t-id"
                    expect_name = False
                after_type_intro = False
                prev_was_dot = False
                prev_was_colon = False
            out.append(_span(cls, word))
            i = j
            continue
        if ch == "<":
            generic_depth += 1
            prev_was_dot = False
        elif ch == ">" and generic_depth:
            generic_depth -= 1
            prev_was_dot = False
        elif ch == ".":
            prev_was_dot = True
            prev_was_colon = False
            after_type_intro = False
            expect_name = False
        elif ch == ":":
            prev_was_colon = True
            prev_was_dot = False
        elif not ch.isspace():
            prev_was_dot = False
            if ch not in "<,":
                prev_was_colon = False
                if ch not in "<>[]":
                    after_type_intro = False
        out.append(_span("t-op", ch))
        i += 1
    return "".join(out) if out else "&#160;"


def vs_editor(
    text: str,
    lang: str = "python",
    compact: bool = False,
    playground: bool = False,
    expected: str | None = None,
) -> str:
    highlight = highlight_csharp_line if lang == "csharp" else highlight_python_line
    rows = []
    for num, line in enumerate(text.splitlines(), 1):
        rows.append(
            f'<tr><td class="gutter">{num}</td><td class="src">{highlight(line)}</td></tr>'
        )
    if not rows:
        rows.append('<tr><td class="gutter">1</td><td class="src">&#160;</td></tr>')
    body = "\n".join(rows)
    compact_cls = " vs-editor-compact" if compact else ""
    highlighted = (
        f'<div class="vs-editor{compact_cls}"><table class="vs-code"><tbody>\n{body}\n</tbody></table></div>'
    )
    if not playground:
        return highlighted
    src = html.escape(text)
    if lang not in ("python", "csharp"):
        labels = {
            "typescript": "TypeScript",
            "javascript": "JavaScript",
            "sql": "SQL",
            "yaml": "YAML",
            "dockerfile": "Dockerfile",
        }
        label = labels.get(lang, lang.upper())
        exp = (expected or "").rstrip("\n")
        exp_attr = html.escape(exp, quote=True)
        exp_html = html.escape(exp) if exp else "(read the comments — this sample is not executed in the browser)"
        out_hidden = "" if exp else " hidden"
        return (
            f'<div class="code-playground" data-lang="{html.escape(lang)}">'
            '<div class="code-toolbar">'
            f'<span class="code-toolbar-label">Code editor ({html.escape(label)})</span>'
            '<button type="button" class="btn-run-py" onclick="showExpectedOutput(this)" title="Show expected notes">&#9654; Expected</button>'
            '<button type="button" class="btn-reset-py" onclick="resetPlayground(this)">Reset</button>'
            '<button type="button" class="btn-reset-py" onclick="copyPlayground(this)">Copy</button>'
            f'<span class="py-status">{html.escape(label)} sample — explain it, do not only read it</span>'
            "</div>"
            '<div class="py-resize-top" title="Drag up/down to resize editor height" role="separator" aria-orientation="horizontal"></div>'
            f'<textarea class="py-editor" spellcheck="false" data-lang="{html.escape(lang)}" data-expected="{exp_attr}">{src}</textarea>'
            f'<div class="py-output-label" style="font-size:11px;font-weight:700;padding:4px 10px;background:#f0fdf4;color:#166534;border-top:1px solid #bbf7d0">OUTPUT (expected)</div>'
            f'<pre class="py-output"{out_hidden} data-expected="1">{exp_html}</pre>'
            '<details class="py-highlight" open><summary>Syntax-colored view</summary>'
            '<div class="py-resize-top" title="Drag up/down to resize syntax view" role="separator" aria-orientation="horizontal"></div>'
            f"{highlighted}"
            "</details>"
            "</div>"
        )
    if lang == "python":
        # Editable + runnable panel (Pyodide wired in the HTML page)
        return (
            '<div class="code-playground" data-lang="python">'
            '<div class="code-toolbar">'
            '<span class="code-toolbar-label">Code editor</span>'
            '<button type="button" class="btn-run-py" onclick="runPlayground(this)">&#9654; Run</button>'
            '<button type="button" class="btn-reset-py" onclick="resetPlayground(this)">Reset</button>'
            '<span class="py-status"></span>'
            "</div>"
            '<div class="py-resize-top" title="Drag up/down to resize editor height" role="separator" aria-orientation="horizontal"></div>'
            f'<textarea class="py-editor" spellcheck="false">{src}</textarea>'
            '<pre class="py-output" hidden></pre>'
            '<details class="py-highlight" open><summary>Syntax-colored view</summary>'
            '<div class="py-resize-top" title="Drag up/down to resize syntax view" role="separator" aria-orientation="horizontal"></div>'
            f"{highlighted}"
            "</details>"
            "</div>"
        )
    # C#: Expected + live ▶ Run (Wandbox/Mono) + SharpLab fallback
    exp = (expected or "").rstrip("\n")
    exp_attr = html.escape(exp, quote=True)
    exp_html = html.escape(exp) if exp else "(no expected output yet — use ▶ Run for live result)"
    out_hidden = "" if exp else " hidden"
    return (
        '<div class="code-playground" data-lang="csharp">'
        '<div class="code-toolbar">'
        '<span class="code-toolbar-label">Code editor (C#)</span>'
        '<button type="button" class="btn-run-py" onclick="showExpectedOutput(this)" title="Show expected console output">&#9654; Expected</button>'
        '<button type="button" class="btn-run-py" style="background:#16a34a" onclick="runCsharpPlayground(this)" title="Compile &amp; run C# in browser (Wandbox/Mono)">&#9654; Run</button>'
        '<button type="button" class="btn-reset-py" onclick="openSharpLabDirect(this)" title="Copy code and open SharpLab">SharpLab &#8599;</button>'
        '<button type="button" class="btn-reset-py" onclick="resetPlayground(this)">Reset</button>'
        '<button type="button" class="btn-reset-py" onclick="copyPlayground(this)">Copy</button>'
        '<span class="py-status">Expected below · &#9654; Run = live execution</span>'
        "</div>"
        '<div class="py-resize-top" title="Drag up/down to resize editor height" role="separator" aria-orientation="horizontal"></div>'
        f'<textarea class="py-editor" spellcheck="false" data-lang="csharp" data-expected="{exp_attr}">{src}</textarea>'
        f'<div class="py-output-label" style="font-size:11px;font-weight:700;padding:4px 10px;background:#f0fdf4;color:#166534;border-top:1px solid #bbf7d0">OUTPUT (expected)</div>'
        f'<pre class="py-output"{out_hidden} data-expected="1">{exp_html}</pre>'
        '<details class="py-highlight" open><summary>Syntax-colored view</summary>'
        '<div class="py-resize-top" title="Drag up/down to resize syntax view" role="separator" aria-orientation="horizontal"></div>'
        f"{highlighted}"
        "</details>"
        "</div>"
    )


_STEP_PRE_RE = re.compile(r'<div class="step-pre">(.*?)</div>', re.DOTALL)
_EXISTING_MARK_RE = re.compile(r"<mark\b[^>]*>.*?</mark>", re.DOTALL | re.IGNORECASE)
_SECTION_LABEL_RE = re.compile(
    r"#\s*(?:INPUT|OUTPUT)\b(?:\s*\([^)]*\))?",
    re.IGNORECASE,
)
_HTTP_STATUS_RE = re.compile(
    r"HTTP\s+\d{3}(?:\s+Unprocessable Entity)?",
    re.IGNORECASE,
)
_FIELD_CALL_RE = re.compile(r"Field\([^)]*\)")
_DUNDER_RE = re.compile(r"__\w+__")

# Teaching-critical names highlighted in step-pre samples (lavender .hl-key).
_STEP_PRE_IMPORTANT = _PY_KEYWORDS | {
    # Builtins often taught in this deck
    "print", "len", "range", "enumerate", "zip", "map", "filter", "sorted",
    "isinstance", "issubclass", "super", "property", "classmethod", "staticmethod",
    "open", "type", "id", "hasattr", "getattr", "setattr", "vars", "dir",
    "list", "dict", "set", "tuple", "frozenset", "object", "str", "int", "float",
    "bool", "bytes", "bytearray", "memoryview", "sum", "min", "max", "any", "all",
    "next", "iter", "slice", "abs", "round", "repr", "format", "input",
    "copy", "deepcopy",
    # Exceptions
    "Exception", "BaseException", "StopIteration", "GeneratorExit",
    "TypeError", "ValueError", "KeyError", "AttributeError", "IndexError",
    "NameError", "RuntimeError", "ImportError", "FileNotFoundError",
    "AssertionError", "TabError", "SyntaxError",
    # Memory / GC / weakref (slide discussion)
    "gc", "collect", "getrefcount", "sys", "weakref", "ref", "proxy", "finalize",
    "soft_ref", "refcount",
    # APIs / types used across slides
    "BaseModel", "Field", "field_validator", "model_validator", "model_validate",
    "model_dump", "ValidationError", "ConfigDict", "frozen", "Pydantic",
    "greater_than_equal", "less_than_equal", "value_error", "missing",
    "dataclass", "field", "NamedTuple", "TypedDict", "Protocol", "ABC",
    "abstractmethod", "override",
    "Decimal", "Path", "PurePath", "quantize", "getcontext",
    "asyncio", "create_task", "gather", "run",
    "pytest", "unittest", "Mock", "patch", "MagicMock", "raises", "assertEqual",
    "FastAPI", "APIRouter", "Depends", "HTTPException",
    "Session", "select", "commit", "refresh", "query",
    "deque", "maxlen", "popleft", "Counter", "defaultdict", "OrderedDict",
    "namedtuple", "ChainMap", "UserDict",
    "lru_cache", "cache", "partial", "wraps", "functools", "itertools",
    "groupby", "chain", "islice",
    "Generator", "Iterator", "Iterable", "Callable", "Optional", "Union", "Any",
    "Self", "ClassVar", "Final", "Literal", "Annotated",
    "send", "throw", "close",
    "json", "loads", "dumps", "csv", "DictReader",
    "threading", "Lock", "Thread", "Process", "Pool", "Queue", "GIL",
    "pip", "venv", "mypy", "pyright",
}


def _hl_key(text: str) -> str:
    return f'<mark class="hl-key">{text}</mark>'


def _hl_cm(text: str) -> str:
    """Comment text in VS comment green (#008000 via .t-cm)."""
    return f'<span class="t-cm">{text}</span>'


def _mark_important_plain(text: str) -> str:
    """Wrap teaching keywords / labels in plain (non-mark) text with hl-key."""
    out: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]

        # Comments: # INPUT / # OUTPUT keep lavender labels; all other # text → green
        if ch == "#":
            line_end = text.find("\n", i)
            if line_end < 0:
                line_end = n
            line = text[i:line_end]
            label = _SECTION_LABEL_RE.match(line)
            if label:
                out.append(_hl_key(label.group(0)))
                rest = line[label.end() :]
                if rest:
                    out.append(_hl_cm(rest))
            else:
                out.append(_hl_cm(line))
            i = line_end
            continue

        # Strings — leave untouched so words inside quotes stay plain
        if ch in "\"'":
            q = ch
            j = i + 1
            # Byte / f / r / fr prefixes already consumed as identifiers
            while j < n:
                if text[j] == "\\":
                    j += 2
                    continue
                if text[j] == q:
                    j += 1
                    break
                j += 1
            out.append(text[i:j])
            i = j
            continue

        http = _HTTP_STATUS_RE.match(text, i)
        if http:
            out.append(_hl_key(http.group(0)))
            i = http.end()
            continue

        field = _FIELD_CALL_RE.match(text, i)
        if field:
            out.append(_hl_key(field.group(0)))
            i = field.end()
            continue

        dunder = _DUNDER_RE.match(text, i)
        if dunder:
            out.append(_hl_key(dunder.group(0)))
            i = dunder.end()
            continue

        if ch == "@" and i + 1 < n and (text[i + 1].isalpha() or text[i + 1] == "_"):
            j = i + 1
            while j < n and (text[j].isalnum() or text[j] == "_"):
                j += 1
            out.append(_hl_key(text[i:j]))
            i = j
            continue

        if ch.isalpha() or ch == "_":
            j = i
            while j < n and (text[j].isalnum() or text[j] == "_"):
                j += 1
            word = text[i:j]
            if word in _STEP_PRE_IMPORTANT:
                out.append(_hl_key(word))
            else:
                out.append(word)
            i = j
            continue

        out.append(ch)
        i += 1
    return "".join(out)


def mark_important_in_text(text: str) -> str:
    """Highlight important tokens; preserve any existing <mark>...</mark> spans."""
    parts: list[str] = []
    pos = 0
    for m in _EXISTING_MARK_RE.finditer(text):
        if m.start() > pos:
            parts.append(_mark_important_plain(text[pos : m.start()]))
        parts.append(m.group(0))
        pos = m.end()
    if pos < len(text):
        parts.append(_mark_important_plain(text[pos:]))
    return "".join(parts)


def mark_important_in_step_pres(html_text: str) -> str:
    """Add lavender keyword highlights + green comments inside every .step-pre block."""

    def _repl(match: re.Match[str]) -> str:
        return f'<div class="step-pre">{mark_important_in_text(match.group(1))}</div>'

    return _STEP_PRE_RE.sub(_repl, html_text)


def looks_like_csharp(text: str) -> bool:
    return bool(_CS_LOOKS_LIKE.search(text or ""))


def highlight_step_pres(html_text: str, lang: str = "python") -> str:
    """Replace plain <div class="step-pre">...</div> blocks with VS-colored editors."""

    def _repl(match: re.Match[str]) -> str:
        code_text = html.unescape(match.group(1)).rstrip("\n")
        return vs_editor(code_text + "\n" if code_text else "", lang=lang, compact=True)

    return _STEP_PRE_RE.sub(_repl, html_text)


_STEP_PRE_OPEN_RE = re.compile(
    r'<div class="step-pre"(?P<attrs>[^>]*)>(?P<body>.*?)</div>',
    re.DOTALL,
)


def highlight_csharp_step_pres(html_text: str) -> str:
    """Turn C# .step-pre samples into VS 2022 Light editors (line numbers + colors)."""

    def _repl(match: re.Match[str]) -> str:
        attrs = match.group("attrs") or ""
        body = match.group("body")
        forced = 'data-lang="csharp"' in attrs.replace("'", '"')
        code_text = html.unescape(body).rstrip("\n")
        if not forced and not looks_like_csharp(code_text):
            return match.group(0)
        return vs_editor(code_text + "\n" if code_text else "", lang="csharp", compact=True)

    return _STEP_PRE_OPEN_RE.sub(_repl, html_text)


def code(text: str, *, expected: str | None = None) -> str:
    idx = len(_CODE_SNIPPETS)
    _CODE_SNIPPETS.append(text)
    if expected is not None:
        _CODE_EXPECTED[idx] = expected
    return f"<!--CODE:{idx}-->"


def code_table(idx: int, lang: str = "python") -> str:
    return vs_editor(
        _CODE_SNIPPETS[idx],
        lang=lang,
        playground=True,
        expected=_CODE_EXPECTED.get(idx),
    )


def split_learn(learn: str, lang: str = "python") -> tuple[str, str]:
    notes_parts: list[str] = []
    code_parts: list[str] = []
    chunks = _CODE_MARKER.split(learn)
    for i, chunk in enumerate(chunks):
        if i % 2 == 0:
            notes_parts.append(chunk)
        else:
            code_parts.append(code_table(int(chunk), lang=lang))
    return "".join(notes_parts), "\n".join(code_parts)


highlight_line = highlight_python_line
