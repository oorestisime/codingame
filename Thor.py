import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in raw_input().split()]

DX=LX-TX
DY=LY-TY

# game loop
while 1:
    E = int(raw_input()) # The level of Thor's remaining energy, representing the number of moves he can still make.
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    if(DX > 0):
        if(DY > 0):
            print("SE")
            DX-=1
            DY-=1
        elif(DY <0):
            print("NE")
            DX-=1
            DY+=1
        else:
            print("E")
            DX-=1
    elif(DX <0):
        if(DY > 0):
            print("SW")
            DX+=1
            DY-=1
        elif(DY < 0):
            print("NW")
            DX+=1
            DY+=1
        else:
            print("W")
            DX+=1
    else:
        if(DY > 0):
            print("S")
            DY-=1
        elif(DY <0):
            print("N")
            DY+=1