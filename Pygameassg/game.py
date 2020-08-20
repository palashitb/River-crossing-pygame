import pygame
import sys
from pygame.locals import *
from config import *

pygame.init()

# images

clock = pygame.time.Clock()  # clock for usage in mainloop


class player(object):  # player attributes
    def __init__(self, x, y, width, height):  #mandatory function for definition
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.player1 = True
        self.sf1 = False
        self.sf2 = False
        self.sf3 = False
        self.sf4 = False
        self.one = 0
        self.two = 0
        self.level1 = 0
        self.level2 = 0

    def nil(self):  # function to reinitialize a few boolean variables
        self.sf4 = False
        self.sf3 = False
        self.sf2 = False
        self.sf1 = False

    def score_1(self):  # function for score of player1
        if self.sf1 is False and self.y + self.height < 240:
            self.sf1 = True
            self.one += 15
        elif self.sf2 is False and self.y + self.height < 390:
            self.sf2 = True
            self.one += 15
        elif self.sf3 is False and self.y + self.height < 540:
            self.sf3 = True
            self.one += 15
        elif self.sf4 is False and self.y + self.height < 690:
            self.sf4 = True
            self.one += 15

    def score_2(self):  # function for score of player2
        if self.sf1 is False and self.y + self.height > 240:
            self.sf1 = True
            if self.player1:
                self.two += 15 * self.level1
            else:
                self.two += 15 * self.level2
        elif self.sf2 is False and self.y + self.height > 390:
            self.sf2 = True
            if self.player1:
                self.two += 15 * self.level1
            else:
                self.two += 15 * self.level2
        elif self.sf3 is False and self.y + self.height > 540:
            self.sf3 = True
            if self.player1:
                self.two += 15 * self.level1
            else:
                self.two += 15 * self.level2
        elif self.sf4 is False and self.y + self.height > 690:
            self.sf4 = True
            if self.player1:
                self.two += 15 * self.level1
            else:
                self.two += 15 * self.level2

    def draw(self, win):  # function for managing sprite while player moves
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        elif self.up:
            win.blit(walkUp[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        elif self.down:
            win.blit(walkDown[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        else:
            if self.player1:
                win.blit(char, (self.x, self.y))
            else:
                win.blit(char1, (self.x, self.y))

    def got_hit(self):  # function to accomodate collision
        global l, k
        if self.player1:
            self.player1 = False
            if self.sf4:
                self.one += 5
            self.x = 590
            self.y = 0
            t1.on = False
            t2.on = True
            self.nil()
            l += 1
        else:
            self.player1 = True
            if self.sf1:
                self.two += 5
            self.x = 600
            self.y = 800
            t1.on = True
            t2.on = False
            self.nil()
            k += 1  # class player


def update_score():  # independent function for updating scores
    if man.player1:
        man.score_1()
    else:
        man.score_2()


class SafeZone(object):  # class definition for safezones
    def __init__(self, y):
        self.x = 0
        self.y = y

    def banale(self, win):  # function for drawing the safezone
        pygame.draw.rect(win, (50, 205, 50), (0, self.y, 1200, 50))


class StationaryObs(object):  # class for stationary obstacles
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.choice = z

    def stationobs(self, win):  # function detecting collisions
        if self.choice == 1:  # with a stationary obstacle
            win.blit(venus, (self.x, self.y))
        else:
            win.blit(pitch, (self.x, self.y))

    def move(self):  # function detecting if a player completed a level
        if self.x < man.x + man.width < self.x + self.width:
            if self.y + self.height > man.y + man.width \
                    and self.y < man.y + man.height:
                man.got_hit()


class MovingObs(object):  # moving obstacles class definition
    def __init__(self, x, y, width, height, vel, z):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.velo = vel
        self.choice = z

    def speed(self, level):  # function to decide the velocity of
        self.vel = self.velo * (1 + level)  # obstacle according the level

    def movin_obs(self, win):  # function to put the obstacle sprites in place
        if self.choice == 1:
            win.blit(shark, (self.x, self.y))
        elif self.choice == 2:
            win.blit(pira, (self.x, self.y))
        else:
            win.blit(croc, (self.x, self.y))

    def move(self):  # function to move the obstacle and detect a collision
        if self.x + self.width + self.vel < 1200:  # if it happens
            self.x += self.vel
        else:
            self.x = 0

        if self.x < man.x + man.width and self.x + self.width > man.x:
            if self.y + self.height > man.y + man.width \
                    and self.y < man.y + man.height:
                man.got_hit()
            elif man.y + man.width < 100 and man.player1:
                man.level1 += 1
                man.got_hit()
            elif man.y > 760 and man.player1 is False:
                man.level2 += 1
                man.got_hit()


def redraw_game_window():  # function to redraw the screen with necessary
    win.fill((0, 191, 255))  # changes in each mainloop iteration
    update_score()
    SafeZone(0).banale(win)
    SafeZone(50).banale(win)
    SafeZone(200).banale(win)
    SafeZone(350).banale(win)
    SafeZone(500).banale(win)
    SafeZone(650).banale(win)
    SafeZone(800).banale(win)
    obs1.movin_obs(win)
    obs2.movin_obs(win)
    obs3.movin_obs(win)
    obs4.movin_obs(win)
    obs5.movin_obs(win)
    obs6.movin_obs(win)
    obs7.movin_obs(win)
    obs8.movin_obs(win)
    so1.stationobs(win)
    so2.stationobs(win)
    so3.stationobs(win)
    so4.stationobs(win)
    so5.stationobs(win)
    so6.stationobs(win)
    so7.stationobs(win)
    so8.stationobs(win)
    so9.stationobs(win)
    text1 = font1.render('Player1: ' + str(man.one), 1, (0, 0, 0))
    win.blit(text1, (0, 800))
    text2 = font1.render('Player2: ' + str(man.two), 1, (0, 0, 0))
    win.blit(text2, (900, 20))
    text3 = font2.render('Level: ' + str(man.level2 + 1), 1, (0, 0, 0))
    win.blit(text3, (900, 50))
    text4 = font2.render('Level: ' + str(man.level1 + 1), 1, (0, 0, 0))
    win.blit(text4, (0, 780))
    text5 = font2.render('Time Remaining: ' + str(int(t1.time)), 1, (0, 0, 0))
    win.blit(text5, (0, 750))
    text6 = font2.render('Time Remaining: ' + str(int(t2.time)), 1, (0, 0, 0))
    win.blit(text6, (900, 90))
    man.draw(win)
    pygame.display.update()


class time(object):  # class for countdown timer for both the players
    def __init__(self, player):
        self.player = player
        self.time = 30
        self.on = False

    def timer(self):
        if self.on:
            self.time -= dt


def khatam(i):  # independent function to display the winner
    req_win = pygame.image.load('roadrash.jpg')
    win.blit(pygame.transform.scale(req_win, (1200, 850)), (0, 0))
    text23 = font5.render('Winner is Player' + str(i), 1, (0, 0, 0))
    win.blit(text23, (375, 350))
    pygame.display.update()
    run = False
font1 = pygame.font.SysFont('comicsans', 50, True)
font2 = pygame.font.SysFont('comicsans', 30, True)
font5 = pygame.font.SysFont('comicsans', 80, True)
man = player( 580, 800, 30, 60)
obs1 = MovingObs(0, 110, 100, 50, 5, 1)  # one-time definitions
obs2 = MovingObs(0, 250, 40, 20, 3, 2)
obs3 = MovingObs(1100, 290, 30, 30, 6, 3)
obs4 = MovingObs(700, 400, 120, 20, 7, 1)
obs5 = MovingObs(0, 435, 60, 30, 2, 3)
obs6 = MovingObs(500, 550, 40, 20, 9, 1)
obs7 = MovingObs(1150, 595, 50, 15, 5, 1)
obs8 = MovingObs(0, 715, 200, 40, 4, 2)
so1 = StationaryObs(200, 185, 1)
so2 = StationaryObs(600, 185, 2)
so3 = StationaryObs(500, 335, 2)
so4 = StationaryObs(900, 335, 1)
so5 = StationaryObs(300, 485, 2)
so6 = StationaryObs(600, 485, 1)
so7 = StationaryObs(150, 635, 1)
so8 = StationaryObs(500, 635, 1)
so9 = StationaryObs(1000, 635, 2)
t1 = time(1)
t2 = time(2)
t1.on = True
run = True

while run:  # mainloop

    clock.tick(27)

    if int(t1.time) <= 0 and int(t2.time) <= 0:
        if man.one > man.two:  # detecting if both the players' time is over
            khatam(1)
        else:
            khatam(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # detecting if the game is ordered to be exited

    dt = pygame.time.Clock().tick(30) / 1000

    keys = pygame.key.get_pressed()

    if man.player1:  # defining level of the player presently playing
        level = man.level1
    else:
        level = man.level2
    if man.player1 and t1.time <= 0:
        man.got_hit()
    elif man.player1 is False and t2.time <= 0:
        man.got_hit()

    obs1.move()  # function definitions
    obs2.move()
    obs3.move()
    obs4.move()
    obs5.move()
    obs6.move()
    obs7.move()
    obs8.move()
    so1.move()
    so2.move()
    so3.move()
    so4.move()
    so5.move()
    so6.move()
    so7.move()
    so8.move()
    so9.move()
    t1.timer()
    t2.timer()
    obs1.speed(level)
    obs2.speed(level)
    obs3.speed(level)
    obs4.speed(level)
    obs5.speed(level)
    obs6.speed(level)
    obs7.speed(level)
    obs8.speed(level)

    if keys[pygame.K_LEFT] and man.x > man.vel:  # controller keys conditioning
        if man.player1:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.up = False
            man.down = False
        elif keys[pygame.K_a] and man.x > man.vel and \
                man.player1 is False:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.up = False
            man.down = False
        elif keys[pygame.K_RIGHT] and man.x < 1200 - man.width - man.vel \
                and man.player1:
            man.x += man.vel
            man.right = True
            man.up = False
            man.down = False
            man.left = False
        elif keys[pygame.K_d] and man.x < 1200 - man.width - man.vel \
                and man.player1 is False:
            man.x += man.vel
            man.right = True
            man.up = False
            man.down = False
            man.left = False
        elif keys[pygame.K_UP] and man.y > man.vel \
                and man.player1:
            man.y -= man.vel
            man.right = False
            man.up = True
            man.down = False
            man.left = False
        elif keys[pygame.K_w] and man.y > man.vel \
                and man.player1 is False:
            man.y -= man.vel
            man.right = False
            man.up = True
            man.down = False
            man.left = False
        elif keys[pygame.K_DOWN] and man.y < 850 - man.height - man.vel \
                and man.player1:
            man.y += man.vel
            man.right = False
            man.up = False
            man.down = True
            man.left = False
        elif keys[pygame.K_s] and man.y < 850 - man.height - man.vel \
                and man.player1 is False:
            man.y += man.vel
            man.right = False
            man.up = False
            man.down = True
            man.left = False
        else:
            man.right = False
            man.left = False
            man.down = False
            man.left = False
            man.walkCount = 0  # controls
    elif keys[pygame.K_a] and man.x > man.vel \
            and man.player1 is False:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.up = False
        man.down = False
    elif keys[pygame.K_RIGHT] and man.x < 1200 - man.width - man.vel \
            and man.player1:
        man.x += man.vel
        man.right = True
        man.up = False
        man.down = False
        man.left = False
    elif keys[pygame.K_d] and man.x < 1200 - man.width - man.vel \
            and man.player1 is False:
        man.x += man.vel
        man.right = True
        man.up = False
        man.down = False
        man.left = False
    elif keys[pygame.K_UP] and man.y > man.vel \
            and man.player1:
        man.y -= man.vel
        man.right = False
        man.up = True
        man.down = False
        man.left = False
    elif keys[pygame.K_w] and man.y > man.vel \
            and man.player1 is False:
        man.y -= man.vel
        man.right = False
        man.up = True
        man.down = False
        man.left = False
    elif keys[pygame.K_DOWN] and man.y < 850 - man.height - man.vel \
            and man.player1:
        man.y += man.vel
        man.right = False
        man.up = False
        man.down = True
        man.left = False
    elif keys[pygame.K_s] and man.y < 850 - man.height - man.vel \
            and man.player1 is False:
        man.y += man.vel
        man.right = False
        man.up = False
        man.down = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.down = False
        man.left = False
        man.walkCount = 0  # controls

    redraw_game_window()
    # calling the function to update the screen with changes
pygame.quit()
sys.exit()

