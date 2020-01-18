import pygame
import time
from random import randint

pygame.init()

vel = 15
x_scale = 20
y_scale = 16
window_x = vel * x_scale
window_y = vel * y_scale

possibleSpawn = range(0, window_x, 10)
bg = pygame.image.load('dungeon.png')
bg = pygame.transform.scale(bg, (window_x, window_y))

win = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("First game")


class snake(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = vel
        self.height = vel
    def draw(self, win):
        pygame.draw.rect(win, (40, 255, 80), (self.x, self.y, self.width, self.height))

class food(object):
    def __init__(self):
        self.x = randint(0, x_scale-1) * vel
        self.y = randint(0, y_scale-1) * vel
        self.width = vel
        self.height = vel

    def draw(self, win):
        pygame.draw.rect(win, (255, 30, 30), (self.x, self.y, self.width, self.height))
v
    def randomizePosition(self):
        self.x = randint(0, window_x/10) * 10
        self.y = randint(0, window_y/10) * 10

def redrawGameWindow():
    win.blit(bg, (0,0))
    snakey.draw(win)
    apple.draw(win)
    pygame.display.update()


clock = pygame.time.Clock()

movement = [vel, 0]
snakey = snake(int(window_x/2), int(window_y/2), vel, vel)
apple = food()

running = True
while running:
    clock.tick(8)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if snakey.x < 0 or snakey.x > window_x + vel or snakey.y < 0 or snakey.y > window_y + vel:
        running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and movement != [vel, 0]:
        movement = [-vel, 0]
    elif keys[pygame.K_RIGHT] and movement != [-vel, 0]:
        movement = [vel, 0]
    elif keys[pygame.K_UP] and movement != [0, vel]:
        movement = [0, -vel]
    elif keys[pygame.K_DOWN] and movement != [0, -vel]:
        movement = [0, vel]

    snakey.x += movement[0]
    snakey.y += movement[1]

    redrawGameWindow()


pygame.quit()