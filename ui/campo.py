import pygame
from .constantes import WHITE, GREEN, GRAY, YELLOW, BLACK

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
    for vertice in graph:
        pos_origem = pos_dict[vertice.id]
        for vizinho_id in vertice.vizinhos.keys():
            pos_destino = pos_dict[vizinho_id]
            pygame.draw.line(screen, GRAY, pos_origem, pos_destino, 2)

def draw_shortest_path(screen, path, pos_dict):
    # destaque do Caminho Ótimo
    if path:
        for i in range(len(path) - 1):
            no_atual = path[i]
            proximo_no = path[i+1]
            
            pos_origem = pos_dict[no_atual]
            pos_destino = pos_dict[proximo_no]
            
            # Linha amarela super grossa com borda
            pygame.draw.line(screen, BLACK, pos_origem, pos_destino, 8)
            pygame.draw.line(screen, YELLOW, pos_origem, pos_destino, 4)
