<p align="center"><img src="logo.png" width="128" alt="SayIt logo"></p>

# SayIt – Minecraft Language Learning Mod

**Pick up an item, say its name out loud in the language you're learning, or lose it.**

SayIt is a free Minecraft Java Edition mod that turns everyday gameplay into language practice. Every new item you get shows its name in the language you're learning, and you say it into your microphone to keep it. Speech recognition runs **offline on your own PC**, pronunciation is scored, words come back for spaced review, and a villager teacher helps when you get stuck.

- **24 languages:** English, Mandarin Chinese, Japanese, Korean, German, Spanish, French, Italian, Portuguese, Polish, Russian, Ukrainian, Turkish, Norwegian, Hungarian, Swedish, Finnish, Dutch, Danish, Greek, Filipino, Traditional Chinese, Arabic and Cantonese.
- **Fabric, Forge and NeoForge**, Minecraft 1.20.1 to 26.3, in one mod.
- **Free.** No account, no subscription.

**Website, downloads and FAQ: https://spicesfire.com/sayit/** · **Discord: https://discord.gg/TM4pNVUktW**

<p align="center"><img src="https://spicesfire.com/sayit/assets/shot-dictionary.png" width="640" alt="SayIt's Pocket Dictionary in Minecraft: learned words with their reading and best pronunciation score"></p>

## Features

**Learn by speaking**
- Say the name of every new item, block and creature in the language you're learning. Typing (`Y`) and multiple choice work too, so a microphone is optional.
- Pronunciation score from 0 to 100%. Letters you didn't say clearly turn red. A light accent still passes.
- Short sentences while you play: crafting, fighting, sleeping, trading or entering the Nether ask a sentence. Numbers, colours and biome names come up too.
- Three levels: Beginner (item names), Intermediate (plus places, numbers, colours, creatures) and Advanced (sentences too).

**Remember what you learn**
- Spaced review: learned words come back after 1 day, 3 days, a week and a month.
- Pocket Dictionary (`O`): every word you've learned, with its reading, your best score and a Practice button. Click a word to hear it.
- Immersion mode: every item you've learned shows in the new language everywhere in the game. Everything else stays in your own language.
- Reading help: pinyin for Chinese, furigana and romaji for Japanese, Latin letters for Korean, Russian and Ukrainian.

**Hear it said right**
- Natural offline voices (Piper) in 19 languages, as a woman, man, child or elderly voice. Optional ElevenLabs with your own key.
- `I` reads the word, `K` reads it slowly. After a few misses the villager teacher says it syllable by syllable and the timer slows down.
- `N` names the block or creature you're looking at.

**Make it a game**
- Pick the stakes: lose the item, drop it, a bad effect, lose 2 hearts, an explosion, or nothing. Effect rewards for right answers.
- Hard mode (learn or die): 1, 3 or 5 wrong answers in a row and you die.
- Answer time from 8 to 30 seconds, or no timer with 3 tries. Pause any time with `B`.
- Daily streak with rewards, 10 advancements.

**New in 1.2.0**
- Talk to villagers: say what a villager sells and that trade is about 30% cheaper for a day.
- Bestiary, daily goals, mastery levels (New to ★ Master) and a talking teacher.
- Press `H` to hear your own answer next to the teacher's. Practise one picked word until it's right.
- Readings in your own letters; English shown as it sounds. Flashcard export, save and load your progress.

**Play together**
- Full multiplayer: install on the server and every player's game. Players without the mod are never asked.
- The best speaker wears a gold crown. Word races: the first to say it wins.
- Cobblemon: wild Pokémon ask their own species name (ピカチュウ in Japanese).

## How SayIt compares

Other Minecraft language mods, as of November 2026:

| | SayIt | LinguaCraft | LanguageCraft | Learn or Die |
|---|---|---|---|---|
| Loaders | Fabric, Forge, NeoForge | Fabric | Fabric | Fabric, NeoForge |
| Minecraft | 1.20.1, 1.21.1, 1.21.10, 26.1.2, 26.3 | 1.20.1, 1.21.1, 26.3 | 1.21.1 | 1.21.1, 26.3 |
| Languages | 24, all in one jar | 23 | 14 | 6, one jar per language |
| Answer by voice | Yes, offline (Vosk + whisper.cpp), model downloads by itself | Yes, offline (Vosk) | Yes, offline (Vosk), model installed by hand | Optional beta, about 1.5 GB download |
| Server side | Built in (races, crown, server rules) | With the LinguaCraft Server add-on | Client only | Client only |

## Download

Get the jar for your loader and Minecraft version from the **[latest release](https://github.com/SpicesFire/SayIt/releases/latest)**:

| Loader | Minecraft | Java | File |
|---|---|---|---|
| Fabric | 26.3 | 25 | `sayitenglish-fabric-26.3-1.2.1.jar` |
| Fabric | 26.1.2 | 25 | `sayitenglish-fabric-26.1.2-1.2.1.jar` |
| Fabric | 1.21.10 | 21 | `sayitenglish-fabric-1.21.10-1.2.1.jar` |
| Fabric | 1.20.1 | 17 | `sayitenglish-fabric-1.20.1-1.2.1.jar` |
| Forge | 26.3 | 25 | `sayitenglish-forge-26.3-1.2.1.jar` |
| Forge | 1.20.1 | 17 | `sayitenglish-forge-1.20.1-1.2.1.jar` |
| NeoForge | 26.3 | 25 | `sayitenglish-neoforge-26.3-1.2.1.jar` |
| NeoForge | 1.21.1 | 21 | `sayitenglish-neoforge-1.21.1-1.2.1.jar` |

SayIt is also waiting for review on CurseForge and Modrinth.

## Install

1. Install the loader (Fabric, Forge or NeoForge) for your Minecraft version.
2. Fabric only: also put [Fabric API](https://modrinth.com/mod/fabric-api) in your `mods` folder.
3. Drop the SayIt jar into the `mods` folder and start the game.
4. Join a world, choose the language you want to learn, then pick your microphone.
5. The speech model for your language downloads once (30 to 90 MB). After that it works offline.

For multiplayer, install it on the server and on every player's game.

**Keys:** `U` settings · `Y` type the answer · `I` hear the word · `K` hear it slowly · `N` name what you look at · `O` Pocket Dictionary · `B` pause
**Commands:** `/sayitenglish stats` · `/sayitenglish practice` · `/sayitenglish top` · `/sayitenglish reset`

## FAQ

**Can I learn English with it?** Yes. English is one of the 24 languages. Choose it when you join a world, or later in Settings (`U`).

**Do I need a microphone?** No. You can type every answer (`Y`) or choose Typing only in Settings. Multiple-choice questions only need a click.

**Does it work offline?** Yes. Speech recognition and the Piper voices run on your PC after a one-time download.

**Which systems?** Offline speech runs on Windows x64, Linux x64 and macOS.

## Privacy

Audio is processed in memory on your computer and never saved or sent anywhere, unless you choose the optional Groq engine with your own key. The ElevenLabs voice, if you pick it with your own key, receives only the word being read.

## Help

Questions or bugs: [Discord](https://discord.gg/TM4pNVUktW). Tell us your Minecraft version, loader and the language you're learning.

## Help with the languages

The texts SayIt shows and the sentences it asks you to say are open here, for all 24 languages: **[language-data](language-data/)**. Found a mistake or a clumsy phrase? Propose a fix, the guide is in that folder.

---

Made by SpicesFire. Bundled third-party libraries (Vosk, whisper.cpp, Kuromoji) keep their own licenses; see `THIRD_PARTY_NOTICES_sayitenglish.txt` inside the jar.
