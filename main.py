from state import PuzzleState
from solver import general_search, traceback_path

def main():
    print("Eight Puzzle Game")
    print("*************")

    # default input
    default_board = [
        [1, 6, 7],
        [5, 0, 3],
        [4, 8, 2]
    ]

    # manual input
    use_default = input("Use default state (1,6,7,5,0,3,4,8,2)? (y/n): ").lower() == 'y'

    if use_default:
        board = default_board
    else:
        print("Enter 3x3 board :")
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
        print("Warning: This state is unsolvable.")
        return

    # 1. uniform cost search
    print("\nUniform Cost Search:")
    goal, nodes_expanded, max_queue, time_taken = general_search(initial_state)
    #general without h(n) is unifrom cost search

    if goal:
        path = traceback_path(goal)
        print(f"Solution found, Takes  {len(path) - 1}Steps.")
        print(f"{nodes_expanded} Nodes expanded.")
        print(f"Maximum queue size is {max_queue}")
        print(f"Time taken: {time_taken * 1000:.2f} ms")
    else:
        print("No solution.")

    # 2. A* search with misplaced tile heuristic
    print("\nA* Search with Misplaced Tile heuristic:")
    goal, nodes_expanded, max_queue, time_taken = general_search(initial_state, lambda s: s.misplaced_tile())

    if goal:
        path = traceback_path(goal)
        print(f"Solution found, Takes  {len(path) - 1}Steps.")
        print(f"{nodes_expanded} Nodes expanded.")
        print(f"Maximum queue size is {max_queue}")
        print(f"Time taken: {time_taken * 1000:.2f} ms")
    else:
        print("No solution.")

    # 3. A* search with manhattan distance heuristic
    print("\nA* Search with Manhattan Distance:")
    goal, nodes_expanded, max_queue, time_taken = general_search(initial_state,
                                                                 lambda s: s.manhattan_distance())

    if goal:
        path = traceback_path(goal)
        print(f"Solution found, Takes  {len(path) - 1}Steps.")
        print(f"{nodes_expanded} Nodes expanded.")
        print(f"Maximum queue size is {max_queue}")
        print(f"Time taken: {time_taken * 1000:.2f} ms")

        # Display solution path
        print("\nSolution path:")
        for i, state in enumerate(path):
            print(f"Step {i}:")
            if i > 0:
                print(f"Move: {state.action}")
            state.print_board()
    else:
        print("No solution.")

if __name__ == "__main__":
    main()