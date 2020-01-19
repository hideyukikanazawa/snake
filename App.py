import pygame
import time
from random import randint
import random
import numpy as np
pygame.init()

vel = 15
x_scale = 20
y_scale = 16
window_x = vel * x_scale
window_y = vel * y_scale


bg = pygame.image.load('dungeon.png')
bg = pygame.transform.scale(bg, (window_x, window_y))
apple_image = pygame.image.load('apple.png')
apple_image = pygame.transform.scale(apple_image, (vel, vel))
snakebodyimage = pygame.image.load('snakebody.png')
snakebodyimage = pygame.transform.scale(snakebodyimage, (vel, vel))

win = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("First game")


class SnakeHead(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = vel
        self.height = vel

    def draw(self, win):
        pygame.draw.rect(win, (40, 255, 80), (self.x, self.y, self.width, self.height))


class SnakeBody(object):
    def __init__(self, segments, width, height):
        self.segments = []
        self.width = vel
        self.height = vel

    def draw(self, win):
        for segment in self.segments:
            win.blit(snakebodyimage, (segment[0], segment[1]))

    def extend(self):
        if len(self.segments) == 0:
            self.segments.append([headState[0], headState[1]])
        else:
            self.segments.append([tailState[0], tailState[1]])

    def follow(self):
        for i in range(1, len(self.segments)):
            self.segments[i] = self.segments[i-1]
        self.segments[0] = headState


class Food(object):
    def __init__(self):
        self.x = randint(0, x_scale-1) * vel
        self.y = randint(0, y_scale-1) * vel
        self.width = vel
        self.height = vel

    def draw(self, win):
        # pygame.draw.rect(win, (255, 30, 30), (self.x, self.y, self.width, self.height))
        win.blit(apple_image, (self.x, self.y))

    def randomizePosition(self):
        for segment in body.segments:
            possiblespawns.remove(segment[0] / vel + segment[1] / vel * x_scale)
        possiblespawns.remove(head.x / vel + head.y / vel * x_scale)
        location = random.choice(possiblespawns)
        self.x = location % x_scale * vel
        self.y = (location // x_scale - 1) * vel
        print(self.x, self.y)

def redrawGameWindow():
    win.blit(bg, (0,0))
    head.draw(win)
    body.draw(win)
    apple.draw(win)
    pygame.display.update()


clock = pygame.time.Clock()

movement = [vel, 0]
head = SnakeHead(int(window_x / 2), int(window_y / 2), vel, vel)
body = SnakeBody([], vel, vel)
apple = Food()

running = True
while running:
    clock.tick(8)
    headState = [head.x, head.y]
    possiblespawns = list(range(0, 360))
    if len(body.segments) != 0:
        tailState = [body.segments[-1][0], body.segments[-1][1]]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if head.x < 0 or head.x > window_x + vel or head.y < 0 or head.y > window_y + vel:
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

    head.x += movement[0]
    head.y += movement[1]
    if len(body.segments) != 0:
        body.follow()
    if head.x == apple.x and head.y == apple.y:
        body.extend()
        print(head.x, head.y)
        print(body.segments)
        apple.randomizePosition()

    redrawGameWindow()


pygame.quit()