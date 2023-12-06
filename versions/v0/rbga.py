#!/usr/bin/env python3

import sys

# Define a dictionary that maps color names to RGBA values
color_dict_rgba = {
    "red": (255, 0, 0, 255),
    "green": (0, 255, 0, 255),
    "blue": (0, 0, 255, 255),
    "white": (255, 255, 255, 255),
    "black": (0, 0, 0, 255),
    # Add more color mappings as needed
}

def color_to_rgba(color_name):
    # Convert the input color name to lowercase for case-insensitive matching
    color_name = color_name.lower()

    # Check if the color_name exists in the dictionary
    if color_name in color_dict_rgba:
        return color_dict_rgba[color_name]
    else:
        return None  # Return None for undefined colours

def main():
    # Check if a color name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./color_to_rgba.py <color>")
        sys.exit(1)

    color_name = sys.argv[1]
    rgba_value = color_to_rgba(color_name)

    if rgba_value is not None:
        print(f"The RGBA values for {color_name} are {rgba_value}")
    else:
        print(f"Color '{color_name}' is not defined in the RGBA dictionary.")

if __name__ == "__main__":
    main()

