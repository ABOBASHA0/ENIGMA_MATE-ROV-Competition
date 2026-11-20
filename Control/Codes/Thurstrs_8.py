# Imports #
import time
import pygame as pg
from pca9685 import PCA9685
print("Every Thing Imported")

# Valuables #
MAX_US = 1750  # Upper That 1500 Will Move Forward
MIN_US = 1250  # Lower That 1500 Will Move backward
NEUTRAL = 1500  # It Will Stop Moving
DEADZONE = 0 # It Will Ignore If The JoyStick Is Stick Drift
SPEED = 0  # It Will Increase By Moving The Right Joystick Forward
ACCELERATION = 250 # That Is How Much Speed You Gain By Holding Forward # 

# PCA9685 controller instance
pca = PCA9685()

# Thrusts Names #
Thrusts_List = {"URF": 0, "ULF": 1, "DRF": 2, "DLF": 3, "URB": 4, "ULB": 5, "DRB": 6, "DLB": 7}

# Safety Functional #
def clamp (US,MAX_US,MIN_US):
    if US > MAX_US:
        return MAX_US
    if US < MIN_US:
        return MIN_US
    return US

def set_thruster(thrust_name, target_us):
    Safe_US = clamp(target_us, MAX_US, MIN_US)
    pca.set_pulse_us(Thrusts_List[thrust_name], Safe_US)

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
        
# Functional #
def moving_forward():
    # Front Thrusts Move Forwards
    set_thruster("URF", NEUTRAL + SPEED)
    set_thruster("ULF", NEUTRAL + SPEED)
    set_thruster("DRF", NEUTRAL + SPEED)
    set_thruster("DLF", NEUTRAL + SPEED)

    # Back Thrusts Move Backwards
    set_thruster("URB", NEUTRAL - SPEED)
    set_thruster("ULB", NEUTRAL - SPEED)
    set_thruster("DRB", NEUTRAL - SPEED)
    set_thruster("DLB", NEUTRAL - SPEED)

    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.05)
    

def moving_backward():
    # Front Thrusts Move Backwards
    set_thruster("URF", NEUTRAL - SPEED)
    set_thruster("ULF", NEUTRAL - SPEED)
    set_thruster("DRF", NEUTRAL - SPEED)
    set_thruster("DLF", NEUTRAL - SPEED)

    # Back Thrusts Move Forwards
    set_thruster("URB", NEUTRAL + SPEED)
    set_thruster("ULB", NEUTRAL + SPEED)
    set_thruster("DRB", NEUTRAL + SPEED)
    set_thruster("DLB", NEUTRAL + SPEED)

    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.05)
        
def moving_left():
    # Left Thrusts Move Forwards #
    set_thruster("ULF", NEUTRAL - SPEED)
    set_thruster("ULB", NEUTRAL - SPEED)
    set_thruster("DLF", NEUTRAL - SPEED)
    set_thruster("DLB", NEUTRAL - SPEED)

    # Right Thrusts Move Backwards #
    set_thruster("URF", NEUTRAL + SPEED)
    set_thruster("URB", NEUTRAL + SPEED)
    set_thruster("DRF", NEUTRAL + SPEED)
    set_thruster("DRB", NEUTRAL + SPEED)

    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.05)
    
def moving_right():
    # Left Thrusts Move Backwards #
    set_thruster("ULF", NEUTRAL + SPEED)
    set_thruster("ULB", NEUTRAL + SPEED)
    set_thruster("DLF", NEUTRAL + SPEED)
    set_thruster("DLB", NEUTRAL + SPEED)

    # Right Thrusts Move Forwards #
    set_thruster("URF", NEUTRAL - SPEED)
    set_thruster("URB", NEUTRAL - SPEED)
    set_thruster("DRF", NEUTRAL - SPEED)
    set_thruster("DRB", NEUTRAL - SPEED)  

    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.05)
        
def moving_up():
    # Down Thrusts Move Forwards #
    set_thruster("DRF", NEUTRAL + SPEED)
    set_thruster("DRB", NEUTRAL + SPEED)
    set_thruster("DLF", NEUTRAL + SPEED)
    set_thruster("DLB", NEUTRAL + SPEED)

    # Upper Thrusts Move Backwards  #
    set_thruster("URF", NEUTRAL - SPEED)
    set_thruster("URB", NEUTRAL - SPEED)
    set_thruster("ULF", NEUTRAL - SPEED)
    set_thruster("ULB", NEUTRAL - SPEED)

    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.05)
        
def moving_down():
    # Down Thrusts Move Backwards  #
    set_thruster("DRF", NEUTRAL - SPEED)
    set_thruster("DRB", NEUTRAL - SPEED)
    set_thruster("DLF", NEUTRAL - SPEED)
    set_thruster("DLB", NEUTRAL - SPEED)

    # Upper Thrusts Move Forwards  #
    set_thruster("URF", NEUTRAL + SPEED)
    set_thruster("URB", NEUTRAL + SPEED)
    set_thruster("ULF", NEUTRAL + SPEED)
    set_thruster("ULB", NEUTRAL + SPEED)

    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.05)

def rotate_left():
    # Moving Forward Without AntiForce To Left #
    set_thruster("ULB", NEUTRAL + SPEED)
    set_thruster("DLB", NEUTRAL + SPEED)
    set_thruster("URF", NEUTRAL + SPEED)
    set_thruster("DRF", NEUTRAL + SPEED)
   
    # Moving Backward With Forward Moving To Left #
    set_thruster("URB", NEUTRAL - SPEED)
    set_thruster("DRB", NEUTRAL - SPEED)
    set_thruster("ULF", NEUTRAL - SPEED)
    set_thruster("DLF", NEUTRAL - SPEED)

    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.05)
        
def rotate_right():
    # Moving Forward Without AntiForce To Right #
    set_thruster("ULB", NEUTRAL - SPEED)
    set_thruster("DLB", NEUTRAL - SPEED)
    set_thruster("URF", NEUTRAL - SPEED)
    set_thruster("DRF", NEUTRAL - SPEED)
 
    # Moving Backward With Forward Moving To Right #
    set_thruster("URB", NEUTRAL + SPEED)
    set_thruster("DRB", NEUTRAL + SPEED)
    set_thruster("ULF", NEUTRAL + SPEED)
    set_thruster("DLF", NEUTRAL + SPEED)

    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.05)
    
def rotate_upward():
    # Moving Forward Without AntiForce To Upward #
    set_thruster("DRF", NEUTRAL + SPEED)
    set_thruster("DLF", NEUTRAL + SPEED)
    set_thruster("URB", NEUTRAL + SPEED)
    set_thruster("ULB", NEUTRAL + SPEED)

    # Moving Backward With Forward Moving To Upward #
    set_thruster("URF", NEUTRAL - SPEED)
    set_thruster("ULF", NEUTRAL - SPEED)
    set_thruster("DRB", NEUTRAL - SPEED)
    set_thruster("DLB", NEUTRAL - SPEED)

    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.05)
    
def rotate_backward():
    # Moving Forward Without AntiForce To Backward #
    set_thruster("URF", NEUTRAL + SPEED)
    set_thruster("ULF", NEUTRAL + SPEED)
    set_thruster("DRB", NEUTRAL + SPEED)
    set_thruster("DLB", NEUTRAL + SPEED)
    
    # Moving Backward With Forward Moving To Backward #
    set_thruster("DRF", NEUTRAL - SPEED)
    set_thruster("DLF", NEUTRAL - SPEED)
    set_thruster("URB", NEUTRAL - SPEED)
    set_thruster("ULB", NEUTRAL - SPEED)

    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.05)
    
def stopping_moving():
    for Ch in Thrusts_List.values():
        pca.set_pulse_us(Ch, NEUTRAL)


try:
    # Controller Function # 
    while True :

    # Update Pygame #
        pg.event.pump()

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
            SPEED = 250  # Full speed when pressing R3 or L3 to move up/down
        elif Stick_Power > DEADZONE:
            SPEED = round(Stick_Power * ACCELERATION)
            SPEED = clamp(SPEED, 250, 0)
            
            print(f"Speed is {SPEED}")
        else:
            SPEED = 0
            stopping_moving()

    # Functionality #    

        # Control Movement X|Z By Right Joystick
        if Right_Joystick_X > DEADZONE and Right_Joystick_X > 0 :       # 1 Mean That I Move The Joystick Right #
            moving_right()
            print("Moving Right")
        elif Right_Joystick_X < -DEADZONE and Right_Joystick_X < 0 :    # -1 Mean That I Move The Joystick Left #
            moving_left()
            print("Moving Left")
        elif Right_Joystick_Y < -DEADZONE and Right_Joystick_Y < 0 :    # -1 Mean That I Move The Joystick Up #
            moving_forward()
            print("Moving Forward")
        elif Right_Joystick_Y > DEADZONE and Right_Joystick_Y > 0 :     # 1 Mean That I Move The Joystick Down #
            moving_backward()
            print("Moving Backward")

        # Control Movement Y By L3 | R3 #
        if R1 == 1 :
            moving_up()
            print("Moving Up")
        elif L1 == 1 :
            moving_down()
            print("Moving Down")
        
        # Control Rotation By Left Joystick        
        if Left_Joystick_X > DEADZONE and Left_Joystick_X > 0 :
            rotate_right()
            print("rotate right")
        elif Left_Joystick_X < -DEADZONE and Left_Joystick_X < 0 :
            rotate_left()
            print("rotate Left")
        elif Left_Joystick_Y < -DEADZONE and Left_Joystick_Y < 0 :
            rotate_upward()
            print("rotate Upward")
        elif Left_Joystick_Y > DEADZONE and Left_Joystick_Y > 0 :
            rotate_backward()
            print("rotate Backward")

except KeyboardInterrupt:
    time.sleep(0.05)
        
finally:
    stopping_moving()
