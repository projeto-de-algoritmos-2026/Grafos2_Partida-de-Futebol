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
    # Etapa 3: Varre dists nao visitadas pra pegar o menor valor
    pass

def dijkstra(graph, start_name, end_name):
    # Etapa 2: logica principal de achar o caminho
    pass

def reconstruct_path(predecessors, start_name, end_name):
    # voltar a partir do ultimo no
    pass


# -> minha parte (visual/pygame)

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
    
    # Mantendo o print do terminal feito pela Marys para fins de validação
    print("Grafo:")
    for v in grafo:
        print(f"{v.id}: {v.vizinhos}")

    # Definindo a fonte visual
    font_jogs = pygame.font.Font(None, 18)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fundo e marcações do campo
        draw_soccer_field(screen)
        
        # desenhar as arestas gerais
        # draw_connections(screen, grafo, posicoes_tela)

        # desenhar caminho do dijkstra
        # path = dijkstra(grafo, "Goleiro", "Centroavante")
        # se tiver caminho, pinta ele dps de desenhar tudo:
        # draw_shortest_path(screen, path, posicoes_tela)

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