a=int(input())
s=set()
for _ in range(a):
    b=input().split()
    if(b[1]=='enter'): s.add(b[0])
    else: s.remove(b[0])
l=sorted(list(s), reverse=True)
for i in l:
    print(i)