import dialogs
from tkinter import ttk

class Combobox(dialogs.Dialogs):
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

if __name__ == "__main__":
  c = Combobox("TestDialog", "Select Item", dialogs.Dialogs.BUTTON_OK)
  c.items = ["test1", "test2", "test3"]
  print(c.show())
  c = Combobox("TestDialog", "Select Item", dialogs.Dialogs.BUTTON_YES | dialogs.Dialogs.BUTTON_NO)
  c.items = ["test1", "test2", "test3"]
  c.timeout = 10
  print(c.show())
