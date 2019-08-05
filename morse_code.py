# Converts a string of morse code to a string of english and vice versa

from re import fullmatch

morse_dict = {
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
    ".": ".-.-.-",
    "?": "..--..",
    ",": "--..--",
    "!": "-.-.--"
}

# example
# .. / .- -- / ..-. .. -. . .-.-.- / .... --- .-- / .- .-. . / -.-- --- ..- ..--..

input_string = input('Enter a string: ').strip().lower()
input_list = input_string.split()
total_string = ''
if fullmatch('[. -/]*', input_string):
    for entry in input_list:
        if entry == '/':
            total_string += ' '
            continue
        for key, value in morse_dict.items():
            if value == entry:
                total_string += key
else:
    for entry in input_list:
        for letter in entry:
            total_string += morse_dict.get(letter) + ' '
        total_string += '/ '
total_string = total_string.capitalize()
print(total_string)
