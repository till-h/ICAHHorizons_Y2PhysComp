'''
Pin config:
Right motor:
Left motor:
Right LS:
Left LS:
USS:
'''

import gpiozero
from ICAHSensor import ICAHSensor

sensor = ICAHSensor(trig=21,echo=20)

while True:
	print(sensor.get_distance())
