from typing import MutableSequence
from random import SystemRandom as sr


class Player():
    random = sr()

    def __init__(self, deck: MutableSequence[int]) -> None:
        """_Initializes the class that will represent a player in the game of Blackjack. It calls the method initial_hand() to give the player two initial cards._

        Args:
            deck (Sequence[int]): _A sequence containing the cards that will be used in the game._

        Attributes:
            deck (Sequence[int]): _A sequence containing the cards that will be used in the game._
            hand (list[int]): _A list containing the cards that the player has in his hand._
            score (int): _The score of the player._
        """
        self.deck: MutableSequence[int] = deck
        self.hand: MutableSequence[int] = []
        self.score: int = 0
        self.initial_hand()

    def initial_hand(self) -> None:
        """_Gives the player two initial cards and removes them from the deck._"""
        self.hand.append(Player.random.choice(self.deck))
        self.deck.remove(self.hand[-1])
        self.hand.append(Player.random.choice(self.deck))
        self.deck.remove(self.hand[-1])
        self.score = (self.hand[0] + self.hand[1])

    def show_hand_and_score(self, player_number: int) -> None:
        """_Prints the player's hand and score._

        Args:
            player_number (int): _The number of the player._
        """
        print(f"\nThe player {player_number}'s hand is: {self.hand}. Their current score is: {self.score}")

    def hit(self, player_number: int) -> None:
        """_Adds a card to the player's hand and removes it from the deck, then calls the methods update_score() and show_hand_and_score to update the player's score after adding the card to their hand and print the player's hand and score._

        Args:
            player_number (int): _The number of the player._
        """
        self.hand.append(Player.random.choice(self.deck))
        self.deck.remove(self.hand[-1])
        self.update_score()
        self.show_hand_and_score(player_number)

    def update_score(self) -> None:
        """_Updates the player's score based on the last card added to their hand. If the player has dug an ace, it checks through an input if the player wants it to be worth 1 or 11 points._
        """
        if self.hand[-1] == 11:
            ace_value_choice = None
            while ace_value_choice not in ['1', '11']:
                ace_value_choice = input(
                    "You drew an ace. Do you want it to be worth 1 or 11 points? ")
            self.hand[-1] = 1 if ace_value_choice == '1' else 11
        self.score += self.hand[-1]

    def busted(self) -> bool:
        """_Returns True if the player's score is greater than 21, otherwise returns False._"""
        return self.score > 21

    def restart_the_game(self, cards: MutableSequence[int]) -> None:
        """_Resets the player's hand and score and calls the method initial_hand() to give the player two initial cards._

        Args:
            cards (MutableSequence[int]): _A sequence containing the cards that will be used in the game._
        """
        self.hand.clear()
        self.score = 0
        self.deck = cards
        self.initial_hand()
