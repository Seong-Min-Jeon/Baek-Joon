a=int(input())
for i in range(1,2*a):
    if(i>a):
        print((i-a)*' '+(4*a-2*i-1)*'*')
    else:
        print((a-i)*' '+(2*i-1)*'*')