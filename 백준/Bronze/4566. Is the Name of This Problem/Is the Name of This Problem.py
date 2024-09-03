while True:
    i=input()
    if(i=="END"): exit(0)
    l=i.split("\"")
    if(i[0]!='\"'):
        print("not a quine")
        continue
    if(len(l)!=3):
        print("not a quine")
        continue    
    if(l[1]==''):
        print("not a quine")
        continue    
    if(l[1]==l[2][1:] and l[2][0]==' '):
        print(f'Quine({l[1]})')
    else:
        print("not a quine")
        continue