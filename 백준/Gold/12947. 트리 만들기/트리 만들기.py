input()
l=list(map(int,input().split()))
s=set()
while 1 in l: 
    i=l.index(1)
    s.add(len(l)+i)
    l=l[i+1:]
s.add(len(l)*2)
print(max(s))