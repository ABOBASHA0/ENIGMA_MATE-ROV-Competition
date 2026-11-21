# Imports #
import json
import socket
import time
import pygame as pg 
print("Every Thing Imported")

# Valuables #
Jetson = ("192.168.1.20", 5005) # PlaceHolder #
DEADZONE = 0.1 # It Will Ignore If The JoyStick Is Stick Drift #
ACCELERATION = 250 # That Is How Much Speed You Gain By Holding Forward # 


# Pygame Start Up #
pg.init()
pg.joystick.init()

# Error Checker #
if pg.joystick.get_count() == 0:
    print("No Controller Detected.")
    exit()
        
# Controller #
Controller = pg.joystick.Joystick(0)
print(f"Connected To:{Controller.get_name()}")  

# Socket Connection #
Sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Controller Function # 
    while True :

    # Update Pygame #
        pg.event.pump()

    # Valuables #
        Move = "none"
        Rotation = "none"
        Lift = "none"

    # Axis --> Up | Down | Left |  Right
        Right_Joystick_X = Controller.get_axis(2)
        Right_Joystick_Y = Controller.get_axis(3)
        Left_Joystick_X = Controller.get_axis(0)
        Left_Joystick_Y = Controller.get_axis(1)

    # Special Trigger
        R1 = Controller.get_button(11)
        L1 = Controller.get_button(10)
    
    # Speed Controller #
        Stick_Power = max(abs(Right_Joystick_X),abs(Right_Joystick_Y),abs(Left_Joystick_X),abs(Left_Joystick_Y))

        if R1 == 1 or L1 == 1:
            SPEED = 250  # Full speed when pressing R1 or L1 to move up/down
        elif Stick_Power > DEADZONE:
            SPEED = round(Stick_Power * ACCELERATION)
            
            print(f"Speed is {SPEED}")
        else:
            SPEED = 0
        
    # Functionality #
         
        # Control Movement X|Z By Right Joystick # 
        if   Right_Joystick_X >  DEADZONE: 
            Move = "right"
            print(f"Moving {Move}")
        elif Right_Joystick_X < -DEADZONE: 
            Move = "left"
            print(f"Moving {Move}")
        elif Right_Joystick_Y < -DEADZONE: 
            Move = "forward"
            print(f"Moving {Move}")
        elif Right_Joystick_Y >  DEADZONE: 
            Move = "backward"
            print(f"Moving {Move}")
        
        # Control Movement Y By L1 | R1 #    
        if R1 == 1:   
            Lift = "up"
            print(f"Moving {Lift}")
        elif L1 == 1: 
            Lift = "down"
            print(f"Moving {Lift}")
            
        # Control Rotation By Left Joystick #
        if   Left_Joystick_X >  DEADZONE:
            Rotation = "right"
            print(f"Rotate {Lift}")
        elif Left_Joystick_X < -DEADZONE:
            Rotation = "left"
            print(f"Rotate {Lift}")
        elif Left_Joystick_Y < -DEADZONE:
            Rotation = "upward"
            print(f"Rotate {Lift}")
        elif Left_Joystick_Y >  DEADZONE:
            Rotation = "backward"
            print(f"Rotate {Lift}")
        
        # Sender Data #
        Packet = {SPEED:"Speed", Move:"Move", Lift:"Lift", Rotation:"Rotation" }
        Sock.sendto(json.dump(Packet).encode(), Jetson)
        time.sleep(0.05)

except KeyboardInterrupt:
    print("Stopped The Sender")