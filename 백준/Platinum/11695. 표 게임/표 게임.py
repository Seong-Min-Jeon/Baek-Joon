n,m=map(int,input().split())
l=[]
for _ in range(n):
    l.append(sum(map(int,input().split())))
x=0
for e in l:
    x^=e
print('august14' if x else 'ainta')