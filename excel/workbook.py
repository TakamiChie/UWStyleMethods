from uwstyle.dialogs import select
from uwstyle.excel.sheet import Sheet

class Workbook:
  """
  Excel Workbook Object
  """
  def __init__(self, owner, oleobject):
    """
    Get Microsoft Excel Workbook Object.
    This class is basically derived from the uwstyle.excel.Excel object.
    so the user does not basically invoke this method.

    Parameters
    ----
    owner: uwstyle.excel.Excel
      owner Object.
    oleobject: Excel.Workbook
      An OLEObject that represents an Excel workbook
    """
    self.excel = owner
    self.raw = oleobject

  @property
  def sheets(self):
    """
    Get a list of all the sheet objects in the workbook.

    Returns
    ----
    list: list(Sheet)
      Sheet list.
    """
    result = []
    for i in range(1, self.raw.sheets.count + 1):
      result.append(Sheet(self.excel, self.raw.sheets(i)))
    return result

  @property
  def name(self):
    "Get/Set the display name of the workbook."
    return self.raw.name

  @name.setter
  def name(self, value):
    "Get/Set the display name of the workbook."
    self.raw.name = value

  def add(self):
    "Add a sheet."
    return Sheet(self.excel, self.raw.sheets.Add())

  ### Utility Methods.

  def chooseworksheet(self, message="Choose Worksheet"):
    """
    Select a worksheet.
    When two or more worksheets are open, a dialog is displayed to prompt the user for selection.
    If there is only one worksheet open, it returns the name of the worksheet without displaying anything.

    Parameters
    ----
    message: str
      The message that is displayed in the dialog.

    Returns
    ----
    worksheet: Sheet|None
      the worksheet object. None if the dialog has been cancelled.
    """
    ws = self.sheets;
    sheets = [s.name for s in ws]
    if len(sheets) == 1:
      return ws[0]
    else:
      r = select(message, sheets)
      if r is None:
        return None
      else:
        return ws[r[2]]
