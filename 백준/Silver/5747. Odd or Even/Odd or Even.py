while True:
    a=int(input())
    if(a==0):
        break
    m=list(map(int,input().split()))
    j=list(map(int,input().split()))
    me=0
    for i in m:
        if(i%2==0): me+=1
    jo=0
    for i in j:
        if(i%2!=0): jo+=1
    print(abs(me-jo))