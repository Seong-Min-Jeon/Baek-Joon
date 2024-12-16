a,b=map(int,input().split())
l=[]
m=[]
for _ in range(a):
    r=''
    s=input()
    for c in s:
        r+=c*2
    l.append(r)
for _ in range(a):
    m.append(input())
if(l==m): print('Eyfa')
else: print('Not Eyfa')