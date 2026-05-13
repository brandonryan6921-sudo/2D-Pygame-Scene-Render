import pygame

#-Clock File

#-Function that draws the item and gets the position and scale of the item to be printed in the main file
def draw_clock(screen, pos=(0,0), scale=1.0):
    #Position coordinates
    x, y = pos
    
    #-1. The Clock Face
    # Yellow Border 
    pygame.draw.circle(screen, (255, 255, 0), (x, y), int(110 * scale))
    #-White Face (Inside Clock)
    pygame.draw.circle(screen, (255, 255, 255), (x, y), int(100 * scale))

    #-Times
    #-12 o clock
    pygame.draw.line(screen, (0,0,0), (x, y - int(95*scale)), (x, y - int(75*scale)), int(5*scale) or 1)
    #-1 o clock
    pygame.draw.line(screen, (0,0,0), (x + int(47*scale), y - int(87*scale)), (x + int(39*scale), y - int(72*scale)), int(2*scale) or 1)
    #-2 o clock
    pygame.draw.line(screen, (0,0,0), (x + int(82*scale), y - int(47*scale)), (x + int(65*scale), y - int(38*scale)), int(2*scale) or 1)
    #-3 o clock
    pygame.draw.line(screen, (0,0,0), (x + int(95*scale), y), (x + int(75*scale), y), int(5*scale) or 1)
    #-4 o clock
    pygame.draw.line(screen, (0,0,0), (x + int(82*scale), y + int(47*scale)), (x + int(65*scale), y + int(37*scale)), int(2*scale) or 1)
    #-5 o clock
    pygame.draw.line(screen, (0,0,0), (x + int(47*scale), y + int(87*scale)), (x + int(39*scale), y + int(72*scale)), int(2*scale) or 1)
    #-6 o clock
    pygame.draw.line(screen, (0,0,0), (x, y + int(95*scale)), (x, y + int(75*scale)), int(5*scale) or 1)
    #-7 o clock
    pygame.draw.line(screen, (0,0,0), (x - int(47*scale), y + int(87*scale)), (x - int(39*scale), y + int(72*scale)), int(2*scale) or 1)
    #-8 o clock
    pygame.draw.line(screen, (0,0,0), (x - int(82*scale), y + int(47*scale)), (x - int(65*scale), y + int(37*scale)), int(2*scale) or 1)
    #-9 o clock
    pygame.draw.line(screen, (0,0,0), (x - int(95*scale), y), (x - int(75*scale), y), int(5*scale) or 1)
    #-10 o clock
    pygame.draw.line(screen, (0,0,0), (x - int(82*scale), y - int(47*scale)), (x - int(65*scale), y - int(38*scale)), int(2*scale) or 1)
    #-11 o-clock
    pygame.draw.line(screen, (0,0,0), (x - int(47*scale), y - int(87*scale)), (x - int(39*scale), y - int(72*scale)), int(2*scale) or 1)

    #-3. The Hands (Time: 9:20:30)
    
    #-Hour Hand 
    pygame.draw.line(screen, (0,0,0), (x, y), (x - int(45*scale), y - int(15*scale)), int(6*scale) or 1)

    #-Minute Hand
    pygame.draw.line(screen, (0,0,0), (x, y), (x + int(60*scale), y + int(35*scale)), int(4*scale) or 1)

    #-Second Hand 
    pygame.draw.line(screen, (255,0,0), (x, y), (x, y + int(80*scale)), int(2*scale) or 1)

    #-Center Nub
    pygame.draw.circle(screen, (0,0,0), (x, y), int(5*scale))