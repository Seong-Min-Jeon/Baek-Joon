while True:
    try:
        a,b,c,d,w,x,y,z=map(float,input().split())
        if(a==w and b==x): a,c=c,a; b,d=d,b
        elif(a==y and b==z): a,c=c,a; b,d=d,b; w,y=y,w; x,z=z,x
        elif(c==y and d==z): w,y=y,w; x,z=z,x
        p=str(round(y-w+a,3))+'000'
        q=str(round(z-x+b,3))+'000'
        print(f'{p.split('.')[0]}.{p.split('.')[1][:3]} {q.split('.')[0]}.{q.split('.')[1][:3]}')
    except: break