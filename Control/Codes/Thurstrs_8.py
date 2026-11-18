# Imports #
import time
import pygame as pg
from pca9685 import PCA9685

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


# Valuables #
MAX_US = 1750  # Upper That 1500 Will Move Forward
MIN_US = 1250  # Lower That 1500 Will Move backward
NEUTRAL = 1500  # It Will Stop Moving
DEADZONE = 0.1 # It Will Ignore If The JoyStick Is Stick Drift
SPEED = 100  # PLaceHolder



# PCA9685 controller instance
pca = PCA9685()

# Thrusts Names #
Thrusts_List = {"URF": 0, "ULF": 1, "DRF": 2, "DLF": 3, "URB": 4, "ULB": 5, "DRB": 6, "DLB": 7}

# Functional #
def moving_forward():
    # Front Thrusts Move Forwards
    pca.set_pulse_us(Thrusts_List["URF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["ULF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DRF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DLF"], NEUTRAL + SPEED)
    print("All Front Thrusts Moved Forwards")
    # Back Thrusts Move Backwards
    pca.set_pulse_us(Thrusts_List["URB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["ULB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DRB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DLB"], NEUTRAL - SPEED)
    print("All Back Thrusts Moved Backwards")
    # Delay Time To Avoid Hardware Conflict  #
    

def moving_backward():
    # Front Thrusts Move Backwards
    pca.set_pulse_us(Thrusts_List["URF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["ULF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DRF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DLF"], NEUTRAL - SPEED)
    print("All Front Thrusts Moved Backwards")
    # Back Thrusts Move Forwards
    pca.set_pulse_us(Thrusts_List["URB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["ULB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DRB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DLB"], NEUTRAL + SPEED)
    print("All Back Thrusts Moved Forwards")
    
def moving_left():
    # Left Thrusts Move Forwards #
    pca.set_pulse_us(Thrusts_List["ULF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["ULB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DLF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DLB"], NEUTRAL - SPEED)
    print("All Left Thrusts Moved Forwards ")
    # Right Thrusts Move Backwards #
    pca.set_pulse_us(Thrusts_List["URF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["URB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DRF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DRB"], NEUTRAL + SPEED)
    print("All Right Thrusts Moved Backwards")
    
def moving_right():
    # Left Thrusts Move Backwards #
    pca.set_pulse_us(Thrusts_List["ULF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["ULB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DLF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DLB"], NEUTRAL + SPEED)
    print("All Left Thrusts Moved Backwards ")
    # Right Thrusts Move Forwards #
    pca.set_pulse_us(Thrusts_List["URF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["URB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DRF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DRB"], NEUTRAL - SPEED)  
    print("All Right Thrusts Moved Forwards ")
    
def moving_up():
    # Down Thrusts Move Forwards #
    pca.set_pulse_us(Thrusts_List["DRF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DRB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DLF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DLB"], NEUTRAL + SPEED)
    print("All Down Thrusts Moved Forwards ")
    # Upper Thrusts Move Backwards  #
    pca.set_pulse_us(Thrusts_List["URF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["URB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["ULF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["ULB"], NEUTRAL - SPEED)
    print("All Upper Thrusts Moved Backwards ")
    
def moving_down():
    # Down Thrusts Move Backwards  #
    pca.set_pulse_us(Thrusts_List["DRF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DRB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DLF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DLB"], NEUTRAL - SPEED)
    print("All Down Thrusts Moved Backwards ")
    # Upper Thrusts Move Forwards  #
    pca.set_pulse_us(Thrusts_List["URF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["URB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["ULF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["ULB"], NEUTRAL + SPEED)
    print("All Upper Thrusts Moved Forwards ")


def rotate_left():
    # Moving Forward Without AntiForce To Left #
    pca.set_pulse_us(Thrusts_List["ULB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DLB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["URF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DRF"], NEUTRAL + SPEED)
    print("Moving Forward Without AntiForce To Left")
    
    # Moving Backward With Forward Moving To Left #
    pca.set_pulse_us(Thrusts_List["URB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DRB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["ULF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DLF"], NEUTRAL - SPEED)
    print("Moving Backward With Forward Moving To Left")
    
def rotate_right():
    # Moving Forward Without AntiForce To Right #
    pca.set_pulse_us(Thrusts_List["ULB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DLB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["URF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DRF"], NEUTRAL - SPEED)
    print("Moving Forward Without AntiForce To Right")
    
    # Moving Backward With Forward Moving To Right #
    pca.set_pulse_us(Thrusts_List["URB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DRB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["ULF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DLF"], NEUTRAL + SPEED)
    print("Moving Backward With Forward Moving To Right")

def rotate_upward():
    # Moving Forward Without AntiForce To Upward #
    pca.set_pulse_us(Thrusts_List["DRF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DLF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["URB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["ULB"], NEUTRAL + SPEED)
    print("Moving Forward Without AntiForce To Upward")
    
    # Moving Backward With Forward Moving To Upward #
    pca.set_pulse_us(Thrusts_List["URF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["ULF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DRB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DLB"], NEUTRAL - SPEED)
    print("Moving Backward With Forward Moving To Upward")

def rotate_backward():
    # Moving Forward Without AntiForce To Backward #
    pca.set_pulse_us(Thrusts_List["URF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["ULF"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DRB"], NEUTRAL + SPEED)
    pca.set_pulse_us(Thrusts_List["DLB"], NEUTRAL + SPEED)

    print("Moving Forward Without AntiForce To Backward")
    
    # Moving Backward With Forward Moving To Backward #
    pca.set_pulse_us(Thrusts_List["DRF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["DLF"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["URB"], NEUTRAL - SPEED)
    pca.set_pulse_us(Thrusts_List["ULB"], NEUTRAL - SPEED)
    print("Moving Backward With Forward Moving To Backward")

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
        left_Joystick_X = Controller.get_axis(0)
        left_Joystick_Y = Controller.get_axis(1)

    # Special Trigger
        Right_Joystick_R3 = Controller.get_button(9)
        Left_Joystick_L3 = Controller.get_button(8)

    # Functionality #    

        # Control Movement X|Z By Right Joystick
        if Right_Joystick_X > DEADZONE and Right_Joystick_X > 0 :
            moving_right()
        elif Right_Joystick_X < -DEADZONE and Right_Joystick_X < 0 :
            moving_left()
        elif Right_Joystick_Y < -DEADZONE and Right_Joystick_Y < 0 : 
            moving_forward()
        elif Right_Joystick_Y > DEADZONE and Right_Joystick_Y > 0 :
            moving_backward()

        # Control Movement Y By L3 | R3 #
        if Right_Joystick_R3 == 1 :
            moving_up()
        elif Left_Joystick_L3 == 1 :
            moving_down()
        
        # Control Rotation By Left Joystick        
        if left_Joystick_X > DEADZONE and left_Joystick_X > 0 :
            rotate_right()
        elif left_Joystick_X < -DEADZONE and left_Joystick_X < 0 :
            rotate_left()
        elif left_Joystick_Y < -DEADZONE and left_Joystick_Y < 0 :
            rotate_upward()
        elif left_Joystick_Y > DEADZONE and left_Joystick_Y > 0 :
            rotate_backward()

        time.sleep(1)
        
finally:
    stopping_moving()