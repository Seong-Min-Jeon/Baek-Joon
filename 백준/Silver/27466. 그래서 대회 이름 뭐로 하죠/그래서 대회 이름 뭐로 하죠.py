n,m=map(int,input().split())
l=list(input().strip())
s=''
f=0
while len(s)+len(l)>=m:
    if(f>=3):
        print('YES')
        for _ in range(m-3):
            s+=l.pop()
        print(s[::-1])
        exit()
    if(f==0 and l[-1] not in ('A','E','I','O','U')):
        f=1
        s+=l[-1]            
    elif(f>0 and l[-1]=='A'):
        f+=1
        s+=l[-1]
    l.pop()
print('NO')