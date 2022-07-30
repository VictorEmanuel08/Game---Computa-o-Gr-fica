import pygame
from pygame.locals import *
from math import *

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

#definidos conforme desenho no GeoGebra
vertices=((1.5,2),(-1.5,2),(-1.5,-2),(1.5,-2),
(1.25, 1.75),(-1.25,1.75),(-1.25,-1.75),(1.25,-1.75),
(0.8,-1.75),(0.8,-1),(-0.8,-1),(-0.8,-1.75),
(-0.8,1.75),(-0.8,1),(0.8,1),(0.8,1.75),
(-0.3,-1.75),(-0.3,-1.45),(0.3,-1.45),(0.3,-1.75),
(-0.3,1.75),(-0.3,1.45),(0.3,1.45),(0.3,1.75),
(-1.25,0),(1.25,0)
) 

arestas=((0,1),(1,2),(2,3),(3,0),
(4,5),(5,6),(6,7),(7,4),
(8,9),(9,10),(10,11),(11,8),
(12,13),(13,14),(14,15),(15,12),
(16,17),(17,18),(18,19),(19,16),
(20,21),(21,22),(22,23),(23,20),
(24,25),(25,24)
)

#Todas as linhas do campo são definidas aqui: Linhas limites, grande área, pequena área e linha do meio de campo 
def Linhas():
    glBegin(GL_QUADS) #Definiu-se aqui a cor verde para todos o desenho
    for e in arestas:
        glColor3f(0, 1, 0)
        for vertex in e:
            glVertex2fv(vertices[vertex])
    glEnd()
   
    glBegin(GL_LINES)
    glColor3f(1, 1, 1) #Definiu-se aqui a cor branca para as linhas
    for e in arestas:
        for vertex in e:
            glVertex2fv(vertices[vertex])
   
    glEnd()

def circulo(): #Função para desenho do circulo do meio campo
    raio = 0.4
    glColor3f(1.0, 1.0, 1.0) #Linhas brancas
    glBegin(GL_LINE_LOOP)
    for i in range(30):
        calx= raio * cos(i * 2*pi / 30)
        caly=raio * sin(i * 2*pi / 30)
        glVertex2d(calx, caly)
    glEnd()


def parabola1(): #Função para parábola próxima à grande área na metade do campo de baixo
    raio = 0.2
    posx, posy = 0, -1
    glColor3f(1.0, 1.0, 1.0) #Linhas brancas
    glBegin(GL_LINES)
    for i in range(33):
        cosine = raio * cos(i * pi / 32) + posx
        sine = raio * sin(i * pi / 32) + posy
        glVertex2f(cosine, sine)
    glEnd()

def parabola2(): #Função para parábola próxima à grande área na metade do campo de cima
    raio = -0.2
    sides = 32
    posx, posy = 0,1
    glColor3f(1.0, 1.0, 1.0) #Linhas brancas
    glBegin(GL_LINES)
    for i in range(33):
        cosine = raio * cos(i * pi / sides) + posx
        sine = raio * sin(i * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()

def identificador(): #mini objeto criado só para identificação da orientação
    raio = 0.1
    sides = 32
    posx, posy = 2,-1.5
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for i in range(100):
        cosine = raio * cos(i * 2*pi / sides) + posx
        sine = raio * sin(i * 2*pi / sides) + posy
        glVertex2d(cosine, sine)
    glEnd()

def desenho():
    Linhas()
    circulo()
    parabola1()
    parabola2()
    identificador()

def main():
    pygame.init()
    display = (800, 600) #Tamanho da tela em 800x600
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(70, display[0]/display[1], 1, 10)
    glTranslate(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #Rotação em vários sentidos com scroll do mouse  
            #é necessário descomentar a linha para ver a movimentação específica
            if event.type == pygame.MOUSEBUTTONDOWN:
                glRotatef(1.0, 1, 0, 0) #ROTAÇÃO NO EIXO Y
                #glRotatef(1.0, 0, 1, 0) #ROTAÇÃO NO EIXO X
                #glRotatef(1.0, 1, 1, 1) #ROTAÇÃO NA DIAGONAL

            #Translação com botões direita e esquerda do teclado    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    glTranslate(0.5, 0, 0)
                if event.key == pygame.K_LEFT:
                    glTranslate(-0.5, 0, 0)

                #Escala com botões cima e baixo do teclado
                if event.key == pygame.K_UP:
                    glScalef(1.1,1.1,1.1)
                if event.key == pygame.K_DOWN:
                    glScalef(0.8,0.8,0.8)

                #Reflexão com botões A e D do teclado
                if event.key == pygame.K_a:
                    glScalef(-1,1,1)
                if event.key == pygame.K_d:
                    glScalef(1,-1,1)

                #Reflexão com botões W e S do teclado, mas em eixo diferente ao anterior
                if event.key == pygame.K_w:
                    glScalef(1,1,1)
                if event.key == pygame.K_s:
                    glScalef(-1,-1,1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #Limpar o cachê

        desenho()
        pygame.display.flip()
        pygame.time.wait(20)

main()