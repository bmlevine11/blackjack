import random

cardNames = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class CardDeck():
    """
        Representation of the card deck.
    """
    deck = []

    # Blackjack can be played with more than one deck at a time
    def __init__(self, numberOfDecks=1):
        for cardType in cardNames:
            for numberOfCardType in xrange(4*numberOfDecks):
                self.deck.append(Card(cardType))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def dealCard(self):
        return self.deck.pop()

class Card():
    """
        Very simple definition of a card. The deck will be an array of cards
    """

    def __init__(self, cardType):
        self.cardType = cardType

class Player():
    """
        Represents a player, need to keep track of score and name for now, maybe
        total amount of cash later.
    """

    def __init__(self, name):
        self.name = name
        self.isBusted = False
        self.score = 0
        self.cards = []

    def calculateScore(self):

        # We're recalculating score, so reset it to zero before any action
        self.score = 0
        numberOfAces = 0
        for card in self.cards:
            if card.cardType in ['King', 'Queen', 'Jack']:
                self.score = self.score + 10
            elif card.cardType is not 'Ace':
                self.score = self.score + int(card.cardType)
            else:
                numberOfAces = numberOfAces + 1

        # Aces should be added last as their value depends on the total
        if self.score + numberOfAces*11 > 21:
            self.score = self.score + numberOfAces*1
        else:
            self.score = self.score + numberOfAces*11

        if self.score > 21:
            self.isBusted = True

        return self.score

    def getCard(self, card):
        self.cards.append(card)

    def setScore(self, newScore):
        self.score = newScore
