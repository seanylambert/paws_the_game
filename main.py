import pygame
import character

running = False
def update(screen):
    print("Updating")
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_character.(

            elif event.key == pygame.K_LEFT:
        if event.type == pygame.KEYUP:
        if event.type == pygame.QUIT:
            print("Quitting")
            running = False


def render(screen):
    print("Rendering")
    screen.fill((255, 255, 0))
    pygame.display.flip()

def main_loop(screen):
    running = True
    while (running):
        update(screen)
        render(screen)

    pygame.display.quit()
    pygame.quit()

def main():
    pygame.init() 

    screen = pygame.display.set_mode((500,500))

    main_loop(screen)

if __name__ == "__main__":
    main()
