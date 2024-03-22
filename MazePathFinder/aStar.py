import numpy as np


def a_star_search(maze_nodes, start_node, goal_node, barrier_nodes):
    visited_nodes = []
    s_row, s_column = getting_node_index(maze_nodes, start_node)        # getting start node row, column value
    g_row, g_column = getting_node_index(maze_nodes, goal_node)     # getting goal node row, column value
    total_time = 0

    # path_value = 1
    # heuristic_value = 1000      # for this maze 1000 works as a infinity amount cuz the heuristic + path values total is for any cse is less than 1000
    # total_travel_value = heuristic_value + path_value

    p_row, p_column = s_row, s_column       # at first the 'processing_node' is start node
    process_node = start_node

    while True:
        # Check left, right, up, and down and diagonal neighbors
        lowest_heu_value = None
        lowest_heu_value_node = None

        # checking if an Up-left node is available for the processing node
        if p_row > 0 and p_column > 0 and process_node not in barrier_nodes:
            # if exist getting the new upLeft neighbour node's value using the relevant row, column values.
            up_left_neighbour_node = getting_node_value(p_row - 1, p_column - 1)
            up_left_neighbour_node_heu_val = get_heuristic_value(maze_nodes, up_left_neighbour_node, goal_node)     # getting the heuristic value

            if lowest_heu_value is None or lowest_heu_value > up_left_neighbour_node_heu_val:
                lowest_heu_value = up_left_neighbour_node_heu_val
                lowest_heu_value_node = up_left_neighbour_node

        # Left
        if p_column > 0 and process_node not in barrier_nodes:
            left_neighbour_node = getting_node_value(p_row, p_column - 1)
            left_neighbour_node_heu_val = get_heuristic_value(maze_nodes, left_neighbour_node, goal_node)
            if lowest_heu_value is None or lowest_heu_value > left_neighbour_node_heu_val:
                lowest_heu_value = left_neighbour_node_heu_val
                lowest_heu_value_node = left_neighbour_node

        # Down-left
        if p_row < maze_nodes.shape[0] - 1 and p_column > 0 and process_node not in barrier_nodes:  # maze.shape[0] return 6 for this 6*6 maze
            down_left_neighbour_node = getting_node_value(p_row + 1, p_column - 1)
            down_left_neighbour_node_heu_val = get_heuristic_value(maze_nodes, down_left_neighbour_node, goal_node)
            if lowest_heu_value is None or lowest_heu_value > down_left_neighbour_node_heu_val:
                lowest_heu_value = down_left_neighbour_node_heu_val
                lowest_heu_value_node = down_left_neighbour_node

        # Up
        if p_row > 0 and process_node not in barrier_nodes:
            up_neighbour_node = getting_node_value(p_row - 1, p_column)
            up_neighbour_node_heu_val = get_heuristic_value(maze_nodes, up_neighbour_node, goal_node)
            if lowest_heu_value is None or lowest_heu_value > up_neighbour_node_heu_val:
                lowest_heu_value = up_neighbour_node_heu_val
                lowest_heu_value_node = up_neighbour_node

        # down
        if p_row < maze_nodes.shape[0] - 1 and process_node not in barrier_nodes:
            down_neighbour_node = getting_node_value(p_row + 1, p_column)
            down_neighbour_node_heu_val = get_heuristic_value(maze_nodes, down_neighbour_node, goal_node)
            if lowest_heu_value is None or lowest_heu_value > down_neighbour_node_heu_val:
                lowest_heu_value = down_neighbour_node_heu_val
                lowest_heu_value_node = down_neighbour_node

        # up_right
        if p_row > 0 and p_column < maze_nodes.shape[1] - 1 and process_node not in barrier_nodes:
            up_right_neighbour_node = getting_node_value(p_row - 1, p_column + 1)
            up_right_neighbour_node_heu_val = get_heuristic_value(maze_nodes, up_right_neighbour_node, goal_node)
            if lowest_heu_value is None or lowest_heu_value > up_right_neighbour_node_heu_val:
                lowest_heu_value = up_right_neighbour_node_heu_val
                lowest_heu_value_node = up_right_neighbour_node

        # right
        if p_column < maze_nodes.shape[1] - 1 and process_node not in barrier_nodes:
            right_neighbour_node = getting_node_value(p_row, p_column + 1)
            right_neighbour_node_heu_val = get_heuristic_value(maze_nodes, right_neighbour_node, goal_node)
            if lowest_heu_value is None or lowest_heu_value > right_neighbour_node_heu_val:
                lowest_heu_value = right_neighbour_node_heu_val
                lowest_heu_value_node = right_neighbour_node

        # down_right
        if p_row < maze_nodes.shape[0] - 1 and p_column < maze_nodes.shape[1] - 1 and process_node not in barrier_nodes:
            down_right_neighbour_node = getting_node_value(p_row + 1, p_column + 1)
            down_right_neighbour_node_heu_val = get_heuristic_value(maze_nodes, down_right_neighbour_node, goal_node)
            if lowest_heu_value is None or lowest_heu_value > down_right_neighbour_node_heu_val:
                lowest_heu_value = down_right_neighbour_node_heu_val
                lowest_heu_value_node = down_right_neighbour_node

        # changing the new processing node which has the lowest heuristic value to use it for the next iteration
        p_row, p_column = getting_node_index(maze_nodes, lowest_heu_value_node)
        process_node = getting_node_value(p_row, p_column)

        visited_nodes.append(lowest_heu_value_node)

        if p_row == g_row and p_column == g_column:
            break;

        total_time += 1

    print("Visited nodes : ")
    for node in visited_nodes:
        print(node, end=' ')

    print("\n Time taken to find the goal : ", total_time, "minutes.")


def get_heuristic_value(maze_nodes, neighbour_node, goal_node):
    p_row, p_column = getting_node_index(maze_nodes, neighbour_node)
    g_row, g_column = getting_node_index(maze_nodes, goal_node)
    return abs(g_row - p_row) + abs(g_column - p_column)


def check_neighbor_barrier(neighbour_node, barrier_nodes):
    for barrier in barrier_nodes:
        if barrier == neighbour_node:
            return True


def getting_node_index(maze_nodes, node_value):
    return np.where(maze_nodes == node_value)


def getting_node_value(row, column):
    return column * 6 + row
