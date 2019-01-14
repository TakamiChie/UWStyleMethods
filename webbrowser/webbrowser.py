import webdriver

from selenium.webdriver.common.keys import Keys

class WebBrowser(object):
  """
  A class for remote operation of a Web browser.
  Use selenium internally. You need to install it in advance.

  The following is the preparation for working with chrome.
  ```powershell
  > pip install Selenium
  > pip install chromedriver_binary
  ```
  The current version supports Chrome-only remote operations. Other browser operations supported by selenium will be supported in the future.
  """
  def __init__(self, driver):
    """
    Initialize this

    Parameters
    ----
    driver: uwstyle.webbrowser.webdriver
      uwstyle's webdriver object
    """
    if not issubclass(type(driver), webdriver.WebDriver):
      raise ValueError("Invalid WebDriver")
    self.driver = driver.get_browser()

  def get(self, url):
    """
    Make the browser display a specific URL.
    This method works synchronously. The method does not return processing until the browser has finished navigating.

    Parameters
    ----
    url: str
      navigate url
    """
    self.driver.get(url)

  @property
  def title(self):
    """
    Get the title of the page.

    Returns
    ----
    title: str
      title of the page.
    """
    return self.driver.title

  @property
  def url(self):
    """
    Get the url of the page.

    Returns
    ----
    url: str
      url of the page.
    """
    return self.driver.current_url

  def quit(self):
    """
    Quit browser.
    """
    return self.driver.quit()

  def id(self, id):
    """
    Gets the DOM element on the HTML.
    Use a ID to get it.
    Equivalent to `document.getElementById()` in JavaScript.

    Parameter
    ----
    id: str
      DOM id.
    """
    return element(self, self.driver.find_element_by_id(id))

  def find(self, selector):
    """
    Gets the DOM element on the HTML.
    Use a CSS selector to get it.
    Equivalent to `document.querySelector()` in JavaScript.

    Parameter
    ----
    selector: str
      CSS selector.
    """
    return element(self, self.driver.find_element_by_css_selector(selector))

  def find_all(self, selector):
    """
    Gets the DOM element on the HTML at All.
    Use a CSS selector to get it.
    Equivalent to `document.querySelectorAll()` in JavaScript.

    Parameter
    ----
    selector: str
      CSS selector.
    """
    elems = []
    for elem in self.driver.find_elements_by_css_selector(selector):
      elems.append(element(self, elem))
    return elems

class element(object):
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

if __name__ == "__main__":
  from webdriver import *
  import time
  args = []
#  args = [r'--user-data-dir=D:\Users\TakamiChie\AppData\Local\Google\Chrome\User Data', "--prifile-dir=Default"]
  browser = WebBrowser(ChromeDriver(args))
  browser.get("https://sbc.yokohama/")
  browser.find(".wpcf7-form .your-name input").settext("this is a test")
  print(browser.title)
  print(browser.url)
  browser.get("https://onpu-tamago.net/about")
  print(browser.id("outline").innertext)
  for elem in browser.find_all("#about > div > p"):
    print(elem.innertext)
  time.sleep(1)
  browser.quit()