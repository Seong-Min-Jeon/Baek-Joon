d={'010':'1','093':'2','079':'3',
   '106':'4','103':'5','119':'6',
   '011':'7','127':'8','107':'9',
   '063':'0'}
while True:
    s=input().strip()
    if(s=='BYE'): break
    f,t=0,0
    a,b='',''
    r=''
    for i in range(len(s)):
        if(s[i]=='+'): t=1
        elif(s[i]=='='): pass
        else: f+=1; r+=s[i]
        if(f==3):
            if(t):
                b+=d[r]
            else:
                a+=d[r]
            f,r=0,''
    g=str(int(a)+int(b))
    r=''
    for c in g:
        for k in d:
            if(d[k]==c):
                r+=k
    print(s+r)