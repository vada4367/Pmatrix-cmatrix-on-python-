#import librares
import os
import string
import keyboard
import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

#create list with simvals
sims = list(map(chr, range(32, 127)))
main = True

#input size matrix and speed
x = str(input("X (default 40): "))
y = str(input("Y (default 30): "))
speed = str(input("Speed (default 0): "))

if speed == "" or speed == " ":
    speed = 1
speed = int(speed)
speed /= 100
speed += 0.04

if x == "" or x == " ":
    x = 40

if y == "" or y == " ":
    y = 30
x = int(x)
y = int(y)

#create matrix
matrix = []
for i in range(0, y):
    matrix.append([])
for g in range(0, y):
    for i in range(0, x):
        matrix[g].append(" ")

#return matrix
def ret():
    global matrix
    #clear console
    os.system("clear")

    for i in range(len(matrix) - 1):     
        for j in range(len(matrix[i])): 
            #print white simvols
            if matrix[i + 1][j] == " ":
                print(Fore.WHITE + matrix[i][j], end = ' ')
            #and red simvols
            else:
                print(Fore.GREEN + matrix[i][j], end = ' ')
        print()  

#create simvols on first string
def create():
    global matrix
    global sims
    #quantity simvols
    raan = random.randint(0, 10)
    for i in range(0, raan):
        #what string
        ran = random.randint(0, x - 1)
        if matrix[0][ran] == " ":
            #what simvol
            sim = str(sims[random.randint(0, len(sims) - 1)])
            matrix[0][ran] = sim

#create vertically lines 
def down():
    for g in range(0, x):
        i = y - 1
        #with top to down
        while i > 0:
            if matrix[i][g] == " " and not matrix[i - 1][g] == " ":
                matrix[i][g] = str(sims[random.randint(0, len(sims) - 1)])
            i -= 1

#delit string 
def delit():
    global matrix
    for i in range(0, random.randint(0, 10)):
        matrix[0][random.randint(0, x - 1)] = " "

#delit vertically lines
def downdelit():
    global matrix
    for g in range(0, x):
        i = y - 1
        #with top to down
        while i > 0:
            if not matrix[i][g] == " " and matrix[i - 1][g] == " ":
                matrix[i][g] = " "
            i -= 1

#main
while main:
    if keyboard.is_pressed('q'):
        exit()
    delit()
    downdelit()
    down()
    create()
    ret()
    time.sleep(speed)