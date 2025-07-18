from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)

kit.servo[3].angle = 0
print("set servo to 0")
sleep(3)

kit.servo[3].angle = 90
print("set servo to 90")
sleep(3)

kit.servo[3].angle = 180
print("set servo to 180")
sleep(3)

while True:
    kit.servo[3].angle = 90
    print('indefinitely set angle to 90')
    sleep(3)
