import sys

def remove(l,x,y):
    if(l[x-1][y-1]=='#'):
        l[x-1][y-1]='.'
        remove(l,x-1,y-1)
    elif(l[x-1][y]=='#'):
        l[x-1][y]='.'
        remove(l,x-1,y)
    elif(l[x-1][y+1]=='#'):
        l[x-1][y+1]='.'
        remove(l,x-1,y+1)
    elif(l[x][y-1]=='#'):
        l[x][y-1]='.'
        remove(l,x,y-1)
    elif(l[x][y+1]=='#'):
        l[x][y+1]='.'
        remove(l,x,y+1)
    elif(l[x+1][y-1]=='#'):
        l[x+1][y-1]='.'
        remove(l,x+1,y-1)
    elif(l[x+1][y]=='#'):
        l[x+1][y]='.'
        remove(l,x+1,y)
    elif(l[x+1][y+1]=='#'):
        l[x+1][y+1]='.'
        remove(l,x+1,y+1)

input=sys.stdin.readline
a,b=map(int,input().split())
l=[[] for _ in range(a+2)]
l[0]=['.' for _ in range(b+2)]
l[len(l)-1]=['.' for _ in range(b+2)]
for i in range(1,a+1):
    t=list(input().strip())
    t.insert(0,'.')
    t.append('.')
    l[i]=t
c,p=0,0
while True:
    s=0
    for i in range(a):
        if('#' in l[i]):
            c+=1
            s=l[i].index('#')
            l[i][s]='.'
            break
        if(i==a-1):
            p=1
    if(p==1):
        break
    remove(l,i,s)
print(c)