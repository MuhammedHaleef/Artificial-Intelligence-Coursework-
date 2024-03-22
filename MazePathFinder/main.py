import matplotlib.pyplot as plt
import numpy as np
import random as rand
from matplotlib.lines import Line2D
from dfs import dfs_search_maze
from aStar import a_star_search


def plot_maze(maze):
    fig, ax = plt.subplots(figsize=(8, 4))  # Set a larger plot window size

    # Set the colormap: 0 for white, 1 for black (barriers), 0.5 for gray (path)
    cmap = plt.cm.gray
    norm = plt.Normalize(vmin=0, vmax=1)

    # Convert the maze to a NumPy array for easier manipulation
    maze_array = np.array(maze)

    # Display the maze with outlines
    ax.imshow(maze_array, cmap=cmap, norm=norm, extent=[-0.5, 5.5, 5.5, -0.5], origin='upper')

    # Add color for start node (green)
    start_node = np.where(maze == 1)
    ax.add_patch(plt.Rectangle((start_node[1][0] - 0.5, start_node[0][0] - 0.5), 1, 1, fill=True, color='green'))

    # Add color for goal node (yellow)
    goal_node = np.where(maze == 2)
    ax.add_patch(plt.Rectangle((goal_node[1][0] - 0.5, goal_node[0][0] - 0.5), 1, 1, fill=True, color='yellow'))

    # Add color for barrier nodes (black)
    barrier_nodes = np.where(maze == 9)
    for i in range(len(barrier_nodes[0])):
        ax.add_patch(plt.Rectangle((barrier_nodes[1][i] - 0.5, barrier_nodes[0][i] - 0.5), 1, 1, fill=True, color='gray'))

    # Add white or gray face color for other nodes
    for i in range(maze_array.shape[1]):
        for j in range(maze_array.shape[0]):
            if maze_array[i, j] == 0:
                ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=True, color='white'))

                # Add node values as text in the corner of each node
            ax.text(i - 0.5, j - 0.5, str(i * maze_array.shape[1] + j), ha='left', va='top', fontsize=6)

    # Add black outlines for each node
    for i in range(maze_array.shape[0] + 1):
        ax.axhline(i - 0.5, color='black', linewidth=1)
    for j in range(maze_array.shape[1] + 1):
        ax.axvline(j - 0.5, color='black', linewidth=1)

    # Set axis ticks and labels
    ax.set_xticks(np.arange(0, 6, 1))
    ax.set_yticks(np.arange(0, 6, 1))
    ax.set_yticklabels(np.arange(5, -1, -1))  # Reverse the y-axis labels

    # Create custom legend for color mapping
    legend_elements = [
        Line2D([0], [0], marker='s', color='w', markerfacecolor='green', markersize=10, label='Start Node (Green)'),
        Line2D([0], [0], marker='s', color='w', markerfacecolor='yellow', markersize=10, label='Goal Node (Yellow)'),
        Line2D([0], [0], marker='s', color='w', markerfacecolor='gray', markersize=10, label='Barrier Nodes (Gray)'),
    ]

    # Display the legend outside the plot
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))

    # Show the plot
    plt.title("Random Maze Layout")
    plt.show()


def check_if_possible_path_exist(barriers, node):      #checks for the special case : if the start node is fully surrounded by barriers
    # Checking the surrounding of StartNode
    if node == 5:
        if node + 6 in barriers and node - 1 in barriers and node + 5 in barriers:
            return False
    if node == 0:
        if node + 6 in barriers and node + 1 in barriers and node + 7 in barriers:
            return False
    if node == 35:
        if node - 6 in barriers and node - 1 in barriers and node - 7 in barriers:
            return False
    if node == 30:
        if node - 6 in barriers and node - 1 in barriers and node - 7 in barriers:
            return False

# Initializing a np.array to store the maz layout
maze_base = np.array([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])
# contains the maze node values from 0 to 35
maze_nodes = np.array([[0, 6, 12, 18, 24, 30],
    [1, 7, 13, 19, 25, 31],
    [2, 8, 14, 20, 26, 32],
    [3, 9, 15, 21, 27, 33],
    [4, 10, 16, 22, 28, 34],
    [5, 11, 17, 23, 29, 35]
])


# generate the barriers
barrier_nodes = []
while len(barrier_nodes) < 4:   # 4 barriers need to be generated
    barrier_node = rand.randint(0, 35)  # total nodes in the maze is 36
    if barrier_node not in barrier_nodes:
        barrier_nodes.append(barrier_node)
    else:
        continue
# print(barrier_nodes)
for node in barrier_nodes:
    node_index_row = node % 6
    node_index_column = node // 6
    # barrier nodes are denoted as '9' in the 2d maze base layout
    maze_base[(node_index_row, node_index_column)] = 9  # inserting all the barrier nodes to the maze base layout

# generating and inserting start, goal nodes to the maze base layout
while True:     # generating a start node
    start_node = rand.randint(0, 11)
    if start_node not in barrier_nodes and not check_if_possible_path_exist(barrier_nodes, start_node):
        # getting start node row, column index values.
        node_index_row = start_node % 6
        node_index_column = start_node // 6
        # start node is denoted as '1'  in the 2d maze base layout
        maze_base[(node_index_row, node_index_column)] = 1        # inserting the start node to the maze base layout
        break
    else:
        continue

while True:     # generating a goal node
    goal_node = rand.randint(24, 35)
    if goal_node not in barrier_nodes and not check_if_possible_path_exist(barrier_nodes, goal_node):
        # getting start node row, column index values.
        node_index_row = goal_node % 6

        node_index_column = goal_node // 6
        # goal node is denoted as '2'  in the 2d maze base layout
        maze_base[(node_index_row, node_index_column)] = 2        # inserting the goal node to the maze base layout
        break
    else:
        continue


print(maze_base)
print("Start node value ", start_node)
print("Goal node value ", goal_node)
print("Barrier nodes : ", end=' ')
for bar in barrier_nodes:
    print(bar)
print("\n")

print("DFS searching algorithm is being applied to the maze.\n")
dfs_search_maze(maze_base, maze_nodes)

print("\nA* searching algorithm is being applied to the maze.\n\n")
a_star_search(maze_nodes, start_node, goal_node, barrier_nodes)


plot_maze(maze_base)


# heuristic_function(maze_base,neighbour_node,goal_node)
# plot_maze(maze_base)
