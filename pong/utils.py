import pygame

def drawtext(screen, color=(255,255,0), coords=(100,100), text="hello"):
    pygame.font.init()
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(text, 1, color)
    screen.blit(label, coords)