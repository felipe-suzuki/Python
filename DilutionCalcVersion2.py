# Function to enter the concentration of the solution
def in_conc(conc, final_init, sol_num):
    while type(conc) != float or conc <= 0:
        try:
            conc = float(input('Please, insert the Concentration of the {} Solution {}: '.format(final_init, sol_num )))
        except:
            print('Please, insert a valid number')
    return conc

# Function to enter the unit of mass of the solution concentration  
def in_mc_unit(unit, final_init, sol_num):
    while unit not in range(1,5):
        try:
            unit = int(input('For the Mass unit of the Concentration of the {} Solution {}, please \
choose the number for the respective unit: \n 1-g    2-mg    3-ug    4-ng \n Your entry: '.format(final_init, sol_num)))
        except:
            print('Please, insert a valid number')
    return unit

# Function to enter the unit of volume of the solution concentration 
def in_vc_unit(unit, final_init, sol_num):
    while unit not in range(1,5):
        try:
            unit = int(input('For the Volume unit of the Concentration of the {} Solution {}, please \
choose the number for the respective unit: \n 1-L    2-mL    3-uL    4-nL \n Your entry: '.format(final_init, sol_num)))
        except:
            print('Please, insert a valid number')
    return unit

# Function to enter the volume of the solution
def in_vol(vol, final_init, sol_num):
    while type(vol) != float or vol <= 0:
        try:
            vol = float(input('Please, insert the Volume of the {} Solution {}: '.format(final_init, sol_num)))
        except:
            print('Please, insert a valid number')
    return vol

# Function to enter the unit of volume of the solution
def in_v_unit(unit, final_init, sol_num):
    while unit not in range(1,5):
        try:
            unit = int(input('For the Volume unit of the {} Solution {}, please choose \
the number for the respective unit: \n 1-L    2-mL    3-uL    4-nL \n Your entry: '.format(final_init, sol_num)))
        except:
            print('Please, insert a valid number')
    return unit

# Function to calculate the final volume of the diluted solution
def calc_dilution(vol_dil, f_c1, f_mass_c_unit, f_vol_c_unit, f_v1, f_v_unit, f_c2):
    vol_dil = ((f_c1*((f_mass_c_unit[1][0])/(f_vol_c_unit[1][0])))*(f_v1*f_v_unit[1][0]))/(f_c2*((f_mass_c_unit[2][0])/(f_vol_c_unit[2][0])))
    return vol_dil

# Fuction to show the complete answer to the problem if calculate c1
def answer_dil(f_c1, f_v1, f_c2, f_v2, f_mass_c_unit, f_vol_c_unit, f_v_unit):
    print('To create a Final Solution with concentration of ', (f_c2*((f_mass_c_unit[2][0])/(f_vol_c_unit[2][0]))), 'g/L \
you should dilute the ', v1*v_unit[1][0], 'L of the Initial Solution with concentration of \
', (f_c1*((f_mass_c_unit[1][0])/(f_vol_c_unit[1][0]))), ' g/L to the final total volume of ', f_v2, 'L.')
    
# Function to get the answer to run the program again (still implementing)
def run_again():
    
    return input('Do you want to calculate again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Solution Dilution Calculator!')

while True:
    # Declare and reset variables
    c1, v1, c2, v2, mass_c_unit, vol_c_unit, v_unit, unit_index = (0,0,0,0,({1:0, 2:0}),({1:0, 2:0}),({1:0, 2:0}),0)
    mass_units = {1:(10**0, 'g'), 2:(10**-3, 'mg'), 3:(10**-6, 'ug'), 4:(10**-9, 'ng')}
    vol_units = uv = {1:(10**0, 'L'), 2:(10**-3, 'mL'), 3:(10**-6, 'uL'), 4:(10**-9, 'nL')}
    
    # Insert the initial solution concentration (numbers only)
    c1 = in_conc(c1, 'Initial', '1')
    
    # Insert the mass unit of the concentration: g, mg, ug, ng (initial solution)
    mass_c_unit[1] = mass_units[in_mc_unit(unit_index, 'Initial', '1')]
    
    # Insert the volume unit of the concentration: L, mL, uL, nL (initial solution)
    vol_c_unit[1] = vol_units[in_vc_unit(unit_index, 'Initial', '1')]
    
    # Insert the initial volume of the solution (numbers only)
    v1 = in_vol(v1, 'Initial', '1')
    
    # Insert the volume unit: L, mL, uL, nL (initial solution)
    v_unit[1] = vol_units[in_v_unit(unit_index, 'Initial', '1')]
    
    # Insert the final diluted solution concentration (numbers only)
    c2 = in_conc(c2, 'Final', '2')
    
    # Insert the mass unit of the concentration: g, mg, ug, ng (final diluted solution) 
    mass_c_unit[2] = mass_units[in_mc_unit(unit_index, 'Final', '2')]
    
    # Insert the volume unit of the concentration: L, mL, uL, nL (final diluted solution)
    vol_c_unit[2] = vol_units[in_vc_unit(unit_index, 'Final', '2')]
    
    # Calculate the final volume of the diluted solution
    v2 = calc_dilution(v2, c1, mass_c_unit, vol_c_unit, v1, v_unit, c2)
    
    # Show the answer to the user!
    answer_dil(c1, v1, c2, v2, mass_c_unit, vol_c_unit, v_unit)
    
    # If run_again = False, stop. If True, start the program again.
    if not run_again():
        break