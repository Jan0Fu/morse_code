from code import morse_code
from art import logo

print(logo)
user_input = input("Translate to Morse Code: ").upper()

code_message = []


def cipher():
    try:
        for letter in user_input:
            code_message.append(morse_code[letter])

    except KeyError:
        print("Error, invalid input")


cipher()
print(' '.join(code_message))
