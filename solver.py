import heapq,time

def general_search(initial_state, heuristic=None):

    # uniform search uses 0 h(n)
    if heuristic is None:
        heuristic = lambda s: 0

    # initialize stat
    nodes_expanded = 0
    max_queue_size = 0
    start_time = time.time()

    # initialize priority queue
    start_f = initial_state.cost + heuristic(initial_state)
    frontier = [(start_f, 0, initial_state)]
    heapq.heapify(frontier)

    #data structures
    explored = set()
    #explore states explores in linear time
    frontier_dict = {str(initial_state.board): (initial_state, start_f)}
    #dictionary to check states faster than p
    counter = 1
    #used in even f(n)

    while frontier:
        # Update maximum queue size
        max_queue_size = max(max_queue_size, len(frontier))

        # using heap to get minimum f(n)
        _, _, state = heapq.heappop(frontier)

        # remove from dict
        state_str = str(state.board)
        if state_str in frontier_dict:
            del frontier_dict[state_str]

        # check if reach goal
        if state.whether_is_goal():
            end_time = time.time()
            return state, nodes_expanded, max_queue_size, end_time - start_time

        # update explored set
        explored.add(state_str)
        nodes_expanded += 1

        # try possible moves
        for move in state.try_moves():
            child = state.move(move)
            child_str = str(child.board)

            if child_str in explored:
                continue

            child_f = child.cost + heuristic(child)

            # update if find a better path
            if child_str in frontier_dict:
                if child_f < frontier_dict[child_str][1]:
                    # make all old entry invalid
                    for i, (_, _, s) in enumerate(frontier):
                        if s == frontier_dict[child_str][0]:
                            frontier[i] = (float('inf'), counter, s)
                            heapq.heapify(frontier)
                            break

                    # add a new entry
                    heapq.heappush(frontier, (child_f, counter, child))
                    frontier_dict[child_str] = (child, child_f)
                    counter += 1
            else:
                # add to frontier
                heapq.heappush(frontier, (child_f, counter, child))
                frontier_dict[child_str] = (child, child_f)
                counter += 1

    # no solution
    end_time = time.time()
    return None, nodes_expanded, max_queue_size, end_time - start_time

def traceback_path(state):
    #track back from solution to initial state
    if not state:
        return []

    path = []
    current = state

    while current:
        path.append(current)
        current = current.parent

    return list(reversed(path))