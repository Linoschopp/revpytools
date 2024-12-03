import pyautogui as _pag
import pynput as _pynput
import time as _time

keyboard = pynput.keyboard.Controller()

def altf4(count=1, interval=0.2):
  for x in range (count):
    _pag.hotkey("alt", "f4")
    if not x == count-1:
      _time.sleep(interval)

def open_app(name):
  keyboard.tap(pynput.keyboard.Key.cmd)
  _time.sleep(0.75)
  keyboard.type(name)
  _time.sleep(0.25)
  keyboard.tap(pynput.keyboard.Key.enter)

def slash(n=1):
  for _ in range(n):
      _pag.keyDown("shift")
      _pag.hotkey("7")
      _pag.keyUp("shift")
  return ""

def open_url(url, open_delay=2):
  open_app("Google Chrome")
  _time.sleep(open_delay)
  with keyboard.pressed(pynput.keyboard.Key.ctrl):
    keyboard.tap("l")
  _time.sleep(0.75)
  if not (url.startswith("http://") or  url.startswith("https://")):
    url = f"http://"+url
  url = url.split("/")
  for p in range(len(url)-1):
      _pag.write(url[p])
      slash()
  _pag.write(url[-1])
  _time.sleep(0.25)
  _pag.hotkey("enter")
