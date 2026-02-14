n=int(input())
print(f'{n} in Ottawa')
for a,b in ((n-300,'Victoria'),(n-200,'Edmonton'),(n-100,'Winnipeg'),(n,'Toronto'),(n+100,'Halifax'),(n+130,"St. John's")):
    if(a%100>=60): a-=60; a+=100
    if(a<0): a+=2400
    if(a>2400): a-=2400
    print(f'{a} in {b}')