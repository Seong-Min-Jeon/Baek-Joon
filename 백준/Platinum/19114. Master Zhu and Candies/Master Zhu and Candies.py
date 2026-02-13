I=input;I();x=0
for e in map(int,I().split()):
    if(e%8==0): x^=(e-1)
    elif(e%8==7): x^=(e+1)
    else: x^=e
print('First' if x else 'Second')