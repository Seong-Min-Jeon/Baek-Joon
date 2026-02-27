d={}
for _ in range(9):
    n=input().strip()
    d[n]=d.get(n,0)+1
x,y='',0
for k in d:
    if(d[k]>y): x=k;y=d[k]
print(x)