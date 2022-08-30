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

## Adding stuff to the EmuGUI wiki

For EmuGUI, a wiki is hosted on a stable repository on Codeberg: https://codeberg.org/lucien-rowan/EmuGUI/wiki

Basically, if you know how to write Markdown, you know how to contribute to these wikis.

### Ways to contribute to the wiki

Not everyone can do everything for the wiki but you don't have to be able to do everything for the wiki! Here are the things how you can contribute.

#### Making new articles

Managed to install an operating system which is not mentioned in the EmuGUI wiki? Go ahead, write a tutorial about this! I'm pretty sure there are some users who struggle to install it.

However, there are some rules:
- New articles must be written in English - they can be translated into other languages afterwards.
- Pictures of the operating system are recommended, but not required as you will have to host them on an external site or repository.
- Due to copyright, not every download link is allowed. General rule: Linux/BSD/FOSS distributions and (probably) free-to-distribute BIOSes are allowed while paid software is not.

#### Updating existing articles

Some articles are outdated or not correct? Updating these will help users to install their desired operating system. The rules from above apply.

#### Translating existing articles

The article is not available in your language or not fully translated yet? I've got an idea: Make or complete the translation! The translation rules from above apply.