
morse_code = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",

	"0": "-----",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----.",

	".": ".-.-.-",
	",": "--..--",
	"?": "..--..",
	"!": "-.-.--",
	"'": ".----.",
	"/": "-..-.",
	"(": "-.--.",
	")": "-.--.-",
	"&": ".-...",
	":": "---...",
	";": "-.-.-.",
	"=": "-...-",
	"+": ".-.-.",
	"-": "-....-",
	"_": "..--.-",
	'"': ".-..-.",
	"$": "...-..-",
	"@": ".--.-."
}


# Convert normal text to Morse code
def text_to_morse(text):
	text = text.upper()

	result = ""

	for letter in text:

		if letter == " ":
			result += "/ "

		elif letter in morse_code:
			result += morse_code[letter] + " "

	return result.strip()


# Convert Morse code back to normal text
def morse_to_text(morse):
	result = ""

	codes = morse.split(" ")

	for code in codes:

		if code == "/":
			result += " "

		else:
			for letter, morse_value in morse_code.items():
				if morse_value == code:
					result += letter
					break

	return result



