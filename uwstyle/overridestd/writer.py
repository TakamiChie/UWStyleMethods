if __name__ == "__main__":
  import sys
  import pathlib
  sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))

NEUTRAL = "NEU"
ERROR = "ERR"

class OverrideManager:
  """
  Manage overrides for stdout, stderr.
  """
  def __init__(self):
    """
    Start override stdout, stderr.
    """
    import sys
    self._dialog = MessageWindow()
    self._nativeout = sys.stdout
    self._nativeerr = sys.stderr
    sys.stdout = OverrideWriter(self._dialog, NEUTRAL)
    sys.stderr = OverrideWriter(self._dialog, ERROR)

  def quit(self):
    """
    Quit Override Manager.

    Restore stdout and stderr values.
    """
    import sys
    sys.stdout = self._nativeout
    sys.stderr = self._nativeerr

class OverrideWriter:
  """
  Override for stdout, stderr class.
  """
  def __init__(self, dialog, tag):
    """
    Initialize this.

    Parameters
    ----
    dialog: MessageWindow
      Display window object.

    tag: str
      The value of the tag to use on output.
    """
    self._dialog = dialog
    self._tag = tag

  def write(self, text):
    """
    The override method. 
    Called when some value is written to standard output or standard error, 
    such as in the Print method.
    """
    self._dialog.insert(text, self._tag)

class MessageWindow:
  """
  Message only window

  This dialog show on subthread.
  """

  def __init__(self, caption = __name__, geometry=None):
    """
    Start dialog.

    Parameters
    ----
    caption: str
      Title bar caption.

    geometry: str
      The geometry of the window.
      The default is None (leave it to Tkinter).
    """
    import threading
    ev = threading.Event()
    def showdlg(self, ev, c, g):
      "The thread that displays the window."
      import tkinter
      self._dialog = dialog = tkinter.Tk()
      dialog.title(c)
      dialog.attributes("-toolwindow", 1)
      dialog.attributes("-topmost", 1)
      if geometry is not None:
        dialog.geometry(g)
      dialog.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
      self._logbox = log = tkinter.Text(dialog, state='disabled')
      log.tag_config(NEUTRAL)
      log.tag_config(ERROR, foreground="red")
      log.pack(expand=1,fill="both")
      ev.set()
      dialog.mainloop()
    threading.Thread(target=showdlg, args=(self, ev, caption, geometry), daemon=True).start()
    ev.wait()

  def insert(self, text, tag=NEUTRAL):
    """
    Insert text in logbox

    Parameters
    ----
    text: str
      Insert text.

    tag: str
      Text tag.
      (NEU or ERR default NEU)
    """
    self._logbox.configure(state='normal')
    self._logbox.insert("1.0", text, tag)
    self._logbox.configure(state='disabled')

  def close(self):
    self._dialog.quit()

if __name__ == "__main__":
  import time
  import sys
  # MessageWindow Test.
  win = MessageWindow(caption="test", geometry="300x400")
  for i in range(3):
    win.insert(f"test{i}")
    time.sleep(1)
  time.sleep(2)
  win.insert("closing")
  win.close()
  time.sleep(3)

  # OverrideManager Test.
  om = OverrideManager()
  print("---stdout part---")
  for i in range(3):
    print(f"test{i}")
    time.sleep(1)
  time.sleep(3)
  print("---stderr part---")
  for i in range(3):
    print(f"test{i}", file=sys.stderr)
    time.sleep(1)
  time.sleep(3)
  print("finished.")
  om.quit()
  print("finished.")
