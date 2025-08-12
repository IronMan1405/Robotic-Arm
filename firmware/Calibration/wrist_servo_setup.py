from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)

kit.servo[1].angle = 0
print("Set servo to 0")
sleep(3)

kit.servo[1].angle = 90
print("Set servo to 90")
sleep(3)

kit.servo[1].angle = 180
print("Set servo to 180")
sleep(3)


while True:
    kit.servo[1].angle = 90
    print("Set servo to 90 till program terminates")
    sleep(3)
