# Guide to contributing to EmuGUI

There are a few ways to contribute to EmuGUI. Here we will discuss them more precisely.

## General information

While stable releases are maintained on both GitHub and Codeberg, the development builds are maintained on a seperate repository on Codeberg only. See README.md for the mirrors. Generally, bugfixes, security fixes and corrections of existing translations can be considered something for both releases while new features, translations etc. are for pre-release builds. I also recommend you to state your changes in CHANGELOG.md, however, if you forgot it, I may be clever enough to do it for you. Also, you will be listed in CONTRIBUTORS.md if you commited at least one time.

## Programming

EmuGUI is written in Python, although some SQL scripts are embedded into the Python scripts in order to save your settings and virtual machines. Of course, this all needs attention.

### Dependencies

- Python 3
- Qt 6
- PySide6
- QEMU
- requests
- Python Magic

### Coding style

Well, I don't like specifying a specific coding style. Just make sure it can be easily checked if it's dangerous or not.

### Converting Qt files into Python scripts

Qt Designer: Edit > Show Python code > Save to uiScripts/ui_(ui_file_here).py

Qt Creator: `pyside6-uic ui/(ui_file_here).ui -o uiScripts/ui_(ui_file_here).py`

## Translation

If you are able to speak English and another language, you should be able to translate EmuGUI to your language.

### What I care about

- You don't have to speak this language natively, so if you can speak more than that and all of them are not available yet, don't fear to stay away because of it.
- If unsure, you may look into a dictionary to look up specific words.
- Translation solutions (like Google Translate) may only be used to check the grammar.
- Translations must be in their specific alphabet (e.g. Latin alphabet for English, German, French etc., Cyrillic for Russian, Ukrainian, ...).
- Special stuff (like EmuGUI, QEMU or i386) stay in the Latin alphabet.
- If you can't translate it at all, leave it in English.

If you follow these rules (which are quite nice in my opinion), your translation will get approved.

### Languages and their current state

#### Available languages

| Language | Completeness |
| -------- | ------------ |
| English | Default language for EmuGUI |
| German | Translated everything what is possible |
| Ukrainian | Only single words have been translated |

There are still a lot of languages that are not available in EmuGUI. If you feel like you can at least start to translate EmuGUI to your desired language, copy the English translation, rename that copy to the short form of your desired language and start translating.