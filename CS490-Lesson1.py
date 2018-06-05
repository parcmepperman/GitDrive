#Marc Pepperman - CS490 - Lesson 1
#number 1
import sys
print("the version of python is... ")
print("")
print(sys.version)
print("""
the print statements are different between 2 and 3, version 3 requires parenthesis and quotes and 2 just quotes
python 2 has library support that is not offered in 3
some commented that python 3 has limited 3rd party module support
""")

#number 2

fname = input("What is your FIRST name?  ")
lname = input("What is your LAST name?  ")
x = int(input("enter a number: "))
print("great job!", fname, lname)
y = int(input("enter another number: "))

backlast = lname[::-1]
backfirst = fname[::-1]
quotient = x / y
remainder = x % y

print("Your name in reverse is: ", backlast, backfirst)
print("the numbers you gave me have a quotient of ", quotient)
print("and they have a remainder of ", remainder)
print("thanks for playing", fname, "!!")

#number 3

import random

value = random.randint(0,9)

guess = float(input("We have generated a random number between 0-9, guess what it is: "))


if guess < value:
    guess = float(input("guess a little higher: "))

if guess > value:
    guess = float(input("guess a little lower: "))

else:
    print("YOU WIN!!! Nice work", fname)
