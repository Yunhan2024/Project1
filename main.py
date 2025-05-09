from state import PuzzleState
from solver import general_search

def main():
    print("Eight Puzzle Game")
    print("*************")

    # default input
    default_board = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    # manual input
    use_default = input("Use default state (1,2,3,4,0,6,7,5,8)? (y/n): ").lower() == 'y'

    if use_default:
        board = default_board
    else:
        print("Enter 3x3 board (use 0 for blank):")
        board = []
        for i in range(3):
            row = list(map(int, input(f"Row {i + 1} (space separated): ").split()))
            board.append(row)

    #  initial state
    initial_state = PuzzleState(board)

    print("\nInitial state:")
    initial_state.print_board()

    # check if solvable  using inversion
    if hasattr(initial_state, 'is_solvable') and not initial_state.is_solvable():
        print("Warning: This state is not solvable!")
        print("For the 3x3 eight-puzzle, only half of the initial states are solvable.")
        return