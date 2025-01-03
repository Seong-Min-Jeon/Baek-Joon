ip=input
c=int(ip())
d={0:[0,0]}
for i in range(1,c+1):
    a=int(ip())
    if(i==1): d[i]=[a,a]; continue    
    d[i]=[d[i-1][1]+a,max(d[i-2])+a]
print(max(d[c]))