import sys
I=sys.stdin.readline
r,c,h=map(int,I().split())
l=[[list(I().strip()) for _ in range(r)] for _ in range(h)]
q=''
for k in range(h):
    for i in range(r):
        for j in range(c):            
            if(l[k][i][j]=='*'): q+='*'
            else:
                b=0
                for z in range(k-1,k+2):
                    for x in range(i-1,i+2):
                        for y in range(j-1,j+2):
                            if(0<=z<h and 0<=x<r and 0<=y<c and l[z][x][y]=='*'): b+=1
                q+=str(b%10)
            if(len(q)==c): print(q); q=''