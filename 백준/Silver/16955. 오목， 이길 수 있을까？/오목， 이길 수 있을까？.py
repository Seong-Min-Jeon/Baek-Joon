def f():
    for i in range(10):
        for j in range(10):
            if(l[i][j]=='X'):
                if(j<6 and len(set([l[i][j],l[i][j+1],l[i][j+2],l[i][j+3],l[i][j+4]]))==1): return 1
                elif(i<6 and len(set([l[i][j],l[i+1][j],l[i+2][j],l[i+3][j],l[i+4][j]]))==1): return 1
                elif(i<6 and j<6 and len(set([l[i][j],l[i+1][j+1],l[i+2][j+2],l[i+3][j+3],l[i+4][j+4]]))==1): return 1
                elif(i<6 and j>3 and len(set([l[i][j],l[i+1][j-1],l[i+2][j-2],l[i+3][j-3],l[i+4][j-4]]))==1): return 1
    return 0
l=[]
for _ in range(10):
    l.append(list(input()))
for i in range(10):
    for j in range(10):
        if(l[i][j]=='.'):
            l[i][j]='X'
            if(f()): print(1); exit()
            l[i][j]='.'
print(0)