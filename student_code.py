import math
import heapq
import networkx as nx    # link graphs

def calculate_distance(point1, point2, metric='euclidean'):
    if len(point1) != 2 or len(point2) != 2:
        raise ValueError("Points must be 2D (x, y pairs)")
    
    if metric == 'euclidean':
        squared_sum = (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
        distance = math.sqrt(squared_sum)
    elif metric == 'manhattan':
        distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    else:
        raise ValueError("Unsupported distance metric. Choose 'euclidean' or 'manhattan'") # 
    
    return distance

def shortest_path(M, start, goal): # start and goal are points in the graph 
    intersections = M.intersections # M is the object representing the graph. 
    roads = M.roads # dict holds the coordinates of points of intersections and roads - separately
    
    if start not in intersections or goal not in intersections: # check validity of nodes - the dictionaries for intersections and roads
        raise ValueError("Start or goal not present in intersections")
    
    open_queue = [(0, start)]   # priority queue for open nodes, tuples that contain the (cost, node)
    visited = set()   # keep track of visited nodes
    parent_map = {}   # store the parent node of each node to help reconstruct path
    cost_map = {node: float('inf') for node in intersections}  # store the cost to reach each node - f()
    cost_map[start] = 0
    
    while open_queue: # priority queue / tuples (cost, node)
        current_cost, current_node = heapq.heappop(open_queue)  # each iteration pops the node with lowest estimated cost
        print(f"Exploring node: {current_node}, Cost: {current_cost}")

        if current_node == goal:
            path = [] # create a list to store the optimal path
            while current_node is not None:
                path.insert(0, current_node) # insert the current node at the beginning of the list
                current_node = parent_map.get(current_node)
            return path
        
        if current_node in visited: #skip node
            continue
        
        visited.add(current_node) # add current node to visited if not already in
        
        for neighbor in roads[current_node]: # new_cost calculates the cost to reach the neighbour from current node
            new_cost = cost_map[current_node] + calculate_distance(intersections[current_node], intersections[neighbor]) # estimated cost/diastance from start to current node - g(n)
            if new_cost < cost_map[neighbor]: # if new cost is less then the prev cost to reach that neighbour, update parent map and new cost
                parent_map[neighbor] = current_node
                cost_map[neighbor] = new_cost
                heapq.heappush(open_queue, (new_cost + calculate_distance(intersections[neighbor], intersections[goal]), neighbor)) # and push the new cost and neighbour in the priority queue, and base the priority on this eq ->> f(n) = g(n) + h(n)
                print(f"  Added neighbor: {neighbor}, New cost: {new_cost}, Priority: {new_cost}")

    return None # if no path is found, return None




# g(n) -> cost/distance of path from start to node n 
# h(n  -> estimated cost/diastance from node n to goal 
# f(n) = g(n) + h(n)  -> total estimated cost/diastance from start to goal


"""
References: 
https://www.geeksforgeeks.org/a-search-algorithm/
https://dhruvs.space/posts/understanding-the-a-star-algorithm/#the-a-star-algorithm
https://www.geeksforgeeks.org/priority-queue-set-1-introduction/
https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/#:~:text=Dijkstra's%20Algorithm%20finds%20the%20shortest,node%20and%20all%20other%20nodes.
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
https://www.geeksforgeeks.org/find-minimum-weight-cycle-undirected-graph/?ref=lbp
https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
https://brilliant.org/wiki/a-star-search/
https://www.geeksforgeeks.org/python-__lt__-magic-method/
https://www.geeksforgeeks.org/a-search-algorithm/
https://plotly.com/python/network-graphs/
https://www.geeksforgeeks.org/star-graph-using-networkx-python/
https://www.youtube.com/watch?v=ySN5Wnu88nE
https://www.youtube.com/watch?v=aKYlikFAV4k



"""