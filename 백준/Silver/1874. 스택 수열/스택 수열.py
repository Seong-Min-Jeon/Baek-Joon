import sys
ip=sys.stdin.readline
s=[]
n=1
r=[]

def push(n):    
    r.append('+'); s.append(n)

def pop():
    r.append('-'); s.pop()

for _ in range(int(ip())):
    a=int(ip())
    while True:
        if(len(s)==0): push(n); n+=1
        elif(s[-1]<a): push(n); n+=1
        elif(s[-1]==a): pop(); break
        else: print('NO'); exit()
for e in r:
    print(e)