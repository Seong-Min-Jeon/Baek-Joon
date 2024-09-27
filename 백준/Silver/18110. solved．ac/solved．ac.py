import sys
def round(n):
    if(n-int(n)>=0.5):
        return int(n)+1
    return int(n)

ip=sys.stdin.readline
n=int(ip())
if(n==0): print(0); exit()
l=[]
for _ in range(n):
    l.append(int(ip()))
l.sort()
k=round(n*15/100)
l=l[k:len(l)-k]
print(round(sum(l)/len(l)))