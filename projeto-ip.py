import pygame
import random
from pygame.locals import *
pygame.init()

pygame.mixer.init()
icone = pygame.image.load('c:/Users/kauã/OneDrive/Área de Trabalho/Projeto IP/icone.png')
pygame.display.set_icon(icone)

som_efeito = pygame.mixer.Sound('c:/Users/kauã/OneDrive/Área de Trabalho/Projeto IP/efeito-maca.mp3')
som_derrota = pygame.mixer.Sound('c:/Users/kauã/OneDrive/Área de Trabalho/Projeto IP/derrota.mp3')

TAMANHO_JANELA = (800, 600)
TAMANHO_PIXEL = 10

pygame.init()
tela = pygame.display.set_mode(TAMANHO_JANELA)
pygame.display.set_caption('Cobra Rush')

fonte = pygame.font.SysFont('pressstart2p', 20)

PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
VERDE_ESCURO = (0, 100, 0)

def posicao_aleatoria():
    x = random.randint(0, TAMANHO_JANELA[0] - TAMANHO_PIXEL)
    y = random.randint(0, TAMANHO_JANELA[1] - TAMANHO_PIXEL)
    return (x // TAMANHO_PIXEL * TAMANHO_PIXEL, y // TAMANHO_PIXEL * TAMANHO_PIXEL)

def exibir_pontuacao(pontuacao):
    texto = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    tela.blit(texto, (10, 10))

def tela_game_over(pontuacao):
    img_gameover = pygame.image.load('c:/Users/kauã/OneDrive/Área de Trabalho/Projeto IP/gameover.png')
    img_gameover = pygame.transform.scale(img_gameover, TAMANHO_JANELA)
    tela.blit(img_gameover, (0, 0))
    texto_game_over = fonte.render("GAME OVER", True, VERMELHO)
    texto_pontuacao = fonte.render(f"Pontuação Final: {pontuacao}", True, BRANCO)
    texto_restart = fonte.render("Pressione R para Reiniciar", True, BRANCO)
    texto_menu = fonte.render("Pressione M para Menu", True, BRANCO)

    tela.blit(texto_game_over, (TAMANHO_JANELA[0] // 2 - texto_game_over.get_width() // 2, TAMANHO_JANELA[1] // 3))
    tela.blit(texto_pontuacao, (TAMANHO_JANELA[0] // 2 - texto_pontuacao.get_width() // 2, TAMANHO_JANELA[1] // 2))
    tela.blit(texto_restart, (TAMANHO_JANELA[0] // 2 - texto_restart.get_width() // 2, TAMANHO_JANELA[1] // 2 + 40))
    tela.blit(texto_menu, (TAMANHO_JANELA[0] // 2 - texto_menu.get_width() // 2, TAMANHO_JANELA[1] // 2 + 80))

    pygame.display.update()

    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                quit()
            if evento.type == KEYDOWN:
                if evento.key == K_r:
                    return True
                if evento.key == K_m:
                    menu_inicial()
                    return False

def menu_inicial():
    imagem_fundo = pygame.image.load('c:/Users/kauã/OneDrive/Área de Trabalho/Projeto IP/menu.png')
    imagem_fundo = pygame.transform.scale(imagem_fundo, TAMANHO_JANELA)
    tela.blit(imagem_fundo, (0, 0))
    iniciar = fonte.render("1. Iniciar Jogo", True, BRANCO)
    configuracoes = fonte.render("2. Configurações", True, BRANCO)
    sair = fonte.render("3. Sair", True, BRANCO)

    tela.blit(iniciar, (TAMANHO_JANELA[0] // 2 - iniciar.get_width() // 2, TAMANHO_JANELA[1] // 2 - 30))
    tela.blit(configuracoes, (TAMANHO_JANELA[0] // 2 - configuracoes.get_width() // 2, TAMANHO_JANELA[1] // 2))
    tela.blit(sair, (TAMANHO_JANELA[0] // 2 - sair.get_width() // 2, TAMANHO_JANELA[1] // 2 + 30))

    pygame.display.update()

    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                quit()
            if evento.type == KEYDOWN:
                if evento.key == K_1:
                    return
                if evento.key == K_2:
                    menu_configuracoes()
                if evento.key == K_3:
                    pygame.quit()
                    quit()

def menu_configuracoes():
    global velocidade, range_obstaculos
    tela_config = pygame.image.load('c:/Users/kauã/OneDrive/Área de Trabalho/Projeto IP/config.png')
    tela_config = pygame.transform.scale(tela_config, TAMANHO_JANELA)
    tela.blit(tela_config, (0, 0))
    titulo = fonte.render("Configurações", True, BRANCO)
    facil = fonte.render("1. Fácil", True, BRANCO)
    medio = fonte.render("2. Médio", True, BRANCO)
    dificil = fonte.render("3. Difícil", True, BRANCO)
    voltar = fonte.render("4. Voltar", True, BRANCO)

    tela.blit(titulo, (TAMANHO_JANELA[0] // 2 - titulo.get_width() // 2, TAMANHO_JANELA[1] // 4))
    tela.blit(facil, (TAMANHO_JANELA[0] // 2 - facil.get_width() // 2, TAMANHO_JANELA[1] // 2 - 40))
    tela.blit(medio, (TAMANHO_JANELA[0] // 2 - medio.get_width() // 2, TAMANHO_JANELA[1] // 2 - 10))
    tela.blit(dificil, (TAMANHO_JANELA[0] // 2 - dificil.get_width() // 2, TAMANHO_JANELA[1] // 2 + 20))
    tela.blit(voltar, (TAMANHO_JANELA[0] // 2 - voltar.get_width() // 2, TAMANHO_JANELA[1] // 2 + 60))

    pygame.display.update()

    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                quit()
            if evento.type == KEYDOWN:
                if evento.key == K_1:
                    velocidade = 10
                    range_obstaculos = 10
                    menu_inicial()
                    return
                if evento.key == K_2:
                    velocidade = 15
                    range_obstaculos = 20
                    menu_inicial()
                    return
                if evento.key == K_3:
                    velocidade = 20
                    range_obstaculos = 30
                    menu_inicial()
                    return
                if evento.key == K_4:
                    return

def ler_pontuacao_mais_alta():
    try:
        with open('high_score.txt', 'r') as arquivo:
            return int(arquivo.read())
    except FileNotFoundError:
        return 0

def escrever_pontuacao_mais_alta(pontuacao):
    with open('high_score.txt', 'w') as arquivo:
        arquivo.write(str(pontuacao))

def atualizar_pontuacao_mais_alta(pontuacao):
    pontuacao_mais_alta = ler_pontuacao_mais_alta()
    if pontuacao > pontuacao_mais_alta:
        escrever_pontuacao_mais_alta(pontuacao)
        return True
    return False

velocidade = 15
range_obstaculos = 20
menu_inicial()

pos_cobra = [(250, 50), (260, 50), (270, 50)]
direcao_cobra = K_LEFT
pos_maca = posicao_aleatoria()
pontuacao = 0

superficie_cobra = pygame.Surface((TAMANHO_PIXEL, TAMANHO_PIXEL))
superficie_cobra.fill(VERDE)

superficie_maca = pygame.Surface((TAMANHO_PIXEL, TAMANHO_PIXEL))
superficie_maca.fill(VERMELHO)

obstaculos = []
for _ in range(range_obstaculos):
    obstaculos.append(posicao_aleatoria())

macadaourada_ativa = False
valor_macadaourada = 5
chance_macadaourada = 0.1
tempo_macadaourada = 5000
superficie_macadaourada = pygame.Surface((TAMANHO_PIXEL, TAMANHO_PIXEL))
superficie_macadaourada.fill((255, 215, 0))

while True:
    pygame.time.Clock().tick(velocidade)
    tela.fill(VERDE_ESCURO)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()
        if evento.type == KEYDOWN:
            if evento.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                direcao_cobra = evento.key

    if direcao_cobra == K_UP:
        nova_cabeca = (pos_cobra[0][0], pos_cobra[0][1] - TAMANHO_PIXEL)
    elif direcao_cobra == K_DOWN:
        nova_cabeca = (pos_cobra[0][0], pos_cobra[0][1] + TAMANHO_PIXEL)
    elif direcao_cobra == K_LEFT:
        nova_cabeca = (pos_cobra[0][0] - TAMANHO_PIXEL, pos_cobra[0][1])
    else:
        nova_cabeca = (pos_cobra[0][0] + TAMANHO_PIXEL, pos_cobra[0][1])

    pos_cobra.insert(0, nova_cabeca)

    if nova_cabeca == pos_maca:
        som_efeito.play()
        if macadaourada_ativa:
            pontuacao += valor_macadaourada
        else:
            pontuacao += 1
        pos_maca = posicao_aleatoria()
        if random.random() < chance_macadaourada:
            macadaourada_ativa = True
            tempo_macadaourada_inicio = pygame.time.get_ticks()
    else:
        pos_cobra.pop()

    if macadaourada_ativa and pygame.time.get_ticks() - tempo_macadaourada_inicio > tempo_macadaourada:
        macadaourada_ativa = False

    if (nova_cabeca in pos_cobra[1:] or 
        not (0 <= nova_cabeca[0] < TAMANHO_JANELA[0] and 0 <= nova_cabeca[1] < TAMANHO_JANELA[1]) or 
        nova_cabeca in obstaculos):
        som_derrota.play()
        if tela_game_over(pontuacao):
            pos_cobra = [(250, 50), (260, 50), (270, 50)]
            direcao_cobra = K_LEFT
            pontuacao = 0
            pos_maca = posicao_aleatoria()
            macadaourada_ativa = False
            obstaculos = []
            for _ in range(range_obstaculos):
                obstaculos.append(posicao_aleatoria())

    for i, pos in enumerate(pos_cobra):
        tela.blit(superficie_cobra, pos)
        if i == 0:
            pygame.draw.circle(tela, BRANCO, (pos[0] + 3, pos[1] + 3), 2)
            pygame.draw.circle(tela, BRANCO, (pos[0] + 7, pos[1] + 3), 2)

    if macadaourada_ativa:
        tela.blit(superficie_macadaourada, pos_maca)
    else:
        tela.blit(superficie_maca, pos_maca)

    for obstaculo in obstaculos:
        pygame.draw.rect(tela, PRETO, (obstaculo[0], obstaculo[1], TAMANHO_PIXEL, TAMANHO_PIXEL))

    exibir_pontuacao(pontuacao)
    texto_high_score = fonte.render(f"High Score: {ler_pontuacao_mais_alta()}", True, BRANCO)
    tela.blit(texto_high_score, (10, 40))
    pygame.display.update()

    if pontuacao > ler_pontuacao_mais_alta():
        atualizar_pontuacao_mais_alta(pontuacao)