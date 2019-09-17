#github repo: https://github.com/kristjanleifur4/TileTraveller.git
x,y = 1,1
while (x,y) != (3,1): #á meðan x,y er ekki 3,1 þá heldur programmið áfram
    a = x
    b = y
    north = True
    east = True
    south = True
    west = True
    if y == 3 or (x,y) == (2,2) or (x,y) == (3,1):
        north = False
    if (x,y) != (1,2) and (x,y) != (1,3) and (x,y) != (2,3):
        east = False
    if y == 1 or (x,y) == (2,3):
        south = False
    if y == 1 or x == 1 or (x,y) == (3,2):
        west = False

    direction = ""
    while direction == "": #hvaða átt notandinn fer í 
        if north == True:
            direction += "(N)orth"
        elif east == True:
            direction += "(E)ast"
        elif south == True:
            direction += "(S)outh"
        elif west == True:
            direction += "(W)est"
    if east == True and direction != "(E)ast":
        direction += " or (E)ast"
    if south == True and direction != "(S)outh":
        direction += " or (S)outh"
    if west == True and direction != "(W)est":
        direction += " or (W)est"
    print("You can travel: " + direction + ".") #hvaða valmöguleikar eru í boði

    directionChoice = ""
    while (x,y) == (a,b):
        directionChoice = input("Direction: ")
        directionChoice = directionChoice.upper()
        if directionChoice == "N" and north == True:
            y += 1
        elif directionChoice == "E" and east == True:
            x += 1
        elif directionChoice == "S" and south == True:
            y -= 1
        elif directionChoice == "W" and west == True:
            x -= 1
        else:
            print("Not a valid direction!")
print("Victory!") #ef það er farið á 3,1 þá prentast út victory 
    

