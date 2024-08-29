l=['123','456','789','147','258','369','580']
u=False
a=input()
for i in l:
    if(a[0] in i and a[1] in i and a[2] in i):
        u=True
if(len(set(a))!=3):
    u=False
if(u):
    print('Unlocked')
else:
    print('Locked')