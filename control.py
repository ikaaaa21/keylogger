from pynput.mouse import Controller

# controlling your mouse  
def controlMouse():
    mouse = Controller() # variable mouse is assigned to the Controller object
    mouse.position = (10,20) # this moves the mouse to the position 10,20 (left to right, top to bottom from top left of the screen) which is the pixels on the screen
controlMouse() # calling the function, this moves my mouse to 10,20 when i un the  function 

