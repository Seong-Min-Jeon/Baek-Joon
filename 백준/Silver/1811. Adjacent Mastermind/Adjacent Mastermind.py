import sys
ip=sys.stdin.readline
while True:
    s=ip()
    if(s.strip()=='#'): break
    l=[]
    l.append(list(s.split()[0]))
    l.append(list(s.split()[1]))
    b,g,w=0,0,0
    for i in range(len(l[0])):
        if(l[0][i]==l[1][i]):
            b+=1
            l[0][i]='#'
            l[1][i]='#'
    for i in range(len(l[0])):
        if(l[1][i]=='#'): continue
        if(i>0 and l[0][i-1]==l[1][i]):
            g+=1
            l[0][i-1]='#'
            l[1][i]='#'
        elif(i<len(l[0])-1 and l[0][i+1]==l[1][i]):
            g+=1
            l[0][i+1]='#'
            l[1][i]='#'
    for i in range(len(l[0])):
        if(l[1][i]=='#'): continue
        if(l[1][i] in l[0]):
            w+=1
            l[0][l[0].index(l[1][i])]='#'
            l[1][i]='#'
    print(f'{s.split()[1]}: {b} black, {g} grey, {w} white')