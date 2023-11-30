#!/usr/bin/env python3

import sys

# Define a dictionary that maps color names to HSL values
color_dict_hsl = {
    "red": (0, 100, 50),
    "green": (120, 100, 50),
    "blue": (240, 100, 50),
    "white": (0, 0, 100),
    "black": (0, 0, 0),
    # Add more color mappings as needed
}

def color_to_hsl(color_name):
    # Convert the input color name to lowercase for case-insensitive matching
    color_name = color_name.lower()

    # Check if the color_name exists in the dictionary
    if color_name in color_dict_hsl:
        return color_dict_hsl[color_name]
    else:
        return None  # Return None for undefined colours

def main():
    # Check if a color name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./color_to_hsl.py <color>")
        sys.exit(1)

    color_name = sys.argv[1]
    hsl_value = color_to_hsl(color_name)

    if hsl_value is not None:
        print(f"The HSL values for {color_name} are {hsl_value}")
    else:
        print(f"Color '{color_name}' is not defined in the HSL dictionary.")

if __name__ == "__main__":
    main()

