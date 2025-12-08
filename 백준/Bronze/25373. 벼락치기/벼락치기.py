from bisect import bisect_left as B
n=int(input())
if(n<28):
    l=[0]
    for i in range(1,7):
        l.append(l[-1]+i)
    print(B(l,n))
else:
    if(n%7==0): print(n//7+3)
    else: print(n//7+4)