import pygame
import sys

#-MAIN file that prints out all the other files and blends into into one scene

#-All files for the project
from data.Background import draw_background
from data.Table import draw_table
from data.Chair import draw_chair
from data.Plant import draw_plant
from data.Bookshelf import draw_bookshelf
from data.Clock import draw_clock
from data.Picture import draw_picture
from data.Mat import draw_mat



pygame.init()

#-Screen scene size
WIDTH, HEIGHT = 800, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Room Scene")

#-To run program
clock = pygame.time.Clock()

#-CONTROL positions for each item here
table_pos = (30, 50)
chair_pos = (80, 320) 
plant_pos = (600, 350)
bookshelf_pos = (350, -100)
clock_pos = (150, 80)
picture_pos = (550, 100)  
mat_pos = (320, 350)     

#-Extra plant to be placed on the table
plant_pos_2 = (440, 250)     


#-These lines run the pygame program
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #-Draw all elements/items 
    draw_background(screen, WIDTH, HEIGHT)
    draw_table(screen, pos=table_pos, scale=1.2)
    draw_chair(screen, pos=chair_pos, scale=0.8)
    draw_plant(screen, pos=plant_pos, scale=0.8)
    draw_bookshelf(screen, pos=bookshelf_pos)
    draw_clock(screen, pos=clock_pos, scale=0.4)
    draw_picture(screen, pos=picture_pos, scale=0.4)  
    draw_mat(screen,pos=mat_pos, scale= 0.4)
    #-Second Plant
    draw_plant(screen, pos=plant_pos_2, scale=0.3)

    pygame.display.flip()
    clock.tick(60)

#End of file
pygame.quit()
sys.exit()