from gpiozero import Robot, DistanceSensor, LED
from time import sleep
#Import the library with all the functions needed
led = LED(pin=18)
#Use the LED object, calling it 'led'
led.blink(0.5, 0.5,  None, True)
#on for 0.5 seconds, off for 0.5 seconds, run continuously, run in the background

leftPins = (12, 16)
rightPins = (23, 24)
#Define what BCM pins the motor drivers are connected to

robot = Robot(left=leftPins, right=rightPins)
#Define the robot object

while True:
    # Continuously perform the following function
    robot.forward()
    sleep(3)
    # Go forward for 3 seconds

    robot.backward()
    sleep(3)
    # Go backward for 3 seconds
    # robot functions allows you to put in a speed between 0 and 1. 1 being the max and the default

    robot.left()
    sleep(3)
    # turn left for 3 seconds

    robot.right()
    sleep(3)
    # turn right for 3 seconds
    robot.stop()
    sleep(3)
    # stop for 3 seconds
