import sys
a=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
if(a<=2):
    print(0)
    exit(0)
s=0
n=len(l)
while True:
    d=0
    for i in range(1,n-1):
        a=l[i-1]
        b=l[i]
        c=l[i+1]
        if(2*b>a+c): 
            s+=b-(a+c)//2
            l[i]=(a+c)//2
            d=1
    if(d==0): break
print(s)