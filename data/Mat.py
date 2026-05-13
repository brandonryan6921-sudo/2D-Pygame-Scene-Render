import pygame

#-Mat File

#-Colors for the mat
MAT_OUTER_BORDER = (51, 51, 51)
MAT_INNER_BORDER = (102, 102, 102)
MAT_MAIN_COLOR = (230, 230, 230)
LINE_COLOR = (0, 0, 0)

#-Function that draws the item and gets the position and scale of the item to be printed in the main file
def draw_mat(screen, pos=(0, 0), scale=1.0):
    #-Positions for the mat
    x, y = pos

    #-Mat Boarder
    pygame.draw.rect(screen, MAT_OUTER_BORDER, (x + 0*scale,  y + 0*scale,  400*scale, 200*scale))
    pygame.draw.rect(screen, MAT_INNER_BORDER, (x + 5*scale,  y + 5*scale,  390*scale, 190*scale))
    pygame.draw.rect(screen, MAT_MAIN_COLOR,   (x + 25*scale, y + 25*scale, 350*scale, 150*scale))
    #-Inside the Mat (lines for more detail)
    pygame.draw.line(screen, LINE_COLOR, (x + 80*scale, y + 40*scale),  (x + 320*scale, y + 40*scale),  max(1, int(1*scale)))
    pygame.draw.line(screen, LINE_COLOR, (x + 70*scale, y + 60*scale),  (x + 330*scale, y + 60*scale),  max(1, int(1*scale)))
    pygame.draw.line(screen, LINE_COLOR, (x + 60*scale, y + 80*scale),  (x + 340*scale, y + 80*scale),  max(1, int(1*scale)))
    pygame.draw.line(screen, LINE_COLOR, (x + 50*scale, y + 100*scale), (x + 350*scale, y + 100*scale), max(1, int(1*scale)))
    pygame.draw.line(screen, LINE_COLOR, (x + 60*scale, y + 120*scale), (x + 340*scale, y + 120*scale), max(1, int(1*scale)))
    pygame.draw.line(screen, LINE_COLOR, (x + 70*scale, y + 140*scale), (x + 330*scale, y + 140*scale), max(1, int(1*scale)))
    pygame.draw.line(screen, LINE_COLOR, (x + 80*scale, y + 160*scale), (x + 320*scale, y + 160*scale), max(1, int(1*scale)))