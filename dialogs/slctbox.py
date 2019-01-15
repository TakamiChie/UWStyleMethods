if __name__ == "__main__":
  import sys
  import pathlib
  sys.path.append(str(pathlib.Path(__file__).parent.parent))

  import dialogs
import tkinter
from tkinter import ttk

class Combobox(dialogs.Dialogs):
  def __init__(self, caption, message, buttons=dialogs.Dialogs.BUTTON_OK):
    """
    Initialize this class

    Parameters
    ----
    caption: str
      Caption string
    message: str
      Dialog message
    buttons: int
      Dialog buttons(Default=OK Button Only)
    """
    super().__init__(caption, message, buttons)
    self._combo_select_value = None
    self.items = []

  def _prepare(self, frame):
    """
    Add Combobox.
    """
    super()._prepare(frame)
    self._combo = combo = ttk.Combobox(values=self.items, state="readonly")
    combo.current(0)
    combo.pack(padx=8, pady=8)

  def _close(self, event):
    """
    Override Close Method
    """
    self._combo_select_value = self._combo.get()
    super()._close(event)

  def show(self):
    """
    Show Dialog.

    Returns
    ----
    result: Tuple|None
      If you cancel the dialog, return None
      1: int
        The button index
      2: str
        Selected Items
    """
    retcode = super().show()
    return None if retcode is None else (retcode, self._combo_select_value)

class Choose(dialogs.Dialogs):
  def __init__(self, caption, message):
    """
    Initialize this class

    Parameters
    ----
    caption: str
      Caption string
    message: str
      Dialog message
    """
    super().__init__(caption, message, 0)
    self._button_select_value = None
    self.items = []

  def _prepare(self, frame):
    """
    Add Buttons.
    """
    super()._prepare(frame)
    self._buttons = []
    for (index, item) in enumerate(self.items):
      b = tkinter.Button(frame, command=index, text=item)
      b.pack(fill=tkinter.BOTH, expand=1)
      b.bind("<1>", self._close)
      b.bind("<Return>", self._close)
      b.bind("<space>", self._close)

  def _close(self, event):
    """
    Override Close Method
    """
    self._button_select_value = self.items[event.widget["command"]]
    super()._close(event)

  def show(self):
    """
    Show Dialog.

    Returns
    ----
    result: Tuple|None
      If you cancel the dialog, return None
      1: int
        The button index
      2: str
        Selected Items
    """
    retcode = super().show()
    return None if retcode is None else (retcode, self._button_select_value)

if __name__ == "__main__":
  c = Combobox("TestDialog", "Select Item")
  c.items = ["test1", "test2", "test3"]
  print(c.show())
  c = Combobox("TestDialog", "Select Item", dialogs.Dialogs.BUTTON_YES | dialogs.Dialogs.BUTTON_NO)
  c.items = ["test1", "test2", "test3"]
  c.timeout = 10
  print(c.show())
  c = Choose("TestDialog", "Select there. Which one would you choose?")
  c.items = ["A", "B", "C", "D", "E"]
  print(c.show())
  c.timeout = 10
  print(c.show())
