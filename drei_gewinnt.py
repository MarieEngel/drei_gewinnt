# the game board contains 9 fields - arranged 3 x 3 - at the beginning of the game
# each field contains a number from 1-9, the players can select
# a field by their number

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# players can select fields & put their sign (x or o) depending
# which fields are still available (haven't been selected before)


def show_board(values):
    board = f"------- \n|{values[0]}|{values[1]}|{values[2]}|\n--+-+--\n|{values[3]}|{values[4]}|{values[5]}|\n--+-+--\n|{values[6]}|{values[7]}|{values[8]}|\n-------"
    return board


def check_selected_field(selected_field, values, current_player):
    if selected_field not in values or not isinstance(selected_field, int):
        return False
    else:
        return True


def check_won(values):
    if (
        (values[0] == values[1] == values[2])
        or (values[3] == values[4] == values[5])
        or (values[6] == values[7] == values[8])
        or (values[0] == values[4] == values[8])
        or (values[2] == values[4] == values[6])
        or (values[0] == values[3] == values[6])
        or (values[1] == values[4] == values[7])
        or (values[2] == values[5] == values[8])
    ):
        return True
    else:
        return False


# Player 'x' always starts, than it is player 'o's turn


def main():
    current_player = "x"
    while True:
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(
            "Would you like to start a new game? Type 'yes' to start, type 'no' to exit."
        )
        start_input = input()
        if start_input == "no":
            break
        elif start_input == "yes":
            for round in range(9):
                print(show_board(values))
                try:
                    print(f"Player {current_player}, which field do you want to mark?")
                    selected_field = int(input())
                except ValueError:
                    print("Select of the numbers in the grid.")
                    continue

                while check_selected_field(selected_field, values, current_player) is False:
                    print(f"This field {selected_field} is not available.")
                    print(show_board(values))
                    print(f"Player {current_player}, which field do you want to mark?")
                    selected_field = int(input())
                else:
                    values[selected_field - 1] = current_player
                if check_won(values):
                    print(show_board(values))
                    print(f"Player {current_player} won!")
                    break
                else:
                    if current_player == "x":
                        current_player = "o"
                    else:
                        current_player = "x"

            else:
                print("No more fields available. Remis.")

        else:
            print(
                "You had a typo. Would you like to start a new game? Type 'yes' to start, type 'no' to exit."
            )


if __name__ == "__main__":
    main()


# Get input
# Validate (boolean)
# Update field
# Check if won
