import gpiozero
from morse_code import morse_to_text, text_to_morse, try_encode, try_decode
from time import time, sleep
from threading import Thread

def encode(clear_text):
	morse_list = [try_encode(letter) for letter in clear_text]
	morse_text = "".join(morse_list)
	return morse_text

def test_encode(clear_text):
	morse_code = encode(clear_text)
	print(morse_code)
	led = gpiozero.LED(14)
	for c in morse_code:
		led.on()
		if c == "-":
			sleep(0.3)
		elif c == ".":
			sleep(0.05)
		led.off()
		sleep(1)

def decode():
	inp = gpiozero.LightSensor(15, charge_time_limit = 0.001)
	while True:
		inp.wait_for_light()
		print("ON")
		inp.wait_for_dark()
		print("OFF")

if __name__ == "__main__":
	t1 = Thread(target=test_encode, args=["SOS"], daemon=False)
	t2 = Thread(target=decode, daemon=True)
	t1.start()
	t2.start()
	#test_encode("SOS")
