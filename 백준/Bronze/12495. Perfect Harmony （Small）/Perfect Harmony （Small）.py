I=input
F=lambda:map(int,I().split())
for k in range(int(I())):
    n,l,h=F()
    t=[*F()]
    for i in range(l,h+1):
        f=0
        for e in t:
            if(e%i==0 or i%e==0): f=1
            else: f=0; break            
        if(f): print(f'Case #{k+1}: {i}'); break
    if(f==0): print(f'Case #{k+1}: NO')