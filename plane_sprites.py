import random
import pygame
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FS = 60
GAME_ENEMY_EVENT = pygame.USEREVENT
HERO_SHOOT_EVENT = pygame.USEREVENT + 1
RIGHT =1
LEFT =0


class GameSprites(pygame.sprite.Sprite):
    # the sprite of plane wars.

    def __init__(self, image_name, x=0, y=0, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprites):
    """game background sprites"""

    def __init__(self, is_alter=False):
        super().__init__("./images/background.png")

        if is_alter:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y == SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprites):

    def __init__(self):
        super().__init__("./images/enemy1.png")

        self.rect.bottom = 0
        self.speed = random.randint(1, 3)

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            print("del enemy's plain")
            self.kill()


class Hero(GameSprites):

    def __init__(self):
        super().__init__("./images/me1.png", speed=0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.height - 120
        self.bullet_group = pygame.sprite.Group()
        self.spped_x = 0
        self.speed_y = 0

    def shoot(self):
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - i*20
            self.bullet_group.add(bullet)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right


class Bullet(GameSprites):

    def __init__(self):
        super().__init__("./images/bullet1.png", speed=-2)

    def update(self):
        super().update()
        if self.rect.bottom == 0:
            self.kill()
