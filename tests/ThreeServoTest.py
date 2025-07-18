import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)
        


kit.servo[0].angle = 95
kit.servo[1].angle = 0
kit.servo[2].angle = 0

print("Set all servos to 0")
time.sleep(2)

while True:
    for angle in range(0, 185, 5):
        kit.servo[0].angle = angle    
        kit.servo[1].angle = angle
        kit.servo[2].angle = angle
        print(f"servo 0: {angle}")
        print(f"servo 1: {angle}")
        print(f"servo 2: {angle}")
    ##    time.sleep(0.5)

