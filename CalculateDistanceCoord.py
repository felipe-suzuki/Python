from math import sin, cos, asin, pi

def get_coord1():
    
    global x1,y1

    x1 = 0
    y1 = 0
    
    while y1 == 0:
        
        try:
            y1 = float(input('Please insert the latitude of the location 1: '))
        except:
            print('Please, insert the value in decimals')
        
    while x1 == 0:
        try:
            x1 = float(input('Please insert the longitude of the location 1: '))
        except:
            print('Please, insert the value in decimals')

def get_coord2():
      
    global x2,y2

    x2 = 0
    y2 = 0
    
    while y2 == 0:
        
        try:
            y2 = float(input('\nPlease insert the latitude of the location 2: '))
        except:
            print('Please, insert the value in decimals')
        
    while x2 == 0:
        try:
            x2 = float(input('Please insert the longitude of the location 2: '))
        except:
            print('Please, insert the value in decimals')  

def calc_dist(x1,x2,y1,y2):
    
    rx1 = x1*(pi/180)
    rx2 = x2*(pi/180)
    ry1 = y1*(pi/180)
    ry2 = y2*(pi/180)
    
    dist_x = abs(rx2 - rx1)
    dist_y = abs(ry2 - ry1)
    
    #wrong first try = a = ((((sin(Δlat/2))**2)+cos(lat1))*(cos(lat2)*((sin(Δlong/2))**2)
    #a = sin(Δlat/2)**2+cos(lat1)*cos(lat2)*sin(Δlong/2)**2)
    a = sin(dist_y/2)**2+cos(ry1)*cos(ry2)*sin(dist_x/2)**2
    
    #c = 2*asin(√a)
    c = 2*asin((a**0.5))
        
    #d = R*c, R is the Earth's radius in kilometer = 6,371 km
    d = 6371*c
    
    print('\nLocation 1: latitude',y1,'and longitude',x1)
    print('Location 2: latitude',y2,'and longitude',x2)
    print(f'\nThe distance between the 2 locations is equal to {d:0.2f} km.')

get_coord1()

get_coord2()

calc_dist(x1,x2,y1,y2)

input('Press any key to exit.')