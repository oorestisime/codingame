import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# W: width of the building.
# H: height of the building.
W, H = [int(i) for i in raw_input().split()]
N = int(raw_input()) # maximum number of turns before game over.
X0, Y0 = [int(i) for i in raw_input().split()]
xl = 0;
yt = 0;
xr = W;
yb = H;
# game loop
while 1:
    BOMB_DIR = raw_input() # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    # Write an action using print
    print >> sys.stderr, BOMB_DIR
    if "L" in BOMB_DIR:
        xr=X0
    if "R" in BOMB_DIR:
        xl=X0+1
    if "U" in BOMB_DIR:
        yb=Y0
    if "D" in BOMB_DIR:
        yt=Y0+1
  
    X0 = (xl + xr) / 2;
    Y0 = (yt + yb) / 2;
    print X0,Y0
    #print "0 0" # the location of the next window Batman should jump to.