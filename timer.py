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
enemy_speed = 1

# Set up collectible
collectible_width = 30
collectible_height = 30
collectible_x = random.randint(0, window_width - collectible_width)
collectible_y = 50

powerup_width = 40
powerup_height = 40
powerup_x = random.randint(0, window_width - powerup_width)
powerup_y = 50
shield_active = False
shield_timer = 0

# Set up score
score = 0
font = pygame.font.Font(None, 36)

# Set up timer for power-up respawn
powerup_respawn_timer = 0

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
        if not shield_active:
            running = False
    
    # Collision detection with collectible
    if (player_x < collectible_x + collectible_width) and \
                        (player_x + player_width > collectible_x) and \
                        (player_y < collectible_y + collectible_height) and \
                        (player_y + player_height > collectible_y):
        collectible_x = random.randint(0, window_width - collectible_width)
        collectible_y = 50
        score += 10
    
    # Collision detection with power-up
    collision_powerup = (player_x < powerup_x + powerup_width) and \
                        (player_x + player_width > powerup_x) and \
                        (player_y < powerup_y + powerup_height) and \
                        (player_y + player_height > powerup_y)

    if collision_powerup:
        powerup_x = random.randint(0, window_width - powerup_width)
        powerup_y = 50
        shield_active = True
        shield_timer = pygame.time.get_ticks()
    
    # Check shield timer
    if shield_active:
        current_time = pygame.time.get_ticks()
        if current_time - shield_timer > 10000:  
            shield_active = False
    
    # Check power-up timer
    if not shield_active:
        current_time = pygame.time.get_ticks()
        if current_time - powerup_respawn_timer > 3000:  
            powerup_x = random.randint(0, window_width - powerup_width)
            powerup_y = 50
            powerup_respawn_timer = pygame.time.get_ticks()

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

    # Define the vertices of the triangle
    x1 = powerup_x + powerup_width / 2
    y1 = powerup_y
    x2 = powerup_x
    y2 = powerup_y + powerup_height
    x3 = powerup_x + powerup_width
    y3 = powerup_y + powerup_height

    # Draw the triangle
    pygame.draw.polygon(window, (255, 255, 0), [(x1, y1), (x2, y2), (x3, y3)])

    # Collision detection with shield active
    collision_shield = shield_active and \
                    (player_x < enemy_x + enemy_width) and \
                    (player_x + player_width > enemy_x) and \
                    (player_y < enemy_y + enemy_height) and \
                    (player_y + player_height > enemy_y)

    if collision_shield:
        enemy_x = random.randint(0, window_width - enemy_width)
        enemy_y = 0
    
    # Draw collectible
    pygame.draw.circle(window, (0, 255, 0), collectible_pos, collectible_width)

    # Draw score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
