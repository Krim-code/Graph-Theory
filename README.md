# Graph-Theory
## DFS (Depth First Search) and BFS (Breadth First Search) are two commonly used graph traversal algorithms used to explore and search through a graph data structure.

### DFS:
  DFS is a graph traversal algorithmthat starts at a source vertex and 
  explores as far as possible along each branch before backtracking. 
  It works by visiting a node and then recursively visiting all of its adjacent nodes that have not been visited before.
  This process is repeated until all nodes in the graph have been visited or until the target node is found

### BFS:
BFS is a graph traversal algorithm that explores all the nodes at the present 
depth before moving on to the nodes at the next depth.It starts at a source vertex and explores all the vertices 
at the current level before moving to the next level. It works by maintaining 
a queue of nodes to be visited and visiting the nodes in the order they were added to the queue.

## Kruskal's algorithm:
Kruskal's algorithm is a greedy algorithm used to find the minimum spanning tree of a
weighted undirected graph. The minimum spanning tree is a subset of the edges of the graph
that connect all the vertices with the minimum total edge weight. Kruskal's algorithm 
works by sorting the edges of the graph by weight, and then adding edges to the minimum spanning tree
one by one in increasing order of weight, while ensuring that the tree remains acyclic.

### The steps of Kruskal's algorithm are as follows:

1. Sort the edges of the graph by weight.
2. Initialize an empty set of edges to be added to the minimum spanning tree.
3. Iterate through the sorted edges in increasing order of weight.
4. For each edge, check whether adding it to the minimum spanning tree would create a cycle.
5. If adding the edge does not create a cycle, add it to the set of edges in the minimum spanning tree.
6. Repeat steps 4-5 until all vertices are connected in the minimum spanning tree.

## Finding the maximum connected component:
To find the maximum connected component in an undirected graph, we can use a depth-first search (DFS) 
or breadth-first search (BFS) algorithm. The steps are as follows:

1. Choose a random vertex as the starting vertex.
2. Perform a DFS or BFS traversal from the starting vertex, keeping track of the visited vertices.
3. After the traversal is complete, the visited vertices will form a connected component.
4. Repeat steps 1-3 for all vertices in the graph that have not been visited.
5. Compare the size of each connected component to find the largest one.

Alternatively, we can use a union-find data structure to efficiently find the maximum connected component.
The union-find data structure allows us to keep track of the connected components in a graph while efficiently merging them.
We can initialize each vertex as a separate connected component and then merge connected components as we traverse the edges of the graph.
The size of the largest connected component can be found by keeping track of the size of each connected component as we merge them.
