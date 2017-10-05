import gpiozero
from morse_code import morse_to_text, text_to_morse, try_encode, try_decode
from time import time, sleep
from threading import Thread

DOT = 0.1 # short Morse symbol
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
		#inp.wait_for_inactive()
		t0 = time()
		inp.wait_for_active()
		t1 = time()
		inp.wait_for_inactive()
		t2 = time()
		pause_dur = t1 - t0
		symbol_dur = t2 - t1
		print(pause_dur / DOT, symbol_dur / DOT)
		if abs(pause_dur / GAP - 1) < .2: # are inside same letter
			if abs(symbol_dur / DOT - 1) < .2: # its a dot
				buf = buf + "."
			else: # its a dash
				buf = buf +  "-"
		else:
			print(buf)
			if try_decode(buf) != None:
				print(try_decode(buf))
				buf = ""
		

if __name__ == "__main__":
	t1 = Thread(target=test_encode, args=["SOS"], daemon=False)
	t2 = Thread(target=decode, daemon=True)
	t2.start()
	sleep(.3)
	t1.start()
	
	#test_encode("SOS")
