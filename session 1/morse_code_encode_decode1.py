import gpiozero
from morse_code import morse_to_text, text_to_morse, try_encode, try_decode
from time import time, sleep
from threading import Thread

DOT = 0.005 # short Morse symbol
DASH = 3 * DOT # long Morse symbol
GAP = DOT # gap between symbols
NEWLETTER = 3 * DOT - GAP # gap between letters
NEWWORD = 7 * DOT # between words

def encode(clear_text):
	morse_list = [try_encode(letter) + " "  for letter in clear_text]
	morse_text = "".join(morse_list)
	return morse_text

def test_encode(clear_text):
	morse_code = encode(clear_text)
	print("Encoder is sending: " + clear_text + " => " + morse_code)
	with gpiozero.LED(4) as led:
		for c in morse_code:
			if c == "-":
				led.on()
				sleep(DASH)
				led.off()
				sleep(GAP)
			elif c == ".":
				led.on()
				sleep(DOT)
				led.off()
				sleep(GAP)
			elif c == " ":
				sleep(NEWLETTER)


def decode():
	inp = gpiozero.DigitalInputDevice(17)
	buf = ""
	while True:
		inp.wait_for_inactive()
		t0 = time()
		inp.wait_for_active()
		t1 = time()
		inp.wait_for_inactive()
		t2 = time()
		pause_dur = round((t1 - t0) / DOT)
		symbol_dur = round((t2 - t1) / DOT)
		print(pause_dur, symbol_dur)
		if pause_dur == 3:
			print(try_decode(buf))
			buf = ""
		if symbol_dur == 1:
			buf = buf + "."
		elif symbol_dur == 3:
			buf = buf + "-"
		
		

if __name__ == "__main__":
	t1 = Thread(target=test_encode, args=["MEPHISTOOOPHELES"], daemon=False)
	t2 = Thread(target=decode, daemon=False)
	t2.start()
	t1.start()
	sleep(3)
	
	#test_encode("SOS")
