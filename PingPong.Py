#Create your own shooter

from pygame import *
from time import sleep

wd_w = 600
wd_h = 500
bg = (200, 255, 255)

wd = display.set_mode(
    (wd_w, wd_h)
)

wd.fill(bg)

clock = time.Clock()

game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        wd.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < wd_h - 100:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < wd_h - 100:
            self.rect.y += self.speed
        

P1 = Player("Racket.png", 5, 395, 50, 100, 3.5)
P2 = Player("Racket.png", 540, 395, 50, 100, 3.5)
ball = GameSprite("Tennis Ball.png", 275, 200, 50, 50, 3)

font.init()
font1 = font.Font(None, 70)
P1_Win = font1.render('PLAYER 1 WIN!', True, (255, 215, 0))
P2_Win = font1.render('PLAYER 2 WIN!', True, (255, 215, 0))

speed_x = 3
speed_y = 3

finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False                    

    if finish != True:
        wd.fill(bg)
        P1.update_r()
        P2.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(P1, ball) or sprite.collide_rect(P2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > wd_h - 50 or ball.rect.y < 0:
            speed_y *= -1

    if ball.rect.x > wd_w:
        finish = True
        wd.blit(P1_Win, (200, 200))
        game = False

    if ball.rect.x < 0:
        finish = True
        wd.blit(P2_Win, (200, 200))
        game = False
        

    P1.reset()
    P2.reset()
    ball.reset()

    display.update()
    clock.tick(60)
sleep(3)    
display.update()