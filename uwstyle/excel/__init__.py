if __name__ == "__main__":
  import sys
  import pathlib
  sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))

import win32com.client
from uwstyle.excel.workbook import Workbook
from uwstyle.dialogs import select, DIALOGBUTTON_OKCANCEL

class Excel:
  """
  Require win32com module(pip install pywin32)
  """
  def __init__(self, active=True):
    """
    Get Microsoft Excel Object

    Parameters
    ----
    active: bool
      True to get Excel that is already booting.
      False if necessary to start a new Excel.

    Exceptions
    ----
    com_error
      Occurs when Excel is not running when active is true.
    """
    if active:
      self.excel = win32com.client.GetActiveObject("Excel.Application")
    else:
      self.excel = win32com.client.Dispatch("Excel.Application")

  @property
  def workbooks(self):
    """
    Get a list of open workbooks.

    Returns
    ----
    list: list(Workbook)
      Workbook object list.
    """
    result = []
    for i in range(1, self.excel.workbooks.count + 1):
      result.append(Workbook(self, self.excel.workbooks(i)))
    return result

  @property
  def displayalert(self):
    "Get/Set alert control flag"
    return self.raw.displayalert

  @displayalert.setter
  def displayalert(self, value):
    "Get/Set alert control flag"
    self.raw.displayalert = value

  def add_workbook(self):
    "Add a book."
    return Workbook(self.excel, self.excel.workbooks.Add())

  ### Utility Methods.

  def chooseworkbook(self, message="Choose Workbook"):
    """
    Select a workbook.
    When two or more workbooks are open, a dialog is displayed to prompt the user for selection.
    If there is only one workbook open, it will return the file name without displaying anything.

    Parameters
    ----
    message: str
      The message that is displayed in the dialog.

    Returns
    ----
    workbook: Workbook|None
      The Workbook object. None if the dialog has been cancelled.
    """
    wb = self.workbooks
    files = [f.name for f in wb]
    if len(files) == 1:
      return wb[0]
    else:
      r = select(message, files, buttons=DIALOGBUTTON_OKCANCEL)
      if r is None or r[0] == False:
        return None
      else:
        return wb[r[2]]

if __name__ == "__main__":
  excel = Excel()
  wb = excel.chooseworkbook()
  if wb is not None:
    ws = wb.chooseworksheet()
    if ws is not None:
      print(ws.raw.name)
    ws = wb.add()
    ws.name = "TEST"
    ws.cells(1, 1).value = "TEST"