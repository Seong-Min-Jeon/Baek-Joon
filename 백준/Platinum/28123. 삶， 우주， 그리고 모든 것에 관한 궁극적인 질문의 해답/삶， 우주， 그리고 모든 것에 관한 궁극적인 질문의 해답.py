n,k,x=map(int,input().split())
if(x==1): print(n-3*(k-1))
elif(x in [2,3,4]): print(n-3*(k-1)-1)
elif(x in [5,6,7,8,9]): print(n-3*(k-1)-2)