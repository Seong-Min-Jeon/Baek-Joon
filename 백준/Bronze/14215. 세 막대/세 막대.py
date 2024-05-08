a,b,c=map(int,input().split())
if(a+b+c<=2*max(a,b,c)): print(2*(a+b+c-max(a,b,c))-1)
else: print(a+b+c)