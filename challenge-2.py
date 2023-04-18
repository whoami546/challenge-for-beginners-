#!/usr/bin/python3
import re
from random import randint

get = ''
def call_this(name):
    global get
    num = randint(1,4)
    messege = [ x for x in range(1,5) ]
    iterate_flag = 0
    while iterate_flag < 100:
        iterate_flag += 2

    file = open(f"{name}_{num}", mode='w+')
    get += file.name
    file.write(f"{name} wrote to this file is {iterate_flag} percent more important")
    file.close()

user = input("Enter your name : ")
if not user:
    print("At one user name required !!! ")
else:
    call_this(user)
    print("file created : %s" % (get))
    previously_created = open(get, mode="r")
    content = previously_created.read()
    eval(content)
