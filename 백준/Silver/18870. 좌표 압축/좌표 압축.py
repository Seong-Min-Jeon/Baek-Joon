import sys
a=int(sys.stdin.readline())
l=list(map(int, sys.stdin.readline().split()))
m=sorted(list(set(l)))
dic={}
for i in range(len(m)):
    dic[m[i]]=i
for i in l:
    print(dic[i], end = ' ')