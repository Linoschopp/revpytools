import pynput as _pynput
import time as _time

keyboard = _pynput.keyboard.Controller()

def altf4(count=1, interval=0.2):
  for x in range(count):
    with keyboard.pressed(_pynput.keyboard.Key.alt):
      keyboard.tap(_pynput.keyboard.Key.f4)
    if not x == count-1:
      _time.sleep(interval)

def minimize(count=1, interval=0.2):
  for x in range(count):
    with keyboard.pressed(_pynput.keyboard.Key.cmd):
      keyboard.tap(_pynput.keyboard.Key.h)
    if not x == count-1:
      _time.sleep(interval)

def open_app(name):
  keyboard.tap(_pynput.keyboard.Key.cmd)
  _time.sleep(0.75)
  keyboard.type(name)
  _time.sleep(0.25)
  keyboard.tap(_pynput.keyboard.Key.enter)


def open_url(url, open_delay=2):
  open_app("Google Chrome")
  _time.sleep(open_delay)
  with keyboard.pressed(_pynput.keyboard.Key.ctrl):
    keyboard.tap("l")
  _time.sleep(0.75)
  keyboard.type(url)
  _time.sleep(0.25)
  keyboard.tap(_pynput.keyboard.Key.enter)
