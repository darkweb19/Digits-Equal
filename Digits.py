#To check wheather the digits of number are equal or not

def Check(num1 , num2) :
    newRem = newRem2= 0
    
    while num1 > 0 :
        rem = num1 % 10 
        newRem = newRem +rem
        num1 //=10

    while num2 > 0 :
        rem2 = num2 %10
        newRem2 = newRem2 + rem2
        num2 //=10

    if newRem == newRem2 :
        print("Equal")
    else :
        print('Not equal')


Check(112,21)