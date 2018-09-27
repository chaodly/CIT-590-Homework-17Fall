def ask_yes_or_no(prompt):
    flag=True
    while flag:
        
        user_input = str(input(prompt))
        if user_input[0] == 'N'or user_input[0] == 'n':
            flag = False
            f = False
            break
        if user_input[0] == 'Y'or user_input[0] == 'y':
            f = True
            break
            
        print (user_input[0])
        print (user_input != 'y')
        
        while user_input[0] != 'N'or user_input[0] != 'n'or user_input[0] != 'Y'or user_input[0] != 'y':
            while True:
                try:
                    user_input = str(input('\nRoll again??????????? (y/n)\n'))
                    if user_input[0] == 'N'or user_input[0] == 'n':
                        flag = False
                        f = False
                        break
                    if user_input[0] == 'Y'or user_input[0] == 'y':
                        flag=False
                        f = True
                        break
                except IndexError:
                    continue
    return f
ask_yes_or_no('fuckyou')
