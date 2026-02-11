from bisect import bisect_left as B
I=input;I()
m=[]
for e in map(int,I().split()):
    i=B(m,e)
    if(i>=len(m)): m.append(e)
    else: m[i]=e
print(len(m))