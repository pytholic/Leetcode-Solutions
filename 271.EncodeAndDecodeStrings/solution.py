"""
DESCRIPTION:

Design an algorithm to encode a list of strings to a string. The 
encoded string is then sent over the network and is decoded back 
to the original list of strings.

EXAMPLE:

Input = ["lint", "code", "love", "you"]
Output = ["lint", "code", "love", "you"]

"""


def encode(strs: list[str]) -> str:
    encoded_string = ""
    for s in strs:
        encoded_string += s + "\n"
    return encoded_string


def decode(encoded_string):
    decoded_string = []
    s = ""
    for char in encoded_string:
        if char != "\n":
            s += char
        else:
            decoded_string.append(s)
            s = ""
    return decoded_string


strs = ["lint", "code", "love", "you"]
encoded_string = encode(strs)
decoded_string = decode(encoded_string)
print(encoded_string)
print(decoded_string)
