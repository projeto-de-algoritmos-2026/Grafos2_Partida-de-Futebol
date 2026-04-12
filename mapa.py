import pygame

LARGURA = 1500
ALTURA = 800
VERDE_CAMPO = (34, 139, 34)
BRANCO = (255, 255, 255)

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

rodando = True
clock = pygame.time.Clock()

while rodando:
    pos_mouse = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                
                for id_jogador, centro in posicoes.items():
                    img = imgs[id_jogador]
                    rect_jogador = img.get_rect(center=centro)
                    
                    if rect_jogador.collidepoint(pos_mouse):
                        print(f"O {id_jogador} foi clicado")

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

    for id_jogador, img in imgs.items():
        pos_centro = posicoes[id_jogador]
        rect_img = img.get_rect(center=pos_centro)
        tela.blit(img, rect_img)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()