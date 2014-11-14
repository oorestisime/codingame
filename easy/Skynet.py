import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(raw_input()) # the length of the road before the gap.
G = int(raw_input()) # the length of the gap.
L = int(raw_input()) # the length of the landing platform.

# game loop
while 1:
    S = int(raw_input()) # the motorbike's speed.
    X = int(raw_input()) # the position on the road of the motorbike.
    if( R + G - X > 0):
        if( R + G - X > S):
            if(S < G + 1 ):
                print("SPEED"); 
            elif(S > G + 1):
                print("SLOW"); 
            else:
                print("WAIT"); 
        else:
          print("JUMP"); 
    else:
        print("SLOW"); 
   