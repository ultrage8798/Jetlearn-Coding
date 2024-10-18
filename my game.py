import pygame 
import random

pygame.init()

WIDTH=700
HEIGHT=500

screen=pygame.display.set_mode([WIDTH,HEIGHT])

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("dog.png")
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()
        self.rect.x=WIDTH//2
        self.rect.y=HEIGHT//2

    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)

        if self.rect.left<=0:
            self.rect.left=0
        elif self.rect.right>=WIDTH:
            self.rect.right=WIDTH
        if self .rect.top<=0:
            self.rect.top=0
        elif self.rect.bottom>=HEIGHT:
            self.rect.bottom=HEIGHT

#sprites=pygame.sprite.Group()

class Treat(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image=pygame.image.load("dogbone.png")
        self.image=pygame.transform.scale(self.image,(35,50))
        self.rect=self.image.get_rect()

        self.rect.x=random.randint(0,WIDTH-self.rect.width)
        self.rect.y=random.randint(0,HEIGHT-self.rect.height)

    def respawn(self):
        self.rect.x=random.randint(0,WIDTH-self.rect.width)
        self.rect.y=random.randint(0,HEIGHT-self.rect.height)

all_sprites=pygame.sprite.Group()

treats=pygame.sprite.Group()

def start_game():
    player=Player()
    all_sprites.add(player)
    treat=Treat()
    treats.add(treat)
    all_sprites.add(treat)
    return player

player=start_game()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
    pressed_keys=pygame.key.get_pressed()
    all_sprites.update(pressed_keys)
    if pygame.sprite.spritecollide(player,treats,False,pygame.sprite.collide_rect):
        print("Collision detected.")
        for treat in treats:
            treat.respawn()
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.delay(30)
