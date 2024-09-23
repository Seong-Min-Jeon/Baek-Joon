import sys
ip=sys.stdin.readline
for _ in range(int(ip())):
    a=int(ip())
    if(a==0 or a==1): print(2); continue
    while True:
        p=1
        for i in range(2,int(a**0.5)+1):
            if(a%i==0): p=0; break
        if(p==1):
            print(a)
            break
        a+=1