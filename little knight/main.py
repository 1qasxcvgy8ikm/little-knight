from pygame import *
from random import randint
from time import time as timer

img_back = 'background.png'
img_player = 'knight.png'
img_block = 'block.png'

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)


       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    


win_width = 1920
win_height = 1080
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background,(0,0))


    display.update()
    time.delay(30)