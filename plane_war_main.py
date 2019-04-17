from plane_sprites import *


class PlainGame(object):
    def __init__(self):
        print("游戏初始化")

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__creat_sprites()
        pygame.time.set_timer(GAME_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_SHOOT_EVENT, 500)

    def __creat_sprites(self):
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.hero = Hero()
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_check(self):
        for event in pygame.event.get():

            # 判断事件类型是否是退出事件
            if event.type == pygame.QUIT:
                print("游戏退出...")
                PlainGame.__game_over()
            elif event.type == GAME_ENEMY_EVENT:
                print("enemy come")
                enemy_plane = Enemy()
                self.enemy_group.add(enemy_plane)
            elif event.type == HERO_SHOOT_EVENT:
                self.hero.shoot()

            keys_press = pygame.key.get_pressed()
            if keys_press[pygame.K_RIGHT]:
                self.hero.speed_x = 2

            elif keys_press[pygame.K_LEFT]:
                self.hero.speed_x = -2

            elif keys_press[pygame.K_UP]:
                self.hero.speed_y = -2

            elif keys_press[pygame.K_DOWN]:
                self.hero.speed_y = 2

            else:
                self.hero.speed_x = 0
                self.hero.speed_y = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            self.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.enemy_group.update()
        self.hero_group.update()
        self.hero.bullet_group.update()

        self.back_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()

    def start_games(self):
        print("游戏开始")
        while True:
            self.clock.tick(FS)
            self.__check_collide()
            self.__event_check()
            self.__update_sprites()
            pygame.display.update()


if __name__ == '__main__':
    game = PlainGame()
    game.start_games()




