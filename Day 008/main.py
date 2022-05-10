# ==========================================
# Day 008 - Project: Caesar Cipher
# ==========================================

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


def encode(message, offset):
    message_list = list(message)
    result = ""

    for pos, char in enumerate(message_list):
        pos_str = letters.index(char)
        if (pos_str + offset) >= len(letters):
            new_index = pos_str + offset - len(letters) + 1
        else:
            new_index = pos_str + offset
        result += letters[new_index]

    print(f"Here is the encoded result: {result}")


def decode(message, offset):
    message_list = list(message)
    result = ""

    for pos, char in enumerate(message_list):
        pos_str = letters.index(char)
        if (pos_str - offset) < 0:
            new_index = pos_str - offset + len(letters) - 1
        else:
            new_index = pos_str - offset
        result += letters[new_index]

    print(f"Here is the encoded result: {result}")


selection = ""

while selection != "no":
    selection = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    message = input("Type your message: ")
    offset = int(input("Type the shift number: "))

    if selection == "encode":
        encode(message, offset)
    else:
        decode(message, offset)
    selection = input("Type 'yes' if you want to go again, otherwise type 'no': ")
