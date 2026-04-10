n=int(input())
for i in range(1,n):
    print('*'*i+' '*(2*n-2*i)+'*'*i)
print('*'*(2*n))
for i in range(n-1,0,-1):
    print('*'*i+' '*(2*n-2*i)+'*'*i)