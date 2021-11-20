import keyboard
import time
import os
import random
clear = lambda: os.system('cls')

loading = 0
print("Loading...")
while loading < 100:
    randomwait =  random.uniform(0.2, 1)
    randomprozent = random.randint(1, 14)
    print(loading, "%")
    loading = loading+randomprozent
    time.sleep(randomwait)

print("         Firespammer         ")
c = int(input("Where you want to spam??\n1)Normal or discord without ping\n2)Normal or discord with ping\n3)copy+paste\n4)Paste out of a .txt\nSelect: "))


if c == 1:
    print("         Firespammer         ")
    a = int(input("Number of repeats: "))
    b = input("What to print: ")
    keyboard.send("alt+tab")
    time.sleep(2)
    for x in range(a):
        keyboard.write(b, delay=0.1)
        keyboard.send("enter")
elif c == 2:
    print("         Firespammer         ")
    a = int(input("Number of repeats: "))
    b = input("Pls enter the @username first\nWhat to print: ")
    keyboard.send("alt+tab")
    time.sleep(1)
    for x in range(a):
        keyboard.write(b, delay=0.2)
        keyboard.send("enter")
        keyboard.send("enter")
        time.sleep(0.5)
elif c == 3:
    print("         Firespammer         ")
    a = int(input("Pls copy now what you want to spam\nNumber of repeats: "))
    keyboard.send("alt+tab")
    time.sleep(1)
    for x in range(a):
        keyboard.send("ctrl+v")
        keyboard.send("enter")
elif c == 4:
    print("         Firespammer         ")
    a = int(input("Number of repeats: "))
    b = input("Name of the .txt(dont type .txt): ")
    t = input("what is the name of the programm where to paste?: ")
    keyboard.send("windows+s")
    time.sleep(1)
    keyboard.write(b, delay=0.2)
    keyboard.write(".txt", delay=0.2)
    time.sleep((1))
    keyboard.send("enter")
    time.sleep(2)
    keyboard.send("ctrl+a")
    keyboard.send("ctrl+c")
    time.sleep(0.3)
    keyboard.send("windows+s")
    time.sleep(2)
    keyboard.write(t, delay=0.2)
    time.sleep(1)
    for x in range(a):
        keyboard.send("ctrl+v")
        keyboard.send("enter")
        time.sleep(0.4)
else:
    print("Pls select one of the number that are printed there")

time.sleep(10)