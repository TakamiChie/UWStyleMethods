import tkinter
from tkinter import ttk
import time
class Dialogs(object):
  BUTTON_OK = 1
  BUTTON_CANCEL = 2
  BUTTON_YES = 4
  BUTTON_NO = 8
  BUTTON_ABORT = 16
  BUTTON_RETRY = 32
  BUTTON_IGNORE = 64

  def __init__(self, caption, message, buttons=0):
    """
    Initialize this class

    Parameters
    ----
    caption: str
      Caption string
    message: str
      Dialog message
    buttons: int
      Dialog buttons(Default=No buttons(0))
    """
    self.caption = caption
    self.message = message
    self.buttons = buttons
    self.timeout = 0

  def _prepare(self, frame):
    """
    Perform initialization processing for each class.
    If you inherit this class and create a new dialog class, inherit this method to add your own control.

    Parameters
    ----
    frame: Frame
      A frame object for storing UI controls.
    """
    label = tkinter.Label(frame, text=self.message)
    label.pack(padx=8, pady=8)

  def _setbuttons(self, frame):
    """
    Create a button bar to accept user interaction.

    Parameters
    ----
    frame: Frame
      A frame object for storing UI controls.
    """
    buttonarray = [
      [self.BUTTON_OK, "OK"],
      [self.BUTTON_CANCEL, "Cancel"],
      [self.BUTTON_YES, "Yes"],
      [self.BUTTON_NO, "No"],
      [self.BUTTON_RETRY, "Retry"],
      [self.BUTTON_ABORT, "Abort"],
      [self.BUTTON_IGNORE, "Ignore"],
    ]
    first = True
    for button in buttonarray:
      if self.buttons & button[0] == button[0]:
        b = tkinter.Button(frame, command=button[0], text=button[1], 
          default="active" if first else "disabled")
        if first:
          b.focus()
        b.bind("<1>", self._close)
        b.bind("<Return>", self._close)
        b.bind("<space>", self._close)
        b.pack(padx=4, pady=4, side="left")
        first = False

  def _setprogress(self, frame):
    """
    Position the progress bar when the timeout is specified.

    Parameters
    ----
    frame: Frame
      A frame object for storing UI controls.
    """
    self._progressbar = pb = ttk.Progressbar(
        frame,
        orient=tkinter.HORIZONTAL,
        length=100,
        maximum=self.timeout * 1000,
        mode='determinate')
    pb.configure(value=self._inter_timeout)
    pb.pack(fill=tkinter.BOTH, expand=1)
    self._inter_lasttick = time.time() * 1000
    self._dialog.after(100, self._inter_timecount)

  def _inter_timecount(self):
    lt = time.time() * 1000
    self._inter_timeout -= (lt - self._inter_lasttick)
    self._progressbar.configure(value=self._inter_timeout)
    self._inter_lasttick = lt
    if self._inter_timeout <= 0:
      self._dialog.destroy()
    else:
      self._dialog.after(100, self._inter_timecount)

  def _close(self, event):
    self._retcode = event.widget["command"]
    self._dialog.destroy()

  def show(self):
    """
    Show dialog.
    To enable the dialog to be re-displayed, 
    the dialog is created with this method and is displayed and destroyed.

    Returns
    ----
    retcode: int|None
      The button index. If you cancel the dialog, return None
    """
    self._retcode = None
    self._dialog = dialog = tkinter.Tk()
    dialog.resizable(0, 0)
    dialog.attributes("-toolwindow", 1)
    dialog.attributes("-topmost", 1)
    dialog.title(self.caption)
    uiframe = tkinter.Frame(dialog, relief=tkinter.RAISED)
    buttonframe = tkinter.Frame(dialog, relief=tkinter.RIDGE)
    self._prepare(uiframe)
    self._setbuttons(buttonframe)
    uiframe.pack(anchor="n")
    buttonframe.pack(padx=8, pady=8, anchor="s")
    if self.timeout > 0:
      self._inter_timeout = self.timeout * 1000
      timerframe = tkinter.Frame(dialog)
      timerframe.pack(fill=tkinter.X, expand=1)
      self._setprogress(timerframe)
    dialog.update_idletasks()
    screen_width = dialog.winfo_screenwidth()
    screen_height = dialog.winfo_screenheight()
    size = tuple(int(_) for _ in dialog.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2
    dialog.geometry("+%d+%d" % (x, y))
    dialog.after(1, lambda: dialog.focus_force())
    dialog.mainloop()
    return self._retcode

if __name__ == "__main__":
  d = Dialogs("TestDialog", "TestDialogMessage", Dialogs.BUTTON_OK)
  d.timeout = 5
  print(d.show())
  d.message = "This is a Test"
  d.timeout = 10
  print(d.show())
  d = Dialogs("YesNoDialog", "TestDialogMessage", Dialogs.BUTTON_YES | Dialogs.BUTTON_NO)
  d.timeout = 0
  print(d.show())
  d = Dialogs("AllDialog", "TestDialogMessage", Dialogs.BUTTON_YES | Dialogs.BUTTON_NO |
    Dialogs.BUTTON_OK | Dialogs.BUTTON_CANCEL | Dialogs.BUTTON_IGNORE | Dialogs.BUTTON_ABORT |
    Dialogs.BUTTON_RETRY)
  d.timeout = 10
  print(d.show())
