from typing import MutableSequence
from random import SystemRandom as sr


class Player():
    random = sr()

    def __init__(self, deck: MutableSequence[int]) -> None:
        """A class that represents a player in the game of Blackjack.

        Args:
            deck (Sequence[int]): A sequence containing the cards that will be used in the game.
        """
        self.deck = deck
        self.hand: MutableSequence[int] = []
        self.score = 0
        self._initial_hand()

    def _initial_hand(self) -> None:
        """Give the player two initial cards and removes them from the deck."""
        self.hand.append(Player.random.choice(self.deck))
        self.deck.remove(self.hand[-1])
        self.hand.append(Player.random.choice(self.deck))
        self.deck.remove(self.hand[-1])
        self.score = (self.hand[0] + self.hand[1])

    def show_hand_and_score(self, player_number: int) -> None:
        """Print the player's hand and score.

        Args:
            player_number (int): The number of the player.
        """
        print(f"\nThe player {player_number}'s hand is: {self.hand}. Their current score is: {self.score}")

    def hit(self, player_number: int) -> None:
        """Add a card to the player's hand and removes it from the deck, then calls the methods update_score() and show_hand_and_score to update the player's score after adding the card to their hand and print the player's hand and score.

        Args:
            player_number (int): The number of the player.
        """
        self.hand.append(Player.random.choice(self.deck))
        self.deck.remove(self.hand[-1])
        self._update_score()
        self.show_hand_and_score(player_number)

    def _update_score(self) -> None:
        """Update the player's score based on the last card added to their hand. If the player has dug an ace, it checks through an input if the player wants it to be worth 1 or 11 points.
        """
        if self.hand[-1] == 11:
            ace_value_choice = None
            while ace_value_choice not in ['1', '11']:
                ace_value_choice = input(
                    "You drew an ace. Do you want it to be worth 1 or 11 points? ")
            self.hand[-1] = 1 if ace_value_choice == '1' else 11
        self.score += self.hand[-1]

    def busted(self) -> bool:
        """Return True if the player's score is greater than 21, otherwise returns False."""
        return self.score > 21

    def restart_the_game(self, cards: MutableSequence[int]) -> None:
        """Reset the player's hand and score and calls the method initial_hand() to give the player two initial cards.

        Args:
            cards (MutableSequence[int]): A sequence containing the cards that will be used in the game.
        """
        self.hand.clear()
        self.score = 0
        self.deck = cards
        self._initial_hand()
