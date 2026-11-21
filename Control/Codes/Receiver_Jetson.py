# imports #
import socket
import json
import time
from pca9685 import PCA9685

# Valuables #
MOVES   = {"Forward": moving_forward, "Backward": moving_backward,"Left": moving_left, "Right": moving_right}
LIFTS   = {"Up": moving_up, "Down": moving_down}
ROTATES = {"Left": rotate_left, "Right": rotate_right,"Upward": rotate_upward, "Backward": rotate_backward}
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

# Socket Functional #
Sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Sock.bind(("0.0.0.0", 5005))
Sock.settimeout(0.5)


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

# Starting Process #        
try:
    # Heating Up To Avoid Conflict #
    stopping_moving() 
    time.sleep(4)
    
    # Infinity Process #
    while True :    
        try:
            
            # Valuables #
            data,_ = Sock.recvfrom(1024) # Transform Bitys To Data #
            Packet = json.loads(data.decode()) # Load Data #
            SPEED = Packet["Speed"] # Determined Speed #
            if SPEED == 0:
                stopping_moving()
            else:
                
                # Send To Thrusts What In The Packet #
                if Packet["Move"] in MOVES:
                    MOVES[Packet["Move"]]()
                    print(f"Moving {MOVES}")
                if Packet["Lift"] in LIFTS:
                    LIFTS[Packet["Lift"]]()
                    print(f"Lifting {LIFTS}")
                if Packet["Rotation"] in ROTATES:
                    ROTATES[Packet["Rotation"]]()
                    print(f"Rotate {ROTATES}")
        
        # Stop When Packet Is None For --> 0.5s
        except socket.timeout:
            stopping_moving()   
        except (ValueError, KeyError):
            pass

# Ctrl + C Stop All Thrusters #
finally:
    stopping_moving()