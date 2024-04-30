# simulation of blacker than jack.
# sim assumes a king was drawn, 
# and there is only one player vs the dealer

#import np and plt
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

# Define key variables
players = int(input('Number of players to simulate? (plus the dealer): '))
print('Simulating ' + str(players) + ' players (plus the dealer)...')

N = int(input('\nNumber of games to simulate?: '))
print('Simulating ' + str(N) + ' games...\n')

# Generate card drawn
def card_draw():
    '''simulate drawning a card and return int 1-14 (ace to king)'''
    card_i = np.random.randint(1,14)
    return card_i

# generate 1 dice roll

def roll_die():
    '''Simulate rolling a die and return an integer'''
    roll_i = np.random.randint(1,7)
    return roll_i

# define dealer and player rolling functions

def dealer_roll():
    roll_1 = roll_die()
    roll_2 = roll_die()
    dealer_i = roll_1 + roll_2
    return dealer_i

def players_roll():
    '''Player roll function: may have multiple players'''
    roll_1 = roll_die()
    roll_2 = roll_die()
    player_i = roll_1 + roll_2
    return player_i

# Simulate the game

win_count = 0
loss_count = 0
dealer_ingame = 1

for i in tqdm(range(N)):
    # draw a card
    card_i = card_draw()
    # dealer rolls
    dealer_i = dealer_roll()
    dealer_score = abs(dealer_i - card_i)
    # player(s) rolls
    best_score = 999
    for n in list(range(players)):
        player_i = players_roll()
        player_score = abs(player_i - card_i)
        if player_score < best_score:
            best_score = player_score
        if player_i == 2:
            # if a player rolls 2 their score will be -1, gaurenteed to be the lowest score
            best_score = -1
    # win scenarios
    if dealer_i == 2:
        win_count = win_count + 1
    elif dealer_score < best_score:
        win_count = win_count + 1
    # tie scenarios
    elif dealer_score == best_score:
        win_count = win_count + 1
    # lose scenarios
    elif best_score < dealer_score:
        loss_count = loss_count + 1


# End stats:

total_debug = win_count + loss_count
print('\ntotal games: ' + str(total_debug))
print('\nWins: ' + str(win_count))
print('Losses: ' + str(loss_count))

win_loss_ratio = win_count/loss_count
print('\nWin/Loss ratio: ' + str(win_loss_ratio))
win_percentage = win_count/(win_count + loss_count)
print('Win %: ' + str(win_percentage))
profit_loss_ratio = win_loss_ratio * players
print('Profit/Loss ratio: ' + str(profit_loss_ratio))
