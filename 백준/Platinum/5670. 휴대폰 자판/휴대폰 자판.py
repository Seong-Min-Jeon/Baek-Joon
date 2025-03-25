import sys
I=sys.stdin.readline
def f(d,s):
    for c in s:
        if(c not in d): d[c]={}
        d=d[c]
    d['*']=0
def g(d,s):
    n=1
    for i,c in enumerate(s):
        if(len(s)-1==i): break
        if(len(d[c])>1): d=d[c]; n+=1
        elif(len(d[c])==1): d=d[c]
    return n
while True:
    try:
        d={}
        l=[]
        for _ in range(int(I())): 
            s=list(input().strip())
            f(d,s)
            l.append(s)
        t=0
        for s in l: t+=g(d,s)
        print(f'{round(t/len(l),2):.2f}')
    except:
        break