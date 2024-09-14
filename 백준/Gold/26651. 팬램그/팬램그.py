def p(b,e,c):
    s=''
    s+='A'*b
    s+='BCDEFGGHIJKLMNOPQRSSTUVWXY'
    s+='Z'*e
    s+='ABCDEFGGHIJKLMNOPQRSSTUVWXYZ'*c
    print(s)
    exit()

a=int(input())
if(a==0): print('A'); exit()
l=[]
c=0
while True:
    for i in range(1,int(a**0.5+1)):
        if(a%i==0):
            l.append(i)
    for e in l:
        b=a//e
        if(b<50000 and e<50000):
            p(b,e,c)
    a-=1
    c+=1