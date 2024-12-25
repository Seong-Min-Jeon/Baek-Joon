ip=input
for i in range(int(ip())):
    a=int(ip())
    b=sum(list(map(int,ip().split())))
    for i in range(10**9):
        if(a<b*4**i): print(i+1); break