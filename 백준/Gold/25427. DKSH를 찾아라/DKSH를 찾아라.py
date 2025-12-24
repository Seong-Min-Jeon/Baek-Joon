n=int(input())
l=list(input().strip())
d=[[0]*n for _ in range(4)]
for i in range(n):    
    d[0][i]=d[0][i-1]+(l[i]=='D')
    d[1][i]=d[1][i-1]+d[0][i] if l[i]=='K' else d[1][i-1]
    d[2][i]=d[2][i-1]+d[1][i] if l[i]=='S' else d[2][i-1]
    d[3][i]=d[3][i-1]+d[2][i] if l[i]=='H' else d[3][i-1]
print(d[-1][-1])