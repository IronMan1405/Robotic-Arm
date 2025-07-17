from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)

##kit.servo[0].angle = 0
##print("set claw servo to 0")
##
##sleep(3)

kit.servo[0].angle = 95
print("set claw servo to 95")

sleep(3)

kit.servo[0].angle = 180
print("set claw servo to 180")
