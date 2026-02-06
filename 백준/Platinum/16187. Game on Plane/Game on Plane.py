import sys
I=sys.stdin.readline
l=[0]*5001
l[0],l[1],l[2]=0,0,1
for i in range(3,5001):
    s=set()
    for j in range(i-2):
        t=l[j]^l[i-j-2]
        s.add(t)
    for k in range(5000):
        if(k not in s):
            l[i]=k
            break
for _ in range(int(I())):    
    print('First' if l[int(I())]!=0 else 'Second')