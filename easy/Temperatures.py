import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # the number of temperatures to analyse
if(N==0):
    print("0")
else:
    TEMPS = raw_input() # the N temperatures expressed as integers ranging from -273 to 5526
    tokens=TEMPS.split(" ")
    min=6000
    for tok in tokens:
        if(abs(int(tok))<=abs(min)):
           min=int(tok)
    print(min)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

#print "result"