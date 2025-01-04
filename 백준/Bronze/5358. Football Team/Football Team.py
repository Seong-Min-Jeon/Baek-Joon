while True:
    try:
        s=input()
        s=s.replace('i','#')
        s=s.replace('e','i')
        s=s.replace('#','e')
        s=s.replace('I','#')
        s=s.replace('E','I')
        s=s.replace('#','E')
        print(s)
    except:
        exit()