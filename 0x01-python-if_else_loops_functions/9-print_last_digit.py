#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        c = (number * -1) % 10
    else:
        c = number % 10
    return c
