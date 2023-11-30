#!/usr/bin/env python3

import sys

# Define a dictionary that maps color names to RGB values
color_dict = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    # Add more color mappings as needed
}

def color_to_rgb(color_name):
    # Convert the input color name to lowercase for case-insensitive matching
    color_name = color_name.lower()

    # Check if the color_name exists in the dictionary
    if color_name in color_dict:
        return color_dict[color_name]
    else:
        return None  # Return None for undefined colours

def main():
    # Check if a color name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./color_to_rgb.py <color>")
        sys.exit(1)

    color_name = sys.argv[1]
    rgb = color_to_rgb(color_name)

    if rgb is not None:
        print(f"The RGB color code for {color_name} is {rgb}")
    else:
        print(f"Color '{color_name}' is not defined in the dictionary.")

if __name__ == "__main__":
    main()

