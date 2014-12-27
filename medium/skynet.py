import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# N: the total number of nodes in the level, including the gateways
# L: the number of links
# E: the number of exit gateways
N, L, E = [int(i) for i in raw_input().split()]
N1L=[]
N2L=[]
EI=[]
for i in xrange(L):
    # N1: N1 and N2 defines a link between these nodes
    N1, N2 = [int(i) for i in raw_input().split()]
    N1L.append(N1)
    N2L.append(N2)

for i in xrange(E):
    EI.append(int(raw_input())) # the index of a gateway node
#print >> sys.stderr,N1L,N2L,EI,L
# game loop
found=0
while 1:
    SI = int(raw_input()) # The index of the node on which the Skynet agent is positioned this turn
    matches=[i for i,x in enumerate(N1L) if x==SI]
    matches2=[i for i,x in enumerate(N2L) if x==SI]
    #print >> sys.stderr, matches,matches2
    found=0
    for gate in EI:
        for match in matches:
            #print >> sys.stderr,"match1", N2L[match]
            if(N2L[match]==gate):
                print(str(N1L[match])+" "+str(N2L[match]))
                found=1
        for match in matches2:
            #print >> sys.stderr,"match2", N1L[match],EI
            if(N1L[match]==gate):
                print(str(N1L[match])+" "+str(N2L[match]))
                found=1
    if(found==0):
        print >> sys.stderr,"here"
        print(str(SI)+" "+str(N2L[N1L.index(SI)]))
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
#    print "0 1" # Example: 0 1 are the indices of the nodes you wish to sever the link between