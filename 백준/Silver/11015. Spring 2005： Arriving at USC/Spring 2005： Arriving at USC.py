for k in range(int(input())):
    print(f'Data Set {k+1}:')
    l=[input() for _ in range(int(input()))]
    s=input().strip()
    for n in l:
        c=0
        for i in n:
            if(i.lower()==s[c].lower()):
                c+=1
            if(c==len(s)):
                print(n)
                break
    print()