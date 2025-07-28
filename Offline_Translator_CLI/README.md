# 🧭 Simple Offline CLI Translator

A minimal yet powerful Python-based command-line translator (English ↔ Russian) using a custom offline dictionary.

No internet required. Just run and translate — punctuation and case preserved, logs saved.

---

## 🚀 Features

- ✅ **Fully offline** — works with a local JSON dictionary
- 🔠 **Case-sensitive** — keeps original casing (e.g. `Hello → Привет`)
- 🧩 **Preserves punctuation**
- 🔄 **Supports three modes**:
  - English → Russian
  - Russian → English
  - Auto-detect direction
- 🕓 **Logs** every translation with timestamp to `translation.log`

---

## 🧪 Usage

```bash
python translator.py --text "Hello, world!" --dir 2ru     # English to Russian
python translator.py --text "Привет, мир!" --dir 2en      # Russian to English
python translator.py --text "Привет, мир!"                # Auto-detect
```

Example log entry
```bash
[2025-07-27 19:32] [2ru] Hello, world! => Привет, мир!
```

📁 Files

    translator.py — main CLI script
    dict.json — translation dictionary (10,000+ words recommended)
    README.md — this file
    requirements.txt — Python ≥ 3.6 (no external libraries)

✅ You should use or share this if:

    You want a lightweight offline translation tool
    You care about full control over your dictionary
    You need CLI-based, fast, local translation

🪪 License

MIT (or any license you prefer)
