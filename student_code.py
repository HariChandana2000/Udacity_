import heapdict
from math import sqrt

def distance(node_coord, current_node_coord):
    return sqrt(pow((current_node_coord[0] - node_coord[0]), 2) + pow((current_node_coord[1] - node_coord[1]), 2))

def shortest_path(Map, start, goal):
    frontier = heapdict.heapdict()
    #initializing with start node
    frontier[start] = 0
    
    came_from = {}
    came_from[start] = None
    
    cost_so_far = {}
    cost_so_far[start] = 0
    
    explored = {}
    explored[start] = None
    
    while(len(frontier) != 0):
        current_node = frontier.popitem()[0]
        
        if current_node == goal:
            #return the shortest path using came_from dictionary
            final_path = []
            while current_node != start:
                final_path.append(current_node)
                current_node = explored[current_node]
            final_path.append(start)
            return final_path[::-1]
            
        for node in Map.roads[current_node]:
            update_score = cost_so_far[current_node] + distance(Map.intersections[node], Map.intersections[current_node])
            if (node not in explored) or (update_score < cost_so_far[node]):
                cost_so_far[node] = update_score
                total_distance = update_score + distance(Map.intersections[node], Map.intersections[goal])
                frontier[node] = total_distance
                came_from[node] = current_node
                explored[node] = current_node