import sys

def valid(y:int, m:int, d:int):
    if(m==0 or d==0):
        return False
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        if(d<=31):
            return True
    elif(m==4 or m==6 or m==9 or m==11):
        if(d<=30):
            return True
    else:
        if(y%4==0 and d<=29):
            return True
        elif(y%4!=0 and d<=28):
            return True
    return False     

input=sys.stdin.readline
y,m,d=map(int,input().split())
n=int(input())
for _ in range(n):
    a,b,c=map(int,input().split())
    o=0
    p=0
    q=0
    if(b<=12 and valid(a,b,c)):
        if(y<a or (y==a and m<b) or (y==a and m==b and d<=c)):
            o=1
    else:
        o=-1
    if(b<=12 and valid(c,b,a)):
        if(y<c or (y==c and m<b) or (y==c and m==b and d<=a)):
            p=1
    else:
        p=-1    
    if(a<=12 and valid(c,a,b)):
        if(y<c or (y==c and m<a) or (y==c and m==a and d<=b)):
            q=1
    else:
        q=-1
    s=set((o,p,q))
    if(s=={1, -1} or s=={1}):
        print("safe")
    elif(s=={-1}):
        print("invalid")
    else:
        print("unsafe")