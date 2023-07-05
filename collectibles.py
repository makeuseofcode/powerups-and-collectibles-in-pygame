import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My Game")

# Set up player
player_width = 50
player_height = 50
player_x = (window_width - player_width) // 2
player_y = window_height - player_height - 10
player_speed = 2

# Set up enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, window_width - enemy_width)
enemy_y = 50
enemy_speed = 0.8

# Set up collectible
collectible_width = 30
collectible_height = 30
collectible_x = random.randint(0, window_width - collectible_width)
collectible_y = 50

# Set up score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] :
        player_y -= player_speed
    if keys[pygame.K_DOWN] :
        player_y += player_speed

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > window_height:
        enemy_x = random.randint(0, window_width - enemy_width)
        enemy_y = 0

    # Collision detection
    if (player_x < enemy_x + enemy_width) and \
        (player_x + player_width > enemy_x) and \
        (player_y < enemy_y + enemy_height) and \
        (player_y + player_height > enemy_y):
        running = False
    
    # Collision detection with collectible
    if (player_x < collectible_x + collectible_width) and \
                        (player_x + player_width > collectible_x) and \
                        (player_y < collectible_y + collectible_height) and \
                        (player_y + player_height > collectible_y):
        collectible_x = random.randint(0, window_width - collectible_width)
        collectible_y = 50
        score += 10

    # Clear the screen
    window.fill((0, 0, 0))

    player_pos = (player_x, player_y, 
                  player_width, player_height)
    enemy_pos =  (enemy_x, enemy_y, 
                  enemy_width, enemy_height)

    # Draw player
    pygame.draw.rect(window, (255, 255, 255), player_pos)

    # Draw enemy
    pygame.draw.rect(window, (255, 0, 0), enemy_pos)

    collectible_pos = (collectible_x, collectible_y)
    
    # Draw collectible
    pygame.draw.circle(window, (0, 255, 0), collectible_pos, collectible_width)

    # Draw score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
