import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(raw_input()) # the length of the road before the gap.
G = int(raw_input()) # the length of the gap.
L = int(raw_input()) # the length of the landing platform.

'''
Works for tests 1-4
'''


# game loop
while 1:
    S = int(raw_input()) # the motorbike's speed.
    X = int(raw_input()) # the position on the road of the motorbike.
    print >> sys.stderr, R,X,L,G,S
    if(X==0):
        if(S-G<3):
            print("SPEED")
        else:
            print("SLOW")
    elif(R-(X+S)<2 and X<R):
        print("JUMP")
    elif(S==G+1 and X<R):
        print("WAIT")
    elif(X>R):
        print("SLOW")
    elif(S>=G+1 and X<R):
        if(R-X-S<=G+1):
            print("WAIT")
        else:
            print("SLOW")
    else:
        print("SPEED")
   