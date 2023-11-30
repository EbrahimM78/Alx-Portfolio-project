#!/usr/bin/env python3

import sys

# Define a dictionary that maps color names to Hex values
color_dict_hex = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "white": "#FFFFFF",
    "black": "#000000",
    # Add more color mappings as needed
}

def color_to_hex(color_name):
    # Convert the input color name to lowercase for case-insensitive matching
    color_name = color_name.lower()

    # Check if the color_name exists in the dictionary
    if color_name in color_dict_hex:
        return color_dict_hex[color_name]
    else:
        return None  # Return None for undefined colours

def main():
    # Check if a color name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./color_to_hex.py <color>")
        sys.exit(1)

    color_name = sys.argv[1]
    hex_value = color_to_hex(color_name)

    if hex_value is not None:
        print(f"The Hex value for {color_name} is {hex_value}")
    else:
        print(f"Color '{color_name}' is not defined in the Hex dictionary.")

if __name__ == "__main__":
    main()

