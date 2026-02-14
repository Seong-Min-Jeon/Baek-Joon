import sys
I=sys.stdin.readline
n=int(I())
s=I().strip()
d=[1e99]*(n+1)
d[0]=0
for i in range(1,n+1):
    for k in range(1,4):
        j=i-k
        if(j<0): break
        if(s[j]=='0'): continue
        v=int(s[j:i])
        if(1<=v<=641):
            d[i]=min(d[i],d[j]+1)
print(d[n])