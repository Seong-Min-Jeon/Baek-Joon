l=[[0]*(2**15+1) for _ in range(4)]
for i in range(1,int(32768**0.5)+1):
    l[0][i*i]=1
    for k in range(i**2,32768+1):
        l[1][k]+=l[0][k-i**2]
        l[2][k]+=l[1][k-i**2]
        l[3][k]+=l[2][k-i**2]
while True:
    n=int(input())
    if(n==0): break
    print(l[0][n]+l[1][n]+l[2][n]+l[3][n])