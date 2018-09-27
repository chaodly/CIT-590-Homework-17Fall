# CIT-590 Homework 2

# Zhengchao Ni 73173892

import random

# In order to add some time delay so that when computer plays, the program looks more agreeable
import time 

# Return the instructions of the game
def instructions():
    print ('\n--------------------------Instructions--------------------------\n')
    print ("Two players take turns. On each turn, \n\
a player rolls a six-sided dieas many times as she wishes, \n\
or until she rolls a 6.\n\
Each number she rolls, except a 6, is added to her score this turn; \n\
but if she rolls a 6, her score for this turn is zero, and her turn ends. \n\
At the end of each turn, \n\
the score for that turn is added to the player's total score.\n\
The first player to reach or exceed 50 wins.\n\
To make the game more fair, \n\
we will say that if the first player reaches or exceeds 50, \n\
the second player gets one additional turn. \n\
(If the second player is the first to reach 50, \n\
the first player does not get an additional turn.)")
    print ('\n----------------------------------------------------------------\n')


# A roll of the dice, using random function.
def roll():
    return random.randint(1,6)


# Determine whether the game is over, if yes return true.
def is_game_over(computer_score, human_score):
    
    if (computer_score >= 50 and computer_score != human_score) or \
       (human_score >= 50 and computer_score != human_score):
        return True
    else:
        return False

# Repeatedly ask the user whether to roll again.
def ask_yes_or_no(prompt):
    
    # flag controls the while loop(repeatedly ask), f is the binary variable returned by this function.
    flag=True
    
    while flag:
        
        # Adding a space is to avoid the IndexError (String Index out of range),
        # meanwhile it will not affect the input.
        # When accidentally pressing an Enter while a user is inputting, the program is likely to crash.
        # By adding the space, it will not report an error (String Index will not out of range).
        user_input = str(input(prompt)) + ' '        
        if user_input[0] == 'N'or user_input[0] == 'n':
            flag = False
            f = False
            break
        if user_input[0] == 'Y'or user_input[0] == 'y':
            f = True
            break
        
        while user_input[0] != 'N'or user_input[0] != 'n'or user_input[0] != 'Y'or user_input[0] != 'y':
            user_input = str(input(prompt))+ ' '
            if user_input[0] == 'N'or user_input[0] == 'n':
                flag = False
                f = False
                break
            if user_input[0] == 'Y'or user_input[0] == 'y':
                flag=False
                f = True
                break
    return f


def human_move(computer_score, human_score):
    print ('\n~~~~~~~~~~~~~~~~~~~~~~Your Movement Begin~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    
    print ('--------------------------------------------')
    print (' Your current score is ' + str(human_score) + '.')
    print (" The computer's current score is " +str(computer_score) + '.')
    print ('--------------------------------------------')
    
    d = computer_score - human_score
    
    if d > 1:
        print ('You are ' + str(d) + ' points behind.')
    elif d == 1:
        print ('You are 1 point behind.')
    elif d == -1:
        print ('You are 1 point ahead.')
    elif d == 0:
        print ('Tie!')
    else:
        print ('You are ' + str(-d) + ' points ahead.')

    t = 0 # Your score of this turn.

    Flag = ask_yes_or_no('\nRoll again?(y/n)\n')

    # Human move
    while Flag == True:
        r = roll()
        print ('Your Move!!...\n   --This turn! r = ' + str(r))

        # t is the total score of this turn.
        t += r
        
        if r == 6:
            Flag = False
            t = 0
            print ('\n')
            print ('$$$$$$$$$$$$$$$$$$$$$$')
            print ('$                    $')
            print ('$ Oh.....6 appears...$')
            print ('$                    $')
            print ('$$$$$$$$$$$$$$$$$$$$$$')
            print ('\n')
            break
        Flag = ask_yes_or_no('\nRoll again?(y/n)\n')
    
    human_score = human_score + t
    print ('\n~~~~~~~~~~~~~~~~~~~~~~Your Movement Ended~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    return computer_score, human_score

def computer_move(computer_score, human_score):
    print ('\n======================Computer Movement Begin======================\n')

    # r, t means the same as above
    r = 0
    i = 0
    t = 0
    exp = 0 # a random number
    
    # Different movement of computer when facing different score gap.
    if (computer_score - human_score) > 20:
        b = 0
    elif (computer_score - human_score) > 10 and (computer_score - human_score) < 20:
        b = 0
    elif computer_score > human_score  and (computer_score - human_score) <10:
        b = 1
    elif computer_score < human_score and (human_score - computer_score) <10:
        # sometimes it roll twice, sometimes it roll three times
        exp = random.randint(1,6)
        b = 2 * (1 + pow(-1, exp))/2 + 3 * (1 - pow(-1, exp))/2
        
    else:
        # sometimes it roll three times, sometimes it roll four times
        # roll too many times may cause the appearance of 6.
        exp = random.randint(1,6)
        b = 3 * (1 + pow(-1, exp))/2 + 4 * (1 - pow(-1, exp))/2
        
    # Roll more times so that it acts more aggressively.    
        
    # Computer move
    
    while i < b:
        r = roll()
        t += r
        i += 1
        if r == 6:
            print ('\n')
            print ('$$$$$$$$$$$$$$$$$$$$$$')
            print ('$                    $')
            print ('$ Oh.....6 appears...$')
            print ('$                    $')
            print ('$$$$$$$$$$$$$$$$$$$$$$')
            print ('\n')
            t = 0
            break
        print ('Computer Move!!...\n   --This turn: r = ' + str(r))
          
    computer_score = computer_score + t
    print ('\n======================Computer Movement Ended======================\n')
    return computer_score, human_score
        
def show_results(computer_score, human_score):
    if computer_score < human_score:
        print ('*********************')
        print ('* Congratulations!! *')
        print ('*********************')
        print ('\nYou win by ' + str (human_score - computer_score) + ' points.')
    else:
        print ('@@@@@@@@@@@@@@@@@@@@')
        print ('@ Unfortunately....@')
        print ('@@@@@@@@@@@@@@@@@@@@')
        print ('\nYou lose by ' + str (computer_score - human_score) + ' points.')

def main():
    print ('************************')
    print ('* Welcome to Pig Game  *')
    print ('************************')

    # wait for 1 second
    # otherwise the results will appear suddenly
    time.sleep(1)
    instructions()
    
    computer_score = 0
    human_score = 0
    
    while is_game_over(computer_score, human_score) == False:
        print ('The computer is playing... ...')
        time.sleep(1)
        print ('...')
        time.sleep(1)
        print ('...')
        
        [computer_score, human_score] = computer_move(computer_score, human_score)
        [computer_score, human_score] = human_move(computer_score, human_score)

        print ('\n        %%%%%%%%%%%%%%%%%% Current Score %%%%%%%%%%%%%%%%%%')
        print ('        ' + 'Computer Score: ', computer_score, 'Your score: ', human_score)
        print ('        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
        
    show_results(computer_score, human_score)

    print ('\n')
    print ('************************')
    print ('*       Game Over      *')
    print ('************************')

if (__name__) == '__main__':
    main()

    

