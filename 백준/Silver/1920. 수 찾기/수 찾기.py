input()
s=set(list(map(int,input().split())))
input()
l=list(map(int,input().split()))
for e in l:
    if(e in s): print(1)
    else: print(0)