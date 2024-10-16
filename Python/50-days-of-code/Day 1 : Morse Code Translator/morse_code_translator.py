# Morse Dictionnary
morse_code = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.", 
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
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
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--", 
    "'": ".----.",
    ":": "---...",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "_": "..--.-",
    "=": "-...-",
    "+": ".-.-.",
    "@": ".--.-.",
    '"': ".-..-.",
    ";": "-.-.-.",
    "$": "...-..-",
    "&": ".-...",
    "%": ".--.-.",
    " ": "/"
}

# Translation Function
def translate(latin_string) : 
    length = len(latin_string)
    count = 0
    morse_string = ""
    while count <= length - 1 : 
        character = morse_code[latin_string[count]]
        morse_string = morse_string + character + " "
        count += 1
    return morse_string

# Execution
while 0 != 1 :
    output = translate(input("Enter a string to convert to Morse code (^C to quit) : "))
    print(output)

# My errors during programming
# - I wrote >= instead of <= on the while loop (line 92)

# Possibles improvements : 
# - Handle the case where the user enters an unknown character
# - Use a "for" loop instead of a "while" loop (I only know "while" now)
# - Add characters in the dictionnary