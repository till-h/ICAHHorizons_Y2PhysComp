from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=4, queue_len=1)
print("RR")
while True:
    print('Distance: ', sensor.distance)
    sleep(1)
