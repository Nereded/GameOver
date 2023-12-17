import pygame

pygame.init()
window_width = 590
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
gameover_image = pygame.image.load('gameover.png')
x = -600
y = 0
speed = 200

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0, 0, 255))
    window.blit(gameover_image, (x, y))
    if x < -10:
        x += speed / 60
    pygame.display.flip()

pygame.quit()
