#The card credit validator will take every digit out of a 16-digit number inserted by the user and multiply it by 2. Then if the result of the multiplication is a 2-digit number, it will subtract 9.
#After this, the sum of these multiplications must be a number divisible by 10. In this case, the card credit number is validated, else it is not a valid number.

#Example: 2323 2323 2323 2323
#After multiplication by 2: 4646 4646 4646 4646
#Sum each digit: 4+6+4+6+4+6+4+6+4+6+4+6+4+6+4+6 = 80
#80 is divisible by 10, so it is a valid number.

def get_cardn():
    
    global mycard
    
    mycard = []
        
    while mycard == [] or len(str(mycard)) != 16:
        
        try:
            mycard = int(input('\nInsert the 16 numbers of your credit card: '))
                
        except:
            print('Please insert a 12-digit value')
        
def check_sum(mycard):
    
    total_sum = 0
    a = 0
    mycard = str(mycard)
        
    for n in range(0,len(mycard)):
        
        a = int(mycard[n])*2
        
        if a > 9:
            a = int(mycard[n])*2 - 9
            total_sum += a
        
        else:
            a = int(mycard[n])*2
            total_sum += a
            
    if total_sum%10 == 0:
        print('\nThe number',mycard,'is a valid credit card!')
            
    else:
        print('\nThe number',mycard,'is not a valid credit card!')

get_cardn()

check_sum(mycard)

input('\nPress any key to exit')
