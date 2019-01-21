# UWStyleMethods

Modules for handling UWSC styles in Python

## What's This

UWSC is a macro software that automates the operation of applications on Windows.
However, as of March 2018, the public site of the application becomes 403 error, and the trend of the future is in an unknown state.

This module group is intended to achieve UWSC-like processing in Python by realizing some of the UWSC methods in Python.

## ToDo

* Implementing a simple Dialog method
  * [x] (UWSC) MSGBOX method
  * [x] (UWSC) SLCTBOX method
* Methods to display messages on the screen
  * [ ] (UWSC) Baloon method
* Ability to work with other GUI applications
  * [ ] (UWSC) CLKITEM method
  * [ ] (UWSC) CHKBTN method
  * [ ] (UWSC) GETSTR method
  * [ ] (UWSC) GETITEM method
  * [ ] (UWSC) GETSLCTL method
  * etc.
* [x] InternetExplorer operation Method (actually planned to be implemented as an Edge or Chrome operation)
* [x] Excel operation methods (other incompatible offices not supported)

The author basically used UWSC to realize a simple GUI, and the automation processing such as Excel was done mainly.
Therefore, there is no plan to implement the function other than the above.

However, pull requests are accepted.

## Usage

[Uploaded to PyPI!](https://pypi.org/project/uwstyle/)

```PowerShell
> pip install uwstyle
```

The usage is described in `__init__.py` under each directory, so refer to it.

```python
from uwstyle.dialogs import dialog, select, choose, DIALOGBUTTON_OK, DIALOGBUTTON_YESNO, DIALOGBUTTON_RETRYIGNOREABORT
from uwstyle.webbrowser import WebBrowser
from uwstyle.webbrowser.driver import ChromeDriver
from uwstyle.excel import Excel
```
