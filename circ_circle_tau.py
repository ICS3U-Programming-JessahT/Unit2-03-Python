#!/usr/bin/env python3

# Created By: Jessah
# Date: Oct 3, 2022
# This program calculates the circumference using TAU.

import constants


def main():
    # input

    radius = float(input("Enter the radius of the circle (cm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print()
    print("The circumference of the circle: {:.2f} cm".format(circumference))


if __name__ == "__main__":
    main()
