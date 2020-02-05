
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.mixer.init() 
pygame.mixer.music.load("TotoAfrica.mp3")
pygame.mixer.set_num_channels(274)
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(.05)
# Set the width and height of the screen [width, height]
size = (150, 200)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
start_time = time.clock()
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
timer=0
channel = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
    
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    
    if pygame.time.get_ticks()-timer > 1000:
        timer = pg.time.get_ticks()
        pygame.mixer.Channel(channel).play(pygame.mixer.music("TotoAfrica.mp3"))
        channel += 1

 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
