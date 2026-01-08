l=[int(input()) for _ in range(int(input()))]
if(l[1]-l[0]==l[2]-l[1]): print(l[-1]+l[1]-l[0])
else: print(l[-1]*(l[1]//l[0]))