print('Gnomes:')
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if((a<=b and b<=c) or (a>=b and b>=c)):
        print('Ordered')
    else: print('Unordered')