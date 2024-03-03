# ? 1. sprite.collide_rect : спрайт - спрайт
# ? 2. sprite.spritecollide : спрайт - группа
# ? 3. sprite.groupcollide : группа - группа

from pygame import *

# ! Основные переменные для проекта
FPS = 60
GAME_FINISHED, GAME_RUN = False, True
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 960
CLOCK = time.Clock()

# ! Создание окна игры
WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Hero in another world")
collide_left = False
collide_top = False
collide_right = False
collide_bottom = False
# ! Классы
class GameSprite(sprite.Sprite):
    def __init__(self, img, position, size, speed):
        super().__init__()
        self.image = transform.smoothscale(
            image.load(img),
            size
        )
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.speed = speed
        self.width, self.height = size
        
    def reset(self):
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            if collide_top == False:
                if bg.rect.y < 0:
                    bg.rect.y += self.speed
                    tree.rect.y += self.speed  
                else:
                    self.rect.y -= self.speed
                if self.rect.y > 0 and self.rect.y != 480:
                    self.rect.y -= self.speed
            
        if keys[K_s] and self.rect.y < WINDOW_HEIGHT - self.height:
            if collide_bottom == False:
                if bg.rect.y + bg.height > WINDOW_HEIGHT:
                    bg.rect.y -= self.speed
                    tree.rect.y -= self.speed  
                else:
                    self.rect.y += self.speed
                if self.rect.y < WINDOW_HEIGHT - self.height and self.rect.y != 480:
                    self.rect.y += self.speed

        if keys[K_a] and self.rect.x > 0:
            if collide_left == False:
                if bg.rect.x < 0:
                    bg.rect.x += self.speed
                    tree.rect.x += self.speed  
                else:
                    self.rect.x -= self.speed
                if self.rect.x > 0 and self.rect.x != 620:
                    self.rect.x -= self.speed

        if keys[K_d] and self.rect.x < WINDOW_WIDTH - self.width:
            if collide_right == False:
                if bg.rect.x + bg.width > WINDOW_WIDTH:
                    bg.rect.x -= self.speed
                    tree.rect.x -= self.speed  
                else:
                    self.rect.x += self.speed
                if self.rect.x < WINDOW_WIDTH - self.width and self.rect.x != 620:
                    self.rect.x += self.speed

class Wall(GameSprite):
    def __init__(self, img, position, size, speed):
        super().__init__(img, position, size, speed)
    



        
    
bg = GameSprite(img="bg.png",
                position=(0, 0),
                size=(4000, 2000),
                speed=5)

player = Player(img="school_form.png",
                position=(620, 480),
                size=(50, 70),
                speed=5)
tree = Wall(img="school_form.png",
                position=(800, 550),
                size=(50, 70),
                speed=0)


# ! Игровой цикл
while GAME_RUN:
    for ev in event.get():
        if ev.type == QUIT:
            GAME_RUN = False  
    
    # ? Отрисовка
    bg.reset()
    player.reset()
    tree.reset()

    if player.rect.bottom  tree.rect.top:
        collide_bottom = True



    # ? Логика игры (работает пока не проиграем/выиграем)
    if not GAME_FINISHED:
        player.update()
 
    display.update()
    CLOCK.tick(FPS)
