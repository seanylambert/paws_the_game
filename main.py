import pygame
from character import Character
from map import Map

running = False
main_character = None
planet = None
pygame.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)

def update(screen):
    global running
    global main_character
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                main_character.y_direction = -1
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                main_character.y_direction = 1
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                main_character.x_direction = -1
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                main_character.x_direction = 1
            elif event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                main_character.y_direction = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                main_character.y_direction = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                main_character.x_direction = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                main_character.x_direction = 0

        if event.type == pygame.QUIT:
            print("Quitting")
            running = False
    main_character.update()

def render(screen):
    global main_character
    global planet
    screen.fill((255, 255, 0))          # 0-255  2**8==256
    planet.render(screen)
    main_character.render(screen)
    text_surface = myfont.render('Hello', False, (100, 0, 0))
    screen.blit(text_surface, (300, 300))
    text_surface = myfont.render('Steven', False, (100, 0, 0))
    screen.blit(text_surface, (300, 350))
    pygame.display.flip()

def main_loop(screen):
    global running
    running = True
    while (running):
        update(screen)
        render(screen)

    pygame.display.quit()
    pygame.quit()

def main():
    global main_character
    global planet

    screen = pygame.display.set_mode((500,500))
    main_character = Character(10, 10, 20, 20, color=(0, 0, 255))
    planet = Map(50, 50, 20, 20, color=(100, 100, 100))

    main_loop(screen)

if __name__ == "__main__":
    main()
