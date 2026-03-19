# Importing modules:
import pygame
import random
import os

# Initializing pygame:
pygame.init()

# Color variables:
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
albescent_white = (211, 240, 222)

# Creating Game window:
screen_width = 900
screen_height = 500
game_window = pygame.display.set_mode((screen_width, screen_height))

bg_img = pygame.image.load("main_window.jpeg")
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height)).convert_alpha()

main_img = pygame.image.load("welcome_window.jpeg")
main_img = pygame.transform.scale(main_img, (screen_width, screen_height)).convert_alpha()

game_over_window = pygame.image.load("game_over_window.jpeg")
game_over_window = pygame.transform.scale(game_over_window, (screen_width, screen_height)).convert_alpha()

# Game title:
pygame.display.set_caption("Snake Game")
pygame.display.update()

# Game specific variables:
fps = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)
pygame.mixer.init()

# Game realted functions:
def score_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

def plot_snake(game_window, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(game_window, color,[x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(albescent_white)
        game_window.blit(main_img)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("background.mp3")
                    pygame.mixer.music.play()
                    game_loop()
                    pygame.mixer.music.load("background.mp3")
                    pygame.mixer.music.play()
        pygame.display.update()
        clock.tick(fps)

# Game loop:
def game_loop():
    exit_game = False
    game_over = False

    snake_x = 43
    snake_y = 67
    snake_size = 20
    score = 0

    velocity_x = 0
    velocity_y = 0
    init_velocity = 3

    snake_list = []
    snake_lenght = 1

    food_x = random.randint(0, screen_width//2)
    food_y = random.randint(0, screen_height//2)

    if not os.path.exists("Hiscore.txt"):
        with open("Hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt") as f:
        hiscore = f.read()
    while not exit_game:
        if game_over:
            game_window.fill(albescent_white)
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            # score_screen("Game Over! Press Enter To Continue", charcoal, 310, 210)
            game_window.blit(game_over_window)
        
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    # if event.key == pygame.K_q: # Cheat code that increases score by 1000 points
                    #     score += 1000
                    # if event.key == pygame.K_v: # Cheat code that increases speed
                    #     init_velocity += 12

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) <12 and abs(snake_y - food_y) <12:
                score += 10
                food_x = random.randint(0, screen_width//2)
                food_y = random.randint(0, screen_height//2)
                snake_lenght += 2
                if score > int(hiscore):
                    hiscore = score
            
            game_window.fill(albescent_white)
            game_window.blit(bg_img)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_lenght:
                del snake_list[0]

            if snake_x<0 or snake_x>screen_width or snake_y <0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()
            
            score_screen(f"Score:{score}-Hiscore: {hiscore}", black, 5,5)
            pygame.draw.rect(game_window, red,[food_x, food_y, snake_size, snake_size])
            plot_snake(game_window, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()