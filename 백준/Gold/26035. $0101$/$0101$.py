M=10**9+7
a,b=map(int,input().split())
print((pow(2,a,M)+pow(2,b,M)-2)%M)