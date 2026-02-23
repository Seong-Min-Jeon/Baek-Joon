import sys
I=sys.stdin.readline
x=0
for _ in range(int(I())):
    a,b=map(int,I().split())
    if(b%2):
        if(a%2): x^=1
        else: x^=0
    else:
        a+=1;b+=1
        t=a%b
        if(a%b==0): x^=2
        else:
            if(t%2): x^=0
            else: x^=1
print('Alice' if x else 'Bob')