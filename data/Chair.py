import pygame

#-CHAIR File

#-Colors
C_DARK = (40, 44, 52)      # Dark gray for seat/back
C_SILVER = (180, 180, 180) # Silver/light gray for metal base
C_WHEEL = (20, 20, 20)     # Black for wheels

#-Border Colors
BORDER_BLACK = (0, 0, 0)
BORDER_STAND = (100, 100, 100) 

#-Function that draws the item and gets the position and scale of the item to be printed in the main file
def draw_chair(screen, pos=(300, 220), scale=1.0):
    #-Position coordinates
    x, y = pos
    
    #-SEAT & BACK of chair
    
    #-Backrest
    pygame.draw.rect(screen, C_DARK, (x + -10*scale, y + -170*scale, 40*scale, 180*scale), border_radius=15)
    pygame.draw.rect(screen, BORDER_BLACK, (x + -10*scale, y + -170*scale, 40*scale, 180*scale), max(1, int(2 * scale)), border_radius=15)

    #-Seat Base
    pygame.draw.rect(screen, C_DARK, (x + 0*scale, y + 0*scale, 150*scale, 30*scale), border_radius=8)
    pygame.draw.rect(screen, BORDER_BLACK, (x + 0*scale, y + 0*scale, 150*scale, 30*scale), max(1, int(2 * scale)), border_radius=10)

    #-Armrest Top
    pygame.draw.rect(screen, C_DARK, (x + 20*scale, y + -30*scale, 70*scale, 15*scale), border_radius=5)
    pygame.draw.rect(screen, BORDER_BLACK, (x + 20*scale, y + -30*scale, 70*scale, 15*scale), max(1, int(2 * scale)), border_radius=10)

    #-Armrest Vertical
    pygame.draw.rect(screen, C_DARK, (x + 20*scale, y + -30*scale, 15*scale, 60*scale))
    pygame.draw.rect(screen, BORDER_BLACK, (x + 20*scale, y + -30*scale, 15*scale, 60*scale), max(1, int(2 * scale)))

    #-STAND 
    
    #-Cylinder Stand
    pygame.draw.rect(screen, C_SILVER, (x + 65*scale, y + 30*scale, 15*scale, 80*scale), border_radius=5)
    pygame.draw.rect(screen, BORDER_STAND, (x + 65*scale, y + 30*scale, 15*scale, 80*scale), max(1, int(2 * scale)), border_radius=10)

    #-Legs
    pygame.draw.line(screen, C_SILVER, (x + 72*scale, y + 110*scale), (x + -28*scale, y + 140*scale), max(1, int(15*scale)))
    pygame.draw.line(screen, C_SILVER, (x + 72*scale, y + 110*scale), (x + 172*scale, y + 140*scale), max(1, int(15*scale)))
    
    #-Wheels
    pygame.draw.circle(screen, C_WHEEL, (x + -28*scale, y + 140*scale), 12*scale)
    pygame.draw.circle(screen, C_WHEEL, (x + 172*scale, y + 140*scale), 12*scale)
    
    #-Wheel highlights
    pygame.draw.circle(screen, (255, 255, 255), (x + -28*scale, y + 140*scale), 5*scale)
    pygame.draw.circle(screen, (255, 255, 255), (x + 172*scale, y + 140*scale), 5*scale)