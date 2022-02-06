def change_value():
    
    global change
    
    change = 0
    money_given = 0
    total_cost = 0
    
    while money_given == 0:
        
        try:
            money_given = float(input('Please, insert the amount of money given (insert value in US$): '))
        except:
            print('Insert a valid value')
        if money_given == 0:
            print('Insert a value greater than 0')
    
    while total_cost == 0 or total_cost > money_given:
        
        try:
            total_cost = float(input('Please, insert the total cost of the products (insert value in US$): '))
        except:
            print('Insert a valid value')
        if total_cost == 0:
            print('Insert a value greater than 0')
        elif total_cost > money_given:
            print('Please, insert a value smaller than the money given')
    
    change = money_given - total_cost
    
    print (f'\nThe change is US$ {change:0.2f}')
        
def get_change(change):
    
    coins = {'quarters':0,'dimes':0,'nickels':0,'pennies':0}
    remainder = change
    
    coins['quarters'] = int(remainder//.25)
    remainder = remainder%0.25
    
    coins['dimes'] = int(remainder//0.1)
    remainder = remainder%0.1
    
    coins['nickels'] = int(remainder//0.05)
    remainder = remainder%0.05 
    
    coins['pennies'] = int(remainder//0.01)
        
    print ('\nThe change should be',coins['quarters'], 'quarters,', coins['dimes'],'dimes,', coins['nickels'],'nickels and', coins['pennies'],'pennies')

change_value()

get_change(change)

input('\nPress any key to exit')     