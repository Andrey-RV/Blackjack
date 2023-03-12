def get_number_of_players() -> range:
    """_Get the number of players from the user and returns a range iterable with the number of players._

    Returns:
        int: _The number of players._
    """
    str_num_of_player = input("How many players? ")

    if not str_num_of_player.isdigit():
        print("Please enter a number.")
        str_num_of_player = input("How many players? ")
    if int(str_num_of_player) < 1:
        print("Please enter a number greater than 0.")
        str_num_of_player = input("How many players? ")
    return range(int(str_num_of_player))
