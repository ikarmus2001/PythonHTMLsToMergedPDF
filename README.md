# PythonHTMLsToMergedPDF
Very short, low-optimized solution to convert many htmls into merged pdf

# Installation
## Install Python libs
```
pip install pypdf2 weasyprint
```
I used [WeasyPrint](https://weasyprint.org/) v60.2 and [PyPDF2](https://pypdf2.readthedocs.io/en/latest/index.html) 3.0.1
## To use WeasyPrint you will need GTK3 installed 
(Windows solution: [GTK-for-Windows-Runtime-Environment-Installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer))

Also you have to set env variable to GTK3 binaries (example with default installation path)
```cmd
set WEASYPRINT_DLL_DIRECTORIES=C:\Program Files\GTK3-Runtime Win64\bin
```

More on [WeasyPrint website](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)

# Usage
## Throw `main.py` right into your directory with `.html`s:
```
someDir/
├── EventualHTMLDependenciesCssOrImages/
│   └── PartyImage.png
├── one.html
├── 2.html
├── whatever.anyFormatNotTakenUnderConsideration
└── main.py
```
(Created with [tree.nathanfriend.io](https://tree.nathanfriend.io/))

and run with python
```
someDir>py main.py
```
Profit!
Based on the amount of merged files it may take some time, script dumps everything into your RAM, so it might not be the most suitable one for the low-memory pcs (of course you can write separate pdfs and merge them, but that would be a bit different solution, totally possible with included libraries).
