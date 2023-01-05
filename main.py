from code import morse_code
from art import logo

print(logo)
user_input = input("Translate to Morse Code: ").upper()

result = []


def cipher():
    try:
        for char in user_input:

            result.append(morse_code[char])

    except KeyError:
        print("Error, invalid input")


cipher()
print(' '.join(result))
