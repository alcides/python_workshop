import pygame

from config import *
from utils import drawtext

def process_keys(event):
    if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
        print event.key
    # print event.type, event.key
    # pygame.KEYDOWN, pygame.KEYUP
    # pygame.K_LEFT, pygame.K_RIGHT

if __name__ == '__main__':
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    clock=pygame.time.Clock()
    running = True
    
    while running:
        screen.fill(WHITE)
        # draw objects
        
        pygame.draw.circle(screen,RED,(100,100),20)
        
        pygame.draw.rect(screen,BLUE,(10,10,100,20))
        pygame.draw.rect(screen,GREEN,(10,HEIGHT - 10 - 20,100,20))
        
        drawtext(screen)
        
        pygame.display.flip()
        
        event=pygame.event.poll()
        process_keys(event)
        if event.type == pygame.QUIT:
              running = False
        
        clock.tick(CLOCKSPEED)
