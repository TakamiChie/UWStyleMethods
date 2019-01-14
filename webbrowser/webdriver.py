from selenium import webdriver as seledriver

class WebDriver(object):
  """
  The base class for controlling the browser in the webbrowser class.
  Selenium Webdriver wrapper class.
  """
  def __init__(self, options = None):
    """
    Initialize Class

    Parameters
    ----
    options: str|list
      arguments of webdriver
    """
    self._webdriver = None
    self.options = []
    if options is not None:
      self.add_options(options)

  def add_options(self, value):
    """
    add options

    Parameters
    ----
    value: str|list
      arguments
    """
    if type(value) == str:
      self.options.append(value)
    elif type(value == list):
      for v in value:
        if type(v) == str:
          self.options.append(v)
        else:
          raise ValueError("Invalid Value")
    else:
      raise ValueError("Invalid Value")

  def get_browser(self):
    """
    get browser object

    Returns
    ----
    driver: selenium.webdriver
      browser's driver object
    """
    raise NotImplementedError

class ChromeDriver(WebDriver):
  """
  Google Chrome's driver
  require chromedriver_binary
  `pip install chromedriver_binary`

  This class does not currently support using Chrome with an existing profile.
  The option does not specify User-data-dir because "Selenium.common.exceptions.webdriverexception" occurs.
  """
  def __init__(self, options = None):
    super().__init__(options)

  def get_browser(self):
    """
    get browser object

    Returns
    ----
    driver: selenium.webdriver
      browser's driver object
    """
    import chromedriver_binary
    options = seledriver.ChromeOptions()
    for o in self.options:
      options.add_argument(o)
    return seledriver.Chrome(options=options)