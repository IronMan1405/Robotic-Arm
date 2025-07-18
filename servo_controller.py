from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)

clawServo = 0
wristServo = 1

def setServoAngle(servoChannel, angle):
    angle = max(0, min(180, angle))
    kit.servo[servoChannel].angle = angle