import pygame
from pygame import mixer
import random
import math

pygame.init()      # initializing pygame

screen = pygame.display.set_mode((800, 800))  # display
# loading music and images
img = pygame.image.load('a.png')
bull = pygame.image.load('c.png')
bg = pygame.image.load('bg2.jpeg')
d = pygame.image.load('dead.png')
mixer.music.load('on.mp3')
mixer.music.play(-1)

# setting initial positions
p = 0
u = 0
shipx = 380
shipy = 700
ene = pygame.image.load('b1.png')
ex = random.randint(0, 736)
ey = random.randint(80, 100)
exp = 0.5
eyu = 45



state = 'n'
o = shipy
bx = 0
score = 0


def bullet (bx,o):      #commands to bullet img
    screen.blit(bull,(bx,o))        #img blinking -- screenname.blit(imagename,(x,y))
    global state
    state = 'r'

def enemy (x,y):       #enemy image 
    screen.blit(ene, (x,y))

def player(x,y):        #player img
    screen.blit(img, (x,y))

def collition(ex,ey,bx,o):      #if collition of ship and bullet takes place
    dis = math.sqrt((math.pow(ex-bx,2))+math.pow(ey-o,2))
    return dis <= 25

def deadof(x,y,ex,ey):      #if collition of ship and virus takes place 
    de = math.sqrt((math.pow(x-ex,2))+(math.pow(y-ey,2)))
    if de <= 40:
        ds = mixer.Sound('go.mp3')
        ds.play()
    return de <= 40
run = True
while run:
    screen.fill((0,0,0))
    screen.blit(bg, (0,0))
    for event in pygame.event.get():        #gets the input from the user -- event.get
        if event.type == pygame.QUIT:
            run = False
        #if key is pressed checking it
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                p =- 0.5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                p = 0.5
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                u -= 0.5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                u = 0.5
            if event.key == pygame.K_SPACE:
                    bs = mixer.Sound('bull.mp3')
                    bs.play()
                    bx = shipx
                    o = shipy
                    bullet(bx, o)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                p = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                u = 0
                 
               
    shipx += p
    shipy += u
    if shipx > 733:
        shipx = 733
    elif shipx < 0:
        shipx = 0
    elif shipy > 733:
        shipy = 733
    elif shipy < 0:
        shipy = 0

    ex += exp
    if ex > 764:
        exp = -0.5
        ey += eyu
    elif ex < 0:
        exp = 0.5
        ey += eyu
    #collisinon
    collide = collition(ex, ey, bx, o)
    if collide:
        coll = mixer.Sound('coll.mp3')
        coll.play()
        bx = 480
        state = 'n'
        ex = random.randint(0, 736)
        ey = random.randint(50, 200)
        score += 1
        print("score - ",score)
    enemy(ex, ey,)
    dead = deadof(shipx, shipy, ex,ey)
    if dead:
        ex = 1000
        ey = 1000
        bg = d
        mixer.music.stop()
        klm = mixer.Sound('Telugu Dj.mp3')
        klm.play()
    if o <= 0:
        o = 870
        state = 'n'
    if state == 'r':
        bullet(bx, o)
        o -= 4

    player(shipx, shipy)



    pygame.display.update()




