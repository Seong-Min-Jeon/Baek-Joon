input()
s=input()
l=[]
for i in range(len(s)):
    if(s[i]=='.'):
        l.append(i)
m=10**6
for i in range(1, len(l)):
    v=l[i]-l[i-1]-1
    if(m>v):
        m=v
print(m)