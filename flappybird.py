import pygame
from pygame import *
from random import *

icon = image.load('assets/icon.png')
icon = transform.scale(icon, (32,32))

okno = display.set_mode((350,560))
pygame.display.set_caption('Flappy Bird')
pygame.display.set_icon(icon)

fps = time.Clock()
game = True

bird1 = image.load('assets/bird1.png')
bird1 = transform.scale(bird1, (48,36))
bird2 = image.load('assets/bird2.png')
bird2 = transform.scale(bird2, (48,36))
bird3 = image.load('assets/bird3.png')
bird3 = transform.scale(bird3, (48,36))
bgday = image.load('assets/bgday.png')
bgday = transform.scale(bgday, (432,768))
bgnight = image.load('assets/bgnight.png')
bgnight = transform.scale(bgnight, (432,768))
tubeup = image.load('assets/tubeup.png')
tubeup = transform.scale(tubeup, (75,402))
tubedown = image.load('assets/tubedown.png')
tubedown = transform.scale(tubedown, (75,363))
ground1 = image.load('assets/ground.png')
ground1 = transform.scale(ground1, (459,168))
ground2 = image.load('assets/ground.png')
ground2 = transform.scale(ground2, (459,168))
num0 = image.load('assets/0.png')
num0 = transform.scale(num0, (42,60))
num1 = image.load('assets/1.png')
num1 = transform.scale(num1, (30,60))
num2 = image.load('assets/2.png')
num2 = transform.scale(num2, (42,60))
num3 = image.load('assets/3.png')
num3 = transform.scale(num3, (42,60))
num4 = image.load('assets/4.png')
num4 = transform.scale(num4, (42,60))
num5 = image.load('assets/5.png')
num5 = transform.scale(num5, (42,60))
num6 = image.load('assets/6.png')
num6 = transform.scale(num6, (42,60))
num7 = image.load('assets/7.png')
num7 = transform.scale(num7, (42,60))
num8 = image.load('assets/8.png')
num8 = transform.scale(num8, (42,60))
num9 = image.load('assets/9.png')
num9 = transform.scale(num9, (42,60))

bgtype = 1 #1 - day, 2 - night
birdy = 218
birdx = 15
falltime = 0
fly = False
tubexpos = 351
tubedownypos = 300
tubeupypos = tubedownypos - 542
birdtouchcheck = 0
birdanimation = 1
birdshow = 1
groundx = 0
score = 0
numleft = 0
numright = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE or K_UP:
                fly = True
        if e.type == KEYUP:
            if e.key == K_SPACE or K_UP:
                fly = False
                falltime -= 5
    if falltime != 6:
        falltime += 0.6
    if fly == True:
            birdy -= 5
            falltime = 0
    if birdy > 450:
        birdx = 15
        birdy = 218
        falltime = 0
        tubexpos = 351
        birdtouchcheck = 0
        tubedownypos = randint(210,420)
        tubeupypos = tubedownypos - 542
        score = 0
        numleft = 0
        numright = 0
    if birdy < -36:
        birdx = 15
        birdy = 218
        falltime = 0
        tubexpos = 351
        birdtouchcheck = 0
        tubedownypos = randint(210,420)
        tubeupypos = tubedownypos - 542
        score = 0
        numleft = 0
        numright = 0
    birdy += falltime
    okno.fill((12, 186, 245))
    if bgtype == 1:
        okno.blit(bgday, (0,-100))
    if bgtype == 2:
        okno.blit(bgnight, (0,-100))
    if birdanimation != 4:
        birdanimation += 0.1
    if birdanimation > 4:
        birdanimation = 1
    birdshow = round(birdanimation)
    if birdshow == 4:
        birdshow = 2
    if birdshow == 1:
        okno.blit(bird1, (birdx, birdy))
    if birdshow == 2:
        okno.blit(bird2, (birdx, birdy))
    if birdshow == 3:
        okno.blit(bird3, (birdx, birdy))
    okno.blit(tubedown, (tubexpos, tubedownypos))
    okno.blit(tubeup, (tubexpos, tubeupypos))
    okno.blit(ground1, (groundx, 498))
    okno.blit(ground2, (groundx + 459, 498))
    if score < 10:
        if score == 0:
            okno.blit(num0, (160, 15))
        if score == 1:
            okno.blit(num1, (160, 15))
        if score == 2:
            okno.blit(num2, (160, 15))
        if score == 3:
            okno.blit(num3, (160, 15))
        if score == 4:
            okno.blit(num4, (160, 15))
        if score == 5:
            okno.blit(num5, (160, 15))
        if score == 6:
            okno.blit(num6, (160, 15))
        if score == 7:
            okno.blit(num7, (160, 15))
        if score == 8:
            okno.blit(num8, (160, 15))
        if score == 9:
            okno.blit(num9, (160, 15))
    if score > 9:
        numleft = int(str(score)[0])
        numright = int(str(score)[1])
        if numleft == 1:
            okno.blit(num1, (139, 15))
        if numleft == 2:
            okno.blit(num2, (130, 15))
        if numleft == 3:
            okno.blit(num3, (130, 15))
        if numleft == 4:
            okno.blit(num4, (130, 15))
        if numleft == 5:
            okno.blit(num5, (130, 15))
        if numleft == 6:
            okno.blit(num6, (130, 15))
        if numleft == 7:
            okno.blit(num7, (130, 15))
        if numleft == 8:
            okno.blit(num8, (130, 15))
        if numleft == 9:
            okno.blit(num9, (130, 15))
        if numleft != 1:
            if numright == 0:
                okno.blit(num0, (187, 15))
            if numright == 1:
                okno.blit(num1, (187, 15))
            if numright == 2:
                okno.blit(num2, (187, 15))
            if numright == 3:
                okno.blit(num3, (187, 15))
            if numright == 4:
                okno.blit(num4, (187, 15))
            if numright == 5:
                okno.blit(num5, (187, 15))
            if numright == 6:
                okno.blit(num6, (187, 15))
            if numright == 7:
                okno.blit(num7, (187, 15))
            if numright == 8:
                okno.blit(num8, (187, 15))
            if numright == 9:
                okno.blit(num9, (187, 15))
        if numleft == 1:
            if numright == 0:
                okno.blit(num0, (181, 15))
            if numright == 1:
                okno.blit(num1, (181, 15))
            if numright == 2:
                okno.blit(num2, (181, 15))
            if numright == 3:
                okno.blit(num3, (181, 15))
            if numright == 4:
                okno.blit(num4, (181, 15))
            if numright == 5:
                okno.blit(num5, (181, 15))
            if numright == 6:
                okno.blit(num6, (181, 15))
            if numright == 7:
                okno.blit(num7, (181, 15))
            if numright == 8:
                okno.blit(num8, (181, 15))
            if numright == 9:
                okno.blit(num9, (181, 15))
    if groundx > -456:
        groundx -= 3
    else:
        groundx = 0
    if tubexpos != -75:
        tubexpos -= 3
        birdtouchcheck -= 3
        if tubexpos < -72:     #проверка прохождения через трубы
            tubedownypos = randint(210,420)
            tubeupypos = tubedownypos - 542
            tubexpos = 351
            birdtouchcheck = 0
            score += 1
        if birdtouchcheck > -390 and birdtouchcheck < -288:
            if tubedownypos < birdy + 36: #проверка проигрыша от нижней трубы
                birdx = 15
                birdy = 218
                falltime = 0
                tubexpos = 351
                birdtouchcheck = 0
                tubedownypos = randint(210,420)
                tubeupypos = tubedownypos - 542
                birdanimation = 0
                score = 0
                numleft = 0
                numright = 0
            if tubeupypos + 402 > birdy: #проверка проигрыша от вверхней трубы
                birdx = 15
                birdy = 218
                falltime = 0
                tubexpos = 351
                birdtouchcheck = 0
                tubedownypos = randint(210,420)
                tubeupypos = tubedownypos - 542
                birdanimation = 0
                score = 0
                numleft = 0
                numright = 0
    fps.tick(60)
    display.update()