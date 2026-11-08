<p align="center"><img src="logo.png" width="128" alt="SayIt"></p>

# SayIt

**Pick up an item, say its name out loud in the language you're learning, or lose it.**

A Minecraft mod for learning a language by speaking. 17 languages: English, Mandarin Chinese, Japanese, Korean, German, Spanish, French, Italian, Portuguese, Polish, Russian, Ukrainian, Turkish, Norwegian, Hungarian, Swedish and Finnish. Speech recognition runs offline on your own PC.

**Main page and downloads: https://spicesfire.com/sayit/**

## Download

Get the jar for your loader and Minecraft version from the **[latest release](https://github.com/SpicesFire/SayIt/releases/latest)**:

| Loader | Minecraft | Java | File |
|---|---|---|---|
| Fabric | 26.3 | 25 | `sayitenglish-fabric-26.3-1.1.7.jar` |
| Fabric | 26.1.2 | 25 | `sayitenglish-fabric-26.1.2-1.1.7.jar` |
| Fabric | 1.21.10 | 21 | `sayitenglish-fabric-1.21.10-1.1.7.jar` |
| Fabric | 1.20.1 | 17 | `sayitenglish-fabric-1.20.1-1.1.7.jar` |
| Forge | 26.3 | 25 | `sayitenglish-forge-26.3-1.1.7.jar` |
| Forge | 1.20.1 | 17 | `sayitenglish-forge-1.20.1-1.1.7.jar` |
| NeoForge | 26.3 | 25 | `sayitenglish-neoforge-26.3-1.1.7.jar` |
| NeoForge | 1.21.1 | 21 | `sayitenglish-neoforge-1.21.1-1.1.7.jar` |

## Install

1. Install the loader (Fabric, Forge or NeoForge) for your Minecraft version.
2. Fabric only: also put [Fabric API](https://modrinth.com/mod/fabric-api) in your `mods` folder.
3. Drop the SayIt jar into the `mods` folder and start the game.
4. Join a world, choose the language you want to learn, then pick your microphone.
5. The speech model for your language downloads once (30 to 55 MB). After that it works offline.

For multiplayer, install it on the server and on every player's game.

**Keys:** `U` settings · `Y` type the answer instead of speaking
**Commands:** `/sayitenglish stats` · `/sayitenglish practice` · `/sayitenglish reset`

## Privacy

Audio is processed in memory on your computer and never saved or sent anywhere, unless you choose the optional Groq engine with your own key.

## Help

Questions or bugs: [Discord](https://discord.gg/TM4pNVUktW). Tell us your Minecraft version, loader and the language you're learning.

---

Made by SpicesFire. Bundled third-party libraries (Vosk, whisper.cpp) keep their own licenses; see `THIRD_PARTY_NOTICES_sayitenglish.txt` inside the jar.

## Help with the languages

The texts SayIt shows and the sentences it asks you to say are open here, for all 17 languages: **[language-data](language-data/)**. Found a mistake or a clumsy phrase? Propose a fix, the guide is in that folder.
