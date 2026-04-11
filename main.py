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

# dicionario de posicoes (x, y) na tela baseado nos jogadores do Mengão
posicoes_tela = {
    "Rossi": (100, 300),
    "Ayrton Lucas": (250, 100),
    "Léo Pereira": (250, 220),
    "Fabrício Bruno": (250, 380),
    "Varela": (250, 500),
    "Pulgar": (400, 300),
    "De La Cruz": (550, 200),
    "Arrascaeta": (550, 400),
    "Cebolinha": (700, 100),
    "Pedro": (700, 300),
    "Gerson": (700, 500)
}

cargos_jogadores = {
    "Rossi": "GOL",
    "Ayrton Lucas": "LE",
    "Léo Pereira": "ZAE",
    "Fabrício Bruno": "ZAD",
    "Varela": "LD",
    "Pulgar": "VOL",
    "De La Cruz": "MCE",
    "Arrascaeta": "MCD",
    "Cebolinha": "PTE",
    "Pedro": "CA",
    "Gerson": "PTD"
}

def montar_time():
    # Estrutura base trazida da main.py da Marys mas atualizada pro Flamengo
    grafo = Grafo()

    for jogador in posicoes_tela.keys():
        grafo.adicionar_vertice(Vertice(jogador))

    # pesos simulados
    grafo.adicionar_aresta("Rossi", "Léo Pereira", 10)
    grafo.adicionar_aresta("Rossi", "Fabrício Bruno", 10)
    grafo.adicionar_aresta("Fabrício Bruno", "Léo Pereira", 5)
    grafo.adicionar_aresta("Léo Pereira", "Ayrton Lucas", 15)
    grafo.adicionar_aresta("Fabrício Bruno", "Varela", 15)
    grafo.adicionar_aresta("Fabrício Bruno", "Pulgar", 20)
    grafo.adicionar_aresta("Léo Pereira", "Pulgar", 20)
    grafo.adicionar_aresta("Varela", "Arrascaeta", 25)
    grafo.adicionar_aresta("Ayrton Lucas", "De La Cruz", 25)
    grafo.adicionar_aresta("Arrascaeta", "Pulgar", 15)
    grafo.adicionar_aresta("De La Cruz", "Pulgar", 15)
    grafo.adicionar_aresta("De La Cruz", "Cebolinha", 30)
    grafo.adicionar_aresta("Arrascaeta", "Gerson", 30)
    grafo.adicionar_aresta("De La Cruz", "Pedro", 40)
    grafo.adicionar_aresta("Arrascaeta", "Pedro", 40)
    grafo.adicionar_aresta("Pedro", "Cebolinha", 35)
    grafo.adicionar_aresta("Pedro", "Gerson", 35)

    return grafo


# -> minha parte (algoritmos)

def get_min_distance_node(distances, unvisited):

    pass

def dijkstra(graph, start_name, end_name):
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
    pygame.display.set_caption("Simulador Dijkstra Tático - Mengão")
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

        # desenhar caminho do dijkstra (ex: Rossi para Pedro)
        # path = dijkstra(grafo, "Rossi", "Pedro")
        # se tiver caminho, pinta ele dps de desenhar tudo:
        # draw_shortest_path(screen, path, posicoes_tela)

        # renderizando jogadores 
        for v in grafo:
            pos = posicoes_tela[v.id]
            cargo = cargos_jogadores[v.id]
            # Sombra/Contorno
            pygame.draw.circle(screen, BLACK, pos, 17)
            # Jogador (Base Branca)
            pygame.draw.circle(screen, WHITE, pos, 15)
            
            # Texto da sigla no peito
            iniciais = "".join([p[0] for p in v.id.split(" ")])
            text = font_jogs.render(iniciais, True, RED)
            screen.blit(text, (pos[0]-8, pos[1]-6))
            
            # Texto do nome abaixo
            nome_completo = f"{v.id} ({cargo})"
            nome_text = font_jogs.render(nome_completo, True, WHITE)
            # Centraliza um pouco melhor o texto com base no tamanho novo
            screen.blit(nome_text, (pos[0]-35, pos[1]+20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()