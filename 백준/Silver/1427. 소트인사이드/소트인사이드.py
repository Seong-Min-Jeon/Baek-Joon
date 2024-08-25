a=input()
l=list(map(int,a))
l.sort(reverse=True)
for i in l:
    print(i, end='')