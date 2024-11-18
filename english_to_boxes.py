"""
This Python file defines two functions, an encoder and a decoder,
that converts plaintext into spooky blackbox blocks and back.
"""

def encoder():
    user_input = input("Enter a string to be black-box-ified: ")
    output = ""

    zero = '\u2591'
    one = '\u2592'
    two = '\u2593'
    three = '\u2588'

    ranges = [0,2,4,6]

    for char in user_input:
        char_ascii = ord(char)
        char_binary = bin(char_ascii)
        char_binary = char_binary[2:] # drop the '0b' at the front
        while len(char_binary) < 8: # add a missing 0 at the front
            char_binary = '0'+char_binary
        for myrange in ranges:
            snip = char_binary[myrange:myrange+2]
            match snip:
                case '00':
                    output += zero
                case '01':
                    output += one
                case '10':
                    output += two
                case '11':
                    output += three
    print(output)

def decoder():
    user_input = input("Enter faux-binary string to be decoded: ")
    output = ""
    char_bin = ""

    zero = '\u2591'
    one = '\u2592'
    two = '\u2593'
    three = '\u2588'
    for char in user_input:
        if char == zero:
            char_bin += "00"
        elif char == one:
            char_bin += "01"
        elif char == two:
            char_bin += "10"
        elif char == three:
            char_bin += "11"
        if len(char_bin) == 8: # assembled a bin number, turn to ascii
            char_ascii = int(char_bin, 2)
            output += chr(char_ascii)
            char_bin = ""
    print(output)

def main():
    user_choice = input("Encode or decode? ")
    if user_choice.lower() == "encode":
        encoder()
    elif user_choice.lower() == "decode":
        decoder()
    else: print("That is not a legitimate option")

main()