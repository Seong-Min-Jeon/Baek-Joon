def f(l,k):
    if(k==0): print(*sorted(l),end=' '); return
    f(l[:len(l)//2],k//2)
    f(l[len(l)//2:],k//2)
input()
l=list(map(int,input().split()))
f(l,int(input())//2)