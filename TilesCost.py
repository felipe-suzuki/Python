def user_info():

    global w,h,p
    
    w = 0
    h = 0
    p = 0
    
    while w == 0:
        
        try:
            w = float(input('Insert the width of the floor plan (insert the value in meters): '))
                        
        except:
            print('\n\tNot a valid number!')
            
        if w == 0.0:
            print('\n\tPlease, insert a value greater than 0!')
            
    while h == 0:
            
        try:
            h = float(input('Insert the height of the floor plan (insert the value in meters): '))
            
        except:
            print('\n\tNot a valid number!')
        if h == 0.0:
            print('\n\tPlease, insert a value greater than 0!')
            
    while p== 0:
                
        try:
            p = float(input('Insert the price of the tiles (insert the value per square meter): '))
            
        except:
            print('\n\tNot a valid number!')
                    
        if p == 0.0:
            print('\n\tPlease, insert a value greater than 0!')
        
    print (f'\nThe floor has width of {w} m and height of {h} m and the tile price is {p} US$ per m².')    

def calculate_cost(w,h,p):
    
    area = w*h
    total_cost = area*p
    
    print(f'\nThe total tile cost to cover an area of {area:0.2f} m² is {total_cost:0.2f} US$.')


user_info()

calculate_cost(w,h,p)

quit = input('\nPress any key to exit.')
