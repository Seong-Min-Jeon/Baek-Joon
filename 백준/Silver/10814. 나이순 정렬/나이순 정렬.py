import sys
a=int(input())
l=[[] for _ in range(201)]
for _ in range(a):    
    i=sys.stdin.readline().strip()    
    l[int(i.split()[0])].append(i)
for i in l:
    if(len(i)==0): continue
    for j in i:
        print(j)