import pygame
from grafos import Grafo, Vertice

LARGURA = 1500
ALTURA = 800
VERDE_CAMPO = (34, 139, 34)
BRANCO = (255, 255, 255)
CINZA = (150, 150, 150)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Partida de Futebol")

imgs = {}
tamanho_img = (120, 120)
tamanho_img_goleiro = (120, 100)

try:
    posicoes_nomes = ['CA', 'LD', 'LE', 'MD', 'ME', 'PD', 'PE', 'VOL', 'ZD', 'ZE']
    for nome in posicoes_nomes:
        imgs[nome] = pygame.transform.scale(pygame.image.load(f"src/jogadores_brasil/{nome}.png"), tamanho_img)

    imgs['GL_A']= pygame.transform.scale(pygame.image.load("src/jogadores_brasil/GL_A.png"), tamanho_img_goleiro)

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

# -> ALGORITMOS (Cerebro Dijkstra)
def get_min_distance_node(distances, unvisited):
    min_dist = float('infinity')
    min_node = None
    for no in unvisited:
        if distances[no] < min_dist:
            min_dist = distances[no]
            min_node = no
    return min_node

def dijkstra(graph, start_name, end_name=None):
    distancias = {v.id: float('infinity') for v in graph}
    distancias[start_name] = 0
    predecessores = {v.id: None for v in graph}
    nao_visitados = [v.id for v in graph]
    
    while nao_visitados:
        no_atual = get_min_distance_node(distancias, nao_visitados)
        if no_atual is None or distancias[no_atual] == float('infinity'):
            break 
            
        vertice_atual = graph.vertices[no_atual]
        for vizinho_id, peso in vertice_atual.vizinhos.items():
            if vizinho_id in nao_visitados:
                nova_dist = distancias[no_atual] + peso
                if nova_dist < distancias[vizinho_id]:
                    distancias[vizinho_id] = nova_dist
                    predecessores[vizinho_id] = no_atual
                    
        nao_visitados.remove(no_atual)
        if end_name and no_atual == end_name:
            break
    return predecessores

def reconstruct_path(predecessors, start_name, end_name):
    caminho_tracado = []
    no_atual = end_name
    while no_atual is not None:
        caminho_tracado.insert(0, no_atual)
        if no_atual == start_name:
            break
        no_atual = predecessors.get(no_atual)
        
    if caminho_tracado[0] == start_name:
        return caminho_tracado
    else:
        return []

# -> VISUAIS 
def draw_connections(screen, graph, pos_dict):
    for vertice in graph:
        pos_origem = pos_dict[vertice.id]
        for vizinho_id in vertice.vizinhos.keys():
            pos_destino = pos_dict[vizinho_id]
            pygame.draw.line(screen, CINZA, pos_origem, pos_destino, 2)

def draw_shortest_path(screen, path, pos_dict):
    if path:
        for i in range(len(path) - 1):
            no_atual = path[i]
            proximo_no = path[i+1]
            pos_origem = pos_dict[no_atual]
            pos_destino = pos_dict[proximo_no]
            # Linha amarela super grossa com borda
            pygame.draw.line(screen, PRETO, pos_origem, pos_destino, 12)
            pygame.draw.line(screen, AMARELO, pos_origem, pos_destino, 8)

# VARIAVEIS DE ESTADO DA INTERACAO
no_origem = None
no_destino = None
caminho_calculado = []

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
                            # Dispara o algoritmo pesado 
                            pred = dijkstra(grafo_oficial, no_origem, no_destino)
                            caminho_calculado = reconstruct_path(pred, no_origem, no_destino)
                        else:
                            # Reseta para uma nova busca começando do proximo clicado
                            no_origem = id_jogador
                            no_destino = None
                            caminho_calculado = []

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

    # Desenha o passaporte visual de fundo
    draw_connections(tela, grafo_oficial, posicoes)
    
    # Desenha o caminho se ele tiver sido calculado!
    draw_shortest_path(tela, caminho_calculado, posicoes)

    for id_jogador, img in imgs.items():
        pos_centro = posicoes[id_jogador]
        
        # se for a origem ou destino da animacao, poe um fundo highlight no jogador
        if id_jogador == no_origem:
            pygame.draw.circle(tela, AMARELO, pos_centro, 65)
        elif id_jogador == no_destino:
            pygame.draw.circle(tela, PRETO, pos_centro, 65)
            
        rect_img = img.get_rect(center=pos_centro)
        tela.blit(img, rect_img)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()