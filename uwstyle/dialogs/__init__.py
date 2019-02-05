if __name__ == "__main__":
  import sys
  import pathlib
  sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))

import uwstyle
import warnings

DIALOGBUTTON_OK = 1
DIALOGBUTTON_OKCANCEL = 3
DIALOGBUTTON_YESNO = 12
DIALOGBUTTON_RETRYIGNOREABORT = 112

def dialog(message, timeout=0, buttons=DIALOGBUTTON_OK):
  """
  Display a message box with an OK button.
  This method is equivalent to `MSGBOX(message, BTN_OK)` in UWSC.

  Parameters
  ----
  message: str
    Dialog messages
  timeout: int
    The dialog timeout.
  buttons: int
    Button flags.
    you can use `uwstyle.dialogs.DIALOGBUTTON_*` constants

  Returns
  ----
  state: bool|str|None
    The button state
    * True if OK, YES.
    * False if CANCEL, NO.
    * "retry" if RETRY.
    * "ignore" if IGNORE.
    * "abort" if ABORT.
    None if the dialog times out when the X button is pressed.
  """
  warnings.warn("This Method moved uwstyle.dialog()", DeprecationWarning)
  return uwstyle.dialog(message, timeout, buttons)

def select(message, items=[], timeout=0, buttons=DIALOGBUTTON_OK):
  """
  Show Select box.
  This method is equivalent to `SLCTBOX(SLCT_CMB + SLCT_STR, timeout, message, items)` in UWSC

  Parameters
  ----
  message: str
    Dialog messages
  items: list(str)
    Items
  timeout: int
    The dialog timeout.
  buttons: int
    Button flags.
    you can use `uwstyle.dialogs.DIALOGBUTTON_*` constants

  Returns
  ----
  result: Tuple|None
    If you cancel the dialog, return None
    1: bool|str
      The button state
      * True if OK, YES.
      * False if CANCEL, NO.
      * "retry" if RETRY.
      * "ignore" if IGNORE.
      * "abort" if ABORT.
    2: str
      Selected Items
    3: int
      Selected Item index
  """
  warnings.warn("This Method moved uwstyle.select()", DeprecationWarning)
  return uwstyle.select(message, items, timeout, buttons)


def choose(message, items=[], timeout=0):
  """
  Show Choose box.
  This method is equivalent to `SLCTBOX(SLCT_BTN + SLCT_STR, timeout, message, items)` in UWSC

  Parameters
  ----
  message: str
    Dialog messages
  items: list(str)
    Items
  timeout: int
    The dialog timeout.

  Returns
  ----
  result: Tuple|None
    If you cancel the dialog, return None
    1: int
      The button index
    2: str
      Selected Items
  """
  warnings.warn("This Method moved uwstyle.choose()", DeprecationWarning)
  return uwstyle.choose(message, items, timeout)

if __name__ == "__main__":
  print(dialog("test"))
  print(dialog("test", buttons=DIALOGBUTTON_YESNO, timeout=5))
  print(dialog("test", buttons=DIALOGBUTTON_RETRYIGNOREABORT))
  print(select("test", items=["A", "B", "C"]))
  print(select("test", items=["A", "B", "C"], timeout=5, buttons=DIALOGBUTTON_YESNO))
  print(choose("test", items=["A", "B", "C", "D", "E"]))
  print(choose("test", items=["A", "B", "C", "D", "E"], timeout=5))
  print(dialog("""
  this is a long long text dialog
  """ * 20))
  print(dialog("""
  this is a long long text dialog
  """ * 30))
  print(dialog("""
  this is a long long text dialog
  """ * 40))
  print(dialog("""
  this is a long long text dialog
  """ * 100))

