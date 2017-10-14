'''
ICAHSensor - a minimal distance sensor (HC-SR04) interface
for use in ICAH workshops.

Till Hackler, David Miller 2017

'''
from gpiozero import DigitalInputDevice, DigitalOutputDevice
from time import time, sleep

class ICAHSensor:
	ping_dur = 0.00015 # s, same as measured for gpiozero
	speed_of_sound = 343 # m/s at 101325 Pa, 293 K

	def __init__(self, trig, echo):
		self.trig = DigitalOutputDevice(trig)
		self.echo = DigitalInputDevice(echo)
		self.hist = []

	def get_distance(self):
		'''
		This could be made non-blocking by using a background
		thread that continually updates the current distance.

		We should also reject outliers in the distance measurements
		using the filter() function or similar.
		'''

		del(hist[:])

		for i in range(10):

			self.trig.on()
			sleep(ping_dur)
			self.trig.off()

			self.echo.wait_for_active()
			t0 = time()
			self.echo.wait_for_inactive()
			dt = time() - t0

			dist = dt * speed_of_sound / 2
			self.hist.append(dist)

		return sum(self.hist) / len(self.hist)
	
