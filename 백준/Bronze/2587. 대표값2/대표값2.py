s=0
l=[]
for i in range(5):
    n=int(input())
    s+=n
    l.append(n)
l.sort()
print(s//5)
print(l[2])