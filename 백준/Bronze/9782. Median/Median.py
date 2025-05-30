i=0
while True:
    i+=1
    l=list(map(int,input().split()))
    del l[0]
    if(len(l)==0): break
    if(len(l)%2==0): print(f'Case {i}: {(l[len(l)//2-1]+l[len(l)//2])/2}')
    else: print(f'Case {i}: {float(l[len(l)//2])}')