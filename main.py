import pygame
import sys
from grafos import Grafo, Vertice

# configs basicas do pygame
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# dicionario de posicoes (x, y) na tela baseado na estrutura da Marys
posicoes_tela = {
    "Goleiro": (100, 300),
    "Lateral Esquerdo": (250, 100),
    "Zagueiro Esquerdo": (250, 220),
    "Zagueiro Direito": (250, 380),
    "Lateral Direito": (250, 500),
    "Volante": (400, 300),
    "Meia Esquerda": (550, 200),
    "Meia Direita": (550, 400),
    "Ponta Esquerda": (700, 100),
    "Centroavante": (700, 300),
    "Ponta Direita": (700, 500)
}

def montar_time():
    # Estrutura base trazida da main.py da Marys
    grafo = Grafo()

    for posicao in posicoes_tela.keys():
        grafo.adicionar_vertice(Vertice(posicao))

    # pesos mantidos simulados por ela pra podermos testar a logica do dijkstra dps
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


# -> minha parte (algoritmos)

def get_min_distance_node(distances, unvisited):
    # Etapa 3: Varre as distâncias dos nós ainda não visitados
    min_dist = float('infinity')
    min_node = None
    
    # Compara a distância salva pra descobrir qual tem o passe mais "rápido" até agora
    for no in unvisited:
        if distances[no] < min_dist:
            min_dist = distances[no]
            min_node = no
            
    return min_node

def dijkstra(graph, start_name, end_name):
    # logica principal de achar o caminho
    distancias = {v.id: float('infinity') for v in graph}
    distancias[start_name] = 0
    predecessores = {v.id: None for v in graph}
    
    nao_visitados = [v.id for v in graph]
    
    while nao_visitados:
        # Chama a função que tem no passo 3
        no_atual = get_min_distance_node(distancias, nao_visitados)
        
        if no_atual is None or distancias[no_atual] == float('infinity'):
            break # Não tem mais como avançar
            
        vertice_atual = graph.vertices[no_atual] # Puxando da estrutura da Marys
        
        # Simulação do relaxamento de arestas
        for vizinho_id, peso in vertice_atual.vizinhos.items():
            if vizinho_id in nao_visitados:
                nova_dist = distancias[no_atual] + peso
                if nova_dist < distancias[vizinho_id]:
                    distancias[vizinho_id] = nova_dist
                    predecessores[vizinho_id] = no_atual
                    
        nao_visitados.remove(no_atual)
        
        # Otimização: Se já chegou no destino, pode parar
        if no_atual == end_name:
            break
            
    return predecessores

def reconstruct_path(predecessors, start_name, end_name):
    # voltar a partir do ultimo no
    pass

def draw_soccer_field(screen):
    screen.fill(GREEN)
    
    # Campo exterior
    pygame.draw.rect(screen, WHITE, (50, 50, 700, 500), 3)
    
    # Linha do meio campo
    pygame.draw.line(screen, WHITE, (400, 50), (400, 550), 3)
    
    # Circulo central
    pygame.draw.circle(screen, WHITE, (400, 300), 70, 3)
    pygame.draw.circle(screen, WHITE, (400, 300), 5)
    
    # Grande área esquerda
    pygame.draw.rect(screen, WHITE, (50, 150, 150, 300), 3)
    # Pequena área esquerda
    pygame.draw.rect(screen, WHITE, (50, 225, 50, 150), 3)
    # Ponto do penalti esquerdo
    pygame.draw.circle(screen, WHITE, (160, 300), 4)
    # Meia lua esquerda
    pygame.draw.arc(screen, WHITE, (130, 250, 100, 100), -1.57, 1.57, 3)

    # Grande área direita
    pygame.draw.rect(screen, WHITE, (600, 150, 150, 300), 3)
    # Pequena área direita
    pygame.draw.rect(screen, WHITE, (700, 225, 50, 150), 3)
    # Ponto do penalti direito
    pygame.draw.circle(screen, WHITE, (640, 300), 4)
    # Meia lua direita
    pygame.draw.arc(screen, WHITE, (570, 250, 100, 100), 1.57, 4.71, 3)


def draw_connections(screen, graph, pos_dict):
    # desenha as linhas cinzas pra mostrar os passes que da pra fazer
    pass

def draw_shortest_path(screen, path, pos_dict):
    # pinta a linha por cima do caminho encontrado
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulador Dijkstra Tático")
    clock = pygame.time.Clock()

    grafo = montar_time()

    # print("Grafo:")
    # for v in grafo:
    #     print(f"{v.id}: {v.vizinhos}")

    # print("\n--- TESTE DO DIJKSTRA (Etapas 1, 2 e 3) ---")
    # teste_predecessores = dijkstra(grafo, "Goleiro", "Centroavante")
    # print("O algoritmo rodou com sucesso! Veja quem antecede quem no caminho ideal:")
    # for no_destino, origem_anterior in teste_predecessores.items():
    #     print(f"Para o passe chegar em '{no_destino}', a bola veio de: '{origem_anterior}'")

    # Definindo a fonte visual
    font_jogs = pygame.font.Font(None, 18)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fundo e marcações do campo
        draw_soccer_field(screen)

        # renderizando jogadores 
        for v in grafo:
            pos = posicoes_tela[v.id]
            # Sombra/Contorno
            pygame.draw.circle(screen, BLACK, pos, 17)
            # Jogador (Base Branca)
            pygame.draw.circle(screen, WHITE, pos, 15)
            
            # Sigla no peito baseada na posicao real ("GE" em vez de "Rossi")
            partes_nome = v.id.split(" ")
            if len(partes_nome) == 1:
                # ex: "Goleiro" -> "G"
                iniciais = partes_nome[0][:1]
            else:
                # ex: "Zagueiro Esquerdo" -> "ZE"
                iniciais = partes_nome[0][:1] + partes_nome[1][:1]
                
            text = font_jogs.render(iniciais, True, RED)
            screen.blit(text, (pos[0]-6, pos[1]-6))
            
            # Texto da posicao completa abaixo
            nome_text = font_jogs.render(v.id, True, WHITE)
            screen.blit(nome_text, (pos[0]-25, pos[1]+20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()