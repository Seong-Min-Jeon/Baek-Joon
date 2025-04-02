for _ in range(int(input())):
    s=input().strip()
    for _ in range(int(input())):
        r=input().strip()
        l=[]
        g=0
        for c in r:
            f=0
            for i in range(len(s)):
                if(s[i]==c and i not in l):
                    l.append(i)
                    f=1
                    break
            if(not f): print('NO'); g=1; break
        if(not g): print('YES')