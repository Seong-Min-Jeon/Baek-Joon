for _ in range(int(input())):
    a,b=input().strip().split()
    s=''
    for i,e in enumerate(b):
        t=ord(e)+ord(a[i%len(a)])%65        
        if(t>90): t-=26
        s+=chr(t)
    print(f'Ciphertext: {s}')