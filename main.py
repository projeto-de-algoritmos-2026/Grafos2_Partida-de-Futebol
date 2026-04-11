from grafos import Grafo, Vertice

def montar_time():
    grafo = Grafo()

    posicoes = [
        "Goleiro", 
        "Lateral Esquerdo", 
        "Zagueiro Esquerdo", 
        "Zagueiro Direito", 
        "Lateral Direito", 
        "Volante", 
        "Meia Direita", 
        "Meia Esquerda", 
        "Ponta Esquerda", 
        "Centroavante", 
        "Ponta Direita"
    ]

    for posicao in posicoes:
            grafo.adicionar_vertice(Vertice(posicao))

    grafo.adicionar_aresta("Goleiro", "Zagueiro Esquerdo", 10)
    grafo.adicionar_aresta("Goleiro", "Zagueiro Direito", 10)
    grafo.adicionar_aresta("Zagueiro Direito", "Zagueiro Esquerdo", 5)

    grafo.adicionar_aresta("Zagueiro Esquerdo", "Lateral Esquerdo", 15)
    grafo.adicionar_aresta("Zagueiro Direito", "Lateral Direito", 15)

    grafo.adicionar_aresta("Zagueiro Direito", "Volante", 20)
    grafo.adicionar_aresta("Zagueiro Esquerdo", "Volante", 20)

    grafo.adicionar_aresta("Lateral Direito", "Meia Direita", 25)
    grafo.adicionar_aresta("Lateral Esquerdo", "Meia Esquerda", 25)

    grafo.adicionar_aresta("Meia Direita", "Volante", 15)
    grafo.adicionar_aresta("Meia Esquerda", "Volante", 15)

    grafo.adicionar_aresta("Meia Esquerda", "Ponta Esquerda", 30)
    grafo.adicionar_aresta("Meia Direita", "Ponta Direita", 30)

    grafo.adicionar_aresta("Meia Esquerda", "Centroavante", 40)
    grafo.adicionar_aresta("Meia Direita", "Centroavante", 40)

    grafo.adicionar_aresta("Centroavante", "Ponta Esquerda", 35)
    grafo.adicionar_aresta("Centroavante", "Ponta Direita", 35)

    return grafo

if __name__ == "__main__":
    meu_time = montar_time()
    
    print("Grafo:")
    for v in meu_time:
        print(f"{v.id}: {v.vizinhos}")