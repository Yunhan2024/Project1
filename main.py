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

        # 1. uniform cost search
        print("\nUniform Cost Search:")
        goal, nodes_expanded, max_queue, time_taken = general_search(initial_state)
        #general without h(n) is unifrom cost search

        if goal:
            path = traceback_path(goal)
            print(f"Solution found! Steps: {len(path) - 1}")
            print(f"Nodes expanded: {nodes_expanded}")
            print(f"Maximum queue: {max_queue}")
            print(f"Time taken: {time_taken * 1000:.2f} ms")
        else:
            print("No solution.")