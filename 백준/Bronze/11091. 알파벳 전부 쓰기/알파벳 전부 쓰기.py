a='abcdefghijklmnopqrstuvwxyz'
for _ in range(int(input())):
    s=input().strip()
    s=s.lower()
    r=[]
    for c in a:
        if(c not in s): r.append(c)
    if(len(r)==0): print('pangram')
    else: print('missing',''.join(r))