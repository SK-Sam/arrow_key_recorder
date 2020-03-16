import keyboard
import sys

#1
print("Please type in any arrow key. Press 'q' to stop")
#2 #3 #4
def detect_key_input(event):
    if event.name == "down":
        print("You typed Down Key")
    elif event.name == "up":
        print("You typed Up Key")
    elif event.name == "left":
        print("You typed Left Key")
    elif event.name == "right":
        print("You typed Right Key")
    #5
    elif event.name == "q":
        sys.exit()

keyboard.on_press(detect_key_input)

while True:
    pass

#1: Have the user type into the terminal with arrow keys. Check
#2: Find out which arrow key the user typed.
#3: Each different arrow key will result to a different text response from the terminal.
#4: If the Arrow key is UP, the terminal will print "UP", if LEFT key, print "LEFT"
    #if RIGHT key, print "RIGHT", if DOWN key, print "DOWN".
#5:Make sure the program runs continuously until the user decides to stop it
    #-The user should type a specific key to stop the program from infinitely asking them to type.
#6:Make sure each time the user types a key in, the terminal will add a line in between each time it prints out a key.
#7:If the user presses the 'r' key, the program will begin to "record" all of the keys pressed.
#8:Make a message that clearly shows the user the program is "recording" and stops "recording".
#9:The recording will stop once the user presses 'r' again to escape the "record" mode.
#10:Make a message that clearly shows the program is about to "play" the "recorded" messages.
#11:The user can then press p key to print every recorded key onto the terminal.


#shot_pressed = 0

#def on_press_reaction(event):
#    global shot_pressed
#    if event.name == "down":
#        shot_pressed += 1
#        print("shot_pressed %d times"%shot_pressed)


#keyboard.on_press(on_press_reaction)

#while True:
#    pass
