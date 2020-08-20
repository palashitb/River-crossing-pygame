import pygame
import sys
from pygame.locals import *


win = pygame.display.set_mode((1200, 850))
pygame.display.set_caption("First Game")
l = 0
t = 0
k = 0
walkRight = [pygame.transform.scale(pygame.image.load('R1.png'), (30, 60)),
             pygame.transform.scale(pygame.image.load('R2.png'), (30, 60)),
             pygame.transform.scale(pygame.image.load('R3.png'), (30, 60)),
             pygame.transform.scale(pygame.image.load('R4.png'), (30, 60)),
             pygame.transform.scale(pygame.image.load('R5.png'), (30, 60)),
             pygame.transform.scale(pygame.image.load('R6.png'), (30, 60)),
             pygame.transform.scale(pygame.image.load('R7.png'), (30, 60)),
             pygame.transform.scale(pygame.image.load('R8.png'), (30, 60)),
             pygame.transform.scale(pygame.image.load('R9.png'), (30, 60))]
walkLeft = [pygame.transform.scale(pygame.image.load('L1.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('L2.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('L3.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('L4.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('L5.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('L6.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('L7.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('L8.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('L9.png'), (30, 60))]
walkUp = [pygame.transform.scale(pygame.image.load('U1.png'), (30, 60)),
          pygame.transform.scale(pygame.image.load('U2.png'), (30, 60)),
          pygame.transform.scale(pygame.image.load('U3.png'), (30, 60)),
          pygame.transform.scale(pygame.image.load('U4.png'), (30, 60)),
          pygame.transform.scale(pygame.image.load('U5.png'), (30, 60)),
          pygame.transform.scale(pygame.image.load('U6.png'), (30, 60)),
          pygame.transform.scale(pygame.image.load('U7.png'), (30, 60)),
          pygame.transform.scale(pygame.image.load('U8.png'), (30, 60)),
          pygame.transform.scale(pygame.image.load('U9.png'), (30, 60))]
walkDown = [pygame.transform.scale(pygame.image.load('D1.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('D2.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('D3.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('D4.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('D5.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('D6.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('D7.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('D8.png'), (30, 60)),
            pygame.transform.scale(pygame.image.load('D9.png'), (30, 60))]
char = pygame.transform.scale(pygame.image.load('U1.png'), (30, 60))
char1 = pygame.transform.scale(pygame.image.load('D1.png'), (30, 60))
croc = pygame.image.load('Croc.png')
pitch = pygame.image.load('lion.png')
venus = pygame.image.load('cactus.png')
shark = pygame.image.load('shark.png')
pira = pygame.image.load('boat.png')
end = pygame.image

