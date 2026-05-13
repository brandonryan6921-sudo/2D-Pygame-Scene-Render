import pygame

#-Table File for all the items of the table which includes the monitor, lamp etc..

#-Colors For the items of the table (Table, Monitor)
WOOD = (160, 110, 60)
WOOD_2 = (104, 71, 39)
LEGS = (110, 70, 40)
Monitor_body = (3, 23, 38)
Monitor_border = (200, 200, 200)
Button_colour = (255, 0, 0)
Monitor_arm_colour = (0, 0, 0)

#-Colours for the keyboard and mouse
KEYBOARD_BASE = (50, 50, 50)
KEY_COLOR = (200, 200, 200)
MOUSE_BODY = (220, 220, 220)
MOUSE_CLICK = (40, 40, 40) 

#-Function that draws the item and gets the position and scale of the item to be printed in the main file
def draw_table(screen, pos=(0,0), scale=1.0):
    #Position coordinates
    x, y = pos

    #-TABLE Drawing

    #-Table Legs 
    pygame.draw.rect(screen, LEGS, (x + 160 * scale, y + 190 * scale, 10 * scale, 100 * scale))   # Left front
    pygame.draw.rect(screen, LEGS, (x + 460 * scale, y + 190 * scale, 10 * scale, 100 * scale))   # Right front
    pygame.draw.rect(screen, LEGS, (x + 190 * scale, y + 150 * scale, 10 * scale, 90 * scale))    # Left back
    pygame.draw.rect(screen, LEGS, (x + 430 * scale, y + 150 * scale, 10 * scale, 90 * scale))    # Right back
    
    #-TableTop:

    #-Surface
    pygame.draw.rect(screen, WOOD, (x + 150 * scale, y + 150 * scale, 330 * scale, 40 * scale))   
    #-Edge
    pygame.draw.rect(screen, WOOD_2, (x + 150 * scale, y + 190 * scale, 330 * scale, 10 * scale)) 

    #-MONITOR 

    #-Monitor Screen
    monitor_rect = pygame.Rect(x + 225 * scale, y + 40 * scale, 160 * scale, 80 * scale)
    pygame.draw.rect(screen, Monitor_body, monitor_rect)
    pygame.draw.rect(screen, Monitor_border, monitor_rect, int(6 * scale))

    #-Monitor Buttons 
    pygame.draw.circle(screen, Button_colour, (x + int(340 * scale), y + int(117 * scale)), int(3 * scale))
    pygame.draw.circle(screen, Button_colour, (x + int(355 * scale), y + int(117 * scale)), int(3 * scale))
    pygame.draw.circle(screen, Button_colour, (x + int(370 * scale), y + int(117 * scale)), int(3 * scale))

    #-MONITOR ARM 
    
    #-Horizontal arm
    pygame.draw.line(screen, Monitor_arm_colour, (x + 210 * scale, y + 112 * scale), (x + 225 * scale, y + 110 * scale), max(1, int(8 * scale)))
    pygame.draw.circle(screen, Monitor_arm_colour, (x + int(208 * scale), y + int(112 * scale)), int(8 * scale))
    
    #-Vertical arm
    pygame.draw.line(screen, Monitor_arm_colour, (x + 206 * scale, y + 115 * scale), (x + 206 * scale, y + 145 * scale), max(1, int(8 * scale)))
    pygame.draw.circle(screen, Monitor_arm_colour, (x + int(206 * scale), y + int(145 * scale)), int(8 * scale))
    
    #-Diagonal & Base of Monitor
    pygame.draw.line(screen, Monitor_arm_colour, (x + 206 * scale, y + 145 * scale), (x + 300 * scale, y + 155 * scale), max(1, int(8 * scale)))
    pygame.draw.line(screen, Monitor_arm_colour, (x + 300 * scale, y + 125 * scale), (x + 300 * scale, y + 155 * scale), max(1, int(10 * scale)))
    
    #-Second Monitor Base
    pygame.draw.rect(screen, Monitor_arm_colour, (x + 285 * scale, y + 155 * scale, 30 * scale, 12 * scale))
    pygame.draw.rect(screen, Monitor_arm_colour, (x + 270 * scale, y + 167 * scale, 60 * scale, 8 * scale))

    #-KEYBOARD
    
    #-Base Position
    kb_x, kb_y = x + 170 * scale, y + 165 * scale
    
    #-Keyboard Base 
    pygame.draw.rect(screen, KEYBOARD_BASE, (kb_x, kb_y, 65 * scale, 20 * scale), border_radius=int(2*scale))
    
    #- Three (3) Rows for the keyboard
    #-Row 1 (Top) 
    r1_y = kb_y + 2 * scale
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 3.0 * scale, r1_y, 4 * scale, 4 * scale)) # Key 1
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 8.5 * scale, r1_y, 4 * scale, 4 * scale)) # Key 2
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 14.0 * scale, r1_y, 4 * scale, 4 * scale)) # Key 3
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 19.5 * scale, r1_y, 4 * scale, 4 * scale)) # Key 4
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 25.0 * scale, r1_y, 4 * scale, 4 * scale)) # Key 5
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 30.5 * scale, r1_y, 4 * scale, 4 * scale)) # Key 6
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 36.0 * scale, r1_y, 4 * scale, 4 * scale)) # Key 7
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 41.5 * scale, r1_y, 4 * scale, 4 * scale)) # Key 8
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 47.0 * scale, r1_y, 4 * scale, 4 * scale)) # Key 9
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 52.5 * scale, r1_y, 4 * scale, 4 * scale)) # Key 10

    #-Row 2
    r2_y = kb_y + 7.5 * scale
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 3.0 * scale, r2_y, 4 * scale, 4 * scale)) # Key 1
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 8.5 * scale, r2_y, 4 * scale, 4 * scale)) # Key 2
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 14.0 * scale, r2_y, 4 * scale, 4 * scale)) # Key 3
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 19.5 * scale, r2_y, 4 * scale, 4 * scale)) # Key 4
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 25.0 * scale, r2_y, 4 * scale, 4 * scale)) # Key 5
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 30.5 * scale, r2_y, 4 * scale, 4 * scale)) # Key 6
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 36.0 * scale, r2_y, 4 * scale, 4 * scale)) # Key 7
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 41.5 * scale, r2_y, 4 * scale, 4 * scale)) # Key 8
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 47.0 * scale, r2_y, 4 * scale, 4 * scale)) # Key 9
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 52.5 * scale, r2_y, 4 * scale, 4 * scale)) # Key 10

    #-Row 3
    r3_y = kb_y + 13 * scale
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 3.0 * scale, r3_y, 4 * scale, 4 * scale)) # Key 1
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 8.5 * scale, r3_y, 4 * scale, 4 * scale)) # Key 2
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 14.0 * scale, r3_y, 4 * scale, 4 * scale)) # Key 3
    #-Spacebar of keyboard
    spacebar_width = (4 * scale * 4) + (4.5 * scale)
    pygame.draw.rect(screen, KEY_COLOR, (kb_x + 19.5 * scale, r3_y, spacebar_width, 4 * scale))

    #-MOUSE
    
    #-Base Position
    mx, my = x + 245 * scale, y + 165 * scale
    
    #-Mouse Body (16 x 22)
    pygame.draw.ellipse(screen, MOUSE_BODY, (mx, my, 16 * scale, 22 * scale))
    
    #-Left button 
    pygame.draw.rect(screen, MOUSE_CLICK, (mx + 2*scale, my + 2*scale, 5 * scale, 8 * scale), border_radius=int(2 * scale))
    #-Right button 
    pygame.draw.rect(screen, MOUSE_CLICK, (mx + 9*scale, my + 2*scale, 5 * scale, 8 * scale), border_radius=int(2 * scale))
    
    #-Seperation of left and right click buttons
    pygame.draw.line(screen, (10, 10, 10), (mx + 8*scale, my + 3*scale), (mx + 8*scale, my + 7*scale), int(1*scale))


    #-LAMP

    #-GLOW EFFECT
    for radius, alpha in [(28, 120), (40, 80), (55, 45)]:  
        glow_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, (255, 255, 150, alpha), (radius, radius), radius)
        screen.blit(glow_surface, (530 - radius, 200 - radius))

    #-BULB
    # Brightness
    pygame.draw.circle(screen, (255, 255, 255), (530, 200), 7)       
    pygame.draw.circle(screen, (255, 255, 180), (530, 200), 12, 2)    

    #-Lamp shade
    pygame.draw.arc(screen, (2,2,2), (495, 182, 80, 100), 0, 3.5/2, 6)

    #-Base parts of the lamp
    pygame.draw.rect(screen, (225, 225, 225), (x + 405 * scale, y + 105 * scale, 25 * scale, 20 * scale), border_radius=6)
    pygame.draw.rect(screen, (225, 225, 225), (x + 445 * scale, y + 142 * scale, 12 * scale, 22 * scale), border_radius=6)
    pygame.draw.rect(screen, (2, 2, 2), (x + 440 * scale, y + 162 * scale, 22 * scale, 16 * scale), border_radius=6)
    pygame.draw.rect(screen, (50, 70, 90), (x + 420 * scale, y + 175 * scale, 50 * scale, 11 * scale), border_radius=5)