n,s=map(int,input().split())
l=list(map(int,input().split()))
i,j=0,0
r,c=l[0],10**6
while True:
    if(r<s):
        j+=1
        if(j>=n): break
        r+=l[j]
    else: 
        c=min(c,j-i+1)        
        r-=l[i]
        i+=1
        if(i>=n): break
if(c==10**6): print(0)
else: print(c)