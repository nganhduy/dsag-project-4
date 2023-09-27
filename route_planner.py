import math
from queue import PriorityQueue
#I used the idea in here https://dbader.org/blog/priority-queues-in-python

# The shortest_path function takes three parameters: 
# graph, which represents the graph containing nodes and edges, start, 
# which is the starting node, and goal, which is the destination node.
def shortest_path(graph, start, goal):

    # Path_queue is created using PriorityQueue(). 
    # This queue will store the nodes to be explored in the order of their priority.
    path_queue = PriorityQueue()
    path_queue.put(start, 0)
    
    # The prev dictionary is created to keep track of the previous node in the shortest path from the start node to each node. 
    prev = {start: None}

    # The score dictionary is used to store the current shortest distance from the start node to each node.
    score = {start: 0}


    # The main part of the algorithm is implemented using a while loop that runs until the path_queue is empty
    while not path_queue.empty():

        # Inside the loop, the node with the highest priority (lowest score) is retrieved from the path_queue using the get() method.
        curr = path_queue.get()

        # If the current node is equal to the goal node, 
        # the generate_path function is called to generate and return the shortest path from the start to the goal.
        if curr == goal:
            generate_path(prev, start, goal)

        # If the current node is not the goal node, the algorithm explores the neighbors of the current node. 
        # For each neighbor, it calculates the updated score by adding the score of the current node and the heuristic measure between the current node and the neighbor.
        for node in graph.roads[curr]:
            update_score = score[curr] + heuristic_measure(graph.intersections[curr], graph.intersections[node])

            # If the neighbor node is not in the score dictionary or the updated score is smaller than the current score, 
            # the score dictionary is updated with the new score, 
            # and the total score (updated score + heuristic measure) is used as the priority to put the neighbor node into the path_queue. 
            # The prev dictionary is also updated to store the previous node for the neighbor node.
            if node not in score or update_score < score[node]:
                score[node] = update_score
                total_score = update_score + heuristic_measure(graph.intersections[curr], graph.intersections[node])
                path_queue.put(node, total_score)
                prev[node] = curr

    # The generate_path function is called to generate and return the shortest path from the start to the goal node.
    return generate_path(prev, start, goal)


# The heuristic_measure function calculates the Euclidean distance between two points, 
# start and goal, 
# using the formula math.sqrt(((start[0] - goal[0]) **2) + ((start[1] - goal[1])** 2))
def heuristic_measure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


# The generate_path function takes the prev dictionary, start node, and goal node as parameters. 
# It starts from the goal node and iteratively finds the previous node until it reaches the start node, appending each node to the path list. 
# Finally, it reverses the path list and returns it.
def generate_path(prev, start, goal):
    curr = goal
    path = [curr]
    while curr != start:
        curr = prev[curr]
        path.append(curr)
    path.reverse()
    return path