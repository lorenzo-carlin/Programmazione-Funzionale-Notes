"""Turn the notes' portable callouts into Material admonitions at build time.

The Markdown source keeps bold blockquotes (``> **Esempio**``) so that the
notes render correctly on GitHub, where Material admonitions do not exist.
MkDocs runs this hook before parsing a page and rewrites each callout as an
``!!! type "Title"`` admonition, so the site gets the proper Material styling
without changing the source that GitHub reads.
"""

from __future__ import annotations

import re

LABEL = re.compile(r"^> \*\*(?P<label>.+?)\*\*$")

# Order matters: longer/more specific prefixes first.
CALLOUT_TYPES: tuple[tuple[str, str], ...] = (
    ("Esercizio", "question"),
    ("Esempi", "example"),
    ("Esempio", "example"),
    ("Osservazione", "note"),
    ("⚠️ Attenzione", "warning"),
    ("Teorema", "abstract"),
)

WARNING_PREFIX = "⚠️ "


def _admonition_type(label: str) -> str:
    for prefix, kind in CALLOUT_TYPES:
        if label.startswith(prefix):
            return kind
    raise ValueError(f"unknown callout label: {label!r}")


def _title(label: str, kind: str) -> str:
    if kind == "warning" and label.startswith(WARNING_PREFIX):
        # The admonition already shows a warning icon.
        return label[len(WARNING_PREFIX) :]
    return label


def _render(label: str, body: list[str]) -> list[str]:
    kind = _admonition_type(label)
    lines = [f'!!! {kind} "{_title(label, kind)}"']
    for line in body:
        lines.append(f"    {line}" if line else "")
    return lines


def convert(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    in_fence = False
    i = 0

    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
            in_fence = not in_fence
            out.append(line.rstrip())
            i += 1
            continue

        match = None if in_fence else LABEL.match(line)
        if not match:
            out.append(line.rstrip())
            i += 1
            continue

        body: list[str] = []
        j = i + 1
        while j < len(lines) and lines[j].startswith(">"):
            content = lines[j][1:]
            body.append(content[1:] if content.startswith(" ") else content)
            j += 1

        out.extend(_render(match.group("label"), body))
        i = j

    return "\n".join(out) + "\n"


def on_page_markdown(markdown: str, **_: object) -> str:
    return convert(markdown)
