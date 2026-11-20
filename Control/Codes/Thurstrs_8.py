# Imports #
import time
import pygame as pg
from pca9685 import PCA9685
print("Every Thing Imported")

# Valuables #
MAX_US = 1750  # Upper That 1500 Will Move Forward
MIN_US = 1250  # Lower That 1500 Will Move backward
NEUTRAL = 1500  # It Will Stop Moving
DEADZONE = 0.1 # It Will Ignore If The JoyStick Is Stick Drift
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
    set_thruster(Thrusts_List[thrust_name], Safe_US)

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
    print("All Front Thrusts Moved Forwards")
    # Back Thrusts Move Backwards
    set_thruster("URB", NEUTRAL - SPEED)
    set_thruster("ULB", NEUTRAL - SPEED)
    set_thruster("DRB", NEUTRAL - SPEED)
    set_thruster("DLB", NEUTRAL - SPEED)
    print("All Back Thrusts Moved Backwards")
    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.5)
    

def moving_backward():
    # Front Thrusts Move Backwards
    set_thruster("URF", NEUTRAL - SPEED)
    set_thruster("ULF", NEUTRAL - SPEED)
    set_thruster("DRF", NEUTRAL - SPEED)
    set_thruster("DLF", NEUTRAL - SPEED)
    print("All Front Thrusts Moved Backwards")
    # Back Thrusts Move Forwards
    set_thruster("URB", NEUTRAL + SPEED)
    set_thruster("ULB", NEUTRAL + SPEED)
    set_thruster("DRB", NEUTRAL + SPEED)
    set_thruster("DLB", NEUTRAL + SPEED)
    print("All Back Thrusts Moved Forwards")
    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.5)
        
def moving_left():
    # Left Thrusts Move Forwards #
    set_thruster("ULF", NEUTRAL - SPEED)
    set_thruster("ULB", NEUTRAL - SPEED)
    set_thruster("DLF", NEUTRAL - SPEED)
    set_thruster("DLB", NEUTRAL - SPEED)
    print("All Left Thrusts Moved Forwards ")
    # Right Thrusts Move Backwards #
    set_thruster("URF", NEUTRAL + SPEED)
    set_thruster("URB", NEUTRAL + SPEED)
    set_thruster("DRF", NEUTRAL + SPEED)
    set_thruster("DRB", NEUTRAL + SPEED)
    print("All Right Thrusts Moved Backwards")
    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.5)
    
def moving_right():
    # Left Thrusts Move Backwards #
    set_thruster("ULF", NEUTRAL + SPEED)
    set_thruster("ULB", NEUTRAL + SPEED)
    set_thruster("DLF", NEUTRAL + SPEED)
    set_thruster("DLB", NEUTRAL + SPEED)
    print("All Left Thrusts Moved Backwards ")
    # Right Thrusts Move Forwards #
    set_thruster("URF", NEUTRAL - SPEED)
    set_thruster("URB", NEUTRAL - SPEED)
    set_thruster("DRF", NEUTRAL - SPEED)
    set_thruster("DRB", NEUTRAL - SPEED)  
    print("All Right Thrusts Moved Forwards ")
    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.5)
        
def moving_up():
    # Down Thrusts Move Forwards #
    set_thruster("DRF", NEUTRAL + SPEED)
    set_thruster("DRB", NEUTRAL + SPEED)
    set_thruster("DLF", NEUTRAL + SPEED)
    set_thruster("DLB", NEUTRAL + SPEED)
    print("All Down Thrusts Moved Forwards ")
    # Upper Thrusts Move Backwards  #
    set_thruster("URF", NEUTRAL - SPEED)
    set_thruster("URB", NEUTRAL - SPEED)
    set_thruster("ULF", NEUTRAL - SPEED)
    set_thruster("ULB", NEUTRAL - SPEED)
    print("All Upper Thrusts Moved Backwards ")
    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.5)
        
def moving_down():
    # Down Thrusts Move Backwards  #
    set_thruster("DRF", NEUTRAL - SPEED)
    set_thruster("DRB", NEUTRAL - SPEED)
    set_thruster("DLF", NEUTRAL - SPEED)
    set_thruster("DLB", NEUTRAL - SPEED)
    print("All Down Thrusts Moved Backwards ")
    # Upper Thrusts Move Forwards  #
    set_thruster("URF", NEUTRAL + SPEED)
    set_thruster("URB", NEUTRAL + SPEED)
    set_thruster("ULF", NEUTRAL + SPEED)
    set_thruster("ULB", NEUTRAL + SPEED)
    print("All Upper Thrusts Moved Forwards ")
    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.5)

def rotate_left():
    # Moving Forward Without AntiForce To Left #
    set_thruster("ULB", NEUTRAL + SPEED)
    set_thruster("DLB", NEUTRAL + SPEED)
    set_thruster("URF", NEUTRAL + SPEED)
    set_thruster("DRF", NEUTRAL + SPEED)
    print("Moving Forward Without AntiForce To Left")
    
    # Moving Backward With Forward Moving To Left #
    set_thruster("URB", NEUTRAL - SPEED)
    set_thruster("DRB", NEUTRAL - SPEED)
    set_thruster("ULF", NEUTRAL - SPEED)
    set_thruster("DLF", NEUTRAL - SPEED)
    print("Moving Backward With Forward Moving To Left")
    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.5)
        
def rotate_right():
    # Moving Forward Without AntiForce To Right #
    set_thruster("ULB", NEUTRAL - SPEED)
    set_thruster("DLB", NEUTRAL - SPEED)
    set_thruster("URF", NEUTRAL - SPEED)
    set_thruster("DRF", NEUTRAL - SPEED)
    print("Moving Forward Without AntiForce To Right")
    
    # Moving Backward With Forward Moving To Right #
    set_thruster("URB", NEUTRAL + SPEED)
    set_thruster("DRB", NEUTRAL + SPEED)
    set_thruster("ULF", NEUTRAL + SPEED)
    set_thruster("DLF", NEUTRAL + SPEED)
    print("Moving Backward With Forward Moving To Right")
    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.5)
    
def rotate_upward():
    # Moving Forward Without AntiForce To Upward #
    set_thruster("DRF", NEUTRAL + SPEED)
    set_thruster("DLF", NEUTRAL + SPEED)
    set_thruster("URB", NEUTRAL + SPEED)
    set_thruster("ULB", NEUTRAL + SPEED)
    print("Moving Forward Without AntiForce To Upward")
    
    # Moving Backward With Forward Moving To Upward #
    set_thruster("URF", NEUTRAL - SPEED)
    set_thruster("ULF", NEUTRAL - SPEED)
    set_thruster("DRB", NEUTRAL - SPEED)
    set_thruster("DLB", NEUTRAL - SPEED)
    print("Moving Backward With Forward Moving To Upward")
    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.5)
    
def rotate_backward():
    # Moving Forward Without AntiForce To Backward #
    set_thruster("URF", NEUTRAL + SPEED)
    set_thruster("ULF", NEUTRAL + SPEED)
    set_thruster("DRB", NEUTRAL + SPEED)
    set_thruster("DLB", NEUTRAL + SPEED)

    print("Moving Forward Without AntiForce To Backward")
    
    # Moving Backward With Forward Moving To Backward #
    set_thruster("DRF", NEUTRAL - SPEED)
    set_thruster("DLF", NEUTRAL - SPEED)
    set_thruster("URB", NEUTRAL - SPEED)
    set_thruster("ULB", NEUTRAL - SPEED)
    print("Moving Backward With Forward Moving To Backward")
    # Delay Time To Avoid Hardware Conflict  #
    time.sleep(0.5)
    
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
        Right_Joystick_R3 = Controller.get_button(9)
        Left_Joystick_L3 = Controller.get_button(8)
    
    # Speed Controller #
        Stick_Power = max(abs(Right_Joystick_X),abs(Right_Joystick_Y),)

        if Right_Joystick_R3 == 1 or Left_Joystick_L3 == 1:
            SPEED = 250  # Full speed when pressing R3 or L3 to move up/down
        elif Stick_Power > DEADZONE:
            SPEED = int(Stick_Power * ACCELERATION)
            SPEED = clamp(SPEED, 250, 0)
            print(f"Speed is {SPEED}")
        else:
            SPEED = 0
            stopping_moving()

    # Functionality #    

        # Control Movement X|Z By Right Joystick
        if Right_Joystick_X > DEADZONE and Right_Joystick_X > 0 :       # 1 Mean That I Move The Joystick Right #
            moving_right()
        elif Right_Joystick_X < -DEADZONE and Right_Joystick_X < 0 :    # -1 Mean That I Move The Joystick Left #
            moving_left()
        elif Right_Joystick_Y < -DEADZONE and Right_Joystick_Y < 0 :    # -1 Mean That I Move The Joystick Up #
            moving_forward()
        elif Right_Joystick_Y > DEADZONE and Right_Joystick_Y > 0 :     # 1 Mean That I Move The Joystick Down #
            moving_backward()

        # Control Movement Y By L3 | R3 #
        if Right_Joystick_R3 == 1 :
            moving_up()
        elif Left_Joystick_L3 == 1 :
            moving_down()
        
        # Control Rotation By Left Joystick        
        if Left_Joystick_X > DEADZONE and Left_Joystick_X > 0 :
            rotate_right()
        elif Left_Joystick_X < -DEADZONE and Left_Joystick_X < 0 :
            rotate_left()
        elif Left_Joystick_Y < -DEADZONE and Left_Joystick_Y < 0 :
            rotate_upward()
        elif Left_Joystick_Y > DEADZONE and Left_Joystick_Y > 0 :
            rotate_backward()

        time.sleep(0.5)
        
finally:
    stopping_moving()
