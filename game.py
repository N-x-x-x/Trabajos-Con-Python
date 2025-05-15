
'''
Nombre del Grupo: Mate amargo y una arepa

Realizado por:

Carolina Villalba
Nelyer Jose Narvaez Briceño
Paulo Gaston Meira Strazzolini
Eros Khalil Berón

'''

import pygame
import random
import sys
from pygame import mixer

#---------------------------------------inicializacion especificas de pygames-----------------------

pygame.init()

#--------------------------------Configuracion de audio y sus caracteristicas----------------------

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

#------------------------------------Cosas de formato de pagina------------------------------------

ANCHOVENTANA, ALTOVENTANA = 600, 800
pygame.display.set_caption('CatchU')#Titulo de la ventana del juego 

superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))#pantalla
reloj = pygame.time.Clock()

fuenteGrande = pygame.font.Font('Pokemon GB.ttf', 40)
fuenteMed = pygame.font.Font('Pokemon GB.ttf', 20) #defino la variable de fuente para no estar escribiendola a cada rato
fuenteChik =  pygame.font.Font('Pokemon GB.ttf', 15)                                         #tiene tamanio y el tipo de fuente (lo de pokemon)
#Para dibujar texto
def dibujaTexto(texto, fuente, colorTexto, x, y):#para dubijar texto
    img = fuente.render(texto, True, colorTexto) #crea el texto
    superficieVentana.blit(img, (x,y)) #lo dibuja en las coordenadas puestas de x y
#----------------------------------------------------------------------------------------------------

#-------------------------------Jugador y cosas del juego (declaraciones y correciones de formato)-------------------------------------------------

jugador = pygame.Rect(296, 500, 120, 120) #ubicacion y tamanio del pj
ImagenJugador = pygame.image.load('mejorado3.png')
ImagenScaleJuga = pygame.transform.scale(ImagenJugador, (120, 120))

#fruta = pygame.Rect(40,40)

ImgBomba = pygame.image.load('bombamejorada.png')
ImgBomba = pygame.transform.scale(ImgBomba, (80, 80))

ImgManzana = pygame.image.load('manzanaa.png')
ImgManzana = pygame.transform.scale(ImgManzana, (45, 45))

ImgCometa = pygame.image.load('cometa.png')
ImgCometa = pygame.transform.scale(ImgCometa, (80,80))

ImgFuego = pygame.image.load('fuego.png')
ImgFuego = pygame.transform.scale(ImgFuego, (80,80))

#botones

botonJugar = pygame.Rect(193,375,184,40)#|
botonSalir = pygame.Rect(400,650,190,40)#|>ubicacion y tamaño de los botones
botonVolver =pygame.Rect(200,100,190,40)
bJ=pygame.image.load('jugar tranqui.png')
bJM=pygame.image.load('jugar_fuego.png')
bS=pygame.image.load('salir.png')
bSM=pygame.image.load('salir1.png')
bV=pygame.image.load('voler.png')
bVM=pygame.image.load('volver azul.png')
# botonJugar = pygame.Rect(225,375,190,40)#|
# botonSalir = pygame.Rect(400,650,190,40)#|>dimenciones y tamaño de los botones
# botonVolver =pygame.Rect(200,100,190,40)
# bJ=pygame.image.load('jugar tranqui.png')
# bS=pygame.image.load('salir.png')
# bV=pygame.image.load('voler.png')

#fondos

menuprincipal = pygame.image.load('menu principal.png')#defino y acomodo la imagen del fondo
menuprincipal = pygame.transform.scale(menuprincipal, (ANCHOVENTANA, ALTOVENTANA))
#menuprincipal = pygame.image.load('Hog Rider Gigachad.jpg').convert()#otra manera
Fondo = pygame.image.load('fondo_estado0.jpg')
FondoCambioEstado_1 = pygame.image.load('car1.jpeg')
FondoCambioEstado_1 = pygame.transform.scale(FondoCambioEstado_1, (ANCHOVENTANA, ALTOVENTANA))
FondoCambioEstado_2 = pygame.image.load('Ftarde.png')
FondoCambioEstado_2 = pygame.transform.scale(FondoCambioEstado_2, (ANCHOVENTANA, ALTOVENTANA))
FondoCambioEstado_3 = pygame.image.load('car3.jpeg')
FondoCambioEstado_3 = pygame.transform.scale(FondoCambioEstado_3, (ANCHOVENTANA, ALTOVENTANA))
#FondoCambioEstado_4 = pygame.image.load('fondo_estado4.jpg')
#FondoCambioEstado_4 = pygame.transform.scale(FondoCambioEstado_4, (ANCHOVENTANA, ALTOVENTANA))
#FondoCambioEstado_5 = pygame.image.load('fondo_estado4-removebg-preview.png')
#FondoCambioEstado_5 = pygame.transform.scale(FondoCambioEstado_5, (ANCHOVENTANA, ALTOVENTANA))
FondoGameOver = pygame.image.load('game_over_imagen1.png')
FondoGameOver = pygame.transform.scale(FondoGameOver, (ANCHOVENTANA, ALTOVENTANA))

#sonido

sonido_agarra_moneda = pygame.mixer.Sound("sonido_de_puntos_adaptando.wav")
sonido_toca_bomba = pygame.mixer.Sound("gameboy-pluck-41265-from-pixabay.mp3")
#sonido_fuchs = pygame.mixer.Sound("")
#sonido_rebote = pygame.mixer.Sound("")

#----------------------------------------------------------------------------------------------------
#------------------------Jugador y cosas del juego (Clases, Funciones y Cosas)-----------------------

def musica_fondo(flagMusica):#Funcion de cambio de musica
    if flagMusica == 0:
        pygame.mixer.music.load("bit-beats-6-171021-by-XtremeFreddy.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
    elif flagMusica == 1:
        pygame.mixer.music.load("music-for-arcade-style-game-146875-by-lucadialessandro.mp3")
        pygame.mixer.music.play(-1)
        #pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.set_volume(0.2)
        #pygame.mixer.music.set_volume(0.0) #esto es para ajustar el volumen 1.0 es lo mas alto y 0.0 lo mas bajo, OJO PONERLO EN  0.0 NO ES QUITAR EL AUDIO ES SEGUIR PONIENDOLO PERO AL VOLUMEN MAS BAJO 

class Cpinguino(pygame.sprite.Sprite):#cosas personaje (de momento 1) 
    def __init__(self, x, y):
        self.sheet = pygame.image.load('pinguino-animado.png')
        self.sheet.set_clip(pygame.Rect(0,0,100,100))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        #self.rect.topleft = position
        self.frame = 0
        # self.left_states = { 0: (0, 0, 100, 100), 1: (100, 0, 100, 100), 2: (200, 0, 100, 100), 3: (300, 0, 100, 100) }
        # self.right_states = { 0: (0, 100, 100, 100), 1: (100, 100, 100, 100), 2: (200, 100, 100, 100), 3: (300, 100, 100, 100) }
        
        self.left_states = {0: (100, 0, 100, 100), 1: (300, 0, 100, 100) }
        self.right_states = {0: (100, 100, 100, 100), 1: (300, 100, 100, 100)}
        
        self.x = x
        self.y = y
        self.vel = 14
        self.hitbox = (self.x, self.y+25, 35, 45)
        
        self.spriteTime=0
        self.interval=0

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if(self.interval==1):
            if type(clipped_rect) is dict:
                self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
            else:
                self.sheet.set_clip(pygame.Rect(clipped_rect))
            return clipped_rect
        
    def spriteRefresh(self):
        self.interval=0
        if(0.25<(pygame.time.get_ticks()-self.spriteTime)/1000):
            self.interval=1
            self.spriteTime=pygame.time.get_ticks()
                  
    def update(self, direction): #movimiento
        self.spriteRefresh()
        if direction == 'left':
            self.clip(self.left_states)
            self.x -= self.vel
        if direction == 'right':
            self.clip(self.right_states)
            self.x += self.vel

            #keys = pygame.key.get_pressed()
                #if keys[pygame.K_a] and pinguinito.x > pinguinito.vel - 5:
                #    pinguinito.x -= pinguinito.vel
                #elif keys[pygame.K_d] and pinguinito.x < 570 - 0 - pinguinito.vel:
                #    pinguinito.x += pinguinito.vel

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > self.vel - 5:
            self.update('left')
        elif keys[pygame.K_d] and self.x < 570 - 0 - self.vel:
            self.update('right')        


        #if event.type == pygame.KEYDOWN:
         #   print("entro")

        #    if event.key == pygame.K_a:
        #        self.update('left')
        #    if event.key == pygame.K_d:
        #        self.update('right')

        # if event.type == pygame.KEYUP:

        #     if event.key == pygame.K_a: 
        #         self.update('stand_left')
        #     if event.key == pygame.K_d:
        #         self.update('stand_right')
        
    def draw(self, superficieVentana):

        superficieVentana.blit(self.image, (self.x-30, self.y))
        #ygame.draw.rect(superficieVentana, (0,0,0), (self.x, self.y+25, 35, 45))
        # self.hitbox = (self.x, self.y+25, 35, 45)
        self.hitbox = (self.x+20, self.y+15, 20, 20)
        
        

class Cfrutas(object):#cosas del cambur 
    def __init__(self, x, y, f_type):
        self.x = x
        self.y = y
        self.f_type = f_type
        #self.hitbox = (self.x, self.y+10, 60, 60)
        #codigo por si quieren añadirle un sonido de caida, el sonido apareceria cada vez que aparezca un cambur 
        #self.sonido = pygame.mixer.Sound("sonido de caida.wav")
        #self.sonido.set_volume(0.01)
        #self.sonido.play()
    def draw(self, superficieVentana):
        if self.f_type == 0:
            ImagenFruta = pygame.image.load('banana.png')
            self.vel = 16
        fruit = pygame.transform.scale(ImagenFruta, (100, 100))
        #pygame.draw.rect(superficieVentana, (0,0,0), (self.x, self.y+32, 55, 45))
        superficieVentana.blit(fruit, (self.x-20, self.y))
        self.hitbox = (self.x, self.y+32, 55, 45)
    def remove(self):
        return self.y >= 800

class Cbombas(object):#cosas de la bombas 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 16
        #self.hitbox = (self.x, self.y+10, 60, 60)
    def draw(self, superficieVentana):
        #pygame.draw.rect(superficieVentana, (0,0,0), (self.x+20, self.y+20, 10, 10))
        superficieVentana.blit(ImgBomba, (self.x-10, self.y))
        self.hitbox = (self.x+20, self.y+20, 10, 10)
    def remove(self):
        return self.y >= 800

#-----------------------cometa--------------------------
class Ccometas(object):#cosas de los cometas
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 20
        #self.hitbox = (self.x, self.y+10, 60, 60)
    def draw(self, superficieVentana):
        #pygame.draw.rect(superficieVentana, (0,0,0), (self.x, self.y+20, 55, 55))
        superficieVentana.blit(ImgCometa, (self.x-10, self.y))
        self.hitbox = (self.x, self.y+20, 55, 55)
    def remove(self):
        return self.y >= 800

class Cfuego(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 20
        #self.hitbox = (self.x, self.y, 40, 60)
        self.creationTime = pygame.time.get_ticks()
    def draw(self, superficieVentana):
        #pygame.draw.rect(superficieVentana, (0,0,0), (self.x, self.y, 40, 60))
        superficieVentana.blit(ImgFuego, (self.x-20, self.y-10))
        self.hitbox = (self.x, self.y, 40, 60)
    def remove(self):
        return pygame.time.get_ticks()-self.creationTime>=2000
#-----------------------cometa--------------------------
        
class Cmanzana(object): #manzana
    def __init__(self, x, y, f_type):
        self.x = x
        self.y = y
        self.f_type = f_type
        #self.hitbox = (self.x, self.y, 20, 20)
    def draw(self, superficieVentana):
        if self.f_type == 0:
            self.vel = 20
            #pygame.draw.rect(superficieVentana, (0,0,0), (self.x+15, self.y+15, 20, 20))
            superficieVentana.blit(ImgManzana, (self.x, self.y))
            self.hitbox = (self.x+15, self.y+15, 20, 20)
    def remove(self):
        return self.y >= 800

#----------------------------------------------------------------------------------------------------

def main():
    puntaje = 0
    manzanas = []
    frutas = []
    bombas = []
    cometas = []
    fuego = []
    sumadorFrutas = 0
    sumadorBombas = 0
    sumadorManzanas = 0
    sumadorCometas = 0
    
    generacionFrutas = 25
    generacionBombas = 100
    generacionManzanas= 85
    generacionCometas = 200
    
    pinguinito = Cpinguino(ANCHOVENTANA * 0.35, ALTOVENTANA - 160)
#------------------------------------------variables nuevas----------------------------------------------
    flagMusica = 0
    cambioMusica = 0
    inicioJuego = 0
    apagoBotones = 0
#--------------------------------------------------------------------------------------------------------
    #chequeador de game over
    
    lifeUp=0
    
    gameOver = False
    play = True
    
    
    #LEVEL MANAGER
    
    stime=0
    time=0
    ctime=0
    
    level1Flag=1
    level2Flag=1
    level3Flag=1
    level4Flag=1
    level5Flag=1
    level6Flag=1
    
    holdFlag=1
    
    counter=60
    
    #GAME LOOOP
    
    while play:
        
        #NOSE
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               play = False 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
        #print(event) #IMPRIME LA POSICION DEL MOUSE CREO
        
        #NOSE CREO QUE TIENE QUE VER CON LOS BOTONES
        
#-----------------------------------nuevo que meti--------------------------------------------------------
        if botonJugar.collidepoint(pygame.mouse.get_pos())==0:
            superficieVentana.blit(menuprincipal,(1,1)) #coloco fondo de menu principal
        
        #-----------------------------------Botones--------------------------------------------------------
        #pygame.draw.rect(superficieVentana,(0,0,0),botonSalir)#|
        #pygame.draw.rect(superficieVentana,(0,0,0),botonJugar)#|>hit-box de los botones
        #superficieVentana.blit(bJ,(200,366))
        #superficieVentana.blit(bS,(390,641))
        if botonSalir.collidepoint(pygame.mouse.get_pos()):#lo que esta dentro del () devuelve la posicion de toda la pantalla 
            superficieVentana.blit(bSM,(390,641))
        else:
            superficieVentana.blit(bS,(390,641))
        if botonJugar.collidepoint(pygame.mouse.get_pos()):
            superficieVentana.blit(bJM,(193,366))
        else:
            superficieVentana.blit(bJ,(193,366))
#--------------------------------------------------------------------------------------------------
        
        if apagoBotones == 0:#manera en como lo resolv///no se me salio lo de la funcion perdon...
            if cambioMusica == 0:
                musica_fondo(flagMusica)
            cambioMusica = 1
            reinicio = 0
            inicioJuego = 0 #apago juego
            
        #-------------------------------------------------------------------------------------------------------
            #esto es para cambiar la imagen de los botones cuando el mouse esta arriba
            #if botonSalir.collidepoint(pygame.mouse.get_pos()):#lo que esta dentro del () devuelve la posicion de toda la pantalla 
             #   superficieVentana.blit(bSM,(390,641))
            #if botonJugar.collidepoint(pygame.mouse.get_pos()):
             #   superficieVentana.blit(bJM,(200,366))
        #-------------------------------------------------------------------------------------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:#si toca el boton de salir sale
                if botonSalir.collidepoint(event.pos):#lo que esta dentro del () devuelve la posicion de solo la pestaña donde corre el juego  
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:#si toca el boton de juga empieza el juego y apaga la musica para poner otra
                if botonJugar.collidepoint(event.pos):
                    #--------------------------------------------------------------------------------------------------
                    pygame.mixer.music.stop()
                    flagMusica = 1
                    cambioMusica = 0
                    if cambioMusica == 0:
                        musica_fondo(flagMusica)
                    cambioMusica = 1
                    inicioJuego = 1
        
        #POR ALGUNA RAZON AHORA EL JUEGO ESTA METIDO ADENTRO DE UN CONDICIONAL MAS            
        
        if inicioJuego == 1:#en 1 pq preciono el boton 
            apagoBotones = 1 #ahora con 1 ya no me detecta los botones
            #aca empieza el juego ---> OK
            if gameOver == False:
                
                #DEJAR DE PONER TODOS LOS PROCESOS PEGADOS QUE NO SE ENTIENDE MUY BIEN PORFA
                
                #MANEJA MOVIMIENTO
                
                pinguinito.handle_event(event)
                        
                # keys = pygame.key.get_pressed()
                # if keys[pygame.K_a] and pinguinito.x > pinguinito.vel - 5:
                #     pinguinito.x -= pinguinito.vel
                # elif keys[pygame.K_d] and pinguinito.x < 500 - 0 - pinguinito.vel:
                #     pinguinito.x += pinguinito.vel
                    
                #RELOJ    
                
                if(level6Flag==1):
                    if(1<(pygame.time.get_ticks()-ctime)/1000):
                        counter-=1
                        ctime=pygame.time.get_ticks()
                    if(counter<0):
                        gameOver=True
                    
                #MANEJA EL FONDO O NIVEl    
                
                Key = pygame.key.get_pressed() 
                if Key[pygame.K_0]:
                    puntaje+=1
                elif Key[pygame.K_9]:
                    lifeUp+=1
               
                #Cambio nivel segun puntos
                if puntaje<10:
                    superficieVentana.blit(Fondo, (0,0)) #NIVEL 1
                    if(level1Flag==1):
                        stime=pygame.time.get_ticks()
                        level1Flag=0
                        pinguinito.spriteTime=pygame.time.get_ticks()
                    if(counter>57):
                        dibujaTexto("LEVEL 1!!!", fuenteMed, "BLACK", 200, 300)
                elif puntaje>=10 and puntaje<25:
                    superficieVentana.blit(FondoCambioEstado_1, (0,0)) #NIVEL 2
                    if(level2Flag==1):
                        level2Flag=0
                        generacionBombas=50
                        generacionFrutas=30
                        counter=60
                        sumadorFrutas=0
                        sumadorBombas=0
                    if(counter>57):
                        dibujaTexto("LEVEL 2!!!", fuenteMed, "BLACK", 200, 300)
                elif puntaje>=25 and puntaje<40:
                    superficieVentana.blit(FondoCambioEstado_2, (0,0)) #NIVEL 3
                    if(level3Flag==1):
                        level3Flag=0
                        generacionBombas=20
                        counter=60
                        sumadorFrutas=0
                        sumadorBombas=0
                    if(counter>57):
                        dibujaTexto("LEVEL 3!!!", fuenteMed, "BLACK", 200, 300)  
                elif puntaje>=40 and puntaje<60:
                    superficieVentana.blit(FondoCambioEstado_3, (0,0)) #NIVEL 4
                    if(level4Flag==1):
                        level4Flag=0
                        generacionBombas=15
                        counter=60
                        sumadorFrutas=0
                        sumadorBombas=0
                    if(counter>57):
                        dibujaTexto("LEVEL 4!!!", fuenteMed, "BLACK", 200, 300)
                elif puntaje>=60 and puntaje<80:
                    superficieVentana.blit(FondoCambioEstado_3, (0,0)) #NIVEL 5
                    if(level5Flag==1):
                        level5Flag=0
                        generacionBombas=5
                        counter=60
                        sumadorFrutas=0
                        sumadorBombas=0
                    if(counter>57):
                        dibujaTexto("LEVEL 5!!!", fuenteMed, "BLACK", 200, 300)
                elif puntaje>=80:
                    superficieVentana.blit(FondoCambioEstado_3, (0,0)) #NIVEL 6
                    if(level6Flag==1):
                        level6Flag=0
                        generacionBombas=3
                        sumadorFrutas=0
                        sumadorBombas=0
                
                #SUMADORES
                    
                sumadorFrutas += 1
                sumadorBombas += 1
                sumadorManzanas += 1
                sumadorCometas += 1
                
                if sumadorManzanas == generacionManzanas:
                    sumadorManzanas = 0
                    f_startx = random.randrange(15, ANCHOVENTANA - 80) #rango de spawneo de manzana en coords de x
                    f_starty = -200 #donde empiezan a caer las manzanas en la coordenadas de y 
                    f_type = 0 #por si queremos hacer rand
                    nuevaManzana = Cmanzana(f_startx, f_starty, f_type)
                    manzanas.append(nuevaManzana) #para que spawneen
                
                if sumadorFrutas == generacionFrutas:
                    sumadorFrutas = 0
                    f_startx = random.randrange(15, ANCHOVENTANA - 80) #rango de spawneo de frutas en coords de x
                    f_starty = -200 #donde empiezan a caer las frutas en la coordenadas de y 
                    f_type = 0
                    nuevaFruta = Cfrutas(f_startx, f_starty, f_type)
                    frutas.append(nuevaFruta) #para que spawneen
                    
                if sumadorBombas == generacionBombas:
                    sumadorBombas = 0 
                    b_startx = random.randrange(5, ANCHOVENTANA-75) #rango de spawneo de bombas en coords de x
                    b_starty = -200 #donde empiezan a caer las bombas en la coordenadas de y 
                    nuevaBomba = Cbombas(b_startx, b_starty)
                    bombas.append(nuevaBomba)

                if sumadorCometas == generacionCometas:
                    sumadorCometas = 0
                    c_startx = random.randrange(15, ANCHOVENTANA - 80)
                    c_starty = -200
                    nuevoCometa = Ccometas(c_startx, c_starty)
                    cometas.append(nuevoCometa)                    
                    
                #MANEJO MANZANAS    
                    
                for item in manzanas: 
                    item.draw(superficieVentana) 
                    item.y += item.vel
                for item in manzanas[:]:
                    #if (item.hitbox[0] >= pinguinito.hitbox[0] - 40) and (item.hitbox[0] <= pinguinito.hitbox[0] + 40): #hitbox en x
                        #if pinguinito.hitbox[1] - 80 <= item.hitbox[1] <= pinguinito.hitbox[1] - 70: #hitbox en y
                    if pygame.Rect(pinguinito.hitbox).colliderect(item.hitbox):
                        sonido_agarra_moneda.set_volume(0.1)#que suene poco
                        sonido_agarra_moneda.play()#si toca al animal pone el sonido
                        manzanas.remove(item) #si toca al pinguino desaparece la fruta
                        lifeUp+=1  #+1 life
                        if item.f_type == 0: 
                            puntaje += 0
                        #print("Puntaje:", puntaje)
                    #if(item.hitbox[1]>=800): #elimina item que caen por debajo de pantalla
                    #    manzanas.remove(item)
                    #    print("CHAU MANZANA")
                    if item.remove():
                        manzanas.remove(item)                    

                #MANEJO FRUTAS
                    
                for item in frutas: 
                    item.draw(superficieVentana) 
                    item.y += item.vel
                for item in frutas[:]:
                    #if (item.hitbox[0] >= pinguinito.hitbox[0] - 40) and (item.hitbox[0] <= pinguinito.hitbox[0] + 40): #hitbox en x
                     #   if pinguinito.hitbox[1] - 80 <= item.hitbox[1] <= pinguinito.hitbox[1] - 70: #hitbox en y
                    if pygame.Rect(pinguinito.hitbox).colliderect(item.hitbox):
                        sonido_agarra_moneda.set_volume(0.1)#que suene poco
                        sonido_agarra_moneda.play()#si toca al animal pone el sonido
                        frutas.remove(item) #si toca al pinguino desaparece la fruta
                        puntaje += 1  #y cuenta +1 en el puntaje
                        if item.f_type == 0: 
                            puntaje += 0
                        #print("Puntaje:", puntaje)
                    #if(item.hitbox[1]>=800): #elimina item que caen por debajo de pantalla
                    #    frutas.remove(item)
                    #    print("CHAU BANANA")
                    if item.remove():
                        frutas.remove(item)       
                             
                #MANEJO BOMBAS           
                
                for item in bombas:
                    item.draw(superficieVentana)
                    item.y += item.vel
                for item in bombas[:]:
                    #if (item.hitbox[0] >= pinguinito.hitbox[0] - 30) and (item.hitbox[0] <= pinguinito.hitbox[0] + 30): #aca es hibox en x
                        #if pinguinito.hitbox[1] - 80 <= item.hitbox[1] <= pinguinito.hitbox[1] - 70: #hitbox en y controla la hitbox de la bomba pegandole al pinguino
                    if pygame.Rect(pinguinito.hitbox).colliderect(item.hitbox):        
                        sonido_toca_bomba.set_volume(0.3)#que suene poco
                        sonido_toca_bomba.play()#si toca al animal pone el sonido
                        bombas.remove(item)
                        lifeUp-=1
                        if(lifeUp<0):
                            gameOver = True #termina el juego si toca una bomba el hitbox del pinguino, agregar un apantalla de game over
                    #if(item.hitbox[1]>=800): #elimina item que caen por debajo de pantalla
                    #    bombas.remove(item)
                    #    print("CHAU BOMBA")
                    if item.remove():
                        bombas.remove(item)

                #MANEJO DE COMETAS Y FUEGO

                for item in cometas:
                    item.draw(superficieVentana)
                    item.y += item.vel
                for item in cometas[:]:
                    if pygame.Rect(pinguinito.hitbox).colliderect(item.hitbox):
                        sonido_toca_bomba.set_volume(0.3)#que suene poco
                        sonido_toca_bomba.play()#si toca al animal pone el sonido
                        cometas.remove(item)
                        lifeUp-=1
                        if(lifeUp<0):
                            gameOver = True #termina el juego si toca una bomba el hitbox del pinguino, agregar un apantalla de game over
                    #if item.remove():
                    #    cometas.remove(item)
                    if item.y == 700:
                        fuego = [Cfuego(item.x, 650)]
                        cometas.remove(item)
                for item in fuego: 
                    if item.remove():
                        fuego.remove(item)
                    else:
                        item.draw(superficieVentana)
                for item in fuego[:]:
                    if pygame.Rect(pinguinito.hitbox).colliderect(item.hitbox):
                            sonido_toca_bomba.set_volume(0.3)
                            sonido_toca_bomba.play()
                            gameOver = True
                
                #SUPONGO QUE ESTO ES EL PUNTAJE Y ALGO MAS
                
                dibujaTexto("Puntaje:"+str(puntaje),fuenteMed,"red", 10, 30)#muestra el puntaje 150 es la coor x
                #pinguinito.draw(superficieVentana)
                #reloj.tick(60) #cambiar por reloj
                #pygame.display.flip()
                
                dibujaTexto("1UP:"+str(lifeUp),fuenteMed,"red", 245, 30)
                #pinguinito.draw(superficieVentana)
                #reloj.tick(60) #cambiar por reloj
                #pygame.display.flip()
                
                if(level6Flag==1):
                    dibujaTexto("Time: "+str(counter),fuenteMed,"red", 400, 30)
                else:
                    dibujaTexto("Time: 00",fuenteMed,"red", 400, 30)
                
                pinguinito.draw(superficieVentana) #dibuja pj
                
                pygame.display.flip() #actualiza la pantalla dibujando todo
                
                
            #LA VERDAD QUE NO HACIA FALTA METER TODO EN UN IF ELSE CREO
                
            #GAME OVER
                
            else: #si el juegador pierde
                if(holdFlag==1):
                    pygame.time.wait(500)
                    holdFlag=0
                    
                fuego.clear()
                manzanas.clear()
                frutas.clear()
                bombas.clear()
                cometas.clear()
                    
                superficieVentana.blit(FondoGameOver, (0,0)) 
                pygame.draw.rect(superficieVentana,(255,255,255),botonSalir)
                pygame.draw.rect(superficieVentana,(255,255,255),botonVolver)
                superficieVentana.blit(bS,(390,641))
                superficieVentana.blit(bV,(190,90))
                
                if botonSalir.collidepoint(pygame.mouse.get_pos()):
                    superficieVentana.blit(bSM,(390,641))
                    
                if botonVolver.collidepoint(pygame.mouse.get_pos()):
                    superficieVentana.blit(bVM,(190,90))
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botonSalir.collidepoint(event.pos):
                        pygame.quit()
                    if botonVolver.collidepoint(event.pos):
                        #gameOver = False
                        flagMusica = 0# pongo esa pista |
                        cambioMusica = 0#               | 
                        reinicio = 1#                   |>reinicio todo
                        apagoBotones = 0 #vuelvo al menu|
                            
                dibujaTexto("GAME OVER!", fuenteGrande, "white", 120, 200) 
                dibujaTexto("Puntaje: " +str(puntaje), fuenteMed, "white",200, 300 ) #convierte el puntaje en una cadena y lo concatena
                dibujaTexto("Pulse 'espacio' para reintentar", fuenteChik, "white", 70, 360)
                Key = pygame.key.get_pressed() 
                
                if Key[pygame.K_SPACE] or reinicio == 1: #chequea si se apreto espacio
                    puntaje=0 #resetea las variables y el estado
                    lifeUp=0
                    generacionBombas=100
                    generacionFrutas=30
                    level1Flag=1
                    level2Flag=1
                    level3Flag=1
                    level4Flag=1
                    level5Flag=1
                    level6Flag=1
                    holdFlag=1
                    sumadorFrutas=0
                    sumadorBombas=0
                    counter=60
                    gameOver = False
                    pinguinito = Cpinguino(ANCHOVENTANA * 0.35, ALTOVENTANA - 160) #posiciona al pinguino donde comenzo
        #else: #----> PARA QUE EXISTE ESTE ELSE????
            #print("Juego Cerrado")
        #-------------------------------------------------FIn ciclo del Juego---------------------------------------------
        pygame.display.flip()
        reloj.tick(45) #define los fps de las imagenes por pantalla, en realidad de todo -> velocidad de las imagenes
main()