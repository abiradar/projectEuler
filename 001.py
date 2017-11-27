import sys
def s(n):
    return n*(n+1)/2

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    n = n-1
    print s(n/3)*3 + s(n/5)*5 - s(n/15)*15
