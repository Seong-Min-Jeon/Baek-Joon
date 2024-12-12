while True:
    a=float(input())
    if(a==0): break
    print(format(round(a**4+a**3+a**2+a**1+1,2),'.2f'))