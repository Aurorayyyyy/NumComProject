import pygame
import os
import numpy as np
import time

os.environ["SDL_VIDEO_CENTERED"]='1'

width = 1600
height = 1200
# h,k = (width//2, height//2)

white, black = (230, 230, 230), (15, 15, 15)
# orange, color = (255, 123, 0), (255, 23, 46)
blue = (0, 166, 255)
base_color = (100, 100, 100)



size = (width, height)
pygame.display.set_caption("Cardioid simulation of ")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()  #set frame rate

point = 200

fps = 30
# radius = 200
previous = 1
angle = 0
factor = 0

list_of_cycles = []
list_of_p = []
list_of_radius = []
list_of_color = []

def partition(point: int, r: int, h:int, k: int):
    angle = 360 / point
    p = {}
    for i in range(point):
        p[i] = (r * np.cos(angle * i * np.pi / 180))+h, (r * np.sin(angle * i * np.pi / 180))+k
    return p

run = True

while run:
    clock.tick(fps)
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if user close the window -> quit game
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            list_of_cycles.append((mouse_x, mouse_y))
            radius = np.random.randint(40, 300)
            list_of_radius.append(radius)
            p = partition(point, radius, h=mouse_x, k=mouse_y)
            list_of_p.append(p)
            R = np.random.randint(0, 255)
            G = np.random.randint(0, 255)
            B = np.random.randint(0, 255)
            color = (R, G, B)
            list_of_color.append(color)
    
    for p_index in range(len(list_of_p)):
        for i in range(point):
            p = list_of_p[p_index]
            color = list_of_color[p_index]
            pygame.draw.circle(screen, color, (list_of_cycles[p_index][0],list_of_cycles[p_index][1]), list_of_radius[p_index], 3)
            # print(p)
            link = int((i * factor) % point)
            x, y = p[i]  # starting point
            x1, y1 = p[link]  # end point
            alpha = int(255 * (1 - abs((factor % 2) - 1)))
            pygame.draw.line(screen, (color[0], color[1], color[2], alpha), (x, y), (x1, y1), width=1)
        
    pygame.display.update()
    factor += 0.01

    
    
pygame.quit()