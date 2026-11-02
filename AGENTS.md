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
- Callouts are portable bold blockquotes: `> **Esercizio 1.1**`, `> **Esempio**`, `> **Osservazione**`, `> **⚠️ Attenzione**`, `> **Teorema**`. Add a `>` blank line between the label and the body, and prefix every body line with `>`. Use `> **Osservazione — Titolo**` or `> **⚠️ Attenzione — Titolo**` when a custom title is needed. Do not reintroduce Obsidian `>[!type]` markers: GitHub only understands five native alert types, and the Italian custom types would render literally. Phase 2 maps these labels to Material admonitions.
- `sml` fences are REPL transcripts with `>` prompts and `(* val it = ... *)` expected output, not standalone runnable programs. Fence languages seen: `sml`, `C++` (capitalized), `txt`, and bare fences.
- Pages intentionally start at `##`; do not add `#` headings or YAML front matter.

## Content audit

Re-read a page for meaning, not only for spelling. The notes were migrated from Obsidian, so formatting damage and factual drift often sit in the same block.

### Standard ML correctness

- Declarations (`val`, `fun`, `datatype`, `type`, `exception`, `structure`, `signature`, `functor`, `open`) do **not** produce `val it`. Only expressions do. Do not leave `val it = (): unit` after a declaration.
- `print` and other side-effecting expressions return `unit`, so their transcripts legitimately end with `val it = (): unit`. Do not strip those.
- `=` and `<>` require an equality type, printed as `''a`. `real` and functions are not equality types. `@`, `null`, `hd`, `tl`, `::` remain polymorphic, but `L = nil` forces `''a`. Check inferred types after changing a condition.
- `type t = int` creates an alias, not a new type; `datatype` creates a new type. A structure field of type `t` is a type component, not a variable.
- Inside a `structure`, use `fun` for functions and `val` for values. `structure S :> SIG` is opaque ascription; `:` is transparent.
- For a BST, state the invariant precisely: with a strict `lt`, the left subtree is `< x` and the right subtree is `> x`; do not describe it as `<=`.
- Check `case`/`fn`/`fun` pattern syntax, exhaustiveness, and `handle` placement. `fn` may have multiple clauses: `fn p1 => e1 | p2 => e2`.
- Lambda calculus: keep free/bound sets, substitution, α-conversion, and β-reduction consistent. `(λx.λy.x y)y` needs α-conversion before substitution, otherwise `y` is captured.
- No SML toolchain is installed (`sml`, `mlton`, `poly` are absent). Verify transcripts by reasoning and say so; do not claim a snippet was executed.

### Formatting and migration artifacts

- Watch for a leftover `---` at the top of a page. It is an Obsidian artifact, not a horizontal rule.
- Convert Obsidian callouts (`>[!warning]`, `> [!WARNING]`) to portable bold blockquotes. Do not leave `[!type]` markers in the Markdown: GitHub only understands five native alert types, and the Italian custom types would render literally. A callout block ends at the first blank line, so every body line needs `>` and the label needs a `>` blank line after it.
- Fences must start at column 0 unless intentionally nested. Do not leave a fence indented after converting an Obsidian list.
- Add a blank line before and after headings and fenced blocks. Trim trailing whitespace; replace tabs outside code with spaces.
- Replace curly quotes (`‘ ’ “ ”`) with ASCII quotes, especially in type variables (`‘a` → `'a`) and SML strings.
- SML comments are `(* ... *)`; remove stray `//` comments. Do not rewrite a transcript into a standalone program or wrap it in `use`.
- Common word-level damage: `foglia`/`foglie`, `cuo`/`cui`, `cosa`/`coda`, `coppa`/`coppia`, `String`/`string`, `srtLT`/`strLT`, `qas`/`as`, `EmptyTeee`/`EmptyTree`.

### Safe bulk edits

- Prefer a one-off script that **fails on a missing pattern** over silent global replacement. Review `git diff` afterwards.
- Keep file moves and content edits in separate commits. Use the link checker after any path or heading change.
- Check the whole page after a scripted edit: an apparently local fix can leave an output block or a later exercise inconsistent (for example, changing a `datatype` label type requires updating the functions and tests that use it).

## Editing guidance

- No build or verification command exists. Check Markdown paths and links with a one-off script; do not invent a toolchain.
- Keep `README.md`, `docs/index.md`, and the actual `docs/` tree in sync when adding, renaming, or moving pages.
- Use `git mv` for renames and update every relative link; do not bulk-rename without checking the link checker.
- There is no site/Pages setup yet. Do not assume `mkdocs.yml`, workflows, or a deployed site exists.
- Do not mix file moves with content edits; one roadmap phase per commit.
