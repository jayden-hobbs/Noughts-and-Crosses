#!/usr/bin/env python3


import random
import math
import time
import sys

global grid
global numberedGrid
global count
global p1Score
global p2Score
global gameCounter

p1Score = 0
p2Score = 0
gameCounter = 0
count = 0
numberedGrid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def player1Name():
    global p1Name
    p1Nameinput = str(input("Please enter Player 1's Name: "))
    p1Name = p1Nameinput.upper()
    while len(p1Nameinput) < 1:
        p1Nameinput = str(input("Please enter at least 1 character: "))
    return p1Name

def player2Name():
    global p2Name
    p2Nameinput = str(input("Please enter Player 2's Name: "))
    p2Name = p2Nameinput.upper()
    while len(p2Nameinput) < 1:
        p2Nameinput = str(input("Please enter at least 1 character: "))
    return p2Name

def blank_board():
    print(numberedGrid[0:3])
    print(numberedGrid[3:6])
    print(numberedGrid[6:])
    time.sleep(0.5)
    print("Please memorise these positional markers")
    time.sleep(0.5)
    memorised = input("Have you memorised them? 'y' for Yes and 'n' for no: ")
    while memorised != 'y':
        memorised = input("Please enter a response or memorise them: ")

def main():
    gameCounter = 0
    print("PLAYER 1 will go first")
    go = 0
    game = 1
    moveCounter = 0
    while game == 1:
        while go != 1:
            move = int(input("PLAYER 1 - Please enter the number for the position you wish to take. 1-9: "))
            if grid[move-1] == " ":
                grid[move-1] = "x"
                go = 1
                moveCounter = moveCounter + 1
            else:
                print("That spot has been taken. \n Please enter a new number")

            if grid[0] == "x" and grid[1] == "x" and grid[2] == "x":
                print("Player 1 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[3] == "x" and grid[4] == "x" and grid[5] == "x":
                print("Player 1 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[6] == "x" and grid[7] == "x" and grid[8] == "x":
                print("Player 1 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[0] == "x" and grid[3] == "x" and grid[6] == "x":
                print("Player 1 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[1] == "x" and grid[4] == "x" and grid[7] == "x":
                print("Player 1 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[2] == "x" and grid[5] == "x" and grid[8] == "x":
                print("Player 1 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[0] == "x" and grid[4] == "x" and grid[8] == "x":
                print("Player 1 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[2] == "x" and grid[4] == "x" and grid[6] == "x":
                print("Player 1 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

        print(grid[0:3])
        print(grid[3:6])
        print(grid[6:])

        go = 0

        if moveCounter == 9:
            print("Game over - its a draw")
            gameCounter = gameCounter + 1
            sys.exit()


        while go != 1:
            move = int(input("PLAYER 2 - Please enter the number for the position you wish to take. 1-9: "))
            if grid[move-1] == " ":
                grid[move-1] = "o"
                go = 1
                moveCounter = moveCounter + 1
            else:
                print("That spot has been taken. \nPlease enter a new number")

            if grid[0] == "o" and grid[1] == "o" and grid[3] == "o":
                print("Player 2 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[3] == "o" and grid[4] == "o" and grid[5] == "o":
                print("Player 2 Wins!")
                sys.exit()

            elif grid[6] == "o" and grid[7] == "o" and grid[8] == "o":
                print("Player 2 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[0] == "o" and grid[3] == "o" and grid[6] == "o":
                print("Player 2 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[1] == "o" and grid[4] == "o" and grid[7] == "o":
                print("Player 2 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[2] == "o" and grid[5] == "o" and grid[8] == "o":
                print("Player 2 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[0] == "o" and grid[4] == "o" and grid[8] == "o":
                print("Player 2 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()

            elif grid[2] == "o" and grid[4] == "o" and grid[6] == "o":
                print("Player 2 Wins!")
                print(grid[0:3])
                print(grid[3:6])
                print(grid[6:])
                sys.exit()
        print(grid[0:3])
        print(grid[3:6])
        print(grid[6:])

        go = 0

        if moveCounter == 9:
            print("Game over - its a draw")
            gameCounter = gameCounter + 1
            sys.exit()



blank_board()
player1Name()
player2Name()
main()