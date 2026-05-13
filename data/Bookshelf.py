import pygame

#-BOOKSHELF

#-Colors for the bookshelf
LEGS_COLOUR = (101, 67, 33)
BASE_COLOUR = (160, 82, 45)
BOOK_COLOURS = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
                (255, 165, 0), (128, 0, 128)]

#-Function that draws the item and gets the position and scale of the item to be printed in the main file
def draw_bookshelf(screen, pos=(0, 0)):
    #-Position coordinates
    x, y = pos

    #-Draw legs
    pygame.draw.rect(screen, LEGS_COLOUR, (200 + x, 200 + y, 20, 30))
    pygame.draw.rect(screen, LEGS_COLOUR, (400 + x, 200 + y, 20, 30))

    #-Draw shelf base
    pygame.draw.rect(screen, BASE_COLOUR, (180 + x, 190 + y, 260, 10))

    #-five 5 vertical books

    # Book 1
    pygame.draw.rect(screen, BOOK_COLOURS[0], (190 + x, 140 + y, 20, 50))
    pygame.draw.rect(screen, (150, 0, 0), (190 + x, 140 + y, 20, 50), 2)
    pygame.draw.rect(screen, (255, 255, 255), (192 + x, 142 + y, 16, 10)) 
    #-Lines below white box
    pygame.draw.line(screen, (255,255,255), (192 + x, 155 + y), (206 + x, 155 + y), 2)
    pygame.draw.line(screen, (255,255,255), (192 + x, 160 + y), (206 + x, 160 + y), 2)
    pygame.draw.line(screen, (255,255,255), (192 + x, 165 + y), (206 + x, 165 + y), 2)

    #-Book 2
    pygame.draw.rect(screen, BOOK_COLOURS[1], (210 + x, 135 + y, 20, 55))
    pygame.draw.rect(screen, (0, 150, 0), (210 + x, 135 + y, 20, 55), 2)
    pygame.draw.rect(screen, (255, 255, 255), (212 + x, 137 + y, 16, 10))
    pygame.draw.line(screen, (255,255,255), (212 + x, 150 + y), (226 + x, 150 + y), 2)
    pygame.draw.line(screen, (255,255,255), (212 + x, 155 + y), (226 + x, 155 + y), 2)
    pygame.draw.line(screen, (255,255,255), (212 + x, 160 + y), (226 + x, 160 + y), 2)
    pygame.draw.line(screen, (255,255,255), (212 + x, 165 + y), (226 + x, 165 + y), 2)

    #-Book 3
    pygame.draw.rect(screen, BOOK_COLOURS[2], (230 + x, 145 + y, 20, 45))
    pygame.draw.rect(screen, (0, 0, 150), (230 + x, 145 + y, 20, 45), 2)
    pygame.draw.rect(screen, (255, 255, 255), (232 + x, 147 + y, 16, 10))
    pygame.draw.line(screen, (255,255,255), (232 + x, 160 + y), (246 + x, 160 + y), 2)
    pygame.draw.line(screen, (255,255,255), (232 + x, 165 + y), (246 + x, 165 + y), 2)
    pygame.draw.line(screen, (255,255,255), (232 + x, 170 + y), (246 + x, 170 + y), 2)
    pygame.draw.line(screen, (255,255,255), (232 + x, 175 + y), (246 + x, 175 + y), 2)
    
    #-Book 4
    pygame.draw.rect(screen, BOOK_COLOURS[3], (250 + x, 130 + y, 20, 60))
    pygame.draw.rect(screen, (200, 100, 0), (250 + x, 130 + y, 20, 60), 2)
    pygame.draw.rect(screen, (255, 255, 255), (252 + x, 132 + y, 16, 10))
    pygame.draw.line(screen, (255,255,255), (252 + x, 145 + y), (266 + x, 145 + y), 2)
    pygame.draw.line(screen, (255,255,255), (252 + x, 150 + y), (266 + x, 150 + y), 2)
    pygame.draw.line(screen, (255,255,255), (252 + x, 155 + y), (266 + x, 155 + y), 2)
    pygame.draw.line(screen, (255,255,255), (252 + x, 160 + y), (266 + x, 160 + y), 2)
    pygame.draw.line(screen, (255,255,255), (252 + x, 165 + y), (266 + x, 165 + y), 2)

    #-Book 5
    pygame.draw.rect(screen, BOOK_COLOURS[4], (270 + x, 150 + y, 20, 40))
    pygame.draw.rect(screen, (80, 0, 80), (270 + x, 150 + y, 20, 40), 2)
    pygame.draw.rect(screen, (255, 255, 255), (272 + x, 152 + y, 16, 10))
    pygame.draw.line(screen, (255,255,255), (272 + x, 165 + y), (286 + x, 165 + y), 2)
    pygame.draw.line(screen, (255,255,255), (272 + x, 170 + y), (286 + x, 170 + y), 2)
    pygame.draw.line(screen, (255,255,255), (272 + x, 175 + y), (286 + x, 175 + y), 2)
    pygame.draw.line(screen, (255,255,255), (272 + x, 180 + y), (286 + x, 180 + y), 2)
    pygame.draw.line(screen, (255,255,255), (272 + x, 185 + y), (286 + x, 185 + y), 2)