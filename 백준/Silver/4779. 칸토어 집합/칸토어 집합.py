def f(n):
    if(n<=1): print('-',end=''); return
    f(n//3)
    for i in range(n//3): print(' ',end='')
    f(n//3)
try:
    while True:
        f(3**int(input()))
        print()
except:
    exit()