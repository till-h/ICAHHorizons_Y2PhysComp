'''
Pin config:
Right motor:
Left motor:
Right LS:
Left LS:
USS:
'''


from gpiozero import DistanceSensor, LED
from time import sleep

sensor = DistanceSensor(echo=20, trigger=21, queue_len=1)
led = LED(pin=18)

led.blink(0.5,0.5,2,False)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(1)
