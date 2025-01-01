for _ in range(int(input())):
    s=input()
    r='0'
    for e in s:
        if(r[-1]!=e): r+=e
    print(r[1:])