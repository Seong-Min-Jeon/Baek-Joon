n=int(input())
l=[*map(int,input().split())]
for i in range(n):
    if(l[i]%2): l[i]=l[i]//2+1
    else: l[i]=l[i]//2-1
x=0
for e in l:
    x^=e
print('koosaga' if x else 'cubelover')