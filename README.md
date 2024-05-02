# BlackerThanJack
Blacker Than Jack is a fictional casino game where a card is drawn and all players (plus the dealer) roll two dice in an attempt to get the closest roll to the card drawn. 
The dealer always rolls first. If any player rolls snake eyes (2) they instantly win the game. If a player ties with the dealer, the dealer wins.

The file BlackerThanJackSIMULATION.py is a Monte Carlo simulation which aims to aproximate the profit ratio from the perspective of the dealer.
DEPENDANCIES TO RUN: Numpy, Matplotlib, and TQDM,
Coded in python 3.12.3

____________________________________________________________________________________________________________________________________________________________________________

The equations below dictate the precise probability of the dealer winning.

P(win via roll x (exculuding roll of 2)) = P(roll x) * P(roll x > roll y > 2)

P(win via 2) = 1/36

P(roll x > roll y > 2) = Pc(roll x) - P(roll y > roll x) - P(2)

P(win) = Sum( P(Win via roll x) + P(Win via roll x+1) + P(Win via roll x+2)...)

P(Tie via roll x) = P(roll x)^2

P(Tie) = Sum( P(tie via roll x) + P(tie via roll x+1) + P(tie via roll x+2)...)

P(Loss) = Pc( P(Win) + P(Tie) )
