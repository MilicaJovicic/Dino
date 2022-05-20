from pickle import REDUCE
from re import A
from turtle import color
import pygame
import time
import random
import math


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN=(29, 124 , 43)
BROWN=(250,150,0)
BALL_TILE_COLOR = (94, 119, 3)
BACKGROUND_COLOR = (0, 200, 255)
SILVERR= (108, 107, 105)


class Rupa:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.koji=2
    def draw (self,surface):
        pygame.draw.rect(surface, BACKGROUND_COLOR, (self.x,self.y,self.width, self.height))
    def move (self, dx):
        self.x+=dx

class Kamen:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.koji=2
    def draw (self,surface):
        pygame.draw.rect(surface, SILVERR, (self.x,self.y-50,self.width, self.height))
    def move (self, dx):
        self.x+=dx
    
class Oblak:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.koji=3
    def draw (self,surface):
        pygame.draw.rect(surface,WHITE, (self.x,self.y-100,self.width,self.height))
    def move(self,dx):
        self.x+=dx


class Dino:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self, dy):
        self.y -=dy
    
    def dole(self):
        dino.height=50
        dino.y+=50
    
    def gore(self):
        self.height=100
        self.y-=50


    

pygame.init()
screen_w = 820
screen_h = 500
dis=pygame.display.set_mode((screen_w,screen_h))
pygame.display.update()
pygame.display.set_caption('Nema neta')
nije_krenuo=True
font = pygame.font.Font('freesansbold.ttf', 50)
font2 = pygame.font.Font('freesansbold.ttf', 30)
while (nije_krenuo):
    dis.fill(BLACK)
    text4=font.render("Za START pritisni SPACE!", True, WHITE, BLACK )
    dis.blit(text4,(screen_w // 2 - 300, screen_h // 2-90))
    text=font2.render("Da preskočiš prepreku pritisni UP", True, WHITE, BLACK)
    dis.blit(text,(screen_w // 2 - 300, screen_h // 2-30))
    text=font2.render("Da se sagneš pritisni DOWN", True, WHITE, BLACK)
    dis.blit(text,(screen_w // 2 - 300, screen_h // 2+10))
    text=font2.render("NE DRŽI TASTERE SAMO PRITISNI!!!", True, RED, BLACK)
    dis.blit(text,(screen_w // 2 - 300, screen_h // 2+60))
    pygame.display.update()
    for event in pygame.event.get():
        print(event)   
        if event.type==pygame.KEYDOWN:
            nije_krenuo=False
        elif event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
            pygame.quit()
            exit()





game_over=False
klika_space=True

najbolji_rezultat=0

while (klika_space):
    dis.fill ( BACKGROUND_COLOR)
    pygame.draw.rect (dis, GREEN, (0,400,820,20) )
    pygame.draw.rect (dis, BROWN, (0,420,820,80) )
    dino= Dino(20,300,50,100, RED)
    P1=Kamen(20,500,0,0)
    P1.draw(dis)
    P2=random.choice([Rupa, Kamen,Oblak]) (270,400,50,50)
    P2.draw(dis)
    P3=random.choice([Rupa, Kamen,Oblak]) (520,400,50,50)
    P3.draw(dis)
    P4=random.choice([Rupa, Kamen,Oblak]) (770,400,50,50)
    P4.draw(dis)
    dino.draw(dis)
    ok=-1
    spustanje=0
    ok1=-1
    kreni=0
    bodovi=0
    V=-0.1
    V2=0.15
    bodovi1=0
    game_over=True
    while game_over:
        for event in pygame.event.get():
            #print(event)   
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                pygame.quit()

        P1.move(V)
        P2.move(V)
        P3.move(V)
        P4.move(V)
        dis.fill (BACKGROUND_COLOR)
        pygame.draw.rect (dis, GREEN, (0,400,820,20) )
        pygame.draw.rect (dis, BROWN, (0,420,820,80) )
        P1.draw(dis)
        P2.draw(dis)
        P3.draw(dis)
        P4.draw(dis)
        if (P1.x<=-180):
            bodovi=bodovi+1
            P1=random.choice([Kamen,Rupa,Oblak]) (820,400,50,50)
            P1.draw(dis)
        if (P2.x<=-180):
            bodovi=bodovi+1
            P2=random.choice([Kamen,Rupa,Oblak]) (820,400,50,50)
            P2.draw(dis)
        if (P3.x<=-180):
            bodovi=bodovi+1
            P3=random.choice([Kamen,Rupa,Oblak]) (820,400,50,50)
            P3.draw(dis)
        if (P4.x<=-180):
            bodovi=bodovi+1
            P4=random.choice([Kamen,Rupa,Oblak]) (820,400,50,50)
            P4.draw(dis)
        
        if (bodovi1+3<bodovi):
            V=V-0.02
            V2=V2+0.03
            bodovi1=bodovi


        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            kreni=1
            ok=1

        if (kreni==1):
            if (dino.y<150):
                ok=-ok
            dino.move(ok*V2)
            if (dino.y>300):
                kreni=0
                dino.y=300
        preskacex=min(P1.x,P2.x,P3.x,P4.x)
        d=500-dino.y

        if keys_pressed[pygame.K_DOWN]:
            spustanje=1
            dino.height=50
            dino.y=350
        if (spustanje==1):
            if (P1.koji==3 and P1.x<-30 and P1.x>-50):
                dino.height=100
                dino.y=300
                spustanje=0
            if (P2.koji==3 and P2.x<-30 and P2.x>-50):
                dino.height=100
                dino.y=300
                spustanje=0
            if (P3.koji==3 and P3.x<-30 and P3.x>-50):
                dino.height=100
                dino.y=300
                spustanje=0
            if (P4.koji==3 and P4.x<-30 and P4.x>-50):
                dino.height=100
                dino.y=300
                spustanje=0

        dino.draw(dis)
        
        if (P1.width!=0 and P1.x<70):
            if (P1.koji==1):
                if (d<250):
                    if (P1.x>-5):
                        game_over=False
            if (P1.koji==2):
                if (dino.y>299.5):
                    if (P1.x>-5):
                        game_over=False
            if (P1.koji==3):
                if (P1.x>20):
                    if (spustanje==0):
                        game_over=False

        if (P2.x<70):    
            if (P2.koji==1):
                if (d<250):
                    if (P2.x>-5):
                        game_over=False
            if (P2.koji==2):
                if (dino.y>299.5):
                    if (P2.x>-5):
                        game_over=False
            if (P2.koji==3):
                if (P2.x>20):
                    if (spustanje==0):
                        game_over=False

        if (P3.x<70):
            if (P3.koji==1):
                if (d<250):
                    if (P3.x>-5):
                        game_over=False
            if (P3.koji==2):
                if (dino.y>299.5):
                    if (P3.x>-5):
                        game_over=False
            if (P3.koji==3):
                if (P3.x>20):
                    if (spustanje==0):
                        game_over=False
        
        if (P4.x<70):
            if (P4.koji==1):
                if (d<250):
                    if (P4.x>-5):
                        game_over=False
            if (P4.koji==2):
                if (dino.y>299.5):
                    if (P4.x>-5):
                        game_over=False
            if (P4.koji==3):
                if (P4.x>20):
                    if (spustanje==0):
                        game_over=False
        poruka="BODOVI: " + str(bodovi)
        text=font2.render(poruka, True, BLACK, BACKGROUND_COLOR)
        dis.blit(text,(0, 40))
        text4=font2.render("NAJBOLJI SKOR: " + str(najbolji_rezultat), True, RED, BACKGROUND_COLOR )
        dis.blit(text4,(0,0 ))
        pygame.display.update()
    
    nije_kliknuo_nista=True
    while nije_kliknuo_nista: 
        if (najbolji_rezultat<bodovi):
            najbolji_rezultat=bodovi
        dis.fill(BLACK)
        text4=font2.render("NAJBOLJI SKOR: " + str(najbolji_rezultat), True, RED, BLACK )
        dis.blit(text4,(0, 20))
        text=font.render("GAME OVER", True, WHITE, BLACK)
        dis.blit(text,(screen_w // 2 - 150, screen_h // 2-50))
        text1=font2.render("OSVOJENI BODOVI: " + str(bodovi), True, WHITE, BLACK )
        dis.blit(text1,(screen_w // 2 - 150, screen_h // 2))
        text2=font2.render("Za nastavak pritisni SPACE", True, WHITE, BLACK )
        dis.blit(text2,(screen_w // 2 - 150, screen_h // 2+30))
        text3=font2.render("Za izlazak pritisni putačicu", True, WHITE, BLACK )
        dis.blit(text3,(screen_w // 2 - 150, screen_h // 2+60))
        pygame.display.update()
        for event in pygame.event.get():
            print(event)   
            if event.type==pygame.KEYDOWN:
                nije_kliknuo_nista=False
            elif event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #for event in pygame.event.get():
         #   print(event)   
          #  if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
           #     nije_kliknuo_nista=False
           # else:
            #    if keys_pressed(pygame.K_SPACE):
             #       nije_kliknuo_nista=False
              #  if keys_pressed(pygame.K_e):
               #     nije_kliknuo_nista=False
                #    klika_space=False 
         


