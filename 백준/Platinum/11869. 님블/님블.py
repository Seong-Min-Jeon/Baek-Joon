I=input;I()
x=0
for e in map(int,I().split()):
    x^=e
print('cubelover' if x==0 else 'koosaga')