import time
from pca9685 import PCA9685
pca = PCA9685()
try:
    while True:
        for i in range(0, 101, 4): # fade up
            pca.set_duty(0, i / 100) # fraction 0.0 - 1.0 of the period
            time.sleep(0.02)
        for i in range(100, -1, -4): # fade down
            pca.set_duty(0, i / 100)
            time.sleep(0.02)
except KeyboardInterrupt:
    pass
finally:
    pca.set_duty(0, 0) # the chip keeps outputting after the script ends