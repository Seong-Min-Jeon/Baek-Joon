i=input()
a=int(i.split()[0])*int(i.split()[1])
for e in list(map(int,input().split())):
    print(e-a, end=' ')