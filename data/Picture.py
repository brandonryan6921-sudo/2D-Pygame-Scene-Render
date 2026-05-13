import pygame

#-picture file

#-PICTURE (Fixed Scale Logic)
BROWN = (139, 69, 19)
SKY_BLUE = (135, 206, 235)
GREEN_BIG = (34, 139, 34)
GREEN_SMALL = (0, 100, 0)
WHITE = (255, 255, 255)

def draw_picture(screen, pos=(0, 0), scale=1.0):
    #-Position coordinates
    x, y = pos

    # Frame
    pygame.draw.rect(
        screen, BROWN,
        (x + 200 * scale, y + 100 * scale, 200 * scale, 200 * scale),
        max(1, int(10 * scale)) # Scales the border thickness too
    )

    # Sky
    pygame.draw.rect(
        screen, SKY_BLUE,
        (x + 210 * scale, y + 110 * scale, 180 * scale, 180 * scale)
    )

    # Big mountain
    pygame.draw.polygon(
        screen, GREEN_BIG,
        [
            (x + 230 * scale, y + 280 * scale),
            (x + 300 * scale, y + 200 * scale),
            (x + 370 * scale, y + 280 * scale)
        ]
    )

    # Small mountain
    pygame.draw.polygon(
        screen, GREEN_SMALL,
        [
            (x + 260 * scale, y + 280 * scale),
            (x + 330 * scale, y + 220 * scale),
            (x + 400 * scale, y + 280 * scale)
        ]
    )

    # Big peak
    pygame.draw.polygon(
        screen, WHITE,
        [
            (x + 287 * scale, y + 215 * scale),
            (x + 300 * scale, y + 192 * scale),
            (x + 313 * scale, y + 215 * scale)
        ]
    )

    # Small peak
    pygame.draw.polygon(
        screen, WHITE,
        [
            (x + 320 * scale, y + 235 * scale),
            (x + 330 * scale, y + 212 * scale),
            (x + 340 * scale, y + 235 * scale)
        ]
    )