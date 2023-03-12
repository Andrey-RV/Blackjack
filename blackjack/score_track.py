from typing import Sequence


def count_points(dealer_score: int, scores: Sequence[int]) -> None:
    """_Counts the points of the players and the dealer and prints the results of the game._

    Args:
        dealer_score (int): _The dealer's score._
        scores (Sequence[int]): _A sequence with the scores of the players._
    """
    players = len(scores)
    winners: list[int] = []
    losers: list[int] = []
    draws: list[int] = []

    for current_player in range(players):
        player_did_not_bust = scores[current_player] <= 21
        dealer_busted = dealer_score > 21
        player_score_is_higher_than_dealer = scores[current_player] > dealer_score
        player_score_is_equal_to_dealer = scores[current_player] == dealer_score
        player_score_is_lower_than_dealer = scores[current_player] < dealer_score

        if (
            player_score_is_higher_than_dealer and player_did_not_bust or
            player_score_is_lower_than_dealer and player_did_not_bust and dealer_busted
        ):
            winners.append(current_player)

        elif player_score_is_equal_to_dealer and player_did_not_bust:
            draws.append(current_player)

        else:
            losers.append(current_player)

    for winner in winners:
        print(f"Player {winner+1} won")
    for draw in draws:
        print(f"It's a push for player {draw+1} and the dealer")
    for loser in losers:
        print(f"Player {loser+1} lost")
