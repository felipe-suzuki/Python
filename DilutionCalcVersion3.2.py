#---------------- CLASSES AND FUNCTIONS: ----------------#

class Concentration:
    
    def __init__(self, value, m, V):
        self.value = value         
        self.m = m
        self.V = V

class Volume:
    
    def __init__(self, value, V):
        self.value = value
        self.V = V
        
def getValue(w, sol, unit):
    w = 0
    while w <= 0:
        try:
            w = float(input('Please, insert the {} {}: '.format(sol, unit)))
        except:
            print('Please insert a numeric entry!')
    return w

def get_massUnit(x, sol):
    x = 0
    while x not in range (1,5):
        try:
            x = int(input('Please choose an option for the mass unit of the {} \
concentration: \n1-g    2-mg    3-\u03BCg    4-ng\nYour entry: '.format(sol)))
        except:
            print('Please insert a correct entry!')
    return x

def get_Vunit(y, sol, unit):
    y = 0
    while y not in range (1,5):
        try:
            y = int(input('Please choose an option for the Volume unit of the {} \
{}: \n1-L    2-mL    3-\u03BCL    4-nL\nYour entry: '.format(sol, unit)))
        except:
            print('Please insert a correct entry!')
    return y

def calc_dilution():
    v2 = ((c1.value*((c1.m[0])/(c1.V[0])))*(v1.value*v1.V[0]))/(c2.value*((c2.m[0])/(c2.V[0])))
    return v2

def answer():
    print("\nTo dilute {} {} of the initial solution with concentration of {} {}/{} to the final concentration of {} {}/{} \
you must add water to a final volume of {} L".format(v1.value, v1.V[1], c1.value, c1.m[1], c1.V[1], c2.value, c2.m[1], c2.V[1], v2))
    
def run_again():
    
    return input('\nDo you want to calculate again? Enter Yes or No: ').lower().startswith('y')

#---------------- SCRIPT ----------------#

while True:

    print('Welcome to Solution Dilution Calculator!')
    
    # Declare and reset variables
    m_unit = {1:(10**0, 'g'), 2:(10**-3, 'mg'), 3:(10**-6, '\u03BCg'), 4:(10**-9, 'ng')}
    V_unit = {1:(10**0, 'L'), 2:(10**-3, 'mL'), 3:(10**-6, '\u03BCL'), 4:(10**-9, 'nL')}
    c1, v1, c2, v2, c1check, c2check = (0, 0, 0, 0, 0, 0)
       
    # Insert the initial solution concentration
    c1 = Concentration(getValue(c1, 'initial', 'concentration'), m_unit[get_massUnit(c1, 'initial')], \
                       V_unit[get_Vunit(c1, 'initial', 'concentration')])
    c1check = (c1.value*((c1.m[0])/(c1.V[0])))
    c2check = c1check + 1
    
    # Insert the initial volume of the solution 
    v1 = Volume(getValue(v1, 'initial', 'Volume'), V_unit[get_Vunit(v1, 'initial', 'solution')])
    
    # Insert the final diluted solution concentration
    while c2check >= c1check:
        print('\nIMPORTANT! THE FINAL CONCENTRATION MUST BE LOWER THAN INITIAL!')
        c2 = Concentration(getValue(c2, 'final', 'diluted concentration'), m_unit[get_massUnit(c2, 'final')], \
                           V_unit[get_Vunit(c2, 'final', 'diluted concentration')])
        c2check = (c2.value*((c2.m[0])/(c2.V[0])))
        
    # Calculate the final volume of the diluted solution
    v2 = calc_dilution()
    
    # Show the answer to the user!
    answer()
    
    # If run_again = False, stop. If True, restart the script
    if not run_again():
        break