import pygame 

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

sprites=pygame.sprite.Group()

class Treat(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image=pygame.image.load("dogbone.png")
        self.image=pygame.transform.scale(self.image,(35,50))
        self.rect=self.image.get_rect()

        if self.rect.left<=0:
            self.rect.left=0
        elif self.rect.right>=WIDTH:
            self.rect.right=WIDTH
        if self .rect.top<=0:
            self.rect.top=0
        elif self.rect.bottom>=HEIGHT:
            self.rect.bottom=HEIGHT

sprites=pygame.sprite.Group()

def start_game():
    player=Player()
    sprites.add(player)
    treat=Treat()
    sprites.add(treat)

for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
        exit(0)
