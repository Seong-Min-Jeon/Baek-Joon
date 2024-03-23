import datetime as d
t=input()
m=int(input())
t=d.datetime.strptime(t,'%H %M')
t=t-d.timedelta(minutes=-m)
print(f'{t.hour} {t.minute}')