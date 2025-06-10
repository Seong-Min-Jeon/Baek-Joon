for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    s=b+c+d
    if(s<55 or b<11 or c<8 or d<12): print(a,s,'FAIL')
    else: print(a,s,'PASS')