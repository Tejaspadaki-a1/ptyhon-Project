import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Badminton Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up player variables
PLAYER_WIDTH, PLAYER_HEIGHT = 15, 60
PLAYER_SPEED = 5

player1_x = 50
player1_y = HEIGHT // 2 - PLAYER_HEIGHT // 2

player2_x = WIDTH - 50 - PLAYER_WIDTH
player2_y = HEIGHT // 2 - PLAYER_HEIGHT // 2

# Set up the ball variables
BALL_RADIUS = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

# Set up the score variables
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= PLAYER_SPEED
    if keys[pygame.K_s] and player1_y < HEIGHT - PLAYER_HEIGHT:
        player1_y += PLAYER_SPEED
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PLAYER_HEIGHT:
        player2_y += PLAYER_SPEED

    # Update ball position
    ball_x += BALL_SPEED_X
    ball_y += BALL_SPEED_Y

    # Ball collision with top and bottom walls
    if ball_y >= HEIGHT - BALL_RADIUS or ball_y <= BALL_RADIUS:
        BALL_SPEED_Y *= -1

    # Ball collision with players
    if (
        player1_x + PLAYER_WIDTH >= ball_x - BALL_RADIUS
        and player1_y <= ball_y <= player1_y + PLAYER_HEIGHT
    ):
        BALL_SPEED_X *= -1
    elif (
        player2_x <= ball_x + BALL_RADIUS
        and player2_y <= ball_y <= player2_y + PLAYER_HEIGHT
    ):
        BALL_SPEED_X *= -1

    # Ball out of bounds
    if ball_x <= 0:
        score2 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
    elif ball_x >= WIDTH:
        score1 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    # Clear the window
    win.fill(BLACK)

    # Draw the players
    pygame.draw.rect(win, WHITE, (player1_x, player1_y, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(win, WHITE, (player2_x, player2_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Draw the ball
    pygame.draw.circle(win, WHITE, (ball_x, ball_y), BALL_RADIUS)

    # Draw the score
    text = font.render(f"Player 1: {score1}", True, WHITE)
    win.blit(text, (50, 20))
    text = font.render(f"Player 2: {score2}", True, WHITE)
    win.blit(text, (WIDTH - 200, 20))

    # Update the window
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
