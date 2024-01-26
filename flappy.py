import pygame
# Initialize the game
pygame.init()

# Set up the game window
window_width = 500
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flappy Bird")

# Set the background color
background_color = (135, 206, 250)  # Light blue color

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update game logic here
    
    # Draw game elements here
    window.fill(background_color)  # Fill the window with the background color
    
    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()