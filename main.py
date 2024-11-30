import pygame
import random

pygame.init()

# Window Size
screen_width = 1000
screen_height = 600
block_size = 20

# Colours Used
red = (213, 50, 80)
green = (0, 255, 0)
gold = (255, 215, 0)
background = (40, 40, 40)  # Dark grey background

# Set up display
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

#  Score Display Properties
def your_score(score):
    font_style = pygame.font.SysFont("Consolas", 30)
    value = font_style.render(f"Score: {score}", True, gold)
    game_display.blit(value, [10, 10])

# Draw snake
def draw_snake(block_size, snake_list):
    for segment in snake_list:
        pygame.draw.rect(game_display, green, [segment[0], segment[1], block_size, block_size], border_radius=5)

# Game loop
def game_loop():
    game_over = False
    game_close = False

    snake_list = []
    snake_length = 1
    score = 0

    lead_x = screen_width / 2
    lead_y = screen_height / 2
    lead_x_change = 0
    lead_y_change = 0
    direction = "RIGHT"

    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    while not game_over:
        while game_close:
            game_display.fill((50, 50, 50))  # light Grey

            # Render game-over text and center it
            font_style = pygame.font.SysFont("Consolas", 40)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            text_rect = message.get_rect(center=(screen_width / 2, screen_height / 2))
            game_display.blit(message, text_rect)

            # Show score below the message
            your_score(score)
            pygame.display.update()

            # Keys defined for Quit or Play Again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "DOWN"

        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y < 0:
            game_close = True

        game_display.fill(background)

        pygame.draw.circle(game_display, gold, (food_x + block_size // 2, food_y + block_size // 2), block_size // 2)

        snake_head = [lead_x, lead_y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        your_score(score)

        pygame.display.update()

        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1
            score += 10

        clock.tick(10) # For Speed of Snake

    pygame.quit()
    quit()

game_loop()
