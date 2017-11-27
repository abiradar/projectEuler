import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    a,b,s = 1,2,0
    while b <= n: 
        if b%2==0:
            s += b
        a,b = b,a+b
    print s
        
