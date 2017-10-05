#!/usr/bin/python3

# Lookup table for morse code to text
morse_to_text = {
    ".-":    "A",
    "-...":    "B",
    "-.-.":    "C",
    "-..":    "D",
    ".":    "E",
    "..-.":    "F",
    "--.":    "G",
    "....":    "H",
    "..":    "I",
    ".---":    "J",
    "-.-":    "K",
    ".-..":    "L",
    "--":    "M",
    "-.":    "N",
    "---":    "O",
    ".--.":    "P",
    "--.-":    "Q",
    ".-.":    "R",
    "...":    "S",
    "-":    "T",
    "..-":    "U",
    "...-":    "V",
    ".--":    "W",
    "-..-":    "X",
    "-.--":    "Y",
    "--..":    "Z",
    ".----":    "1",
    "..---":    "2",
    "...--":    "3",
    "....-":    "4",
    ".....":    "5",
    "-....":    "6",
    "--...":    "7",
    "---..":    "8",
    "----.":    "9",
    "-----":    "0"
}

# Lookup table for morse code to text
text_to_morse = dict([[v,k] for k,v in morse_to_text.items()])

def try_decode(morse_symbol):
    if morse_symbol in morse_to_text.keys():
        return morse_to_text[morse_symbol]
        
def try_encode(letter):
    if letter in text_to_morse.keys():
        return text_to_morse[letter]

if __name__ == "__main__":
	print("Loaded morse code lookup table in morse_code.py")
