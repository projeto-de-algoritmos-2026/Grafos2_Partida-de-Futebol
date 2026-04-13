import pygame
from .constantes import WHITE, GREEN, GRAY, YELLOW, BLACK, LIGHT_GREEN
from ui.constantes import LARGURA, ALTURA, VERDE_CAMPO, BRANCO

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
            pygame.draw.line(screen, LIGHT_GREEN, pos_origem, pos_destino, 3)

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

def draw_ball(screen, pos):
    radius = 14
    # Sombra
    pygame.draw.circle(screen, (20, 20, 20), (pos[0] + 3, pos[1] + 4), radius)
    # Bola branca
    pygame.draw.circle(screen, WHITE, pos, radius)
    # Contorno preto
    pygame.draw.circle(screen, BLACK, pos, radius, 2)
    # Ponto central (pentágono central de uma bola de futebol)
    pygame.draw.circle(screen, BLACK, pos, 4)
    # Listras estilo bola de futebol
    cx, cy = pos
    pygame.draw.line(screen, BLACK, (cx - 6, cy - 6), (cx - 2, cy - 10), 1)
    pygame.draw.line(screen, BLACK, (cx + 6, cy - 6), (cx + 2, cy - 10), 1)
    pygame.draw.line(screen, BLACK, (cx - 8, cy + 2), (cx - 5, cy + 7), 1)
    pygame.draw.line(screen, BLACK, (cx + 8, cy + 2), (cx + 5, cy + 7), 1)

def desenha_campo(tela):
    tela.fill(VERDE_CAMPO)

    largura_linha = 5
    margin = 50 
    campo_largura = LARGURA - (2 * margin)
    campo_altura = ALTURA - (2 * margin)

    pygame.draw.rect(tela, BRANCO, (margin, margin, campo_largura, campo_altura), largura_linha)
    pygame.draw.line(tela, BRANCO, (LARGURA // 2, margin), (LARGURA // 2, ALTURA - margin), largura_linha)
    pygame.draw.circle(tela, BRANCO, (LARGURA // 2, ALTURA // 2), 100, largura_linha)
    pygame.draw.circle(tela, BRANCO, (LARGURA // 2, ALTURA // 2), 7)

    def desenhar_areas(lado):
        x_base = margin if lado == "esq" else LARGURA - margin
        grande_area_largura, grande_area_altura = 220, 400
        pygame.draw.rect(tela, BRANCO, (x_base if lado == "esq" else x_base - grande_area_largura, (ALTURA // 2) - (grande_area_altura // 2), grande_area_largura, grande_area_altura), largura_linha)

        pequena_area_largura, pequena_area_altura = 70, 150
        pygame.draw.rect(tela, BRANCO, (x_base if lado == "esq" else x_base - pequena_area_largura, (ALTURA // 2) - (pequena_area_altura // 2), pequena_area_largura, pequena_area_altura), largura_linha)

    desenhar_areas("esq")
    desenhar_areas("dir")