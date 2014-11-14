import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
height=0
while 1:
    SX, SY = [int(i) for i in raw_input().split()]
    for i in xrange(8):
        MH = int(raw_input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        #print >> sys.stderr, MH
        if(MH>height):
            pos=i
            height=MH
    if(SX==pos):
        #print >> sys.stderr,SX,pos
        print("FIRE")
        height=0
        pos=-1
    else:
        print("HOLD")