#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = "is"
greater = "and is greater than 5"
zero = "and is 0"
less = "and is less than 6 and not 0"
print(number)
last_digit = 0
if number < 0:
    temp_last = abs(number) % 10
    last_digit = temp_last * -1
else:
    last_digit = number % 10
print(f"{last_digit}")