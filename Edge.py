class Edge:
    
    def __init__(self, source = None, destination = None, weight = None):
        self.source = source
        self.destination = destination
        self.weight = weight
    
    def print_edge(self):
        print(f'{self.source} ---> {self.destination} : w = {self.weight}')
