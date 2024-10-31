import sys
ip=sys.stdin.readline

def split(l:list):
    global b,w
    temp=[]
    for i in l:
        for j in i:            
            temp.append(j)
    if('1' not in temp): b+=1; return
    if('0' not in temp): w+=1; return
    n=len(l)
    p=[i[:n//2] for i in l[:n//2]]
    q=[i[n//2:] for i in l[:n//2]]
    r=[i[:n//2] for i in l[n//2:]]
    s=[i[n//2:] for i in l[n//2:]]
    split(p)
    split(q)
    split(r)
    split(s)

n=int(ip())
l=[]
for _ in range(n):
    l.append(ip().split())
b=0
w=0
split(l)
print(b)
print(w)