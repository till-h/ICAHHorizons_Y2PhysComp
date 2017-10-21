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
