#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: September 2019
# This is circle math program withy variables


def main():
    # this function calculates circumference

    # input
    length = int(input("Enter length of rectangle: "))
    width = int(input("Enter width of rectangle: "))

    # process
    area = length*width
    perimeter = 2*(length+width)

    # output
    print("")
    print("Area is {}mm".format(area))
    print("Perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
