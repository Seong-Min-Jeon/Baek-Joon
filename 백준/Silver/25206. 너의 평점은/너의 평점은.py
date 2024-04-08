total_credit=0
credit_x_grade=0
for _ in range(20):
    l=input().split()
    credit=int(float(l[1]))
    total_credit+=credit
    grade=0
    if(l[2]=="A+"): grade=4.5
    elif(l[2]=="A0"): grade=4.0
    elif(l[2]=="B+"): grade=3.5
    elif(l[2]=="B0"): grade=3.0
    elif(l[2]=="C+"): grade=2.5
    elif(l[2]=="C0"): grade=2.0
    elif(l[2]=="D+"): grade=1.5
    elif(l[2]=="D0"): grade=1.0
    elif(l[2]=="F"): grade=0
    else: total_credit-=credit
    credit_x_grade+=credit*grade
print(credit_x_grade/total_credit)