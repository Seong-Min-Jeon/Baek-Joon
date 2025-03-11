n=int(input())
l=list(map(int,input().split()))
m=[0]
for i in range(n):
    if(l[i]>m[-1]):
        m.append(l[i])
        continue
    x,z=0,len(m)-1
    while x<=z:
        y=(x+z)//2
        if(l[i]==m[y]): x=y; break
        elif(l[i]<m[y]): z=y-1
        else: x=y+1
    m[x]=l[i]
print(len(m)-1)