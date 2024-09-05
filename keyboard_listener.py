from pynput import keyboard
from pynput.keyboard import Key

def bprint(string):
    print(string, end="", flush=True)

with keyboard.Events() as events:
    for event in events:
        if isinstance(event, keyboard.Events.Press):
            match event.key:
                case Key.space:
                    bprint(" ")
                case Key.enter:
                    bprint("\u23CE")
                case Key.delete:
                    bprint("\u2421")
                case _:
                    if isinstance(event.key, keyboard.KeyCode):
                        bprint(str(event.key))