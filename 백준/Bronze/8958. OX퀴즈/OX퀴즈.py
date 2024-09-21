import sys
ip=sys.stdin.readline
for _ in range(int(ip())):
    a=ip()
    s,c=0,1
    for e in a:
        if(e=='O'): s+=c; c+=1
        else: c=1
    print(s)