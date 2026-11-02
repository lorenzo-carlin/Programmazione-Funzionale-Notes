# AGENTS.md

## Repo at a glance

- Italian university notes for **Programmazione Funzionale** (A.A. 2025/2026), Standard ML.
- Content repo only: no app, package manifest, build, tests, linter, CI, or codegen. There is no `mkdocs.yml` yet; see `ROADMAP.md` for the planned site.
- All content is flat in `lezioni/`: 19 lesson/lab pages (`01`–`19`) plus `PROGRAMMAZIONE FUNZIONALE.md`, a cover/TOC.
- `Dispensa.pdf` is a 130-page, 5.1 MB snapshot compiled 2026-06-18. No script generates it; editing Markdown makes the PDF stale.
- `ROADMAP.md` is the phased plan. Work through its phases in order.

## Content map

- Theory: `01`, `02`, `04`, `06`, `08`, `10`, `12`, `14`, `16`, `18`. Labs: `03`, `05`, `07`, `09`, `11`, `13`, `15`, `17`, `19`.
- `07. Laboratorio 3 + Pattern Matching.md` mixes lab exercises with the first half of pattern-matching theory; `08` continues it. Do not assume a file is purely theory or purely lab.
- `lezioni/lezione-01.md` is the only file not named `NN. Titolo.md`. It starts with `#`; most other pages start at `##`, so do not assume a top-level heading exists.
- Filenames contain spaces and `+`; quote paths in shell commands. README link destinations are wrapped in `<...>` for this reason.

## Conventions

- Keep prose in Italian; do not translate the notes. Preserve SML keywords and identifiers. Math uses `$...$` / `$$...$$`.
- Callouts use Obsidian syntax: `>[!esercizio]`, `>[!esempio]` (also `[!Esempio]`), `>[!osservazione]`, `>[!warning]`, `>[!teorema]`. GitHub renders them as plain blockquotes; Phase 2 converts them, so do not convert ad hoc.
- `sml` fences are REPL transcripts with `>` prompts and `(* val it = ... *)` expected output, not standalone runnable programs. Fence languages seen: `sml`, `C++` (capitalized), `txt`, and bare fences.
- Only `lezioni/lezione-01.md` has a back-link to the README right now.

## Editing guidance

- No build or verification command exists. Check Markdown paths and links with a one-off script; do not invent a toolchain.
- Keep the README theory/lab tables in sync with `lezioni/` when renaming or adding pages.
- Use `git mv` for renames and update every relative link; do not bulk-rename without checking the README.
- There is no site/Pages setup yet. Do not assume `mkdocs.yml`, workflows, or a deployed site exists.
- Do not mix file moves with content edits; one roadmap phase per commit.
