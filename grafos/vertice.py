class Vertice:
    def __init__ (self, vertice_id):
        self.id = vertice_id
        self.vizinhos = {}

    def adicionar_vizinho(self, vizinho, peso):
        self.vizinhos[vizinho] = peso