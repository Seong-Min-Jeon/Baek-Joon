l=[[int(input()),i+1] for i in range(int(input()))]
c=0
if(len(l)==1): print(0); exit()
while True:
    l.sort()
    if(l[-1][1]==1 and l[-2][0]<l[-1][0]): print(c); break
    l[-1][0]-=1
    for i in range(len(l)):
        if(l[i][1]==1):
            l[i]=[l[i][0]+1,1]
            c+=1