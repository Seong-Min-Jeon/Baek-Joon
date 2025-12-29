for _ in range(int(input())):
    s=input().strip()
    a=s.replace('@','a').replace('[','c').replace('!','i').replace(';','j').replace('^','n').replace('0','o').replace('7','t').replace('\\\\\'','w').replace('\\\'','v')
    b=s.replace('@','%').replace('[','%').replace('!','%').replace(';','%').replace('^','%').replace('0','%').replace('7','%').replace('\\\\\'','%').replace('\\\'','%')
    if(b.count('%')>=len(a)/2): print("I don't understand")
    else: print(a)