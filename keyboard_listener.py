from pynput import keyboard

with keyboard.Events() as events:
        for event in events:
               if isinstance(event, keyboard.Events.Press):
                       if isinstance(event.key, keyboard.KeyCode):
                               print(event.key.char, end="", flush=True)
                       else:
                               if event.key == keyboard.Key.space:
                                       print(" ", end="", flush=True)
