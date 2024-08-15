import pyautogui as _pag
import time as _time

def altf4(count=1, interval=0.2):
  for x in range (count):
    _pag.hotkey("alt", "f4")
    if not x == count-1:
      _time.sleep(interval)

def open_app(name):
  _pag.hotkey("win")
  _time.sleep(0.75)
  _pag.write(name)
  _time.sleep(0.25)
  _pag.hotkey("enter")

def open_url(url):
  open_app("Google Chrome")
  _time.sleep(2)
  _pag.hotkey("ctrl", "l")
  _time.sleep(0.75)
  if not (url.startswith("http://") or  url.startswith("https://")):
    url = "http://"+url
  _pag.write(url)
  _time.sleep(0.25)
  _pag.hotkey("enter")
