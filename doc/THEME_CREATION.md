# How to create custom EmuGUI themes

POV: You find your system theme is getting boring and there is no other theme that you like.

That might be a reason why you want to create a new EmuGUI theme. That is possible with QSS files.

## What is QSS?

QSS (probably) stands for Qt Stylesheet and basically is a CSS (Cascade Stylesheet) dialect for Qt applications. With that, you can create themes for several Qt applications that support custom themes, including EmuGUI.

## What do I need to get started?

It's simple, you just need an idea and a text editor which can handle QSS files. The default editor should do but I recommend to install a text editor which supports syntax highlighting (like Notepad++ or Visual Studio Code), especially on Windows. Linux users may have syntax highlighting with their text editor, but if not, I recommend to install VS Code here as well.

## I'm ready! How does it work?

EmuGUI uses the following widgets which can be customized:
- QWidget
- QMainWindow
- QTabBar::tab
- QListView
- QPushButton
- QLabel
- QComboBox
- QCheckBox
- QLineEdit
- etc.

To see how the syntax works, you can look into the example themes EmuGUI comes with. I'm aware that it's not the full potential of it, but at least you can see how it works in the first place.

## EmuGUI doesn't recognize my themes!

Did you put it into the themes folder of EmuGUI? If not, please do that.

Also, you must set the theme on "Settings/General" manually.