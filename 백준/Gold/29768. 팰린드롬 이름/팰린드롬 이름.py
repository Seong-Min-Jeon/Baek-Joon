n,k=map(int,input().split())
s='a'*(n-k+1)
for i in range(k-1): s+=chr(98+i)
print(s)