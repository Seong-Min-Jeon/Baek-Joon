a=int(input())
l=list(map(int,input().split()))
l.sort()
s=[]
for i in range(a//2):
    s.append(l.pop())
for i in range(a):
    if(i%2==0):
        print(l.pop(), end=' ')
    else:
        print(s.pop(), end=' ')