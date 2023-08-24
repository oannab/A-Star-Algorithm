**Project 4 - A* Algorithm**
*use A* search to implement a "Google-maps" style route planning algorithm.*

_Abbreviation:_
_Time Complexity = TC_
_Space Complexity = SC_

**modules imported
- math module for math
- heapq module for priority queue
- networksx for working with graphs

- the algorithm is an estimated lowest total cost of reaching a goal point from start (start-node --->>>> goal-node)
    - g(n): The cost of the path from the start node to node n.
    - h(n): The estimated cost from node n to the goal node. 
    - heuristic estimate: f(n) = g(n) + h(n) - an optimistic approximation of total cost/distance


**calc_dist()
- f() that takes dictionary input containing the 2d points of each node in graph
- calculates distance between the 2 input points -->> 2 dictionaries containing the cartesian coordinates of nodes and their neighbours
- the method takes either euclidean or manhattan metric to calc distance
    - manhattan method - calc toatl no of nodes, moved horizontally and vertically to reach target
    - h(n) = $abs(x1-x2) + abs(y1-y2)$
    - euclidean method - calc toatl no of nodes, moved horizontally and vertically to reach target
    - h(n) = $sqrt((x1-x2)^2 + (y1-y2)^2)$
- the calculated distance is returned by the function    
- TC is O(1), time is constant since there will always only be 2 input variables in the arithemtic equation. the 'if/else' statement also checks a fixed number of conditions.
- SC is O(1), constant as the space required to perform arithmetic equation is a fixed memory space, regardless of the amount of data inside dictionaries. only ever checks 2 variables inputs at a time. the variables and result are reused with each iteration, are written over with the next call of function. therefore the storage of the vars and result is constant/ the same and does not accumulate or grow regardless of how many times the f() is called


**shortest_path()
- initialize a priority queue for open nodes, tuples that contain the (cost, node) 
    - TC is O(log n), n is the number of nodes in the heap, and each traverse requires poping a node of the heap.
    - SC is O(n), worst case, all nodes can be added to the heap.

- keep track of visited nodes in a set()
    - TC is O(1), as inserting has constant runtime
    - SC is O(n), n is the no of visited nodes, worst case, all nodes are visited.

- store the parent node of each node to help reconstruct path in a dictionary that holds
    - TC is O(1), as inserting has constant runtime
    - SC is O(n), n is the no of visited nodes, worst case, all nodes are visited.

- store the cost to reach each node - f(), except start node which has a cost 0


- the algorithm continues as long as the open_queue (priority queue) is not empty. 
    - TC is O(log n), n is no of nodes in the priority queue
    - SC is O(n), worst case, all nodes can be added to the heap
- pop the node with the lowest cost of the heap
    - TC is O(log n), binary heap 
    - SC is constant operation, O(1), as the space required is the same whilst raeranging the existing elems in the heap.

- while loop for the current node == goal, the goal has been reached and starts reconstructing the path
- initializing the path list to be able to retrace the visited nodes with the lowest cost in order to retrace the steps and provide the most efficient path traversal. path is stored in reverse order.
    - TC is O(1), inserting into the path is constant
    - SC is O(n), n is the no of elems added, worst case, all nodes can be added

- the parent node of the current_node is also updated in order to be able to traceback the traversal
    - TC is O(1), inserting at the end of list since, path is stored in reverse order
    - SC is O(n), n is length of the list

- check if current node has already been visited and add it if not
    - TC is O(1)
    - SC is O(n), when adding the node to the set, n is the no of nodes in the open queue or graph of total nodes

- then check the current_node's neighbour
    - TC is O(n), n is the no of neighbours of current node.
    - SC is O(n), proportional to the no of neighbours

- calculate the distance from the current node to the neighbour and update the cost map of reaching the next neighbour. the parent map is also updated based on lowest cost to reach the neighb.
    - O(1), constant for performing arithemtic calc of calculating distance, also for comparison between costs and updating dictionaries of cost and parent node.
    - O(1), constant as the space required for updating the dict is the same. this does not reflect the space required for the dict.

- based on lowest cost found to reach the next neighbour from current node, the new cost and neighbour are pushed into the open_queue as a tuple (cost, neighbour). this is used as the priority in the priority queue.
    - TC is O(log n), n is no of elems in the heaps
    - SC is O(1), as there is no additional memory required to insert elems into the queue and rearange the heap
   




