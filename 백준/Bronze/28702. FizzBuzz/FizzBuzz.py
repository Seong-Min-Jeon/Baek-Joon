def p(n):
    if(n%3==0 and n%5==0): print('FizzBuzz')
    elif(n%3==0): print('Fizz')
    elif(n%5==0): print('Buzz')
    else: print(n)
    exit()

a,b,c=input(),input(),input()
if(a[0]!='F' and a[0]!='B'): p(int(a)+3)
if(b[0]!='F' and b[0]!='B'): p(int(b)+2)
if(c[0]!='F' and c[0]!='B'): p(int(c)+1)