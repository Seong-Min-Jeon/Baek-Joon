l=[]
for _ in range(int(input())):
    s=input().strip()
    t=''
    for e in s:
        if(e in ('0','1','2','3','4','5','6','7','8','9')):
            t+=e
        elif(t!=''):
            l.append(int(t))
            t=''
    if(t!=''):
        l.append(int(t))
for e in sorted(l):
    print(e)