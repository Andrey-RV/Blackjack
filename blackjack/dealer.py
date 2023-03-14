from typing import MutableSequence
from random import SystemRandom as sr
from .player import Player


class Dealer(Player):
    random = sr()

    def __init__(self, deck: MutableSequence[int]) -> None:
        """_Initializes the class that will represent the dealer in the game of Blackjack.
        It calls the method initial_hand() to give the dealer the initial card._

        Args:
            deck (MutableSequence[int]): _A sequence containing the cards that will be used in the game._

        Attributes:
            deck (MutableSequence[int]): _A sequence containing the cards that will be used in the game._
            hand (list[int]): _A list containing the cards that the dealer has in his hand._
            score (int): _The score of the dealer._
        """
        super().__init__(deck)

    def initial_hand(self) -> None:
        """_Gives the dealer one initial card and remove it from the deck._"""
        self.hand.append(Dealer.random.choice(self.deck))
        self.deck.remove(self.hand[-1])
        self.score = (self.hand[0])

    def show_dealer_hand_and_score(self) -> None:
        """_Prints the dealer's hand and score._"""
        print(f"The dealer hand is: {self.hand}. His score is: {self.score}\n")

    def dealer_hit(self):
        """_Adds a card to the dealer's hand and removes it from the deck until his score is lower than 17.
        Calls the method update_score() at every iteration.
        When his score is greater or equal to 17, calls show_hand_and_score._
        """
        while self.score < 17:
            self.hand.append(Dealer.random.choice(self.deck))
            self.deck.remove(self.hand[-1])
            self.update_score()
        self.show_dealer_hand_and_score()

    def update_score(self):
        """_Updates the dealer's score based on the last card added to his hand. If the dealer has dug an ace, it checks if the dealer's score plus 11 is greater or equal to 17 but lower or equal to 21. If it is, it adds 11 points to the dealer's score. If it isn't, it changes the ace's value to 1 and adds 1 point to the dealer's score._
        """
        if (self.hand[-1] == 11) and (self.score + 11 >= 17) and (self.score + 11 <= 21):
            self.score += 11
        elif self.hand[-1] == 11:
            self.hand[-1] = 1
            self.score += 1
        else:
            self.score += self.hand[-1]

    def restart_the_game(self, cards: MutableSequence[int]):
        """_Resets the dealer's hand and score and calls the method initial_hand() to give the dealer the initial card._

        Args:
            cards (MutableSequence[int]): _A sequence containing the cards that will be used in the game._
        """
        self.hand.clear()
        self.score = 0
        self.deck = cards
        self.initial_hand()
