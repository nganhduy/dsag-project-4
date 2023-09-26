import math
from queue import PriorityQueue


#I used the idea in here https://dbader.org/blog/priority-queues-in-python

def shortest_path(graph, start, goal):
    
    path_queue = PriorityQueue()
    path_queue.put(start, 0)
    
    prev = {start: None}
    score = {start: 0}

    while not path_queue.empty():
        curr = path_queue.get()

        if curr == goal:
            generate_path(prev, start, goal)

        for node in graph.roads[curr]:
            update_score = score[curr] + heuristic_measure(graph.intersections[curr], graph.intersections[node])
            
            if node not in score or update_score < score[node]:
                score[node] = update_score
                total_score = update_score + heuristic_measure(graph.intersections[curr], graph.intersections[node])
                path_queue.put(node, total_score)
                prev[node] = curr

    return generate_path(prev, start, goal)


#returning distance from start to goal
def heuristic_measure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))

def generate_path(prev, start, goal):
    curr = goal
    path = [curr]
    while curr != start:
        curr = prev[curr]
        path.append(curr)
    path.reverse()
    return path