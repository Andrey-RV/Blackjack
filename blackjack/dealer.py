from typing import MutableSequence
from random import SystemRandom as sr
from .player import Player


class Dealer(Player):
    random = sr()

    def __init__(self, deck: MutableSequence[int]) -> None:
        """A class that represents the dealer in the game of Blackjack.

        Args:
            deck (MutableSequence[int]): A sequence containing the cards that will be used in the game.
        """
        super().__init__(deck)

    def _initial_hand(self) -> None:
        """Give the dealer one initial card and remove it from the deck."""
        self.hand.append(Dealer.random.choice(self.deck))
        self.deck.remove(self.hand[-1])
        self.score = (self.hand[0])

    def show_dealer_hand_and_score(self) -> None:
        """Print the dealer's hand and score."""
        print(f"The dealer hand is: {self.hand}. His score is: {self.score}\n")

    def dealer_hit(self):
        """Add a card to the dealer's hand and removes it from the deck until his score is lower than 17. Calls the method update_score() at every iteration. When his score is greater or equal to 17, calls show_hand_and_score.
        """
        while self.score < 17:
            self.hand.append(Dealer.random.choice(self.deck))
            self.deck.remove(self.hand[-1])
            self._update_score()
        self.show_dealer_hand_and_score()

    def _update_score(self):
        """Update the dealer's score based on the last card added to his hand. If the dealer has dug an ace, it checks if the dealer's score plus 11 is greater or equal to 17 but lower or equal to 21. If it is, it adds 11 points to the dealer's score. If it isn't, it changes the ace's value to 1 and adds 1 point to the dealer's score.
        """
        if (self.hand[-1] == 11) and (self.score + 11 >= 17) and (self.score + 11 <= 21):
            self.score += 11
        elif self.hand[-1] == 11:
            self.hand[-1] = 1
            self.score += 1
        else:
            self.score += self.hand[-1]

    def restart_the_game(self, cards: MutableSequence[int]):
        """Reset the dealer's hand and score and calls the method initial_hand() to give the dealer the initial card.

        Args:
            cards (MutableSequence[int]): A sequence containing the cards that will be used in the game.
        """
        self.hand.clear()
        self.score = 0
        self.deck = cards
        self._initial_hand()
