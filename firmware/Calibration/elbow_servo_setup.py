from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)

kit.servo[4].angle = 0
print("set angle to 0")
sleep(3)

kit.servo[4].angle = 90
print("set angle to 90")
sleep(3)

kit.servo[4].angle = 180
print("set angle to 180")
sleep(3)
