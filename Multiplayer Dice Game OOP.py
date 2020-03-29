from random import randrange as r
from time import sleep


class Cradice():
    '''
    A multiplayer dice game with tie breaker (haha!)
    '''

    def start(self):
        '''
        Method handles likely exceptions that can be raised while accepting the number of players.
        '''
        try:
            num = int(input('Enter number of players (minimum of 2): '))
            while num < 2:
                print('Minimum of two players allowed')
                num = int(input('Enter number of players (minimum of 2): '))
            Cradice.play(self, num, 3)
        except ValueError:
            print('Invalid input')
            Cradice.start(self)
            
        
        
    def play(self, players, rounds):
        '''
        The main method, if you'll have it.
        Method takes two arguments:
            players - number of players
            rounds - number of rounds
            
        Method runs for 'rounds' number of iterations
        '''
        
        # Create a score list and set default scores to 0 for all players
        # Create a name list and set default name to '' for all players
        
        self.score_list = [0] * players
        self.name_list = [''] * players 
        self.round = 1
        rounds += 1
        
        # Assign names to players
        for i in range(players):
            self.name_list[i] = input('Enter name for Player {}: '.format(i+1)).title()
        
        while self.round < rounds:
            # Exit loop if all the players withdraw from the game
            if all(self.score_list[scores] == None for scores in range(players)):
                break
            
            print('\nRound {}'.format(self.round))
            for i in range(players):
                
                # Proceed if the player is stil in the game. None means the player has left the game 
                # so they won't be considered in subsequent rounds and when determining the winner
                
                if self.score_list[i] != None:
                    print('{} it is your turn to play'.format(self.name_list[i]))
                    x = input('Do you want to roll the dice? [Y/N]: \n').lower()
                    
                    while x not in ['y', 'n']:
                        print('Invalid selection!')
                        x = input('Do you want to roll the dice? [Y/N]: ').lower()
                        
                    if x == 'y':
                        #Dice rolling logic
                        score = [r(1,6), r(1,6)]
                        self.score_list[i] += sum(score)
                        print('{} rolled and got ===> {}\n'.format(self.name_list[i], score))
                        
                    else:
                        print('{} left the game'.format(self.name_list[i]))
                        self.score_list[i] = None
            
                
                
            sleep(1)
            self.round += 1
            
        print('\n############### RESULT ###############\n')

        # Check if all the players left the game
        if all(self.score_list[scores] == None for scores in range(players)):
            print('No winner.')
            
        else:
            winner, high_score =  0, 0
            for v in range(players):
                if self.score_list[v] != None:
                    print('{} has a total score of ===> {}\n'.format(self.name_list[v], self.score_list[v]))
                if self.score_list[v] != None:
                    if self.score_list[v] > high_score:
                        winner, high_score = v, self.score_list[v]
                        
            if self.score_list.count(high_score) >1:
                print('Tie Breaker!')
                Cradice.play(self, self.score_list.count(high_score), 2)
            else:
                print('\n{} wins with {} points.'.format(self.name_list[winner], high_score))
            
            Cradice.play_again(self)
            
    
    def play_again(self):
        select = input('\nPlay again? [Y/N]: ').lower()
        while select not in ['y', 'n']:
            select = input('\nInvalid selection!\nPlay again? [Y/N]: ').lower()
        if select == 'y':
            Cradice.start(self)
        else:
            print('Thanks for playing.')
    
if __name__ == '__main__':
    cradice = Cradice()
    cradice.start()