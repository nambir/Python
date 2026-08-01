"""VS-style syntax-highlighted code blocks for slides and popups."""

from __future__ import annotations

import html
import re

_CODE_SNIPPETS: list[str] = []
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
    "abstract", "as", "base", "bool", "break", "byte", "case", "catch", "char", "checked",
    "class", "const", "continue", "decimal", "default", "delegate", "do", "double", "else",
    "enum", "event", "explicit", "extern", "false", "finally", "fixed", "float", "for",
    "foreach", "goto", "if", "implicit", "in", "int", "interface", "internal", "is", "lock",
    "long", "namespace", "new", "null", "object", "operator", "out", "override", "params",
    "private", "protected", "public", "readonly", "record", "ref", "return", "sbyte", "sealed",
    "short", "sizeof", "stackalloc", "static", "string", "struct", "switch", "this", "throw",
    "true", "try", "typeof", "uint", "ulong", "unchecked", "unsafe", "ushort", "using",
    "var", "virtual", "void", "volatile", "while",
}
_CS_TYPES = {
    "List", "Dictionary", "IEnumerable", "Task", "Action", "Func", "String", "Int32",
    "Boolean", "Object", "Console", "Exception",
}


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


def highlight_csharp_line(line: str) -> str:
    out: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        if line[i:i + 2] == "//":
            out.append(_span("t-cm", line[i:]))
            break
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
            if word in _CS_KEYWORDS:
                cls = "t-kw"
            elif word in _CS_TYPES:
                cls = "t-bi"
            else:
                cls = "t-id"
            out.append(_span(cls, word))
            i = j
            continue
        out.append(_span("t-op", ch))
        i += 1
    return "".join(out) if out else "&#160;"


def vs_editor(text: str, lang: str = "python", compact: bool = False, playground: bool = False) -> str:
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
    if not playground or lang != "python":
        return highlighted
    # Editable + runnable panel (Pyodide wired in the HTML page)
    src = html.escape(text)
    return (
        '<div class="code-playground">'
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


def highlight_step_pres(html_text: str, lang: str = "python") -> str:
    """Replace plain <div class="step-pre">...</div> blocks with VS-colored editors."""

    def _repl(match: re.Match[str]) -> str:
        code_text = html.unescape(match.group(1)).rstrip("\n")
        return vs_editor(code_text + "\n" if code_text else "", lang=lang, compact=True)

    return _STEP_PRE_RE.sub(_repl, html_text)


def code(text: str) -> str:
    idx = len(_CODE_SNIPPETS)
    _CODE_SNIPPETS.append(text)
    return f"<!--CODE:{idx}-->"


def code_table(idx: int) -> str:
    return vs_editor(_CODE_SNIPPETS[idx], lang="python", playground=True)


def split_learn(learn: str) -> tuple[str, str]:
    notes_parts: list[str] = []
    code_parts: list[str] = []
    chunks = _CODE_MARKER.split(learn)
    for i, chunk in enumerate(chunks):
        if i % 2 == 0:
            notes_parts.append(chunk)
        else:
            code_parts.append(code_table(int(chunk)))
    return "".join(notes_parts), "\n".join(code_parts)


highlight_line = highlight_python_line
