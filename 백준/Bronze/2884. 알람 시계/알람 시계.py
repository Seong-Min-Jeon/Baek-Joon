import datetime as d
t=input()
t=d.datetime.strptime(t,'%H %M')
t=t-d.timedelta(minutes=45)
print(f'{t.hour} {t.minute}')