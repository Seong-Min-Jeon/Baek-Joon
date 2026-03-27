for _ in range(int(input())):
    s=input().strip()
    c=0
    for e in s:
        if(e in ('a','e','i','o','u')):
            c+=1
    print(f'The number of vowels in {s} is {c}.')