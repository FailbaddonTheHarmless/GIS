import Dijkstra
import Graph
import Edge

edges_txt_src = 'C:\\Users\\Dave\\Desktop\\GIS\\test_graph.txt' 
def main():
   
    graph = Graph.Graph(edges_txt_src)
    #graph.show_edges()
    dijkstra = Dijkstra.Dijkstra(graph)
    
    dijkstra.shortestPath(1,7)   
    dijkstra.getPath(1,7)

if __name__ == "__main__":
    main()
