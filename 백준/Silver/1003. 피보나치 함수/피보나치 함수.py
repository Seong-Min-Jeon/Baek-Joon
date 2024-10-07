import sys
ip=sys.stdin.readline
f=[0,1]
for i in range(2,41):
    f.append(f[i-1]+f[i-2])
for _ in range(int(ip())):    
    n=int(ip())
    if(n==0): print(1,0); continue
    print(f[n-1],f[n])