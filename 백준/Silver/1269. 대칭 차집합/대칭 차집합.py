input()
m=set(map(int,input().split()))
n=set(map(int,input().split()))
print(len(m.difference(n))+len(n.difference(m)))