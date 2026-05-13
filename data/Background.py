import pygame
#-Background File

#-IMAGE PATHS FOR THE TEXTURE FLOORING
FLOOR_IMAGE_PATH = "data/Assets/FLOOR-min.jpg"

#-COLORS for background
WHITESMOKE = (161, 150, 142)
TAN = (211, 189, 167)
WHITE = (255, 255, 255)

#-Global variable for floor
floor_surf = None

#-Function that draws the item and gets the position and scale of the item to be printed in the main file
def draw_background(screen, width, height):
    global floor_surf

    #-1. WALL
    pygame.draw.rect(screen, WHITESMOKE, (0, 0, width, 360))

    #-2. TRIM
    pygame.draw.rect(screen, WHITE, (0, 280, width, 30))

    #-3. FLOOR TEXTURE
    floor_rect = (0, 300, width, 180)

    #-Load floor image only once
    if floor_surf is None:
        try:
            img = pygame.image.load(FLOOR_IMAGE_PATH).convert()
            floor_surf = pygame.transform.scale(img, (floor_rect[2], floor_rect[3]))
        #-throw exception warning if the texture does not load
        except (FileNotFoundError, pygame.error):
            print(f"Warning: Could not load {FLOOR_IMAGE_PATH}, using color.")
            floor_surf = pygame.Surface((floor_rect[2], floor_rect[3]))
            floor_surf.fill(TAN)

    screen.blit(floor_surf, (floor_rect[0], floor_rect[1]))