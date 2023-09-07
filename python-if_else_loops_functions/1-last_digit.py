#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = "is"
greater = "and is greater than 5"
zero = "and is 0"
less = "and is less than 6 and not 0"
last_digit = 0
print(number)
if number < 0:
    temp_last = abs(number) % 10
    last_digit = temp_last * -1
else:
    last_digit = number % 1

if last_digit > 5:
    print(f"{str1} {number} {str2} {last_digit} {greater}")
elif last_digit == 0:
    print(f"{str1} {number} {str2} {last_digit} {zero}")
else:
    print(f"{str1} {number} {str2} {last_digit} {less}")