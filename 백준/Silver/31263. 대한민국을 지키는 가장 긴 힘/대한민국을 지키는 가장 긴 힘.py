n=int(input())
s=[*map(int,input().strip())]
i=0
c,p=0,0
for _ in range(10):
    if(i==n):break
    if(s[i]==0 and p//100!=0):
        if(p//10==0): i-=3; c+=1; p=0; continue
        else: i-=2; c+=1; p=0; continue
    if(p*10+s[i]<=641): p=p*10+s[i]
    else: c+=1; p=s[i]
    i+=1
print(c+1)