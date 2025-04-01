for k in range(int(input())):
    l=[input() for _ in range(int(input()))]
    s=input().strip()
    r=[]
    for n in l:
        c=0
        for i in n:
            if(i.lower()==s[c].lower()):
                c+=1
            if(c==len(s)):
                r.append(n)
                break
    print(f'Data Set {k+1}:')
    for e in r:
        print(e)
    print()