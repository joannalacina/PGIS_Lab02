print ('Zadanie 3')

from math import sqrt

def kwadratowa(a,b,c,x):
    y=(a*x)**2+(b*x)+c
    return y

#print kwadratowa(1,2,3,4)

def zerowe(a,b,c):
    delta=(b**2)-(4*a*c)
    if delta>0:
        miejsca_zerowe=[(-b-sqrt(delta))/(2*a),(-b+sqrt(delta))/(2*a)]
    elif delta==0:
        miejsca_zerowe=[-b/(2*a)]
    else:
        return None
    return miejsca_zerowe

#print zerowe(2,4,2)


print zerowe(2,6,5)
for x in range(-10,10):
    print kwadratowa(2,6,5,x)

    


