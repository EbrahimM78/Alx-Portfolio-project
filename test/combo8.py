#!/usr/bin/env python3

import sys
import webcolors
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
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def rgb_to_hsl(rgb):
    # Convert from sRGB1 to XYZ color space first
    xyz = cs.cspace_convert(rgb, start={"name": "sRGB1"}, end={"name": "XYZ"})
    
    # Convert from XYZ to HSL color space
    hsl = cs.cspace_convert(xyz, start={"name": "XYZ"}, end={"name": "HSL"})
    
    return hsl

def rgb_to_hsv(rgb):
    hsv = cs.cspace_convert(rgb, start={"name": "sRGB1"}, end={"name": "HSV"})
    return hsv

def rgb_to_cmy(rgb):
    cmy = cs.cspace_convert(rgb, start={"name": "sRGB1"}, end={"name": "CMY"})
    return cmy

def rgb_to_yiq(rgb):
    yiq = cs.cspace_convert(rgb, start={"name": "sRGB1"}, end={"name": "YIQ"})
    return yiq

def rgb_to_lab(rgb):
    lab = cs.cspace_convert(rgb, start={"name": "sRGB1"}, end={"name": "CIELab"})
    return lab

def rgb_to_yuv(rgb):
    r, g, b = rgb
    y = 0.299 * r + 0.587 * g + 0.114 * b
    u = -0.14713 * r - 0.288862 * g + 0.436 * b
    v = 0.615 * r - 0.51498 * g - 0.10001 * b
    return y, u, v

def rgb_to_hunter_lab(rgb):
    hunter_lab = cs.cspace_convert(rgb, start={"name": "sRGB1"}, end={"name": "HunterLab"})
    return hunter_lab

def main():
    # Check if a color name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./color_converter.py <color>")
        sys.exit(1)

    color_name = sys.argv[1]
    rgb = color_to_rgb(color_name)

    if rgb is not None:
        print(f"The RGB color code for {color_name} is {rgb}")

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

        lab = rgb_to_lab(rgb)
        print(f"\nColor Format: LAB (CIE 1976)")
        print(f"Color: {color_name}")
        print(f"LAB Color Code: {lab}")

        yuv = rgb_to_yuv(rgb)
        print(f"\nColor Format: YUV (Luminance, U, V)")
        print(f"Color: {color_name}")
        print(f"YUV Color Code: {yuv}")

        hunter_lab = rgb_to_hunter_lab(rgb)
        print(f"\nColor Format: Hunter LAB")
        print(f"Color: {color_name}")
        print(f"Hunter LAB Color Code: {hunter_lab}")

    else:
        print(f"Color '{color_name}' is not defined in the webcolors module.")

if __name__ == "__main__":
    main()

