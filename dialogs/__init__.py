import dialogs
import slctbox

DIALOGBUTTON_OK = dialogs.Dialogs.BUTTON_OK
DIALOGBUTTON_YESNO = dialogs.Dialogs.BUTTON_YES | dialogs.Dialogs.BUTTON_NO
DIALOGBUTTON_RETRYIGNOREABORT = dialogs.Dialogs.BUTTON_ABORT | dialogs.Dialogs.BUTTON_IGNORE | dialogs.Dialogs.BUTTON_RETRY

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
    This value is not valid for the current implementation.
  buttons: int
    Button flags.
    you can use `uwstyle.dialogs.DIALOGBUTTON_*` constants

  Returns
  ----
  state: bool|None
    True if the Yes button is pressed, false if no button is pressed.
    None if the dialog times out when the X button is pressed.
  """
  box = dialogs.Dialogs(__name__, message, dialogs.Dialogs.BUTTON_OK)
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
    This value is not valid for the current implementation.
  buttons: int
    Button flags.
    you can use `uwstyle.dialogs.DIALOGBUTTON_*` constants

  Returns
  ----
  Tuple
  1: bool|None
    If the OK button is pressed, true if the X button is pressed, none if the dialog times out.
  2: str
    Selected Items
  """
  box = slctbox.Combobox(__name__, message, buttons)
  box.items = items
  return _retcode2bool(box.show())

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

  if ret == dialogs.Dialogs.BUTTON_YES or ret == dialogs.Dialogs.BUTTON_OK:
    ret = True
  elif ret == dialogs.Dialogs.BUTTON_NO or ret == dialogs.Dialogs.BUTTON_CANCEL:
    ret = False
  elif ret == dialogs.Dialogs.BUTTON_ABORT:
    ret = "abort"
  elif ret == dialogs.Dialogs.BUTTON_RETRY:
    ret = "retry"
  elif ret == dialogs.Dialogs.BUTTON_IGNORE:
    ret = "ignore"

  if type(retcode) == tuple:
    ret = (ret, retcode[1])

  return ret

if __name__ == "__main__":
  print(dialog("test"))
  print(dialog("test", buttons=DIALOGBUTTON_YESNO))
  print(dialog("test", buttons=DIALOGBUTTON_RETRYIGNOREABORT))
  print(select("test", items=["A", "B", "C"]))
  print(select("test", items=["A", "B", "C"], buttons=DIALOGBUTTON_YESNO))
