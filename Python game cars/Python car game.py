import pygame
from pygame.locals import *
import random

pygame.init()

#window
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

#markers size
marker_width = 10
marker_height = 10

#read and edge the markers
road = (100, 0, 300, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

#x cordinates of lanes
left_lane = 150
center_lane = 250
right_lane = 350
lanes = (left_lane, center_lane, right_lane)

#for animated move of the lane markers
lane_marker_move_y = 0

class Vehicle(pygame.sprite.Sprite):

    def __int__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

    #scale the image down so it fits the lane
    image_scale = 45 / image.get_rect().width
    new_width = image.get_rect().width * image_scale
    new_height = image.get_rect().height * image_scale
    self.image = pygame.transform.scale(image, (new_width, new_height))

    self.rect = self.image.get_rect()
    self.rect.center = [x, y]

class PlayerVehicle(Vehicle):
    def __int__(self, x, y):
        image = pygame.image.load('CAR IMAGE.png')
        super().__int__(image, x, y)
#player's starring cordinates
player_x = 250
player_y = 400

#colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

#game settings
gameover = False
speed = 2
score = 50

#timer
clock = pygame.time.Clock()
fps = 120
running = True

while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    #draw grass
    screen.fill(green)

    #draw road
    pygame.draw.rect(screen, gray, road)

    #draw value markers
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    #draw the lane markers
    lane_marker_move_y += 2 * speed
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, marker_width * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

    pygame.display.update()

pygame.quit()
