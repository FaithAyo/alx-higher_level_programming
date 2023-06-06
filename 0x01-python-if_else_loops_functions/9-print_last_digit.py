#!/usr/bin/python3
def print_last_digit(number):
    num = number
    if num < 0:
        num = number * -1
    last_digit = num % 10
    print(last_digit, end="")
    return last_digit
