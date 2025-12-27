while True:
    try:
        n=int(input())
        p,m=1,9
        while p<n:
            p*=m
            m=2 if m==9 else 9
        print('Donghyuk wins.' if m==9 else 'Baekjoon wins.')
    except:
        break