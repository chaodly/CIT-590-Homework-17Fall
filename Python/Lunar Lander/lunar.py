# CIT 590 Homework 1 – Lunar Lander 08/31/2017

# By Zhengchao Ni, 73173892

# Reference: Eric Matthes, "Python Crash Course, A Hands-on Project-Based Introduction to Programming"

def Lunar_Lander():
    
    print ('***************************')
    print ('* Welcome to Lunar Lander *')
    print ('***************************\n')

    current_state = {'Altitude' : 1000, 'Velocity' : 0, 'Fuel' : 1000}
    print ('Current Altitude: ' , str(current_state['Altitude']) + ' m')
    print ('Current Velocity: ' , str(current_state['Velocity']) + ' m/s')
    print ('Current Fuel: ',str(current_state['Fuel'])+' L')

    coef = 0.15 # the propotion by which the velocity decrease
    
        
    print ('\nBegin Landing...\n')

    def input_sd(x):
        x = int(x)
        if x < 0:
            x = 0
        elif x > current_state['Fuel']:
            x = current_state['Fuel']
        return x
    '''
    If a player tries to burn a negative amount of fuel, treat it as if they burnt zero fuel.
    If a player specifies to burn more fuel than they have, burn all their fuel.
    '''
    t = 0  # calculate the total time.

    while (current_state['Altitude'] > 0):
        while True:
            try:
                x = float(input('Please indicate the amount of fuel you want to burn in the next second...'))
                break
            except ValueError:
                continue
        x = input_sd(x)
        current_state['Fuel'] = current_state['Fuel'] - x
        current_state['Velocity'] = current_state['Velocity'] + 1.6 - coef * x
        current_state['Altitude'] = current_state['Altitude'] - current_state['Velocity']
        
        if current_state['Velocity'] < 0:
            current_state['Velocity'] = 0
        if current_state['Altitude'] < 0:
            current_state['Altitude'] = 0    
        print('Current Altitude: ' , str(current_state['Altitude']) + ' m')
        print('Current Velocity: ' , str(current_state['Velocity']) + ' m/s')
        print('Current Fuel: ' , str(current_state['Fuel']) + ' L')
            
        if (current_state['Velocity'] > 10):
            print ('       ----------       ')
            print ('      |Warning!!!|      ')
            print ('       ----------       ') # High speed warning.
            
        t = t+1
        
    print ('\nGame Over!!\n')

    if (current_state['Velocity'] > 10):
        print ('Oh...Crashed...\n')
    else:
        print ('******************************')
        print ('* Well Done!!! Safe Landed!! *')
        print ('******************************')

    print ('\n')
    print ('-----Landing Condition-----')
    print ('Landing Velocity: ' + str(current_state['Velocity']) + 'm/s.')
    print ('Time taken: ' + str(t) + 's.')
    print (str(current_state['Fuel']) + ' litters of fuel remains.')
    print ('---------------------------\n')


###################################################################################    

flag = True

while flag:
    Lunar_Lander()
    user_input = input('Do you want to play again?')
    if user_input == 'N'or user_input == 'n':
        flag = False
        break
    if user_input == 'Y'or user_input == 'y':
        continue
    while user_input != 'N'or user_input != 'n'or user_input != 'Y'or user_input != 'y':
        user_input = input('Do you want to play again?')
        if user_input == 'N'or user_input == 'n':
            flag = False
            break
        if user_input == 'Y'or user_input == 'y':
            break
