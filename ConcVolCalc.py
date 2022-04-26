#PLEASE CHECK THE UPDATED VERSIONS FOR CODE CHANGES AND IMPROVEMENTS. THANK YOU!

# This program can calculate the Volume or the Concentration of a solution that can be diluted into a final Volume and Concentration.
# In this problem, the user should input three variables (Final Concentration, Final Volume, and Initial Concentration or Initial Volume)
# to get the Forth unknown variable.
# This program is being updated and improved, and I will be uploading other versions soon.

# mass_unit = {1:'g', 3:'dg', 4:'cg', 5:'mg', 6:'ug', 7:'ng', 8:'pg'}
# volume_unit = {1:'L', 2:'dL', 3:'cL', 4:'mL', 5:'uL', 6:'nL', 7:'pL'}
mass_unit = {1:10**0, 2:10**-1, 3:10**-2, 4:10**-3, 5:10**-6, 6:10**-9, 7:10**-12}
volume_unit = {1:10**0, 2:10**-1, 3:10**-2, 4:10**-3, 5:10**-6, 6:10**-9, 7:10**-12}

c1 = 0
v1 = 0
mc1u = mass_unit
vc1u = volume_unit
v1u = volume_unit
imc1 = 0
ivc1 = 0
iv1 = 0

c2 = 0
v2 = 0
mc2u = mass_unit
vc2u = volume_unit
v2u = volume_unit
imc2 = 0
ivc2 = 0
iv2 = 0

term = 0

print('Given the formula C1.V1 = C2.V2, please choose C1 or V1 to be calculated.')

while term!='c1' and term!='v1':
    
    try:
        term = input('Insert C1 or V1: ')
        term = term.lower()
    except:
        print('Please insert a valid answer: C1 or V1')

if term == 'c1':
    
    while type(c2) != float:
        
        try:
            c2 = float(input('Please, insert the concentration of the final Solution 2: '))
        except:
            print('Please, insert a valid number')
    
    while imc2 not in range(1,7):
        
        try:
            imc2 = int(input('For the Mass unit of the Concentration of the final Solution 2, please choose the number for the respective unit: please choose the number for the respective unit: \n 1-g \n 2-dg \n 3-cg \n 4-mg \n 5-ug \n 6-ng \n 7-pg \n'))
        except:
            print('Please insert a valid number')
    
    while ivc2 not in range(1,7):
        
        try:
            ivc2 = int(input('For the Volume unit of the Concentration of the final Solution 2, please choose the number for the respective unit: \n 1-L \n 2-dL \n 3-cL \n 4-mL \n 5-uL \n 6-nL \n 7-pL \n'))
        except:
            print('Please insert a valid number')
    
    while type(v2) != float:
        
        try:
            v2 = float(input('Please, insert the volume of the final Solution 2: '))
        except:
            print('Please, insert a valid number')
    
    while iv2 not in range(1,7):
        
        try:
            iv2 = int(input('For the Volume unit of the final Solution 2, please choose the number for the respective unit: \n 1-L \n 2-dL \n 3-cL \n 4-mL \n 5-uL \n 6-nL \n 7-pL \n'))
        except:
            print('Please insert a valid number')
    
    while type(v1) != float:
        
        try:
            v1 = float(input('Please, insert the volume of the initial Solution 1: '))
        except:
            print('Please, insert a valid number')
    
    while iv1 not in range(1,7):
        
        try:
            iv1 = int(input('For the Volume unit of the initial Solution 1, please choose the number for the respective unit: \n 1-L \n 2-dL \n 3-cL \n 4-mL \n 5-uL \n 6-nL \n 7-pL \n'))
        except:
            print('Please insert a valid number')
    
    
    c1 = ((c2*((mc2u[imc2])/(vc2u[ivc2])))*(v2*v2u[iv2]))/(v1*v1u[iv1])
    print('To create', v2*v2u[iv2], 'L of the final Solution 2 with concentration of', (c2*((mc2u[imc2])/(vc2u[ivc2]))), 'g/L', 'you should use', v1*v1u[iv1], 'L of the initial Solution 1 with concentration of', c1, 'g/L')
    
if term == 'v1':
    
    while type(c2) != float:
        
        try:
            c2 = float(input('Please, insert the concentration of the final Solution 2: '))
        except:
            print('Please, insert a valid number')
    
    while imc2 not in range(1,7):
        
        try:
            imc2 = int(input('For the Mass unit of the Concentration of the final Solution 2, please choose the number for the respective unit: please choose the number for the respective unit: \n 1-g \n 2-dg \n 3-cg \n 4-mg \n 5-ug \n 6-ng \n 7-pg \n'))
        except:
            print('Please insert a valid number')
    
    while ivc2 not in range(1,7):
        
        try:
            ivc2 = int(input('For the Volume unit of the Concentration of the final Solution 2, please choose the number for the respective unit: \n 1-L \n 2-dL \n 3-cL \n 4-mL \n 5-uL \n 6-nL \n 7-pL \n'))
        except:
            print('Please insert a valid number')
    
    while type(v2) != float:
        
        try:
            v2 = float(input('Please, insert the volume of the final Solution 2: '))
        except:
            print('Please, insert a valid number')
    
    while iv2 not in range(1,7):
        
        try:
            iv2 = int(input('For the Volume unit of the final Solution 2, please choose the number for the respective unit: \n 1-L \n 2-dL \n 3-cL \n 4-mL \n 5-uL \n 6-nL \n 7-pL \n'))
        except:
            print('Please insert a valid number')
    
    while type(c1) != float:
        
        try:
            c1 = float(input('Please, insert the concentration of the initial Solution 1: '))
        except:
            print('Please, insert a valid number')
    
    while imc1 not in range(1,7):
        
        try:
            imc1 = int(input('For the Mass unit of the Concentration of the initial Solution 1, please choose the number for the respective unit: please choose the number for the respective unit: \n 1-g \n 2-dg \n 3-cg \n 4-mg \n 5-ug \n 6-ng \n 7-pg \n'))
        except:
            print('Please insert a valid number')
    
    while ivc1 not in range(1,7):
        
        try:
            ivc1 = int(input('For the Volume unit of the Concentration of the initial Solution 1, please choose the number for the respective unit: \n 1-L \n 2-dL \n 3-cL \n 4-mL \n 5-uL \n 6-nL \n 7-pL \n'))
        except:
            print('Please insert a valid number')
    
    
    v1 = ((c2*((mc2u[imc2])/(vc2u[ivc2])))*(v2*v2u[iv2]))/(c1*((mc1u[imc1])/(vc1u[ivc1])))
    print('To create', v2*v2u[iv2], 'L of the final Solution 2 with concentration of', (c2*((mc2u[imc2])/(vc2u[ivc2]))), 'g/L', 'you should use', v1, 'L of the initial Solution 1 with concentration of', (c1*((mc1u[imc1])/(vc1u[ivc1]))), 'g/L')

input('\nPress enter to exit')
