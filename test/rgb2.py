#!/usr/bin/env python3

import sys
import webcolors

def color_to_rgb(color_name):
    try:
        rgb = webcolors.name_to_rgb(color_name)
        return rgb
    except ValueError:
        return None

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
        print(f"Color '{color_name}' is not defined in the webcolors module.")

if __name__ == "__main__":
    main()

