# Simple Offline CLI Translator with History

A lightweight Python-based English ↔ Russian sentence translator using a custom JSON dictionary.

## Features
- Preserves punctuation and original case (e.g. **Hello** → **Привет**)
- Works fully offline
- Supports EN→RU, RU→EN, and auto-detection
- Logs all translations with timestamps to `translation.log`

## Usage

```bash
python translator.py --text "Hello, world!" --dir 2ru
python translator.py --text "Привет, мир!" --dir 2en
python translator.py --text "Привет, мир!"           # auto mode
```

Example
```bash
[2025-07-27 19:32] Hello, world! => Привет, мир!```

✅ You can publish this if:

    dict.json contains ~10,000+ clean words

    The translator works from the command line

    You’re okay sharing it publicly (no sensitive data inside)

License

MIT or your preferred open license.
