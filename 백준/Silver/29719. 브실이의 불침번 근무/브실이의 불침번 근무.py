a,b=map(int,input().split());M=1000000007
print((pow(b,a,M)-pow(b-1,a,M))%M)