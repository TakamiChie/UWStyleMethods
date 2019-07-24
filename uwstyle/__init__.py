if __name__ == "__main__":
  import sys
  import pathlib
  sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from uwstyle.dialogs.dialogs import Dialogs
from uwstyle.dialogs.slctbox import Combobox, Choose
from uwstyle.overridestd.writer import OverrideManager

VERSION = "0.0.4"

DIALOGBUTTON_OK = Dialogs.BUTTON_OK
DIALOGBUTTON_OKCANCEL = Dialogs.BUTTON_OK | Dialogs.BUTTON_CANCEL
DIALOGBUTTON_YESNO = Dialogs.BUTTON_YES | Dialogs.BUTTON_NO
DIALOGBUTTON_RETRYIGNOREABORT = Dialogs.BUTTON_ABORT | Dialogs.BUTTON_IGNORE | Dialogs.BUTTON_RETRY

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
  box = Dialogs(__name__, message, buttons)
  box.timeout = timeout
  return _retcode2bool(box.show())

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
  box = Combobox(__name__, message, buttons)
  box.timeout = timeout
  box.items = items
  return _retcode2bool(box.show())


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
  box = Choose(__name__, message)
  box.timeout = timeout
  box.items = items
  return box.show()

def print2message():
  """
  The message output to standard output, such as the `print` method, is displayed in the dialog.
  This method is useful for logging when running programs in environments that do not have a console.

  Returns
  ----
  overridemanager: OverrideManager
    A reference to a manager that converts standard output to output to a dialog.
    You can stop the output to the dialog by calling the `quit()` method of this object.
  """
  return OverrideManager("Output Window")

def _retcode2bool(retcode):
  """
  Converts the return code of a dialog to the return value of a method.
  * True if OK, YES.
  * False if CANCEL, NO.
  * "retry" if RETRY.
  * "ignore" if IGNORE.
  * "abort" if ABORT.
  * None if None.
  is returned.

  Parameters
  ----
  retcode: int|tuple
    retcode
  """
  ret = None
  if type(retcode) is tuple:
    ret = retcode[0]
  else:
    ret = retcode

  if ret == Dialogs.BUTTON_YES or ret == Dialogs.BUTTON_OK:
    ret = True
  elif ret == Dialogs.BUTTON_NO or ret == Dialogs.BUTTON_CANCEL:
    ret = False
  elif ret == Dialogs.BUTTON_ABORT:
    ret = "abort"
  elif ret == Dialogs.BUTTON_RETRY:
    ret = "retry"
  elif ret == Dialogs.BUTTON_IGNORE:
    ret = "ignore"

  if type(retcode) == tuple:
    ret = tuple([ret]) + retcode[1:]

  return ret

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

  m = print2message()
  for i in range(3):
    print(f"output{i}")
  import time
  time.sleep(2)
  m.quit()
  print("not displayed")
  time.sleep(2)

  print2message()
  for i in range(3):
    print(f"output{i}")
  time.sleep(2)
