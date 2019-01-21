class Sheet:
  """
  Excel Sheet Object.
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
    oleobject: Excel.Sheet
      An OLEObject that represents an Excel sheet
    """
    self.excel = owner
    self.raw = oleobject

  @property
  def name(self):
    "Get/Set the display name of the sheet."
    return self.raw.name

  @name.setter
  def name(self, value):
    "Get/Set the display name of the sheet."
    self.raw.name = value

  def cells(self, row, col=None):
    "Get a cell object."
    if col is None:
      return self.raw.cells(row)
    else:
      return self.raw.cells(row, col)

