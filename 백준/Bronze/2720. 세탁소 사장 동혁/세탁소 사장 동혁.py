i=input; c=int(i())
for _ in range(c):
    q,d,n,p = 0,0,0,0
    a=int(i())
    while a>=25: a-=25; q+=1
    while a>=10: a-=10; d+=1
    while a>=5: a-=5; n+=1
    while a>=1: a-=1; p+=1
    print(q,d,n,p)
