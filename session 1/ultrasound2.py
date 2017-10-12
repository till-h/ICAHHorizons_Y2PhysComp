import gpiozero
from time import time,sleep
trig = gpiozero.DigitalOutputDevice(4)
echo = gpiozero.DigitalInputDevice(18)
dat = []
i = 0
while True:
	trig.on()
	sleep(0.15/1000)
	trig.off()
	print("activation")
	echo.wait_for_active()
	t0 = time()
	print("falling")
	echo.wait_for_inactive()
	t1 = time() - t0
	distance = t1 * 330 / 2
	dat.insert(0, distance)
	i = i + 1
	print(i, '\t', sum(dat) / len(dat))
	if len(dat) > 10:
		dat.pop()
	sleep(.01)
	
