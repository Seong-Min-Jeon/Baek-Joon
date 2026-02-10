I=input;I()
x=0
for e in map(int,I().split()):
    x^=e-2
n=I().strip()
if(n=='Whiteking'):
    print('Whiteking' if x else 'Blackking')
else:
    print('Blackking' if x else 'Whiteking')