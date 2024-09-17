import sys
i=sys.stdin.readline
while True:
    s=i().strip()
    g=set(['a','e','i','o','u'])
    if(s=='end'): break
    if(len(g.intersection(set(s)))==0):
        print(f'<{s}> is not acceptable.'); continue
    t=0
    p=''
    b=0
    for e in s:
        if(e in g): 
            if(t<=0): t-=1
            else: t=-1
        else:
            if(t>=0): t+=1
            else: t=1
        if(t==3 or t==-3):
            print(f'<{s}> is not acceptable.'); b=1; break
        if(e==p):
            if(e!='e' and e!='o'):
                print(f'<{s}> is not acceptable.'); b=1; break
        p=e
    if(b==0):
        print(f'<{s}> is acceptable.')