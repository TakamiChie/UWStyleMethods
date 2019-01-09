import dialogs
from tkinter import ttk

class Combobox(dialogs.Dialogs):
  def set_item(self, *items):
    self.items = items

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
    Tuple
    1: int|None
      The button index. If you cancel the dialog, return None
    2: str
      Selected Items
    """
    retcode = super().show()
    return (retcode, self._combo_select_value)

if __name__ == "__main__":
  c = Combobox("TestDialog", "Select Item", dialogs.Dialogs.BUTTON_OK)
  c.set_item("test1", "test2", "test3")
  print(c.show())
