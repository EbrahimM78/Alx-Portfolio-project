#!/usr/bin/env python3

import sys
import webcolors
import colorsys

def color_to_rgb(color_name):
    try:
        rgb = webcolors.name_to_rgb(color_name)
        return rgb
    except ValueError:
        return None

def rgb_to_rgba(rgb):
    return rgb + (255,)

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def rgb_to_hsl(rgb):
    h, l, s = colorsys.rgb_to_hls(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)
    return h, s, l

def rgb_to_hsv(rgb):
    h, s, v = colorsys.rgb_to_hsv(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)
    return h, s, v

def main():
    # Check if a color name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./color_to_rgb.py <color>")
        sys.exit(1)

    color_name = sys.argv[1]
    rgb = color_to_rgb(color_name)

    if rgb is not None:
        print(f"The RGB color code for {color_name} is {rgb}")
        rgba = rgb_to_rgba(rgb)
        print(f"The RGBA color code for {color_name} is {rgba}")
        hex_code = rgb_to_hex(rgb)
        print(f"The HEX color code for {color_name} is {hex_code}")
        hsl = rgb_to_hsl(rgb)
        print(f"The HSL color code for {color_name} is {hsl}")
        hsv = rgb_to_hsv(rgb)
        print(f"The HSV color code for {color_name} is {hsv}")
    else:
        print(f"Color '{color_name}' is not defined in the webcolors module.")

if __name__ == "__main__":
    main()

