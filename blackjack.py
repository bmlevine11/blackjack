from models import CardDeck
from models import Player

class Turn():
    """
        Defines logic for a turn.
    """

    def __init__(self, player, deck):
        self.player = player
        self.deck = deck

    def isBusted(self):
        return self.player.isBusted

    def hit(self):
        card = self.deck.dealCard()
        print "{card} was dealt to {name}".format(
            card=card.cardType,
            name=self.player.name
        )
        self.player.getCard(card)
        self.player.calculateScore()

    def stand(self):
        print "{name} chose to stand with a score of {score}".format(
            name=self.player.name,
            score=self.player.score
        )

    def start(self):
        print "{name}, it's your turn. You currently have these cards: {cards}.".format(
            name=self.player.name,
            cards=', '.join([card.cardType for card in self.player.cards])
        )

        action = ""
        stillPlaying = True

        while stillPlaying:
            action = raw_input("Current score: {}. What would you like to do? (Hit or Stand?) ".format(
                self.player.score
            )
        )

            if action.upper() == 'HIT':
                self.hit()

                if self.player.isBusted:
                    print "{name} busted with a score of {score}".format(
                        name=self.player.name,
                        score=self.player.score
                    )
                    self.player.setScore(-1)
                    stillPlaying = False

            elif action.upper() == 'STAND':
                self.stand()
                stillPlaying = False

class Game():
    """
        We have two players. Need to prompt both for text input, but first they
        are dealt two cards each before any action takes place.
    """

    deck = CardDeck()

    firstPlayerName = raw_input("Player 1, please enter your name:")
    player1 = Player(name=firstPlayerName)
    secondPlayerName = raw_input("Player 2, please enter your name:")
    player2 = Player(name=secondPlayerName)

    # First, deal two cards to each player.
    for i in xrange(2):
        player1.getCard(deck.dealCard())
        player2.getCard(deck.dealCard())

    # Calculate initial scores
    player1.calculateScore()
    player2.calculateScore()

    # Next, ask player 1 for action
    # Nice to have: Double down and split
    Turn(player1, deck).start()

    # Ask player 2 for action.
    Turn(player2, deck).start()
    # After player 2 finishes, compare the scores of each player to determine a winner.

    if player1.score > player2.score:
        print "{} is the winner!".format(player1.name)

    elif player2.score > player1.score:
        print "{} is the winner!".format(player2.name)

    else:
        print "Neither player won!"

if __name__ == '__main__':
    Game()
