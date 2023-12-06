#!/usr/bin/env python3

import sys
import os
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

def rgb_to_cmy(rgb):
    r, g, b = rgb
    c = 1.0 - r / 255.0
    m = 1.0 - g / 255.0
    y = 1.0 - b / 255.0
    return c, m, y

def rgb_to_yiq(rgb):
    yiq = colorsys.rgb_to_yiq(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)
    return yiq

def write_color_format(file, title, color_name, code):
    file.write(f"\nColor Format: {title}\n")
    file.write(f"Color: {color_name}\n")
    file.write(f"{title} Color Code: {code}\n")

def print_and_write_all_formats(file, color_name, rgb):
    print(f"\nThe RGB color code for {color_name} is {rgb}\n")

    # Additional color formats
    rgba = rgb_to_rgba(rgb)
    hex_code = rgb_to_hex(rgb)
    hsl = rgb_to_hsl(rgb)
    hsv = rgb_to_hsv(rgb)
    cmy = rgb_to_cmy(rgb)
    yiq = rgb_to_yiq(rgb)

    # Print to console
    write_color_format(sys.stdout, "RGBA (Red, Green, Blue, Alpha)", color_name, rgba)
    write_color_format(sys.stdout, "HEX (Hexadecimal)", color_name, hex_code)
    write_color_format(sys.stdout, "HSL (Hue, Saturation, Lightness)", color_name, hsl)
    write_color_format(sys.stdout, "HSV (Hue, Saturation, Value)", color_name, hsv)
    write_color_format(sys.stdout, "CMY (Cyan, Magenta, Yellow)", color_name, cmy)
    write_color_format(sys.stdout, "YIQ (Luminance, I, Q)", color_name, yiq)

    # Write to file
    write_color_format(file, "RGBA (Red, Green, Blue, Alpha)", color_name, rgba)
    write_color_format(file, "HEX (Hexadecimal)", color_name, hex_code)
    write_color_format(file, "HSL (Hue, Saturation, Lightness)", color_name, hsl)
    write_color_format(file, "HSV (Hue, Saturation, Value)", color_name, hsv)
    write_color_format(file, "CMY (Cyan, Magenta, Yellow)", color_name, cmy)
    write_color_format(file, "YIQ (Luminance, I, Q)", color_name, yiq)

def main():
    # Check if a color name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./color_to_rgb.py <color>")
        sys.exit(1)

    color_name = sys.argv[1]
    rgb = color_to_rgb(color_name)

    if rgb is not None:
        # Save results to a text file
        file_path = f"output/{color_name}.txt"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            print_and_write_all_formats(file, color_name, rgb)
            print(f"\nResults have been saved to {file_path}")

    else:
        print(f"Color '{color_name}' is not defined in the webcolors module.")

if __name__ == "__main__":
    main()

