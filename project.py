import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animation Example")

# Load sprite sheet or frames
sprite_sheet = pygame.image.load("sprite_sheet.png")

# Define animation frames
frame_width = 64
frame_height = 64
num_frames = 4
current_frame = 0

# Animation variables
clock = pygame.time.Clock()
animation_speed = 200  # Speed of animation in milliseconds

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation frames
    if pygame.time.get_ticks() >= animation_speed:
        current_frame = (current_frame + 1) % num_frames
        pygame.time.set_timer(pygame.USEREVENT, 0)  # Reset the timer
        pygame.time.set_timer(pygame.USEREVENT, animation_speed)  # Start the timer again

    # Set texture rect for the current frame
    frame_rect = pygame.Rect(current_frame * frame_width, 0, frame_width, frame_height)
    sprite = sprite_sheet.subsurface(frame_rect)

    # Render the sprite
    screen.fill((0, 0, 0))
    screen.blit(sprite, (0, 0))
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
