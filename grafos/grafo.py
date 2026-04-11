from .vertice import Vertice

class Grafo:
    def __init__(self):
        self.vertices  = {}

    def adicionar_vertice(self, v):
        if isinstance(v, Vertice) and v.id not in self.vertices:
            self.vertices [v.id] = v
            return True
        else:
            return False

    def adicionar_aresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices [v1].adicionar_vizinho(v2)
            self.vertices [v2].adicionar_vizinho(v1)
            return True
        else:
            return False
        
    def get_vertices(self):
        return self.vertices.keys()
    
    def __iter__(self):
        return iter(self.vertices.values())