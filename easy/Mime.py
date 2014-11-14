import sys, math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # Number of elements which make up the association table.
Q = int(raw_input()) # Number Q of file names to be analyzed.
ext_l=[]
mime_l=[]
found=0
for i in xrange(N):
    # EXT: file extension
    # MT: MIME type.
    EXT, MT = raw_input().split()
    ext_l.append(EXT.lower())
    mime_l.append(MT)
for i in xrange(Q):
    FNAME = raw_input() # One file name per line.
    ext=FNAME.split(".")
    if("." in FNAME):
        if(ext[-1].lower() in ext_l):
            index=ext_l.index(ext[-1].lower())
            print(mime_l[index])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
    

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

#print "UNKNOWN" # For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.