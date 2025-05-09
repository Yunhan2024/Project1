import heapq,time

def general_search(initial_state, heuristic_func=None):

    # uniform search uses 0 h(n)
    if heuristic_func is None:
        heuristic_func = lambda s: 0

    # initialize stat
    nodes_expanded = 0
    max_queue_size = 0
    start_time = time.time()

    # initialize priority queue
    start_f = initial_state.cost + heuristic_func(initial_state)
    frontier = [(start_f, 0, initial_state)]
    heapq.heapify(frontier)