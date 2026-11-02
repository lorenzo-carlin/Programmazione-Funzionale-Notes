"""Collapse lab solutions behind a collapsible block at build time.

Each lab exercise keeps its prompt visible and hides the answer under a
``??? success "Soluzione"`` block, so the site works as a self-test. The
Markdown source is untouched, which keeps the full solution visible on GitHub.
"""

from __future__ import annotations

import re

EXERCISE = re.compile(r'^!!! question "(?P<title>Esercizio[^"]*)"$')
TERMINATOR = re.compile(r'^(?:!!! question "Esercizio|#{1,6} |---\s*$|\[← )')

# Lines that belong to the exercise prompt are indented by four spaces; a
# non-blank line at column 0 starts the solution (usually a code fence).
INDENT = "    "


def _indent(lines: list[str]) -> list[str]:
    return [f"{INDENT}{line}" if line.strip() else "" for line in lines]


def _trim_trailing_blanks(lines: list[str]) -> list[str]:
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def convert(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    i = 0

    while i < len(lines):
        if not EXERCISE.match(lines[i]):
            out.append(lines[i])
            i += 1
            continue

        # Copy the prompt admonition: title plus its indented body.
        prompt: list[str] = [lines[i]]
        i += 1
        while i < len(lines):
            line = lines[i]
            if line.strip() and not line.startswith(INDENT):
                break
            prompt.append(line)
            i += 1
        out.extend(_trim_trailing_blanks(prompt))

        # Collect the solution: everything up to the next exercise, heading,
        # separator, or back-link, ignoring terminators inside code fences.
        while i < len(lines) and not lines[i].strip():
            i += 1
        start = i
        in_fence = False
        while i < len(lines):
            line = lines[i]
            if line.startswith("```"):
                in_fence = not in_fence
                i += 1
                continue
            if not in_fence and TERMINATOR.match(line):
                break
            i += 1
        solution = _trim_trailing_blanks(lines[start:i])

        if solution:
            out.append("")
            out.append('??? success "Soluzione"')
            out.append("")
            out.extend(_indent(solution))
        if i < len(lines):
            out.append("")

    return "\n".join(out) + "\n"


def on_page_markdown(markdown: str, page: object, **_: object) -> str:
    src = getattr(getattr(page, "file", None), "src_uri", "") or ""
    if not src.startswith("laboratori/"):
        return markdown
    return convert(markdown)
