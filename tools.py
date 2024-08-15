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

