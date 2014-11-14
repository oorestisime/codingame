import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

MESSAGE = raw_input()
binaries=""
for m in MESSAGE:
    temp=""
    temp=' '.join(format(ord(x), 'b') for x in m)
    # Character coded in less bits | adding 0 at the begining
    if(len(temp)==6):
        temp="0"+temp
    binaries+=temp
before="-1"
out=""
for i,bin in enumerate(binaries):
    current=binaries[i:i+1]
    if(current!=before):
        if(i!=0):
            out+=" "
        if(current=="1"):
            out+="0 0"
            before="1"
        elif(current=="0"):
            out+="00 0"
            before="0"
        else:
            out+=" "
            before="-1"
    else:
        out+="0"
print(out)
        
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

