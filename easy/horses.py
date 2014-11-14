import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input())
Pi=[]
min=100000;
for i in xrange(N):
    Pi.append(int(raw_input()))
Pi.sort()
for i,item in enumerate(Pi):
    if(i!=len(Pi)-1):
        D = Pi[i] - Pi[i+1];    
        D = ( D ^ ( D >> 31 ) ) - ( D >> 31 );   
        if(min > D):
            min = D;
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print min