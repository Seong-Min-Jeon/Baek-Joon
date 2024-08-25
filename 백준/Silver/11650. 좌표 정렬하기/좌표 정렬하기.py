a=int(input())
l=[]
for i in range(a):
    b,c=map(int,input().split())
    b+=1000000
    c+=1000000
    l.append(b*10000000+c)
l.sort()
for i in l:
    i=str(i)
    if(i[0]=='9'): i='0'+i
    print(int(i[0:7])-1000000, int(i[7:14])-1000000)