n=int(input())
f=1;v=0
while True:
    if(f):
        t=input().strip()
        if(t=='+'):v=1
        elif(t=='-'):v=2
        elif(t=='*'):v=3
        elif(t=='/'):v=4
        else: break
        f=0
    else:
        t=int(input())
        if(v==1):n+=t
        elif(v==2):n-=t
        elif(v==3):n*=t
        elif(v==4):n//=t
        f=1
print(n)