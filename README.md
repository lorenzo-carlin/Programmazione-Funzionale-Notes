# 💻 Programmazione Funzionale — Appunti & Laboratori

Appunti ed esercizi del corso di **Programmazione Funzionale** (A.A. 2025/2026), in Standard ML.

---

## 📖 Inizia da qui

- 📚 **[Indice completo del corso](docs/index.md)** — teoria e laboratori
- 📄 **[Dispensa in PDF](Dispensa.pdf)** — snapshot del 18 giugno 2026
- 🗺️ **[Roadmap](ROADMAP.md)** — com'è organizzata la repository e cosa arriva dopo

---

## 🗂️ Struttura

```text
.
├── docs/
│   ├── index.md          # Indice del corso
│   ├── javascripts/      # Configurazione MathJax
│   ├── teoria/           # Appunti teorici (01–18)
│   └── laboratori/       # Esercizi di laboratorio (03–19)
├── hooks/
│   └── callouts.py       # Converte i callout in admonition Material
├── .github/workflows/
│   └── docs.yml          # Build e deploy su GitHub Pages
├── mkdocs.yml
├── requirements.txt
├── Dispensa.pdf
├── AGENTS.md
├── ROADMAP.md
└── README.md
```

La numerazione segue l'ordine delle lezioni: da `03` in poi i dispari sono laboratori e i pari teoria, con l'eccezione del `07`, diviso tra `docs/teoria/07-pattern-matching.md` e `docs/laboratori/07-laboratorio-3.md`.

---

## 🛠️ Stato

Il sito navigabile è configurato con **MkDocs Material** e viene pubblicato su GitHub Pages a ogni push su `main` tramite [`.github/workflows/docs.yml`](.github/workflows/docs.yml). La configurazione è in [`mkdocs.yml`](mkdocs.yml); [`docs/index.md`](docs/index.md) resta l'indice completo del corso.

## 🚀 Anteprima locale

```bash
pip install -r requirements.txt
mkdocs serve
```

La build di verifica è `mkdocs build --strict`.
