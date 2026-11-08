# Language data

Everything SayIt shows or says in its own words, for all 17 languages: menus, chat messages, the sentences you are asked
to say (*"I just crafted %s."*), the number words, advancement names. **Help us make them sound natural!**

The names of items, blocks and mobs are **not** here. Those come from Minecraft's own language files.

| File | Language |
|---|---|
| `en_us.json` | English (the original, every other file is checked against it) |
| `de_de.json` | German |
| `es_es.json` | Spanish |
| `fi_fi.json` | Finnish |
| `fr_fr.json` | French |
| `hu_hu.json` | Hungarian |
| `it_it.json` | Italian |
| `ja_jp.json` | Japanese |
| `ko_kr.json` | Korean |
| `no_no.json` | Norwegian |
| `pl_pl.json` | Polish |
| `pt_br.json` | Portuguese (Brazil) |
| `ru_ru.json` | Russian |
| `sv_se.json` | Swedish |
| `tr_tr.json` | Turkish |
| `uk_ua.json` | Ukrainian |
| `zh_cn.json` | Chinese (Simplified) |

## How to help

**Fix a text:** open the file of your language here on GitHub, click the pencil icon, change the text and press *Propose changes*. That opens a pull request.

**Not comfortable with pull requests?** [Open an issue](https://github.com/SpicesFire/SayIt/issues/new) with the language, the key (the part on the left, like `sayitenglish.s.craft.1`), the current text and your better text.

**Wrong furigana or reading?** The Japanese readings come from a dictionary and are sometimes wrong. Fix them in `reading_overrides.json`: add a line with the word exactly as the game shows it and how it is read, in hiragana or katakana, for example `"木の斧": "きのおの"`. Or open an issue with the word, the wrong reading and the right one.

## Rules

- Do not change the keys (the part on the left).
- Keep the placeholders exactly as in the English text: `%s`, `%1$s`, `%%`. A sentence with one `%s` gets the item's name there, so the word order is yours to choose, but keep it once.
- Keep the colour codes (`§a`, `§r`…) where they are.
- Sentences should be short, natural and something a learner would really say. No slang.
- Keep "SayIt", key names (U, Y, I) and numbers as they are.

A check runs on every pull request and tells you if a key or a placeholder is wrong. You can also run it yourself: `python3 language-data/check.py`.

## What happens next

Fixes are reviewed before they are used. An accepted change is **not live instantly**: it goes into the mod with the next release, and you will be mentioned in the notes if you like.

By contributing you agree that your changes are released under the MIT License, like the mod.
