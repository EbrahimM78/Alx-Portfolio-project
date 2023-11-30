#!/usr/bin/env python3

import colorsys

def combine_colors(color1, color2):
    color1 = color1.lower()
    color2 = color2.lower()

    # Dictionary mapping color combinations
    color_combinations = {
        ('red', 'yellow'): 'orange',
        ('yellow', 'red'): 'orange',
        ('blue', 'yellow'): 'green',
        ('yellow', 'blue'): 'green',
        # Add more color combinations as needed
    }

    # Check if the combination is in the dictionary
    combination = color_combinations.get((color1, color2))

    if combination:
        return f"The combination of {color1} and {color2} is {combination}."
    else:
        # If the combination is not in the dictionary, use colorsys to mix colors
        rgb_color1 = colorsys.rgb_to_hsv(*colorsys.hex_to_rgb(color1))
        rgb_color2 = colorsys.rgb_to_hsv(*colorsys.hex_to_rgb(color2))

        mixed_color = colorsys.hsv_to_rgb(
            (rgb_color1[0] + rgb_color2[0]) / 2,
            (rgb_color1[1] + rgb_color2[1]) / 2,
            (rgb_color1[2] + rgb_color2[2]) / 2
        )

        mixed_color_hex = "#{:02X}{:02X}{:02X}".format(
            int(mixed_color[0] * 255),
            int(mixed_color[1] * 255),
            int(mixed_color[2] * 255)
        )

        return f"The combination of {color1} and {color2} is {mixed_color_hex}."

def main():
    # Get user input for colors
    color1 = input("Enter the first color: ")
    color2 = input("Enter the second color: ")

    # Combine colors and print the result
    result = combine_colors(color1, color2)
    print(result)

if __name__ == "__main__":
    main()

