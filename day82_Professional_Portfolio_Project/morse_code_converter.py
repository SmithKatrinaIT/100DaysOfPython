'''
 Portfolio Item:1 Morse Code Converter
 	- text-based program
 	-Concepts Used:
 		- input()
 		- print()
 		- conditionals: if/elif/else
 		- for loop
 		- split()
 		- upper()
 		- dictionary {key: value} pair
 		- functions

'''

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
			result = result + "/ "

		elif letter in morse_code:
			result = result + morse_code[letter] + " "

	return result


# Convert Morse code back to normal text
def morse_to_text(morse):
	result = ""

	codes = morse.split(" ")

	for code in codes:

		if code == "/":
			result = result + " "

		else:
			for letter in morse_code:

				if morse_code[letter] == code:
					result = result + letter

	return result


# Main program
while True:

	print()
	print("MORSE CODE CONVERTER")
	print("--------------------")
	print("1 - Text to Morse Code")
	print("2 - Morse Code to Text (** Remember to include a space between letters)")
	print("3 - Exit")

	choice = input("Enter 1, 2, or 3: ")

	if choice == "1":

		message = input("Enter your message: ")

		converted_message = text_to_morse(message)

		print("Morse Code:")
		print(converted_message)

	elif choice == "2":

		message = input("Enter Morse code: ")

		converted_message = morse_to_text(message)

		print("Text:")
		print(converted_message)

	elif choice == "3":

		print("Exiting Morse Code Converter.")
		break

	else:
		print("Invalid choice. Please enter 1, 2, or 3.")
