# Roadmap

Phased plan to turn this repo from a flat Markdown dump into a maintainable, browsable study resource.

**Rules for every phase**

- One phase = one focused commit/PR. Do not mix content edits with file moves.
- Finish and commit a phase before starting the next one.
- Keep the notes in Italian; keep SML keywords and identifiers untouched.
- Read `AGENTS.md` first. Never run `git clean`, `git checkout -- .`, or `git restore .` here.
- Update `AGENTS.md` at the end of any phase that changes paths, commands, or tooling.

**Status**

| Phase | Scope | Status |
| :---: | :--- | :--- |
| 0 | Commit migration, fix README, repo hygiene | Done (2026-11-02) |
| 1 | Restructure content for a site | Done (2026-11-02) |
| 1.5 | Content and formatting audit | Done (2026-11-02) |
| 2 | MkDocs Material site + GitHub Pages | Not started |
| 3 | Interactive study features | Not started |
| 4 | Automation, PDF pipeline, polish | Not started |

---

## Phase 0 — Make the repo truthful and stable

**Goal:** a clean working tree, a README that matches reality, and basic repo hygiene. Nothing is built or moved yet.

### Tasks

- [x] Commit the `notes/` → `lezioni/` migration, preserving rename history:
  - `git add -A -- notes lezioni`
  - confirm `git status` shows renames (`R`), not delete + add
  - commit, e.g. `Move notes/ to lezioni/`
- [x] Rewrite the README "Struttura della Repository" tree. It currently shows `01-espressioni-tipi.md`, `02-type-system.md`, `laboratori/lab-*.md`: none of these exist. Show the real layout (`lezioni/`, `Dispensa.pdf`, `README.md`, `AGENTS.md`, `ROADMAP.md`).
- [x] Fix the theory table. It links to `lezioni/lezione-02.md` … `lezione-05.md`, which do not exist. Map each topic to its real file (`02. Type system…`, `04. Regole di scope…`, `06. Astrazione…`, `08. Patterns…`, and so on). Include all 10 theory topics, or replace the table with a compact grouped index.
- [x] Fix the lab table. There is no `laboratori/` directory; point to the real `03`, `05`, `07`, `09`, `11`, `13`, `15`, `17`, `19` files.
- [x] Fix "Come Navigare la Repo": it claims every page has a backlink, but only `lezioni/lezione-01.md` does. Either soften the claim now or add the backlinks in Phase 3.
- [x] Add `.gitignore`: `.DS_Store`, `Thumbs.db`, `.obsidian/workspace*`, `site/`, `.venv/`, `__pycache__/`.
- [x] Add `.gitattributes`: `* text=auto eol=lf` and `*.pdf binary`.
- [x] Optional: `.editorconfig` (UTF-8, LF, final newline) for Markdown.
- [x] Run a one-off link check over `README.md` and `lezioni/*.md`.

**Done when:** `git status` is clean, every README link resolves, and no file in the repo is described incorrectly.

**Completed:** 2026-11-02. Rename commit `dae42da`; 23 relative links checked, all resolve.

---

## Phase 1 — Restructure content

**Goal:** a predictable layout that a site generator and readers can navigate, without rewriting the notes.

**Decision — keep the course session numbers.** Renaming all 19 files to sequential `01…19` adds churn and breaks links for no real gain. Keep `NN` = original lesson/lab number and split by type. Gaps in the theory sequence (`01, 02, 04, 06…`) are correct: odd numbers are labs.

### Proposed layout

```text
docs/
├── index.md                  # full TOC
├── teoria/
│   ├── 01-espressioni-e-tipi.md
│   ├── 02-type-system.md
│   ├── 04-regole-di-scope.md
│   ├── 06-astrazione-e-ricorsione.md
│   ├── 07-pattern-matching.md
│   ├── 08-patterns-environment.md
│   ├── 10-io-eccezioni-polimorfismo.md
│   ├── 12-ordine-superiore-curried.md
│   ├── 14-data-types.md
│   ├── 16-data-types-astratti.md
│   └── 18-lambda-calcolo.md
└── laboratori/
    ├── 03-laboratorio-1.md
    ├── 05-laboratorio-2.md
    ├── 07-laboratorio-3.md
    ├── 09-laboratorio-4.md
    ├── 11-laboratorio-5.md
    ├── 13-laboratorio-6.md
    ├── 15-laboratorio-7.md
    ├── 17-laboratorio-8.md
    └── 19-laboratorio-9.md

Dispensa.pdf                  # repo root, linked from docs/index.md
```

### Tasks

- [x] Decide whether `Dispensa.pdf` stays at the repo root or moves to `docs/assets/`. It stays at the root; `docs/index.md` links to `../Dispensa.pdf`.
- [x] Create `docs/` and move files with `git mv` (only after Phase 0 is committed).
- [x] Slugs: lowercase, hyphens, no spaces or `+`. Keep the `NN-` prefix.
- [x] Create `docs/index.md` from the 42-line cover/TOC. Keep it short: title, course, PDF link, theory list, lab list.
- [x] Split `07. Laboratorio 3 + Pattern Matching.md`: lab exercises stay in `laboratori/07-laboratorio-3.md`; the pattern-matching theory goes to `teoria/07-pattern-matching.md`. Do not duplicate content; move it.
- [x] Point `README.md` at the site/PDF and keep it short. It should not duplicate the full TOC.
- [x] Fix every relative link after the move (README, index, in-page links).
- [x] Titles: rely on the MkDocs `nav` in Phase 2. Most pages intentionally start at `##`, so no `#` headings or front matter were added.

**Done when:** 21 content pages (11 theory + 9 labs + index) are reachable, every relative link resolves, and `git log --follow` still works on moved files.

**Completed:** 2026-11-02. 21 pages in `docs/`; `07` split into theory + lab; 30 relative links checked, all resolve. Lesson/lab pages keep history across the move; `docs/index.md` is a rewrite of the cover, so Git tracks it as a new file.

---

## Phase 1.5 — Content and formatting audit

**Goal:** make the existing notes correct and consistent before a site generator consumes them. This is a cleanup phase: no restructuring, no new features, no renumbering.

**Scope:** all 11 theory pages and all 9 lab pages under `docs/`.

### Tasks

- [x] Fix Italian grammar, agreement, typos, and garbled words introduced by the Obsidian migration (e.g. `foglia`/`foglie`, `cuo`/`cui`, `cosa`/`coda`, `coppa`/`coppia`, `String`/`string`).
- [x] Correct Standard ML concepts and transcripts:
  - [x] type inference and equality types (`'a` vs `''a`; `real` and functions are not equality types);
  - [x] `case`/`fn`/`fun` pattern syntax, exhaustiveness, and `handle`;
  - [x] `datatype` declarations, mutually recursive `datatype ... and ...`, and `structure`/`signature`/`functor` syntax;
  - [x] BST invariants and `lt` semantics (`<`, not `<=`, unless stated);
  - [x] lambda-calculus free/bound variables, substitution, α-conversion, β-reduction, and Church encodings;
  - [x] I/O functions and `option` handling (`SOME`/`NONE`, `valOf`).
- [x] Reconcile lab `15` exercises 7.7 and 7.8 so both use the same `('a, 'b) mapTree` label type (a list of pairs).
- [x] Normalize formatting:
  - [x] remove leftover top-of-page `---` separators;
  - [x] convert Obsidian callouts to portable bold blockquotes (bold label + `>` body), so they render on GitHub and can be mapped to Material admonitions in Phase 2;
  - [x] unify fence spelling (`sml`, `C++`, `txt`, bare fences) and add blank lines around headings and fences;
  - [x] trim trailing whitespace, remove tabs outside code, replace curly quotes, and remove `//` comments from SML.
- [x] Remove spurious `val it = (): unit` output after declarations, while keeping legitimate unit results from `print` and side-effecting expressions.
- [x] Re-run the relative-link checker and a formatting lint before committing.

**Done when:** prose is Italian, SML examples and inferred types are internally consistent, Markdown renders without broken fences/callouts, and all relative links resolve.

**Completed:** 2026-11-02. 20 content pages edited; 167 callouts converted to portable bold blockquotes; 30 relative links check clean. No SML toolchain is installed, so transcripts were verified by reasoning rather than execution.

**Re-audit trigger:** after adding new notes, after changing `hooks/callouts.py`, or whenever `Dispensa.pdf` is rebuilt.

---

## Phase 2 — MkDocs Material site + GitHub Pages

**Goal:** a real site with search, navigation, math, and proper code blocks.

### Tasks

- [x] Add `requirements.txt` with pinned `mkdocs-material` and `pymdown-extensions`.
- [x] Add `mkdocs.yml`:
  - `site_name`, `site_url`, `repo_url`, `edit_uri`
  - theme features: `navigation.sections`, `navigation.top`, `search.highlight`, `content.code.copy`, `toc.follow`
  - `markdown_extensions`: `admonition`, `pymdownx.details`, `pymdownx.superfences`, `pymdownx.arithmatex`, `attr_list`, `md_in_html`, `tables`, `toc`
  - `nav` mirroring Phase 1 (Teoria / Laboratori / Dispensa)
- [x] Convert portable bold-blockquote callouts to Material admonitions at build time with `hooks/callouts.py`, so the Markdown source keeps rendering on GitHub. Mapping:
  - `> **Esercizio ...**` → `!!! question`
  - `> **Esempio**` / `> **Esempi ...**` → `!!! example`
  - `> **Osservazione ...**` → `!!! note`
  - `> **⚠️ Attenzione ...**` → `!!! warning`
  - `> **Teorema ...**` → `!!! abstract` (or a custom `theorem` type with CSS)
  - Keep the Italian label as the admonition title. Done with a one-off script, then reviewed the diff.
- [x] Normalize fences: `C++` → `cpp`; `txt` → `text`; verify `sml` highlighting works (Pygments has an SML lexer). Do not reformat the REPL transcripts.
- [x] Add blank lines before lists that directly follow a paragraph, so Python-Markdown renders them like GitHub does.
- [x] Math: enable `arithmatex` and MathJax (CDN or `docs/javascripts/mathjax.js`). Check inline `$...$` and display `$$...$$`.
- [x] Add `.github/workflows/docs.yml`: build with `mkdocs build --strict`, upload artifact, deploy to Pages via `actions/deploy-pages`.
- [ ] Enable GitHub Pages with source = GitHub Actions (manual repo setting).
- [x] Verify locally with `mkdocs serve`: nav, 167 admonitions, math, code highlighting, and the PDF link.
- [ ] Verify on the deployed URL: search, nav, code copy, math, mobile.

**Done when:** the site deploys on push to `main`, `--strict` passes, and math/code/search render correctly.

**Status:** `mkdocs build --strict` passes locally with 167 callouts converted into admonitions. Deployment still needs the manual GitHub Pages setting and a check on the deployed URL.

---

## Phase 3 — Interactive study features

**Goal:** the site should help you study, not just display text.

### Tasks

- [x] Make every lab solution collapsible at build time with `hooks/collapse_solutions.py` (`??? success "Soluzione"`). The 94 lab exercises keep the prompt visible and hide the answer; the Markdown source stays fully visible on GitHub.
- [ ] Add per-theory "Ripasso lampo": 3–5 self-check questions with collapsible answers. Prioritize the highest-yield topics (types, scope, recursion, higher-order functions, data types, lambda calculus).
- [x] Add the standard `---` separator and `[← Torna all'Indice del Corso](../index.md)` back-link to all 20 content pages.
- [ ] Add `tags` metadata (`teoria`, `laboratori`, topic) and a tags index page.
- [ ] Add "Esegui in REPL" support:
  - [ ] Pick and verify an online SML REPL (check that it actually accepts the snippets).
  - [ ] Add a link/note to relevant labs.
  - [ ] Add a `.devcontainer/` with SML/NJ and a short `docs/setup.md` for local execution.
- [ ] Optional: `mkdocs-print-site-plugin` to produce one printable page (feeds Phase 4's PDF decision).
- [ ] Optional: progress checkboxes per page. Note that they do not persist without custom JS; treat as cosmetic unless persistence is explicitly wanted.

**Done when:** answers are hidden by default, every lab has a reveal, and a reader can run at least one example without cloning the repo.

**Status:** `mkdocs build --strict` passes with 94 collapsible lab solutions and back-links on all content pages. The REPL/devcontainer item is still open.

---

## Phase 4 — Automation, PDF, polish

**Goal:** keep the site and PDF from going stale, and make contributions safe.

### Tasks

- [ ] Add CI checks on push/PR:
  - [ ] `lychee` link checker (ignore localhost and generated URLs)
  - [ ] `markdownlint-cli2` with `MD013` off, `MD033` allowed for `details`/`summary`, `MD024` `siblings_only`
- [ ] Decide the PDF strategy:
  - **Option A (cheap):** keep `Dispensa.pdf` as a snapshot, add a "compiled on" date and a note that the site is the source of truth.
  - **Option B (recommended):** generate it from Markdown. Spike `mkdocs-print-site-plugin` + browser print, or Pandoc + LaTeX (Eisvogel). Add `scripts/build-pdf.sh` and document it.
  - **Option C:** generate the PDF in a release workflow and attach it to a GitHub Release.
- [ ] Add a release workflow on tags: build site + PDF, attach artifacts.
- [ ] Add a `LICENSE` (decision needed): notes `CC BY-NC-SA 4.0`, code snippets `MIT`, or no license.
- [ ] Optional: short `CONTRIBUTING.md` (how to preview the site, style rules, callout syntax).
- [ ] Update `AGENTS.md` with the final paths and commands (`mkdocs serve`, build/lint commands, PDF script).

**Done when:** CI is green on a fresh clone, the PDF process is either automated or explicitly marked as a snapshot, and `AGENTS.md` matches the final repo.

---

## Open decisions

| Decision | Recommendation |
| :--- | :--- |
| Split `07` into lab + theory? | Yes. The lab exercises and the theory are independent; mixing them breaks navigation. |
| Sequential renumbering? | No. Keep original session numbers; gaps are meaningful. |
| `Dispensa.pdf` location | Keep at repo root; link from the site. |
| Callout syntax | Keep portable bold blockquotes in the source; convert them to Material admonitions at build time. |
| Online SML REPL | Verify one before linking; otherwise ship the devcontainer first. |
| PDF generation | Start with the snapshot (A), move to release-generated (C) once the site is stable. |
| License | Ask the author; do not add one by default. |

---

## Notes

- The `sml` fences are REPL transcripts (`>` prompts, `(* val it = ... *)` output), not runnable programs. Do not "fix" them into standalone code.
- `07. Laboratorio 3 + Pattern Matching.md` and `08. Patterns e environment locali in ML.md` share one topic. Read both before splitting.
- Filenames contain spaces and `+` today; quote paths in shell commands until Phase 1 is done.
