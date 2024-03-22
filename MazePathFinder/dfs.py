import numpy as np

#  this python file contains the code for DFS search algorithm.
def dfs_search_maze(maze_base,maze_nodes):
    visited_nodes = []
    total_time_spent = 0
    node_stack = []
    start_node_maze = getting_node_number(maze_base, 1)
    goal_node_maze = getting_node_number(maze_base, 2)

    barrier_nodes = []  # getting the barrier node values as in the sample maze.
    barrier_node_indexes = np.where(maze_base == 9)
    if len(barrier_node_indexes[0]) > 1:
        # Handle the case where there are multiple indices
        for i in range(len(barrier_node_indexes[0])):
            row, col = barrier_node_indexes[0][i], barrier_node_indexes[1][i]
            node_number = col * 6 + row
            barrier_nodes.append(node_number)
    else:
        row, col = barrier_node_indexes[0][0], barrier_node_indexes[1][0]
        node_number = col * 6 + row
        barrier_nodes.append(node_number)

    node_stack.append(start_node_maze)
    while len(node_stack) > 0:  # add more conditions if needed
        visited_nodes.append(node_stack.pop())      # adding the removed node value to
        # 'visited nodes' list
        processing_node = visited_nodes[len(visited_nodes) - 1]

        # checking whether processing node is the goal
        if processing_node == goal_node_maze:
            break

        neighbour_nodes = []

        # getting processing nodes row and column values
        row, col = np.where(maze_nodes == processing_node)

        # Check left, right, up, and down and diagonal neighbors
        if row > 0 and col > 0:
            neighbour_nodes.append(maze_nodes[row - 1, col - 1])  # Up-left
        if col > 0:
            neighbour_nodes.append(maze_nodes[row, col - 1])  # Left
        if row < maze_base.shape[0] - 1 and col > 0:    # maze.shape[0] return 6 for this 6*6 maze
            neighbour_nodes.append(maze_nodes[row + 1, col - 1])  # Down-left
        if row > 0:
            neighbour_nodes.append(maze_nodes[row - 1, col])  # Up
        if row < maze_base.shape[0] - 1:
            neighbour_nodes.append(maze_nodes[row + 1, col])  # Down
        if row > 0 and col < maze_base.shape[1] - 1:
            neighbour_nodes.append(maze_nodes[row - 1, col + 1])  # Up-right
        if col < maze_base.shape[1] - 1:
            neighbour_nodes.append(maze_nodes[row, col + 1])  # Right
        if row < maze_base.shape[0] - 1 and col < maze_base.shape[1] - 1:
            neighbour_nodes.append(maze_nodes[row + 1, col + 1])  # Down-right

        # calculated the time taken to find the goal
        total_time_spent += 1

        # remove barrier nodes from neighbour_nodes list
        for i in range(len(barrier_nodes)):
            if barrier_nodes[i] in neighbour_nodes:
                neighbour_nodes.remove(barrier_nodes[i])
        #sorting the neighbor_nodes list to descending order
        neighbour_nodes.sort(reverse=True)

        #appending the nodes in descending order to the 'node_stack'
        for j in range(len(neighbour_nodes)):
            if neighbour_nodes[j] not in node_stack and neighbour_nodes[j] not in visited_nodes:
                node_stack.append(neighbour_nodes[j])

    # print(barrier_nodes, "\n")
    print('Visited Nodes in order: ', end=" ")
    for i in range(len(visited_nodes)):
        print(visited_nodes[i], end=' ')

    print("\n")
    print("Time taken to find the goal : ", total_time_spent, " minutes")


def getting_node_number(maze, node_value):  # getting start and goal node numbers
    maze = np.array(maze)  # converting the maze to a numpy array for easy of execution
    index = np.where(maze == node_value)  # getting the node_value's index
    # getting the node number
    node_number = index[1] * 6 + index[0]
    return node_number
