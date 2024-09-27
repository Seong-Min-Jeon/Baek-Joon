n,k=map(int,input().split())
a=k
l=[i for i in range(1,n+1)]
print('<', end='')
while len(l)>0:
    if(len(l)==1): print(l.pop(), end=''); break
    print(l[k-1], end=', ')
    del l[k-1]
    k+=a-1
    k%=len(l)
    if(k==0): k+=len(l)
print('>')