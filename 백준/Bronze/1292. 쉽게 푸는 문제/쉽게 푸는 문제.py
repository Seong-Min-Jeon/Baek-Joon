l=[]
for i in range(1,100):
    l+=[i]*i
a,b=map(int,input().split())
r=0
for i in range(a,b+1):
    r+=l[i-1]
print(r)