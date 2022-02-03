Question

Given a deck of cards, we have to deal a hand containing a certain number of cards. Cards can be dealt from the top of the deck as well as from the bottom. Determine the best hand that can be dealt, in terms of the sum of the values of the cards, assuming each card has a specific value.
​
example: for the deck [3,1,1,6,2,6,9,2,5], we can deal a set of hands [x,x,x,x,x] , [x,x,x,x,x], [x,x,x,x,]. The best hand is [x,x,x,x,x] with a sum of y

Some clarifications:
​
Q: Does the dealer know the values of the cards in the deck and their order? A: Yes, assume complete knowledge of the deck
Q: How large can a hand be? A: The size limit is 1,000,000 cards
Q: Can the hand be empty? A: Yes. In that case, its value is 0
Q: What if there are not enough cards in the deck to build a hand of the requested size? A: Then the whole deck should be dealt

Tommy works at a shady casino and is a card dealer. He always wants to know who has the best set of cards when he has everyone playing at his table of 5. Given a deck of cards, with all face cards worth 10 points and each numbered card worth the number printed on the card, he wants to determine the best hand that can be dealt, in terms of the sum of the value of the cards, if each player is dealt 5 cards.

Write a solution in any programming language that can determine the best hand and its sum that tommy can deal on his table given a random set of cards given as a random array for input.
