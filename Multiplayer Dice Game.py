from random import randrange
from time import sleep


def play(players):
    
    # Create a score list and set default scores to 0 for all players
    score_list = [0] * players
    round_ = 1
    list_length = range(len(score_list))

    while round_ < 4:
        
        # Exit loop if all the players withdraw from the game
        if score_list.count(None) == len(score_list):
            break
        
        print(f'Round {round_}!\n')
        
        for i in list_length:
            if score_list[i] != None:
                print(f'Player {i + 1} it is your turn to play')
                x = input('Do you want to roll the dice? [Y/N]: ').lower()
                
                while x not in ['y', 'n']:
                    print('Invalid selection!')
                    x = input('Do you want to roll the dice? [Y/N]: ').lower()
                    
                if x == 'y':
                    score = roll()
                    score_list[i] += sum(score)
                    print(f'Player {i + 1} rolled and got ===> {score}')
                    
                else:
                    print(f'Player {i + 1} withdrew from from the game')
                    score_list[i] = None
            
                
                
        sleep(1)
        round_ += 1
    
    # Initialize an empty dictionary which is going to hold the players' numbers and scores as
    # keys and values respectively
    dict_ = {}
    
    print('\n############### RESULT ###############')
    
    # Check if all the players withdrew
    if score_list.count(None) == len(score_list):
        print('No winner.')
        
    else:
        # Loop through the score_list and assign the indexes to their corresponding scores 
        # Players' numbers are represented by index + 1
        
        for v in list_length:
            if score_list[v] != None:
                print(f'Player {v + 1} Has a Total Score of ===> [{score_list[v]}]')
                dict_[v] = score_list[v]
                
        
        for i in range(len(dict_)):
            list_tuples = sorted(dict_.items(), key=lambda x: x[1])
        winner = list_tuples[-1][0]
        winner_score = list_tuples[-1][-1]
        
        print(f"\nPlayer {winner+1} wins with {winner_score} points!")

    play_again()
        
    
def play_again():
    select = input('\nPlay again? [Y/N]: ').lower()
    while select not in ['y', 'n']:
        select = input('\nInvalid selection!\nPlay again? [Y/N]: ').lower()
    if select == 'y':
        try:
            play(int(input('Enter Number of Players: ')))
        except ValueError:
            done = True
            while done:
                print('Invalid input.')
                try:
                    play(int(input('Enter Number of Players: ')))
                except ValueError:
                    continue
                done = False
                

def roll():
    out = []
    for i in range(2):
        dice_number = randrange(1, 6)
        out.append(dice_number)
    return out


if __name__ == '__main__':
   try:
       play(int(input('Enter Number of Players: ')))
   except ValueError:
        done = True
        while done:
            print('Invalid input.')
            try:
                play(int(input('Enter Number of Players: ')))
            except ValueError:
                continue
            done = False