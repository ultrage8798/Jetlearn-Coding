import pygame
import random 
from pygame.locals import *
import time

WIDTH=950
HEIGHT=750

def change_bg(img):
    background=pygame.image.load(img)
    bg=pygame.transform.scale(background,(WIDTH,HEIGHT))
    screen.blit(bg,(0,0))
pygame.init()
pygame.display.set_caption("Recycle Marathon")
screen=pygame.display.set_mode([WIDTH,HEIGHT])

class Bin(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/ultra/bin.png")
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__ (self,img):
        super().__init__()
        self.image=pygame.image.load("C:/Users/ultra/box.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()

class Non_recyclable(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/ultra/bag.png")
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

imgs=["item1.png","item2.png","item3.png"]
item_list=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
plastic_list=pygame.sprite.Group()

for i in range(50):
    item=Recyclable(random.choice(imgs))
    item.rect.x=random.randrange(WIDTH)
    item.rect.y=random.randrange(HEIGHT)
    item_list.add(item)
    all_sprites.add(item)

for i in range(20):
    plastic=Non_recyclable()
    plastic.rect.x=random.randrange(WIDTH)
    plastic.rect.y=random.randrange(HEIGHT)
    plastic_list.add(plastic)
    all_sprites.add(plastic)

bin=Bin()
all_sprites.add(bin)
white=(255,255,255)
red=(255,0,0)

playing=True
score=0
clock=pygame.time.Clock()
start_time=time.time()
myFont=pygame.font.SysFont("Times New Roman",22)
timingFont=pygame.font.SysFont("Times New Roman",22)
text=myFont.render("Score="+str(0),True,white)

while playing:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    time_elapsed=time.time()-start_time
    if time_elapsed>=60:
        if score>50:
            text=myFont.render("Bin loot sucessful!",True,red)
            change_bg("C:/Users/ultra/bg.png")
        else:
            text=myFont.render("Better luck next time.",True,white)
            change_bg("C:/Users/ultra/restart.png")
        screen.blit(text,(250,40))
    else:
        change_bg("C:/Users/ultra/recyclebg.png")
        countdown=timingFont.render("Time Left:"+str(60-int(time_elapsed)),True,white)
        screen.blit(countdown,(20,10))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y>0:
                bin.rect.y-=5
        if keys[pygame.K_DOWN]:
            if bin.rect.y<630:
                bin.rect.y+=5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x<850:
                bin.rect.x+=5
        if keys[pygame.K_LEFT]:
            if bin.rect.x>0:
                bin.rect.x-=5
        item_hit_list=pygame.sprite.spritecollide(bin,item_list,True)
        plastic_hit_list=pygame.sprite.spritecollide(bin,plastic_list,True)
        for item in item_hit_list:
            score+=1
            text=myFont.render("ScOrE="+str(score),True,white)
        for plastic in plastic_hit_list:
            score-=5
            text=myFont.render("sCoRe="+str(score),True,white)
        screen.blit(text,(20,50))
        all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()