TurtleGraphics.py
#Name: April Lastra 
#Date: 02/12/2025
#Assignment: Lab 4 

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(april, sides):
    for s in range(sides): 
        april.forward(50)
        april.right(360/sides)

def fillcorner(april, corner):
    #draw big square 
    drawsquare(april,100)
    april.begin_fill()
    drawsquare(april,50)
    april.end_fill()

def square_in_squares(april, num, size):
    if num == 0: 
        return 
    draw_square(april,size)
    april.penup()
    april.forward(size * 0.1)
    april.right(90)
    april.forward(size * 0.1)
    april.left(90)
    april.pendown()
    square_in_squares(april, num -1, size * 0.8)

def main():
    april = turtle.Turtle()


    #drawSquare(april, 100)
    #drawPolygon(april, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
