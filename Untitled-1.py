import os
import subprocess
import string
import keyboard
import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

sims = list(map(chr, range(32, 127)))
main = True

x =  subprocess.check_output('echo $COLUMNS', stderr=subprocess.STDOUT)
y = str(input("Y (default 30): "))
speed = str(input("Speed (default 0): "))

if speed == "" or speed == " ":
    speed = 1
speed = int(speed)
speed /= 100
speed += 0.04


if y == "" or y == " ":
    y = 30
x = int(x)
y = int(y)

matrix = []
for i in range(0, y):
    matrix.append([])
for g in range(0, y):
    for i in range(0, x):
        matrix[g].append(" ")


def ret():
    global matrix

    os.system("clear")

    for i in range(len(matrix) - 1):     
        for j in range(len(matrix[i])): 
            if matrix[i + 1][j] == " ":
                print(Fore.WHITE + matrix[i][j], end = ' ')
            else:
                print(Fore.GREEN + matrix[i][j], end = ' ')
        print()  

def create():
    global matrix
    global sims
    raan = random.randint(0, 10)
    for i in range(0, raan):
        ran = random.randint(0, x - 1)
        if matrix[0][ran] == " ":
            sim = str(sims[random.randint(0, len(sims) - 1)])
            matrix[0][ran] = sim

def down():
    for g in range(0, x):
        i = y - 1
        while i > 0:
            if matrix[i][g] == " " and not matrix[i - 1][g] == " ":
                matrix[i][g] = str(sims[random.randint(0, len(sims) - 1)])
            i -= 1
def delit():
    global matrix
    for i in range(0, random.randint(0, 10)):
        matrix[0][random.randint(0, x - 1)] = " "

def downdelit():
    global matrix
    for g in range(0, x):
        i = y - 1
        while i > 0:
            if not matrix[i][g] == " " and matrix[i - 1][g] == " ":
                matrix[i][g] = " "
            i -= 1


while main:
    if keyboard.is_pressed('q'):
        exit()
    delit()
    downdelit()
    down()
    create()
    ret()
    time.sleep(speed)