from os import system
from blackjack import Player, Dealer, get_number_of_players, count_points

commom_deck = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7,
               7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


def main():
    players_range = get_number_of_players()
    deck = [card for card in commom_deck.copy() for __ in players_range]
    players = [Player(deck) for __ in players_range]
    dealer = Dealer(deck=deck)
    system('cls')

    while True:
        for player in players_range:
            system('cls')
            print(f"\nPlayer {player+1} turn")
            players[player].show_hand_and_score(player_number=player+1)
            dealer.show_dealer_hand_and_score()

            while True:
                dug = input("Hit or stand? 'h' or 's': ").lower()

                if dug not in ['h', 's']:
                    print("Please enter 'h' or 's'.")
                    continue
                if dug.lower() == 's':
                    break

                players[player].hit(player_number=player+1)

                if players[player].busted():
                    break
        system('cls')

        for player in players_range:
            players[player].show_hand_and_score(player_number=player+1)

        dealer.dealer_hit()
        players_score = [player.score for player in players]
        count_points(dealer.score, players_score)

        play_again = input("\nPlay again? 'y' or 'n': ")
        if play_again.lower() == 'n':
            break
        else:
            deck = [card for card in commom_deck.copy() for __ in players_range]
            dealer.restart_the_game(cards=deck)

            for player in players_range:
                players[player].restart_the_game(cards=deck)


if __name__ == '__main__':
    main()
