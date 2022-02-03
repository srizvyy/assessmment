import random

# face cards => 10 points 
# numbered cards => worth number printed on the card
# he wants to determine the best hand that can be dealt, in terms of the sum of the value of the cards, if each player is dealt 5 cards.

# numbersOfCardsInDeck = 52 
# faceCards = 12
# numberCards = 36

# four cards each for numbered cards, last 12 face cards => 10points 
cardsarr = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

def best_hand_in_deck(deckofcards):
    player1 = sum(random.choices(deckofcards, k=5))
    player2 = sum(random.choices(deckofcards, k=5))
    player3 = sum(random.choices(deckofcards, k=5))
    player4 = sum(random.choices(deckofcards, k=5))
    player5 = sum(random.choices(deckofcards, k=5))
    if player1 > player2 and player1 > player3 and player1 > player4 and player1 > player5: 
        return 'player 1:' + str(player1)
    elif player2 > player1 and player2 > player3 and player2 > player4 and player2 > player5:
        return 'player 2:' + str(player2)
    elif player3 > player1 and player3 > player2 and player3 > player4 and player3 > player5:
        return 'player 3:' + str(player3)
    elif player4 > player1 and player4 > player2 and player4 > player3 and player4 > player5:
        return 'player 4:' + str(player4)
    else:
        return 'player 5:' + str(player5)


print(best_hand_in_deck(cardsarr))