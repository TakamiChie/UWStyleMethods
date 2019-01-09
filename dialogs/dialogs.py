import tkinter
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

  def prepare(self, frame):
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

  def setbuttons(self, frame):
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
        b.bind("<1>", self.close)
        b.pack(padx=4, pady=4, side="left")
        first = False

  def close(self, event):
    self._retcode = event.widget["command"]
    self._dialog.destroy()

  def show(self):
    """
    Show dialog.
    To enable the dialog to be re-displayed, 
    the dialog is created with this method and is displayed and destroyed.
    """
    self._retcode = None
    self._dialog = dialog = tkinter.Tk()
    dialog.resizable(0, 0)
    dialog.attributes("-toolwindow", 1)
    dialog.title(self.caption)
    uiframe = tkinter.Frame(dialog)
    buttonframe = tkinter.Frame(dialog)
    self.prepare(uiframe)
    uiframe.pack()
    self.setbuttons(buttonframe)
    buttonframe.pack(padx=8, pady=8)
    dialog.update_idletasks()
    screen_width = dialog.winfo_screenwidth()
    screen_height = dialog.winfo_screenheight()
    size = tuple(int(_) for _ in dialog.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2
    dialog.geometry("+%d+%d" % (x, y))
    dialog.mainloop()
    return self._retcode

if __name__ == "__main__":
  d = Dialogs("TestDialog", "TestDialogMessage", Dialogs.BUTTON_OK)
  print(d.show())
  d.message = "This is a Test"
  print(d.show())
  d = Dialogs("YesNoDialog", "TestDialogMessage", Dialogs.BUTTON_YES | Dialogs.BUTTON_NO)
  print(d.show())
  d = Dialogs("AllDialog", "TestDialogMessage", Dialogs.BUTTON_YES | Dialogs.BUTTON_NO |
    Dialogs.BUTTON_OK | Dialogs.BUTTON_CANCEL | Dialogs.BUTTON_IGNORE | Dialogs.BUTTON_ABORT |
    Dialogs.BUTTON_RETRY)
  print(d.show())