"""
Q1. A graph is said to be a directed acyclic graph if the graphs is directed
and does not have any directed cycles. These are often called as DAGs for 
short. One of the interesting properties of DAGs is that given any pair of
vertices s and t in such a graph, one can count the number of directed paths
from s to t very efficiently. Solve the problem and write a program to implement
your solution. 

The graph itself will be specified by listing the neighbors of each vertex in 
one line each. The vertices s and t are specified as the first line along with 
the number of vertices n as follows.


n  s   t
u1  u2  u3
x1 x2  x3
.
.
z1 z2

The output is the number of paths from s to t.
"""
from collections import defaultdict
  
#This class represents a directed graph 
# using adjacency list representation
class Graph:
  
    def __init__(self,vertices):
        #No. of vertices
        self.V= vertices 
         
        # default dictionary to store graph
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
  
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path):
 
        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)
 
        # If current vertex is same as destination, then print
        # current path[]
        if u ==d:
            print path
        else:
            # If current vertex is not destination
            #Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i]==False:
                    self.printAllPathsUtil(i, d, visited, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False
  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self,s, d):
 
        # Mark all the vertices as not visited
        visited =[False]*(self.V)
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d,visited, path)
  
  
  
# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)
  
s = 2 ; d = 3
print ("Following are all different paths from %d to %d :" %(s, d))
g.printAllPaths(s, d)
#This code is contributed by Neelam Yadav