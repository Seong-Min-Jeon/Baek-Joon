l=[0]
f,M=1,1000000007
for i in range(int(input())-1):
    if(f): l.append((l[-1]*2)%M+1); f=0
    else: l.append((l[-1]*2)%M-1); f=1
print(l[-1]%M)