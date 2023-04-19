#!/usr/bin/python3
from re import findall
from math import pi
from random import randint

integer = randint(1,1000)
division = pi/integer
user = input("Enter your email to recieve magazine : ")
pattern = findall(r'[a-zA-Z0-9]\S*\@.{4}\.com', user)

if pattern:
    content = user + ' : ' + 'here is your magazine my brother and\tI love my PC...!\n\n'
    print(f"sending message to {pattern[0]}...")
    file = open(f"{user}_magazine_{division}", mode="w+")
    file.write(content)
    file.close()
    print(file.name + 'has been created')

    again = open(file.name, mode="r")
    try:
        eval(again.read())
    except:
        print("my ass hurts!!")

if not pattern:
    print("So you want to give a shot to my trully badass attitude ???!")
