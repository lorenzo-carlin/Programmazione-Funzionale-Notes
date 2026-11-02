# AGENTS.md

## Repo at a glance

- Italian university notes for **Programmazione Funzionale** (A.A. 2025/2026), Standard ML.
- Content repo only: no app, package manifest, build, tests, linter, CI, or codegen. There is no `mkdocs.yml` yet; see `ROADMAP.md` for the planned site.
- Content lives in `docs/`: `index.md` (full TOC), `teoria/` (11 pages), `laboratori/` (9 pages). There is no longer a `lezioni/` directory.
- `Dispensa.pdf` is a 130-page, 5.1 MB snapshot compiled 2026-06-18. No script generates it; editing Markdown makes the PDF stale.
- `ROADMAP.md` is the phased plan. Work through its phases in order.

## Content map

- Theory: `01`, `02`, `04`, `06`, `07`, `08`, `10`, `12`, `14`, `16`, `18` under `docs/teoria/`.
- Labs: `03`, `05`, `07`, `09`, `11`, `13`, `15`, `17`, `19` under `docs/laboratori/`.
- `07` is split: `docs/teoria/07-pattern-matching.md` holds the first part of the pattern-matching theory; `docs/laboratori/07-laboratorio-3.md` holds the lab exercises. The two pages cross-link. `08` continues the theory.
- `docs/teoria/01-espressioni-e-tipi.md` is the only content page with an H1 (`docs/index.md` also has one; the other pages start at `##`) and the only page with a back-link to `docs/index.md`.
- Page titles come from the MkDocs `nav` in Phase 2, not from front matter. Do not add `#` headings to pages that intentionally start at `##`.

## Conventions

- Keep prose in Italian; do not translate the notes. Preserve SML keywords and identifiers. Math uses `$...$` / `$$...$$`.
- Callouts use Obsidian syntax: `>[!esercizio]`, `>[!esempio]` (also `[!Esempio]`), `>[!osservazione]`, `>[!warning]`, `>[!teorema]`. GitHub renders them as plain blockquotes; Phase 2 converts them, so do not convert ad hoc.
- `sml` fences are REPL transcripts with `>` prompts and `(* val it = ... *)` expected output, not standalone runnable programs. Fence languages seen: `sml`, `C++` (capitalized), `txt`, and bare fences.

## Editing guidance

- No build or verification command exists. Check Markdown paths and links with a one-off script; do not invent a toolchain.
- Keep `README.md`, `docs/index.md`, and the actual `docs/` tree in sync when adding, renaming, or moving pages.
- Use `git mv` for renames and update every relative link; do not bulk-rename without checking the link checker.
- There is no site/Pages setup yet. Do not assume `mkdocs.yml`, workflows, or a deployed site exists.
- Do not mix file moves with content edits; one roadmap phase per commit.
