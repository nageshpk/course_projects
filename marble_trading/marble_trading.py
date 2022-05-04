'''
Objective -> Create a marble betting game

1. draw a marble from a bag (assume it's random)
2. a bag has 10 marbles: 6 green and 4 red
3. if you draw a green marble you win same amount that you bet, if you draw a red marble you lose amount you bet.
4. marbles are replaced into bag after each round
5. before each draw, decide how much you will bet and enter it
6. you start the game with 1000 gold pieces
7. the number of rounds/draws should be variable
8. if you lose half of your money game is over
9. print/show out data as you go along
Bonus: replace two marbles 1 green with a black 10X winner marble, 1 red with a 5X white loser marble
'''

#import modules
import random

#create a bag with 10 marbles
bag = ['green', 'green', 'green', 'green', 'green', 'black', 'red', 'red', 'red', 'white']

#starting amount of money
start_purse = 1000

#current money amount
purse = start_purse

#result of last round
result = 0

#how many rounds
rounds = int(input("How many rounds you want to play? "))

#last marble
marble = 'none'

#welcome user to the game
print(f"Welcome to the game, you are starting with {start_purse} gold pieces")

#loop drawing marbles
for i in range(1, rounds+1):
    bet = int(input(f"Current purse: {purse}, Last draw: {marble} \nRound {i} - How much do you want to bet? "))

    #draw marble
    marble = random.choice(bag)

    #win or loss
    if marble == 'green':
        result = bet
    elif marble =='black':
        result = 10*bet
    elif marble == 'white':
        result = -5 * bet
    else:
        result = -bet
    purse += result

    #lose game if lose half of money
    if purse < 0.5*start_purse:
        print(f'Game over! You have lost too much gold')
        break

    #print result
    print(f'purse {purse}, last_result: {marble}: {result}')

#print final result
print(f'starting / ending purse: {start_purse} / {purse}')
print(f'gain / loss: {(purse-start_purse) / start_purse*100}%' )