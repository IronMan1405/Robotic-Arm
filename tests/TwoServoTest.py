import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)
        
max_0 = 180
max_1 = 135
step = 5
total_steps = min(max_0, max_1)

kit.servo[0].angle = 0
kit.servo[1].angle = 0
print("Set both servos to 0")
time.sleep(2)

while True:
    for angle in range(0, 185, step):
        kit.servo[0].angle = angle    
        kit.servo[1].angle = angle
        print(f"servo 0: {angle}")
        print(f"servo 1: {angle}")
    ##    time.sleep(0.5)

