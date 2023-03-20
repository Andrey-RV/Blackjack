def get_number_of_players() -> range:
    """Get the number of players from the user and returns a range iterable with the number of players.

    Returns:
        int: The number of players.
    """
    while True:
        str_num_of_player = input("How many players? ")
        if not str_num_of_player.isdigit():
            print("Please enter an integer number.")
            continue
        if '.' in str_num_of_player:
            print("Please enter an integer number.")
            continue
        if int(str_num_of_player) < 1:
            print("Please enter a number greater than 0.")
            continue
        break
    return range(int(str_num_of_player))
