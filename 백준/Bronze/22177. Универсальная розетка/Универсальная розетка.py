n,d=map(int,input().split())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
for i in l:
    for j in l:       
        if(i[2]==j[2]): continue                
        if(d==((i[0]-j[0])**2+(i[1]-j[1])**2)**0.5):
            print('Yes')
            exit(0)
print('No')