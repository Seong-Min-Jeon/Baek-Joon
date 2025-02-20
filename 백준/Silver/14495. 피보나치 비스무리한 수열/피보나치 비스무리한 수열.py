a,b,c=1,1,1
for _ in range(int(input())-3): a,b,c=b,c,a+c
print(c)