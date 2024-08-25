a=int(input())
l=[[] for _ in range(51)]
for i in range(a):
    b=input()
    l[len(b)].append(b)
for i in l:
    if(len(i)==0): continue
    elif(len(i)==1): print(i.pop())
    else:
        for j in sorted(set(i)):
            print(j)