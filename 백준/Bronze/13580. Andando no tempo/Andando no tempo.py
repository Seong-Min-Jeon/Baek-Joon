a,b,c=map(int,input().split())
if(len(set([a,b,c]))<3): print('S'); exit()
if(a+b==c or a+c==b or b+c==a): print('S'); exit()
print('N')