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
        f'<textarea class="py-editor" spellcheck="false">{src}</textarea>'
        '<pre class="py-output" hidden></pre>'
        '<details class="py-highlight"><summary>Syntax-colored view</summary>'
        f"{highlighted}"
        "</details>"
        "</div>"
    )


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
