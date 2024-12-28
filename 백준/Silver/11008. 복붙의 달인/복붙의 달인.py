i=input
for _ in range(int(i())):
    a,b=i().split()
    print(len(a.replace(b,'#')))