import pygame
from logica.grafos import Grafo, Vertice
from logica import dijkstra, reconstruct_path
from ui import draw_soccer_field, draw_connections, draw_shortest_path, desenha_campo
from ui.constantes import LARGURA, ALTURA, RED, PRETO

imgs = {}
tamanho_img = (120, 120)
tamanho_img_goleiro = (120, 100)

no_origem = None
no_destino = None
caminho_calculado = []

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

def montar_time(posicoes_dit):
    grafo = Grafo()
    for pos in posicoes_dit.keys():
        grafo.adicionar_vertice(Vertice(pos))

    grafo.adicionar_aresta("GL_A", "ZE", 10)
    grafo.adicionar_aresta("GL_A", "ZD", 10)
    grafo.adicionar_aresta("ZD", "ZE", 5)
    grafo.adicionar_aresta("ZE", "LE", 15)
    grafo.adicionar_aresta("ZD", "LD", 15)
    grafo.adicionar_aresta("ZD", "VOL", 20)
    grafo.adicionar_aresta("ZE", "VOL", 20)
    grafo.adicionar_aresta("LD", "MD", 25)
    grafo.adicionar_aresta("LE", "ME", 25)
    grafo.adicionar_aresta("MD", "VOL", 15)
    grafo.adicionar_aresta("ME", "VOL", 15)
    grafo.adicionar_aresta("ME", "PE", 30)
    grafo.adicionar_aresta("MD", "PD", 30)
    grafo.adicionar_aresta("ME", "CA", 40)
    grafo.adicionar_aresta("MD", "CA", 40)
    grafo.adicionar_aresta("CA", "PE", 35)
    grafo.adicionar_aresta("CA", "PD", 35)
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
                        elif no_destino is None and id_jogador != no_origem:
                            no_destino = id_jogador

                            pred = dijkstra(grafo_oficial, no_origem, no_destino)
                            caminho_calculado = reconstruct_path(pred, no_origem, no_destino)
                        else:
                            # Reseta para uma nova busca começando do proximo clicado
                            no_origem = id_jogador
                            no_destino = None
                            caminho_calculado = []

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

    pygame.display.flip()
    clock.tick(60)

pygame.quit()