import pygame
import random
from pygame.locals import *
pygame.init()

WIDTH=864
HEIGHT=936

clock=pygame.time.Clock()
fps=60

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

font=pygame.font.SysFont("Arial",60)

white=(255,255,255)

ground_scroll=0
scroll_speed=4
flying=False
gameover=False
pipe_gap=150
pipe_frequency=1500
last_pipe=pygame.time.get_ticks()-pipe_frequency
score=0
pass_pipe=False

bg=pygame.image.load("bg.png")
ground_img=pygame.image.load("ground.png")
restart=pygame.image.load("restart.png")

def draw_text(text,font,text_col,x,y):
    img=font.render(text, True, text_col)
    screen.blit(img,(x,y))

def reset_game  ():
    pipe_group.empty()
    flappy.rect.x=100
    flappy.rect.y=int(HEIGHT/2)
    score=0
    return score

class Bird(pygame.sprite.Sprite):
    def __init__ (self, x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.images= []
        self.index=0
        self.counter=0
        for num in range (1,4):
            img=pygame.image.load(f"img/bird{num}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.vel=0
        self.clicked=False
    def update(self):
        if flying==True:
            self.vel+=0.5
            if self.vel>8:
                self.vel=8
            if self.rect.bottom<768:
                self.rect.y+=int(self.vel)
        if gameover==False:
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                self.vel=-10
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
            flap_cooldown=5
            self.counter+=1
            if self.counter>flap_cooldown:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
                    self.image=self.images[self.index]
            self.image=pygame.transform.rotate(self.images[self.index],self.vel*-2)
        else:
            self.image=pygame.transform.rotate(self.images[self.index],-90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("img/pipe.png")
        self.rect=self.image.get_rect()
        if pos==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-int(pipe_gap/2)]
        elif pos ==-1:
            self.rect.topleft=[x,y+int(pipe_gap/2)]
    def update(self):
        self.rect.x-=scroll_speed
        if self.rect.right<0:
            self.kill()

class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def draw(self):
        action=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action=True
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

pipe_group=pygame.sprite.Group()
bird_group=pygame.sprite.Group()
flappy=Bird(100,int(HEIGHT/2))
bird_group.add(flappy)
button=Button(WIDTH//2-50,HEIGHT//2-100,restart)
run=True

while run:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    pipe_group.draw(screen)
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(ground_img, (ground_scroll,768))
    if len(pipe_group)>0:
        if bird_group.sprites()[0].rect.left>pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right<pipe_group.sprites()[0].rect.right and pass_pipe==False:
            pass_pipe=True
        if pass_pipe==True:
            if bird_group.sprites()[0].rect.left>pipe_group.sprites()[0].rect.right:
                score+=1
                pass_pipe=False
    draw_text(str(score),font,white,int(WIDTH/2),20)
    if pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or flappy.rect.top<0:
        gameover=True
    if flappy.rect.bottom>=768:
        gameover=True
        flying=False
    if flying==True and gameover==False:
        time_now=pygame.time.get_ticks()
        if time_now-last_pipe>pipe_frequency:
            pipe_height=random.randint(-100,100)
            btm_pipe=Pipe(WIDTH,int(HEIGHT/2)+pipe_height,-1)
            top_pipe=Pipe(WIDTH,int(HEIGHT/2)+pipe_height,1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe=time_now
        pipe_group.update()
        ground_scroll-=scroll_speed
        if abs(ground_scroll)>35:
            ground_scroll=0
    if gameover==True:
        if button.draw():
            gameover=False
            score=reset_game()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and gameover==False:
            flying=True
    pygame.display.update()
pygame.quit()