import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Båtspel')


#spel variabler
game_over = 0
x1 = 400
y1 = 100
x2 = 80
y2 = 80


#bilder
background = pygame.image.load(r'images\baby-blue-color-solid-background-1920x1080.png')

class Main():

    main_menu = True
    while main_menu:
        def __init__(Men, x, y):
            kamel = pygame.image.load(r'images/pixelart_logs_2.png')
            Men.image = pygame.transform.scale(kamel, (40, 70))
            Men.rect = Men.image.get_rect()
            Men.rect.x = x
            Men.rect.y = y

        def update(Men):

            screen.blit(Men.image, Men.rect)


class Obstacle():
        def __init__(Kam, x, y):
            kamel = pygame.image.load(r'images/pixelart_logs_2.png')
            Kam.image = pygame.transform.scale(kamel, (40, 70))
            Kam.rect = Kam.image.get_rect()
            Kam.rect.x = x
            Kam.rect.y = y


            # ändring
        def update(Kam):
            dx = 0
            dy = 2

            Kam.rect.x += dx
            Kam.rect.y += dy

            number = random.randint(0, 700)

            if Kam.rect.top > 700:
                Kam.rect.top = 0

            if Kam.rect.top == 0:
                Kam.rect.right = number

            screen.blit(Kam.image, Kam.rect)


Obstacle = Obstacle(x2, y2)

class Player():
        def __init__(self, x, y):
            boat = pygame.image.load(r'images/Pixelart_boat_3.png')
            self.image = pygame.transform.scale(boat, (50, 150))
            self.rect = self.image.get_rect()
            self.width = self.image.get_width()
            self.height = self.image.get_height()
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

            screen.blit(self.image, self.rect)

Player = Player(x1, y1)


run = False
main_menu = False
if main_menu == True:
    Main.update()


if main_menu == False:
    run = True


while run:


            # Setting the framerate to 60fps
    clock.tick(fps)

    collide = pygame.Rect.colliderect(Player.rect, Obstacle.rect)

            # If the objects are colliding
            # then changing the y coordinate
    if collide:
        Obstacle.rect.bottom = Player.rect.top
        pygame.quit()

            # Updating the display surface

    screen.blit(background, (0, 0))
    Obstacle.update()
    Player.update()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
