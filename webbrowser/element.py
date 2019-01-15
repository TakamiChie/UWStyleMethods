from selenium.webdriver.common.keys import Keys

class Element(object):
  """
  An object that represents the DOM element.
  """
  def __init__(self, owner, element):
    self._owner = owner
    self.raw = element

  @property
  def tag_name(self):
    "Get HTML Tag name"
    return self.raw.tag_name

  @property
  def value(self):
    """
    Gets the value of the element.
    For input tags, this method is used to retrieve the value (cannot be obtained with the Textcontent property).
    Note that for DOM elements with no value, the value is none.
    """
    return self.raw.get_attribute("value")

  @property
  def innertext(self):
    "Get the contained text. Equivalent to the JavaScript `element.innerText` method."
    return self.raw.text

  def settext(self, value):
    "Enter values for the elements that can be entered in the text."
    self.raw.send_keys(Keys.CONTROL, "a")
    self.raw.send_keys(Keys.DELETE)
    self.raw.send_keys(value)
