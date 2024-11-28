"""

Copyright (C) 2024 Jason Wu

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>


This Python file defines two functions, an encoder and a decoder,
that converts plaintext into spooky blackbox blocks and back.
"""

def encoder(user_input: str):
    """
    The encoder takes in an English string and turns it into a mass of blackboxes.
    """
    #user_input = input("Enter a string to be black-box-ified: ")
    #print(len(user_input))
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
    #print(output)
    #print(len(output))
    return output

def decoder(user_input: str):
    """
    The decoder takes in a block of blackboxes and returns English text.
    """
    #user_input = input("Enter faux-binary string to be decoded: ")
    #print(len(user_input))
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
    #print(output)
    #print(len(output))
    return output

def debug(user_input: str):
    """debug function to check if decoder() truncated its input"""
    print(len(user_input))
    output = decoder(encoder(user_input))
    print(len(output))
    return output

def debug2():
    """debug function 2"""
    long_ass_mf = input("Long string here: ")
    print(len(long_ass_mf))
    print("END")
    return "Debug ends"

def main():
    """
    Main function
    """
    choice = input("Encode or decode? ").lower()
    user_input = input("Your English or faux-binary here: ")
    #print(f"Len of input is: {len(user_input)}")
    if choice == "encode":
        print(encoder(user_input))
    elif choice == "decode":
        print(decoder(user_input))
    elif choice == "debug":
        print(debug(user_input))
    else:
        print("Ineligible option.")


if __name__ == "__main__":
    main()
