c=0
for _ in range(int(input())):
    s=input()
    if('01' in s or 'OI' in s):
        c+=1
print(c)