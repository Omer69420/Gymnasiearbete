import pygame
pygame.init()

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Båtspel')


background = pygame.image.load(r'images\baby-blue-color-solid-background-1920x1080.png')

class Obstacle():

    def __init__(self, x, y):
        kamel = pygame.image.load(r'images\hari-nandakumar-5U132F-itpg-unsplash.jpg')
        self.image = pygame.transform.scale(kamel, (30, 59))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # ändring
    def update(self):
        dx = 0
        dy = 5

        self.rect.x += dx
        self.rect.y += dy

        screen.blit(self.image, self.rect)

Obstacle = Obstacle(80, 80)

Obstacle.update()

class Player():

    def __init__(self, x, y):
        boat = pygame.image.load(r'images\Pixelart_boat.png')
        self.image = pygame.transform.scale(boat, (170, 170))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # ändring
    # get keypresses
    def update(self):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            dy -= 7
        if key[pygame.K_DOWN]:
            dy += 7
        if key[pygame.K_LEFT]:
            dx -= 7
        if key[pygame.K_RIGHT]:
            dx += 7

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

        if self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0


        #rita båten
        screen.blit(self.image, self.rect)

Player = Player(100, 100)

run = True
while run:

    screen.blit(background, (0, 0))
    Obstacle.update()

    Player.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
