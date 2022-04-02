from collection import deque

class DAG():
    def __init__(self):
        self.graph = {}
        
    def add(self, node, to=None):
        """Add node to the graph""" 
        if not node in self.graph:
            self.graph[node] = []
        if to:
            if not to in self.graph:
                self.graph[to] = []
            self.graph[node].append(to)
        # test for cyclicity
        sorted_nodes = self.sort()
        if len(sorted_nodes) != len(self.graph):
            raise Exception 
    
    def in_degrees(self):
        """Keep track of number of in-degrees for each node"""
        self.degrees = {}
        for node in self.graph: 
            if not node in self.degrees:
                self.degrees[node] = 0
            for linked_node in self.graph[node]:
                if linked_node not in self.degrees:
                    self.degrees[linked_node] = 0
                self.degrees[linked_node] += 1
                
    def sort(self):
        """Sort nodes in graph in order of dependencies (most depended to least depended)"""
        self.in_degrees()
        root_nodes = deque()
        for node in self.graph: 
            if self.degrees[node] == 0:
                root_nodes.append(node)  
        searched = [] 
        while root_nodes:
            node = root_nodes.popleft() 
            for pointer in self.graph[node]:
                self.degrees[pointer] -= 1
                if self.degrees[pointer] == 0:
                    root_nodes.append(pointer) 
            searched.append(node)
        return searched
    