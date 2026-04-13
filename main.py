import pygame
import sys
from logica.grafos import Grafo, Vertice
from logica import dijkstra, reconstruct_path
from ui import draw_soccer_field, draw_connections, draw_shortest_path
from ui.constantes import WIDTH, WHITE, GREEN, DARK_GREEN, GRAY, RED, YELLOW, BLUE, BLACK

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

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulador Dijkstra Tático")
    clock = pygame.time.Clock()

    grafo = montar_time()

    # Definindo a fonte visual
    font_jogs = pygame.font.Font(None, 18)

    # PROCESSAMENTO DO CÉREBRO: O Dijkstra roda 1 única vez antes do Pygame iniciar de fato pros 60 FPS
    predecessores_resultado = dijkstra(grafo, "Goleiro", "Centroavante")
    caminho_perfeito = reconstruct_path(predecessores_resultado, "Goleiro", "Centroavante")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fundo e marcações do campo
        draw_soccer_field(screen)

        # Desenha as arestas cinzas mostrando estrutura de passe (Commit 5)
        draw_connections(screen, grafo, posicoes_tela)
        
        # Desenha o caminho genial em amarelo destacando por cima das linhas apagadas!
        draw_shortest_path(screen, caminho_perfeito, posicoes_tela)

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