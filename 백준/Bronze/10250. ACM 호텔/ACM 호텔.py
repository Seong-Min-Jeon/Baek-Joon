a=int(input())
m=[]
for _ in range(a):
    l=list(map(int,input().split()))
    r=101
    for i in range(l[0]*l[1]):
        if(i+1==l[2]):
            m.append(r)
            break
        if(r//100 < l[0]):
            r+=100
        else:
            r-=100*l[0]
            r+=101
for i in m:
    print(i)