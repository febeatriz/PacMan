
import pygame # biblioteca pygame
import cria_objeto
class objeto(pygame.sprite.Sprite):
    def __init__(self,imagem,posicao):
        super().__init__()
        # imagem associada ao sprite
        self.image=imagem
        # retângulo de colisão do sprite
        self.rect=self.image.get_rect()
        # posição do sprite (x,y)
        self.rect.topleft=posicao
        # Variável de controle para verificar se o sprite sofreu kill
        self.killed = False
    def mudar_imagem(self,nova_imagem):
        self.image = nova_imagem
        # Atualiza o retângulo de colisão
        self.rect = self.image.get_rect(center=self.rect.center)
    def kill(self):
        super().kill()

pygame.init() # iniciando a biblioteca

# criando tela para desenhar
tela=pygame.display.set_mode([796,708])

# neste caso as dimensões da tela são as mesmas da imagem que será carregada como fundo
# carregando a imagem de fundo
caminho='labirinto3.jpg'

background=pygame.image.load(caminho)

rodando=True # variável responssável pela execução do jogo

# carregando as imagens do personagem
pacman=pygame.image.load("pacMan.gif")
pacman2=pygame.image.load("pacman2.gif")
pacman3=pygame.image.load("pacman3.gif")
pacman4=pygame.image.load("pacman4.gif")

# diminuindo a escala do pacman
pacman=pygame.transform.scale(pacman,(40,40))
pacman2=pygame.transform.scale(pacman2,(40,40))
pacman3=pygame.transform.scale(pacman3,(40,40))
pacman4=pygame.transform.scale(pacman4,(40,40))

# carregando as imagens dos fantasmas
samurai=pygame.image.load("samurai.png")
soldado=pygame.image.load("army.png")
pirata=pygame.image.load("pirate.png")
alien=pygame.image.load("alien.png")
guerreiro=pygame.image.load("guerreiro.png")


lanche=pygame.image.load("whopper.png")
lanche2 = pygame.image.load("mcChicken.png")
lanche3 = pygame.image.load("bigmac.png")
lanche4 = pygame.image.load("b_halloween.png")
lanche5 = pygame.image.load("triplo.png")

saida1=pygame.image.load("saida.png")

# redimensionando as imagens dos fantasmas para 60 por 60 pixels
samurai2=pygame.transform.scale(samurai,(60,60))
soldado2=pygame.transform.scale(soldado,(60,60))
pirata2=pygame.transform.scale(pirata,(60,60))
alien2=pygame.transform.scale(alien,(60,60))
guerreiro2=pygame.transform.scale(guerreiro,(60,60))

whopper=pygame.transform.scale(lanche,(60,60))
chicken = pygame.transform.scale(lanche2,(85,60))
bigmac = pygame.transform.scale(lanche3,(60,60))
halloween = pygame.transform.scale(lanche4,(75,60))
triplo = pygame.transform.scale(lanche5,(70,50))

saida2=pygame.transform.scale(saida1,(80,60))

# criando sprites e posicionando(laterais, altura)
sprite0=cria_objeto.objeto(pacman,(1,1))
sprite1=cria_objeto.objeto(samurai2,(333,5))
sprite2=cria_objeto.objeto(soldado2,(465,225))
sprite3=cria_objeto.objeto(pirata2,(5,225))
sprite4=cria_objeto.objeto(alien2,(5,335))
sprite5=cria_objeto.objeto(guerreiro2,(295,545))

sprite6=cria_objeto.objeto(whopper,(355,5))
sprite7=cria_objeto.objeto(chicken,(200,225))
sprite8=cria_objeto.objeto(bigmac,(180,440))
sprite9=cria_objeto.objeto(halloween,(400,330))
sprite10 = cria_objeto.objeto(triplo,(670,440))

saida=cria_objeto.objeto(saida2,(720,650))


grupo_sprites=pygame.sprite.Group(sprite0,sprite1,sprite2,sprite3,sprite4,sprite5,sprite6,sprite7,sprite8, sprite9, sprite10, saida)
placar=0      # variável de placar
vida = 3

# Carrega a música de fundo
pygame.mixer.music.load('musicafundo.mp3')
# Define o volume da música (opcional)
pygame.mixer.music.set_volume(0.5) # Um valor entre 0.0 e 1.0
# Inicia a reprodução da música de fundo
# O argumento -1 faz com que a música repita continuamente
pygame.mixer.music.play(-1)

# variáveis para o controle da direção dos fantasmas
dir_samurai=1    # se for 1, anda para a direita
dir_soldado=1    # se for -1, anda para a esquerda
dir_pirata=1
dir_alien=1
dir_guerreiro=1

# posição inicial do pacman

x=1
y=1

while rodando: # o loop funciona enquanto a variável rodando for True
    for event in pygame.event.get(): # testando se alguma tecla foi pressionada
        if event.type==pygame.QUIT: # se clicou para sair do jogo
            rodando=False # quebra o laço while
            
    tela.blit(background,(0,0)) # desenha a tela de fundo

    keys = pygame.key.get_pressed()  # obtendo a tecla pressionada

    if keys[pygame.K_LEFT]:   # tecla esquerda
       cor=tela.get_at((x-1,y))    # lê a cor
       cor2=tela.get_at((x-1,y+39))
       sprite0.mudar_imagem(pacman2)

       if (cor.r<=40) and (cor2.r<=40): # se for escuro
           x=x-1    # decrementa x
           if x<1:  # se x for menor que 1
               x=1  # limita x para não sair da tela
    if keys[pygame.K_RIGHT]: # algoritmo análogo para as demais teclas
        cor=tela.get_at((x+40,y))
        cor2=tela.get_at((x+40,y+39))
        sprite0.mudar_imagem(pacman)
        if (cor.r<=40) and (cor2.r<=40):
            x=x+1
            if x>755:
                x=755
    if keys[pygame.K_UP]:
        cor=tela.get_at((x,y-1))
        cor2=tela.get_at((x+39,y-1))
        sprite0.mudar_imagem(pacman3)
        if (cor.r<=40) and (cor2.r<=40):
            y=y-1
            if y<1:
                y=1
    if keys[pygame.K_DOWN]:
        cor=tela.get_at((x,y+40))
        cor2=tela.get_at((x+39,y+40))
        sprite0.mudar_imagem(pacman4)
        if (cor.r<=40) and (cor2.r<=40):
            y=y+1
            if y>667:
                y=667


    # atualizando a posição do pacman
    sprite0.rect.x=x
    sprite0.rect.y=y

    # movimentando os fantasmas
    sprite1.rect.x+=dir_samurai  # sprite 1 é o samurai
                                 # se dir_samurai for 1
                                 # o valor da coordenada x
                                 # aumenta em uma unidade
                                 # se dir_samurai for -1
                                 # o valor da coordenada x
                                 # diminui em uma unidade
    if sprite1.rect.x>710:   # se chegou no extremo da tela
        dir_samurai=-1       # muda o valor para -1
    elif sprite1.rect.x<320: # se chegou em um outro extremo   
        dir_samurai=1        # muda o valor para 1

    # Atividade: implementar movimento nos outros fantasmas

    sprite2.rect.x+=dir_soldado  
    if sprite2.rect.x>710:   
        dir_soldado=-1       
    elif sprite2.rect.x<450:   
        dir_soldado=1

    sprite3.rect.x+=dir_pirata  
    if sprite3.rect.x>365:   
        dir_pirata=-1       
    elif sprite3.rect.x<1:   
        dir_pirata=1

    sprite4.rect.x+=dir_alien  
    if sprite4.rect.x>710:   
        dir_alien=-1       
    elif sprite4.rect.x<1:   
        dir_alien=1

    sprite5.rect.x+=dir_guerreiro  
    if sprite5.rect.x>710:   
        dir_guerreiro=-1       
    elif sprite5.rect.x<295:   
        dir_guerreiro=1

    # detectando a colisão
    if pygame.sprite.collide_mask(sprite0,sprite1):
        sprite0.rect.x=1 # manda o pacman para o início do labirinto
        sprite0.rect.y=1
        vida-=1
        x=1
        y=1
    elif pygame.sprite.collide_mask(sprite0,sprite2):
        sprite0.rect.x=1 # manda o pacman para o início do labirinto
        sprite0.rect.y=1
        vida-=1
        x=1
        y=1
    elif pygame.sprite.collide_mask(sprite0,sprite3):
        sprite0.rect.x=1 # manda o pacman para o início do labirinto
        sprite0.rect.y=1
        vida-=1
        x=1
        y=1
    elif pygame.sprite.collide_mask(sprite0,sprite4):
        sprite0.rect.x=1 # manda o pacman para o início do labirinto
        sprite0.rect.y=1
        vida-=1
        x=1
        y=1
    elif pygame.sprite.collide_mask(sprite0,sprite5):
        sprite0.rect.x=1 # manda o pacman para o início do labirinto
        sprite0.rect.y=1
        vida -=1
        x=1
        y=1

    if pygame.sprite.collide_mask(sprite0,sprite6):  # verificando se o pacman
        placar+=1    # incrementa o placar           # colidiu com o lanche
        sprite6.rect.x=1200  # manda o lanche para uma posição x=1200 (fora da tela)

    if pygame.sprite.collide_mask(sprite0,sprite7):  # verificando se o pacman
        placar+=1    # incrementa o placar           # colidiu com o lanche
        sprite7.rect.x=1200  # manda o lanche para uma posição x=1200 (fora da tela)

    if pygame.sprite.collide_mask(sprite0,sprite8):  # verificando se o pacman
        placar+=1    # incrementa o placar           # colidiu com o lanche
        sprite8.rect.x=1200

    if pygame.sprite.collide_mask(sprite0,sprite9):  # verificando se o pacman
        placar+=1    # incrementa o placar           # colidiu com o lanche
        sprite9.rect.x=1200

    if pygame.sprite.collide_mask(sprite0, sprite10):
        placar+=1
        sprite10.rect.x=1200

    if pygame.sprite.collide_mask(sprite0,saida):  # verificando se o pacman
        if placar>2:
            caminho='labirinto4b.jpg'
            background=pygame.image.load(caminho)  
            sprite0.rect.x=1 # manda o pacman para o início do labirinto
            sprite0.rect.y=1
            x=1
            y=1
    if vida == 0:
        caminho = 'gameOver.png'
        background = pygame.image.load(caminho) #os fantasmas e hamburger ainda estao na tela
        sprite0.rect.x=1200
        sprite1.rect.x=1200
        sprite2.rect.x=1200
        sprite3.rect.x=1200
        sprite4.rect.x=1200
        sprite5.rect.x=1200
        sprite6.rect.x=1200
        sprite7.rect.x=1200
        sprite8.rect.x=1200
        sprite9.rect.x=1200
        sprite10.rect.x=1200
        saida.rect.x=1200
        


    
    
    # Atividade: criar mais 8 sprites de lanches
    # incrementar o placar quando o pacman tocar no lanche
    
    # exibir o placar
    tela.blit(pygame.font.SysFont(None,28).render("Pontos="+str(placar),True,(255,255,255)),(10,680))
    tela.blit(pygame.font.SysFont(None,28).render("Vidas="+str(vida),True,(255,255,255)),(128,680))
    
    # atualizando sprites
    grupo_sprites.update()

    # desenhando sprites na tela
    grupo_sprites.draw(tela)
   
    # atualiza a tela   
    pygame.display.flip()
    pygame.time.delay(3) # atraso em ms
# saindo do jogo
pygame.quit()
