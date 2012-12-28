"""
Hot Cold (hot-cold.py)
======================

Problem
-------
Build a two player hide and seek game!

Player 1 enters two numbers:

x his hiding x coordinate 0 - an integer  number between -100 and 100

y his hiding y coordinate 0 - an integer  number between -100 and 100

(The input x``=``0 and y``=``0 is not allowed)

The screen is cleared with the following command:

for i in range(100):
    print

Player 2 starts from 0, 0, and enters n,``s``,``w`` or e
to go north, south, west or east accordingly.

After entering the direction, the programs prints out one of the following options:

colder player 2 is getting far from player 1

warmer player 2 is getting closer to player 1

gotcha! player 2 found player 1 - and the game ends.

Sample Dialog
-------------
In this example player 1 hides here:

          |
          |
          |
          |
          |
          |
          |   @
----------+---------
          |
          |
          |
          |
          |

4
1
s
colder
n
warmer
n
warmer
n
colder
s
warmer
e
warmer
e
warmer
e
warmer
gotcha!

"""
x = int(raw_input("Player 1, Choose X Coordinate: "))
y = int(raw_input("Player 1, Choose Y Coordinate: "))
for i in range(100):
    print
    
player2x = 0
player2y = 0    
lastdistance = abs(player2x - x) + abs(player2y - y)
newdistance = 0
count = 0

while True:
    if player2x == x and player2y == y:
        print "Gotcha!!! It only took me, %d tries." %count
        break
    player2 = raw_input("Player 2, Please choose (n s e w): ")
    count += 1
    if player2 != "w" and player2 != "e" and player2 != "n" and player2 != "s":
        print "You idiot, n s e w ONLY"
    if player2 == "n":
        player2y += 1
    elif player2 == "s":
        player2y -= 1
    elif player2 == "w":
        player2x -= 1
    elif player2 == "e":
        player2x += 1
    newdistance = abs(player2x - x) + abs(player2y - y)
    if newdistance < lastdistance:
        print "Warmer"
    else:
        print "Colder"
    lastdistance = newdistance    
