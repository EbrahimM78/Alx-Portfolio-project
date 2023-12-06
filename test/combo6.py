#!/usr/bin/env python3

import sys
import webcolors
import colorsys
import colorspacious as cs

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

def rgb_to_hunter_lab(rgb):
    hunter_lab = colorsys.rgb_to_hunterlab(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)
    return hunter_lab

def main():
    # Check if a color name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./color_to_rgb.py <color>")
        sys.exit(1)

    color_name = sys.argv[1]
    rgb = color_to_rgb(color_name)

    if rgb is not None:
        print(f"The RGB color code for {color_name} is {rgb}")

        # Additional color formats
        rgba = rgb_to_rgba(rgb)
        print(f"\nColor Format: RGBA (Red, Green, Blue, Alpha)")
        print(f"Color: {color_name}")
        print(f"RGBA Color Code: {rgba}")

        hex_code = rgb_to_hex(rgb)
        print(f"\nColor Format: HEX (Hexadecimal)")
        print(f"Color: {color_name}")
        print(f"HEX Color Code: {hex_code}")

        hsl = rgb_to_hsl(rgb)
        print(f"\nColor Format: HSL (Hue, Saturation, Lightness)")
        print(f"Color: {color_name}")
        print(f"HSL Color Code: {hsl}")

        hsv = rgb_to_hsv(rgb)
        print(f"\nColor Format: HSV (Hue, Saturation, Value)")
        print(f"Color: {color_name}")
        print(f"HSV Color Code: {hsv}")

        cmy = rgb_to_cmy(rgb)
        print(f"\nColor Format: CMY (Cyan, Magenta, Yellow)")
        print(f"Color: {color_name}")
        print(f"CMY Color Code: {cmy}")

        yiq = rgb_to_yiq(rgb)
        print(f"\nColor Format: YIQ (Luminance, I, Q)")
        print(f"Color: {color_name}")
        print(f"YIQ Color Code: {yiq}")

        hunter_lab = rgb_to_hunter_lab(rgb)
        print(f"\nColor Format: Hunter LAB")
        print(f"Color: {color_name}")
        print(f"Hunter LAB Color Code: {hunter_lab}")

    else:
        print(f"Color '{color_name}' is not defined in the webcolors module.")

if __name__ == "__main__":
    main()

