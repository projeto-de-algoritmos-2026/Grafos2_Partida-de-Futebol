import pygame
from logica.grafos import Grafo, Vertice
from logica import dijkstra, reconstruct_path, calcular_distancia
from ui import draw_soccer_field, draw_connections, draw_shortest_path, desenha_campo, draw_ball
from ui.constantes import LARGURA, ALTURA, RED, PRETO

imgs = {}
tamanho_img = (120, 120)
tamanho_img_goleiro = (120, 100)

jogador_selecionado = None
offset_x, offset_y = 0, 0
no_origem = None
no_destino = None
caminho_calculado = []

# Animação da bola ao longo do caminho
animacao_progresso = 0.0   # varia de 0 até len(caminho)-1
VELOCIDADE_ANIMACAO = 0.04  # avanço por frame (~1.5s por segmento a 60fps)

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Partida de Futebol")

try:
    posicoes_nomes = ['CA', 'LD', 'LE', 'MD', 'ME', 'PD', 'PE', 'VOL', 'ZD', 'ZE']
    for nome in posicoes_nomes:
        imgs[nome] = pygame.transform.scale(pygame.image.load(f"assets/jogadores_brasil/{nome}.png"), tamanho_img)

    imgs['GL_A']= pygame.transform.scale(pygame.image.load("assets/jogadores_brasil/GL_A.png"), tamanho_img_goleiro)

except pygame.error as e:
    print(f"Erro ao carregar imagens: {e}")
    pygame.quit()
    exit()

posicoes = {
    'GL_A': (100, 400),
    'LD':   (400, 150), 
    'ZD':   (350, 320),
    'ZE':   (350, 480),
    'LE':   (400, 650),
    'VOL':  (650, 400), 
    'MD':   (850, 250),
    'ME':   (850, 550),
    'PD':   (1150, 150), 
    'CA':   (1300, 400), 
    'PE':   (1150, 650)
}

def montar_time(posicoes):
    grafo = Grafo()

    for nome_jogador in posicoes.keys():
        grafo.adicionar_vertice(Vertice(nome_jogador))

    def conectar(j1, j2):
        peso = calcular_distancia(posicoes[j1], posicoes[j2])

        grafo.adicionar_aresta(j1, j2, peso)

    conectar("GL_A", "ZE")
    conectar("GL_A", "ZD")
    conectar("ZD", "ZE")
    conectar("ZE", "LE")
    conectar("ZD", "LD")
    conectar("ZD", "VOL")
    conectar("ZE", "VOL")
    conectar("LD", "MD")
    conectar("LE", "ME")
    conectar("MD", "VOL")
    conectar("ME", "VOL")
    conectar("ME", "PE")
    conectar("MD", "PD")
    conectar("ME", "CA")
    conectar("MD", "CA")
    conectar("CA", "PE")
    conectar("CA", "PD")
    return grafo

grafo_oficial = montar_time(posicoes)

rodando = True
clock = pygame.time.Clock()

while rodando:
    pos_mouse = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                # Checa cliques nos jogadores
                for id_jogador, centro in posicoes.items():
                    img = imgs[id_jogador]
                    rect_jogador = img.get_rect(center=centro)
                    
                    if rect_jogador.collidepoint(pos_mouse):
                        if no_origem is None:
                            no_origem = id_jogador
                            no_destino = None
                            caminho_calculado = []
                            animacao_progresso = 0.0
                        elif no_destino is None and id_jogador != no_origem:
                            no_destino = id_jogador

                            pred = dijkstra(grafo_oficial, no_origem, no_destino)
                            caminho_calculado = reconstruct_path(pred, no_origem, no_destino)
                            animacao_progresso = 0.0
                        else:
                            # Reseta para uma nova busca começando do proximo clicado
                            no_origem = id_jogador
                            no_destino = None
                            caminho_calculado = []
                            animacao_progresso = 0.0

                        jogador_selecionado = id_jogador
                        offset_x = centro[0] - pos_mouse[0]
                        offset_y = centro[1] - pos_mouse[1]
                        break
        
        elif evento.type == pygame.MOUSEMOTION:
            if jogador_selecionado is not None:
                nova_x = pos_mouse[0] + offset_x
                nova_y = pos_mouse[1] + offset_y
                posicoes[jogador_selecionado] = (nova_x, nova_y)

        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                if jogador_selecionado:
                    grafo_oficial = montar_time(posicoes)
                    
                    if no_origem and no_destino:
                        pred = dijkstra(grafo_oficial, no_origem, no_destino)
                        caminho_calculado = reconstruct_path(pred, no_origem, no_destino)
                        animacao_progresso = 0.0
                    
                    jogador_selecionado = None
    desenha_campo(tela)

    draw_connections(tela, grafo_oficial, posicoes)
    draw_shortest_path(tela, caminho_calculado, posicoes)

    for id_jogador, img in imgs.items():
        pos_centro = posicoes[id_jogador]
        
        # se for a origem ou destino da animacao, poe um fundo highlight no jogador
        if id_jogador == no_origem:
            pygame.draw.circle(tela, RED, pos_centro, 70)
        elif id_jogador == no_destino:
            pygame.draw.circle(tela, PRETO, pos_centro, 70)
            
        rect_img = img.get_rect(center=pos_centro)
        tela.blit(img, rect_img)

    # Animação da bola percorrendo o caminho mais curto
    if len(caminho_calculado) > 1:
        num_segmentos = len(caminho_calculado) - 1
        animacao_progresso += VELOCIDADE_ANIMACAO
        if animacao_progresso >= num_segmentos:
            animacao_progresso = 0.0

        segmento = int(animacao_progresso)
        t = animacao_progresso - segmento

        no_a = caminho_calculado[segmento]
        no_b = caminho_calculado[segmento + 1]
        pos_a = posicoes[no_a]
        pos_b = posicoes[no_b]
        bola_x = int(pos_a[0] + (pos_b[0] - pos_a[0]) * t)
        bola_y = int(pos_a[1] + (pos_b[1] - pos_a[1]) * t)
        draw_ball(tela, (bola_x, bola_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()