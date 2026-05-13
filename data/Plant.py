import pygame

#-PLANT File 

#-Colors for the items
#-Leaf
LEAF = (0, 160, 0)
#-Stalk
STALK = (120, 200, 100)
#-Plant Pot
PLANT_BASE = (160, 82, 45)

#-Texture Path for leaves on the plant
FLOWER_TEX_PATH = "data/Assets/Leaves.jpg" 
flower_tex_surf = None

#-Function that draws the item and gets the position and scale of the item to be printed in the main file
def draw_plant(screen, pos=(0, 0), scale=1.0):
    global flower_tex_surf
    #-position of the plant
    x, y = pos

    #-TEXTURE SETUP

    # Try/catch to load texture once. If it fails, flower_tex_surf remains None.
    if flower_tex_surf is None:
        try:
            flower_tex_surf = pygame.image.load(FLOWER_TEX_PATH).convert_alpha()
        #Else, Mark as NULL
        except (FileNotFoundError, pygame.error):
            flower_tex_surf = "NULL" 

    # Helper function to draw a textured circle
    def draw_flower_head(center_x, center_y, radius):
        r = int(radius)
        if flower_tex_surf and flower_tex_surf != "NULL":
            # 1. Create a clear surface for the flower head
            surf = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
            
            # 2. Draw a white circle (the mask)
            pygame.draw.circle(surf, (255, 255, 255), (r, r), r)
            
            # 3. Scale texture to fit this specific flower size
            tex = pygame.transform.scale(flower_tex_surf, (r * 2, r * 2))
            
            # 4. Multiply: Texture * White Circle = Circular Texture
            surf.blit(tex, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            
            # 5. Draw to screen
            screen.blit(surf, (center_x - r, center_y - r))
        else:
            # Fallback: Solid Color
            pygame.draw.circle(screen, LEAF, (int(center_x), int(center_y)), r)

    #-DRAWING

    #-Stalk drawing using polygon
    pygame.draw.polygon(screen, STALK, [
        (x + 95*scale, y - 25*scale),
        (x + 105*scale, y - 25*scale),
        (x + 115*scale, y + 15*scale),
        (x + 85*scale, y + 15*scale)
    ])

    #-Flower heads (Using the textured helper)
    draw_flower_head(x + 100*scale, y - 65*scale, 42*scale)
    draw_flower_head(x + 70*scale, y - 45*scale, 32*scale)
    draw_flower_head(x + 130*scale, y - 45*scale, 32*scale)
    draw_flower_head(x + 85*scale, y - 95*scale, 26*scale)
    draw_flower_head(x + 115*scale, y - 95*scale, 26*scale)

    #-Pot
    pygame.draw.polygon(screen, PLANT_BASE, [
        (x + 40*scale, y),
        (x + 160*scale, y),
        (x + 130*scale, y + 70*scale),
        (x + 70*scale, y + 70*scale)
    ])