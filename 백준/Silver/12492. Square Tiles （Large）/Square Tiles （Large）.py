I=input
for k in range(int(I())):
    print(f'Case #{k+1}:')
    n,m=map(int,I().split())
    l=[list(I().strip()) for _ in range(n)]
    f=0
    for i in range(n):
        for j in range(m):
            if(l[i][j]=='#'):
                l[i][j]='/'
                if(i+1<n and j+1<m):
                    if(l[i+1][j]=='#'):
                        l[i+1][j]='\\'
                    else:
                        f=1
                    if(l[i][j+1]=='#'):
                        l[i][j+1]='\\'
                    else:
                        f=1
                    if(l[i+1][j+1]=='#'):
                        l[i+1][j+1]='/'
                    else:
                        f=1
                else: 
                    f=1
    if(f):
        print('Impossible')
    else:
        for e in l:
            print(''.join(e))