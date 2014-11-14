import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L = int(raw_input())
H = int(raw_input())
T = list(raw_input().upper())
out=""
for i in xrange(H):
    ROW = raw_input()
    for char in T:
        count=(ord(char)-65)*L
        if(count <0 or count > 26*L): 
            count = 26*L;
        out += ROW[count:count+L]
    print(out)
    out=""

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
