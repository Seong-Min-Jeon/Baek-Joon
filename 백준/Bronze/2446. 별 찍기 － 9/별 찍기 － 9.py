n=int(input())
l=[]
for i in range(n):
    l.append(' '*i+'*'*(2*n-2*i-1))
for e in l:
    print(e)
l.pop()
l.reverse()
for e in l:
    print(e)