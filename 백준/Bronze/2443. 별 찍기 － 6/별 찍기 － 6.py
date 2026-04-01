n=int(input())
s=[]
for i in range(n):
    s.append(' '*(n-i-1)+'*'*(2*i+1))
for e in reversed(s):
    print(e)