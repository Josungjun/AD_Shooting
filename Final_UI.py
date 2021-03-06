import pygame
import sys
from time import sleep
from pygame.locals import *
import random

Black = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (250, 250, 50)
RED = (250, 50, 50)

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 600

FPS = 60

class Fighter(pygame.sprite.Sprite):
    def __init__(self, Fly):
        super(Fighter, self).__init__()
        self.image = pygame.image.load(Fly)
        self.rect = self.image.get_rect()
        self.rect.x = int(WINDOW_WIDTH / 2)
        self.rect.y = WINDOW_HEIGHT - self.rect.height
        self.dx = 0
        self.dy = 0

    def update(self):
        self.rect.x += self.dx
        if self.rect.x < 0 or self.rect.x + self.rect.width > WINDOW_WIDTH:
            self.rect.x -= self.dx

        if self.rect.y < 0 or self.rect.y + self.rect.height > WINDOW_HEIGHT:
            self.rect.y -= self.dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite


class Missile(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Missile, self).__init__()
        self.image = pygame.image.load('missile.png')
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound('missile.wav')

    def launch(self):
        self.sound.play()

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y + self.rect.height < 0:
            self.kill()

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite


class Rock(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Rock, self).__init__()
        rock_image = ('rock.png')
        self.image = pygame.image.load(rock_image)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self):
        if self.rect.y > WINDOW_HEIGHT:
            return True

def draw_text(text, font, surface, x, y, main_color):
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)

def occur_explosion(surface, x, y):
    explosion_image = pygame.image.load('explosion.png')
    explosion_rect = explosion_image.get_rect()
    explosion_rect.x = x
    explosion_rect.y = y
    surface.blit(explosion_image, explosion_rect)

    explosion_sounds = ('explosion.wav')
    explosion_sound = pygame.mixer.Sound(explosion_sounds)
    explosion_sound.play()

def game(background, max_speed, min_speed, occurrock, occurock2, Fly, music):
    default_font = pygame.font.SysFont('suruma', 25)
    background_image = pygame.image.load(background)
    gameover_sound = pygame.mixer.Sound('gameover.wav')
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    fps_clock = pygame.time.Clock()

    fighter = Fighter(Fly)
    missiles = pygame.sprite.Group()
    rocks = pygame.sprite.Group() #많은 객체들을 효과적으로 다뤄주는 pygame 함수

    occur_prob = 40
    shot_count = 0
    count_missed = 0

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    fighter.dx -= 5
                elif event.key == pygame.K_RIGHT:
                    fighter.dx += 5
                elif event.key == pygame.K_SPACE:
                    missile = Missile(fighter.rect.centerx, fighter.rect.y, 10)
                    missile.launch()
                    missiles.add(missile)
                elif event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    return game_menu()
            if event.type == pygame.QUIT:
                return game_menu()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighter.dx = 0

        screen.blit(background_image, background_image.get_rect())

        occur_of_rocks = occurock2 + int(shot_count / occurrock)
        min_rock_speed = 1 + int(shot_count / min_speed)
        max_rock_speed = 1 + int(shot_count / max_speed)

        if random.randint(1, occur_prob) == 1:
            for i in range(occur_of_rocks):
                speed = random.randint(min_rock_speed, max_rock_speed)
                rock = Rock(random.randint(0, WINDOW_WIDTH - 30), 0 , speed)
                rocks.add(rock)


        draw_text('detroyed rocks : {}'.format(shot_count), default_font, screen, 100, 20, YELLOW)
        draw_text('lose rocks : {}'.format(count_missed), default_font, screen, 400, 20, RED)

        for missile in missiles:
            rock = missile.collide(rocks)
            if rock:
                missile.kill()
                rock.kill()
                occur_explosion(screen, rock.rect.x, rock.rect.y)
                shot_count += 1

        for rock in rocks:
            if rock.out_of_screen():
                rock.kill()
                count_missed += 1

        rocks.update()
        rocks.draw(screen)
        missiles.update()
        missiles.draw(screen)
        fighter.update()
        fighter.draw(screen)
        pygame.display.flip()

        if fighter.collide(rocks) or count_missed >= 3:
            pygame.mixer_music.stop()
            occur_explosion(screen, fighter.rect.x, fighter.rect.y)
            pygame.display.update()
            gameover_sound.play()
            sleep(1)
            done = True

        fps_clock.tick(FPS)

    return 'game_menu'

def game_menu():
    start_image = pygame.image.load('fantasy.jpg')
    screen.blit(start_image, [0,0])
    draw_x = int(WINDOW_WIDTH / 2)
    draw_y = int(WINDOW_HEIGHT / 4)
    font_70 = pygame.font.SysFont('suruma', 70)
    font_40 = pygame.font.SysFont('suruma', 40)

    draw_text('ShotingGame', font_70, screen, draw_x, draw_y, Black)
    draw_text('press enter', font_40, screen, draw_x, draw_y + 200, WHITE)
    draw_text('Start game', font_40, screen, draw_x, draw_y + 250, WHITE)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return 'play'
            elif event.key == pygame.K_ESCAPE:
                return 'quit'
        if event.type == QUIT:
            return 'quit'

    return 'game_menu'

def main(background, max_speed, min_speed, occurrock, occurrock2, Fly, music):
    global screen

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('PyShooting')

    action = 'game_menu'
    while action != 'quit':
        if action == 'game_menu':
            action = game_menu()
        elif action == 'play':
            action = game(background, max_speed, min_speed, occurrock, occurrock2, Fly, music)

    pygame.quit()

if __name__ == "__main__":
    main()

