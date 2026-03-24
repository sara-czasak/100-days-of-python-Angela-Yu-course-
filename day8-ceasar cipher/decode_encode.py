import string

alphabet = list(string.ascii_lowercase)


def decode(message, shift):

    decoded = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index + shift
            if new_index >= len(alphabet):
                new_index = new_index % len(alphabet)
                letter = alphabet[new_index]
                decoded += letter
            else:
                letter = alphabet[new_index]
                decoded += letter
        elif letter == " ":
            letter = " "
            decoded += letter
        elif letter == ".":
            decoded += letter
            letter = "."
    decoded = "".join(decoded)
    return decoded

def encode(message, shift):
    encoded = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index - shift
            if new_index > len(alphabet):
                new_index = new_index % len(alphabet)
            letter = alphabet[new_index]
            encoded += letter
        elif letter == " ":
            encoded += " "
        elif letter == ".":
            encoded += "."
    encoded = "".join(encoded)
    return encoded

