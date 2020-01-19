import Graph
import math
class Dijkstra():
    
    def __init__(self, graph = None):
        if not graph:
            self.graph = Graph.Graph()
        else:
            self.graph = graph
        self.predecessors = {}
        self.distances = {}
        for edge in self.graph.graph_dict.keys():
            if edge not in self.predecessors:
                self.predecessors[edge] = -math.inf
                
    def shortestPath(self, source, destination):
        
        self.calculateShortestPath(source, destination)
        
        if destination != -math.inf:
            self.printPath(self.reconstructPath(source,destination))
            print(f'Distance: {self.distances[destination]} \n' )
            
    def calculateShortestPath(self, source, destination):
        if not self.isValidVertex(source) or not self.isValidVertex(destination) and destination != -math.inf:
            raise ValueError('Invalid source or destination')
        
        self.clearState()
        self.updateDistances(source,0)
        priorityQueue = self.createPriorityQueue()
        currentVertex = source
        
        while priorityQueue:
        
            if source==destination:
                break
            self.updateSuccessorDistance(currentVertex)
            priorityQueue.sort(reverse = True)
            currentVertex = priorityQueue.pop()
        
    def createPriorityQueue(self):
        return list(self.predecessors.keys())
    
    def isValidVertex(self, vertex):
        return vertex in self.predecessors
    
    def clearState(self):
        for key in self.predecessors.keys():
            self.predecessors[key] = -math.inf
            self.distances[key] = math.inf
    
    def updateDistances(self, vertex, distance):
        self.distances[vertex] = distance
    
    def updateSuccessorDistance(self, predecessor):
        successorsEdges = self.graph.graph_dict[predecessor]
        
        for successor in successorsEdges:
            if self.getDistance(successor.destination) > self.getDistance(predecessor) + successor.weight:
    
                self.updateDistances(successor.destination, self.getDistance(predecessor) + successor.weight)
                self.updatePredecessors(successor.destination, predecessor)
                
    def getDistance(self, vertex):
        return self.distances[vertex]
    
    def reconstructPath(self, source, destination):
        path = []
        currentVertex = destination
        while currentVertex != source:
            if currentVertex == -math.inf:
                raise ValueError(f'Connection between {source} and {destination} doesnt exist \n')
                
            path.append(currentVertex)
            currentVertex = self.predecessors[currentVertex]
        path.append(source)
        path.reverse()
        return path
            
    def printPath(self, path):
        
        pathString = ''
        for i in range(len(path)-1):
            pathString += str(path[i]) + ' -> '
            
        pathString += str(path[i+1])
        print(f'Dijkstra shortest path: {pathString} \n')
    
    def updatePredecessors(self, vertex, predecessor):
        self.predecessors[vertex] = predecessor
    
    def getPath(self, source, destination):
        self.printPath(self.reconstructPath(source, destination))
        print(f'Distance: {self.distances[destination]} \n')
        
    