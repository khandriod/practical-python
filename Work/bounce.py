# bounce.py
#
import random

height = 100 #meters
bounce = 1

while bounce < 10:
    height = height * 3/5
    print(bounce, round(height, 4))
    bounce = bounce + 1

# Exercise 1.5
