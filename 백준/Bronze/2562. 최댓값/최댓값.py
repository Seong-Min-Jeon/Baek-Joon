a,b=0,0
for i in range(9):
    c=int(input())
    if(c>a): a=c; b=i
print(f'{a}\n{b+1}')