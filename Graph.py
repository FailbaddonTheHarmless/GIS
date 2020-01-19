import Edge
        
class Graph:
    #source_type 'txt' or 'edgelist'
    def __init__(self, source = None, source_type = 'txt'):
        self.graph_dict = {}
        
        if source:
            if source_type == 'txt':
                if type(source) == tuple or type(source) == list:
                    raise TypeError('Expected source of type String')
                else:   
                    self.from_txt(source)
            if source_type == 'edgelist':
                if type(source) != tuple or type(source) != list:
                    raise TypeError('Expected source of type Tuple or List')
                else:
                    self.from_list(source[0], source[1])
        else:
            print('No source recived! Initializing empty Graph.')
        
        
    def from_list(self, node_list, edge_list):    
        if node_list:
            for node in node_list:
                self.graph_dict[int(node)] = []
        if edge_list:
            for edge in edge_list:
                if int(edge[2]) < 0:
                    raise ValueError('Edge weight cannot be negative!')
                    break
                try:
                    self.add_edge(int(edge[0]), int(edge[1]), int(edge[2]))
                except IndexError:
                    print('Wrong edge data format!')
                    break
        else:
            self.graph_dict[node] = [Edge.Edge()]
                    
    def from_txt(self, source):
        edge_list = []
        node_list = []
        with open(source, 'r') as src:
            lines = [x.strip() for x in src]
            
            for line in lines:
                l = line.split()
                if len(l) >= 1:
                    node_list.append(l[0])
                    if len(l) == 3:
                        edge_list.append(l)
                if len(l) == 2 or len(l) > 3:
                    raise ValueError('Wrong data format!')
            
                
        
        self.from_list(node_list, edge_list)
    
    def add_edge(self, source, destination, weight):
        edge = Edge.Edge(source, destination, weight)
        
        if source not in self.graph_dict:
            self.graph_dict[source]=[edge]
        else:
            self.graph_dict[source].append(edge)
            
    def show_edges(self):
        
        
        for node in self.graph_dict.keys():
            for edge in self.graph_dict[node]:
                edge.print_edge()
            
            
            