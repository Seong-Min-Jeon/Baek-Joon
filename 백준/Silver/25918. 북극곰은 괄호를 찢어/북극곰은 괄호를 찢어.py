input()
m,a,b=0,0,0
t=input().strip()
if(t.count('(')!=t.count(')')): print(-1); exit()
for e in t:
    if(e=='('): a+=1; b-=1
    else: a-=1; b+=1
    m=max(m,a,b)
print(m)