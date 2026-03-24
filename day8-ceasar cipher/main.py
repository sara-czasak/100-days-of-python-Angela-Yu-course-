from decode_encode import *
import string

print("*** WELCOME TO SECRET MESSAGE ***")
print("-"*30)
alphabet = list(string.ascii_lowercase)



on = True

while on:
    type = input("Do you need to do:\n- D decode a message\n- E encode a message\n").lower()
    if "d" in type:
        print("*** DECODE MODE ***")
        print("-" * 30)
        message = input("Please provide the message you wish to decode: ")
        shift = int(input("Please provide the shift amount you wish to shift the message: "))
        print(f"*** DECODED MESSAGE ***\n{decode(message, shift)}")

    elif "e" in type:
        print("*** ENCODE MODE ***")
        print("-" * 30)
        message = input("Please provide the message you wish to encode: ")
        shift = int(input("Please provide the shift amount you wish to shift the message: "))
        print(encode(message, shift))
        print(f"*** ENCODED MESSAGE ***\n{encode(message, shift)}")
    again = input("Any other messages I can help with? (Y/N) ").lower()
    if again == "y":
        on = True
    else:
        print("See you next time!")
        on = False

print("*** BYE ***")