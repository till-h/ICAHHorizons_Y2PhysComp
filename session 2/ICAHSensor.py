'''
ICAHSensor - a minimal distance sensor (HC-SR04) interface
for use in ICAH workshops.

Till Hackler, David Miller 2017

'''
from gpiozero import DigitalInputDevice, DigitalOutputDevice
from time import time, sleep

class ICAHSensor:
	rest_dur = 0.01
	ping_dur = 0.000001 # s, same as measured for gpiozero
	speed_of_sound = 343 # m/s at 101325 Pa, 293 K
	call_num = 0

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
		self.call_num = self.call_num+1
		#print("Call No " + str(self.call_num))
		
		del(self.hist[:])

		for i in range(10):
			self.trig.off()
			sleep(self.rest_dur)
			self.trig.on()
			sleep(self.ping_dur)
			self.trig.off()
			#print("wait for active")
			self.echo.wait_for_active(timeout=self.rest_dur)
			t0 = time()
			#print("wait for inactive")
			self.echo.wait_for_inactive(timeout=1)
			dt = time() - t0
			dist = dt * ICAHSensor.speed_of_sound / 2
			
			self.hist.append(dist)

		return sum(self.hist) / len(self.hist)
