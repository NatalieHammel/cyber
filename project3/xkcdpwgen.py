#!/usr/bin/env python3

"""
Homework 3: Password Generator
Course: CY2550
Author: Natalie Hammel
Start Date: 8/9/23
Finish Date: 8/11/23 "
"""

# import packages
import argparse
import random

# create universal variable of symbol list
SYMBOLS = ['%', '$', '#', '@', '!', '+', '*', '^', '~', ':', ';', '<', '>']

# create universal variable of number list
NUMBERS = (['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

# creating the parser
parser = argparse.ArgumentParser(description='Generate a secure, memorable password using the XKCD method',
                                 epilog="https://www.xkcd.com/936/")

parser.add_argument('-w', '--words', type=int, default=4, help='include WORDS words in the password (default=4)')

parser.add_argument('-c', '--caps', type=int, default=0,
                    help='capitalize the first letter of CAPS random words (default=0)')

parser.add_argument('-n', '--numbers', type=int, default=0,
                    help='insert NUMBERS random numbers in the password (default=0)')

parser.add_argument('-s', '--symbols', type=int, default=0,
                    help='insert SYMBOLS random symbols in the password (default=0)')

args = parser.parse_args()

# ERROR HANDLING
# if the user specifies more capitalization than words available, just set the two equal
if args.caps > args.words:
    args.caps = args.words

# ESTABLISH EMPTIES
# create empty list of words
randwords = []

# create empty string for final password
password = ""


def wordSelect():
    """ Opens the imported word file, reads, splits, and selects a random word """

    words = open('words.txt').read().splitlines()
    return random.choice(words)


def insertSN(pwd, sn):
    """ Randomly chooses space within string and inserts symbol or number (sn)"""

    index_select = random.randint(0, len(pwd))
    return pwd[0:index_select] + sn + pwd[index_select:]


# CAPITALIZE: loop to capitalize words for each c specified
for i in range(0, args.words):
    if args.caps > 0:
        randwords.append(wordSelect().capitalize())
        args.caps -= 1
    else:
        randwords.append(wordSelect())

# add to password once capitalized (if specified)
for i in range(0, args.words):
    removed_object = random.choice(randwords)
    randwords.remove(removed_object)
    password += removed_object

# NUMBER: while loop for numbers, specified -n
while args.numbers > 0:
    password = insertSN(password, str(random.randint(0, 9)))
    args.numbers -= 1

# SYMBOL: while loop for symbols, specified -s
while args.symbols > 0:
    password = insertSN(password, random.choice(SYMBOLS))
    args.symbols -= 1

print(password)
