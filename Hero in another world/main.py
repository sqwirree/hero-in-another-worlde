from pygame import *

# Основные переменные для проекта
FPS = 60
GAME_FINISHED, GAME_RUN = False, True
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 960
CLOCK = time.Clock()

# Создание окна игры
WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Hero in another world")

# Классы
class GameSprite(sprite.Sprite):
    def __init__(self, img, position, size, speed):
        super().__init__()
        self.image = transform.smoothscale(
            image.load(img),
            size
        )
        self.rect = self.image.get_rect(topleft=position)
        self.speed = speed
        
    def reset(self):
        WINDOW.blit(self.image, self.rect)

    def is_colliding(self, side, spr):
        if side.lower() == "left":
            is_colliding = self.rect.collidepoint(spr.rect.topright) or self.rect.collidepoint(spr.rect.bottomright) or self.rect.collidepoint(spr.rect.midright)
            return is_colliding
        
        if side.lower() == "right":
            is_colliding = self.rect.collidepoint(spr.rect.topleft) or self.rect.collidepoint(spr.rect.bottomleft) or self.rect.collidepoint(spr.rect.midleft)
            return is_colliding
        
        if side.lower() == "bottom":
            is_colliding = self.rect.collidepoint(spr.rect.topleft) or self.rect.collidepoint(spr.rect.midtop) or self.rect.collidepoint(spr.rect.topright)
            return is_colliding
        
        if side.lower() == "top":
            is_colliding = self.rect.collidepoint(spr.rect.bottomleft) or self.rect.collidepoint(spr.rect.midbottom) or self.rect.collidepoint(spr.rect.bottomright)
            return is_colliding

class Player(GameSprite):
    def __init__(self, img, img_back, position, size, speed):
        super().__init__(img, position, size, speed)
        self.img_back = img_back
        self.images = [transform.smoothscale(
            image.load(img_back + '/' + str(i) + '.png'),
            size
        ) for i in range(8)]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.bottom_collided = False
        self.left_collided = False
        self.right_collided = False
        self.top_collided = False

    def update(self):
        self.bottom_collided = False
        self.left_collided = False
        self.right_collided = False
        self.top_collided = False

        for block in blocks:
            if block.is_colliding("top", self):
                self.bottom_collided = True
            
            if block.is_colliding("bottom", self):
                self.top_collided = True
            
            if block.is_colliding("left", self):
                self.right_collided = True
            
            if block.is_colliding("right", self):
                self.left_collided = True
        
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.image = self.images[self.image_index]
            self.image_index = (self.image_index + 1) % len(self.images)
            if not self.top_collided:
                if bg.rect.y < 0:
                    bg.rect.y += self.speed
                    for block in blocks:
                        block.rect.y += self.speed  
                else:
                    self.rect.y -= self.speed
                if self.rect.y > 0 and self.rect.y != 480:
                    self.rect.y -= self.speed
            
        if keys[K_s] and self.rect.y < WINDOW_HEIGHT - self.rect.height:
            if not self.bottom_collided:
                if bg.rect.y + bg.rect.height > WINDOW_HEIGHT:
                    bg.rect.y -= self.speed
                    for block in blocks:
                        block.rect.y -= self.speed  
                else:
                    self.rect.y += self.speed
                if self.rect.y < WINDOW_HEIGHT - self.rect.height and self.rect.y != 480:
                    self.rect.y += self.speed

        if keys[K_a] and self.rect.x > 0:
            if not self.left_collided:
                if bg.rect.x < 0:
                    bg.rect.x += self.speed
                    for block in blocks:
                        block.rect.x += self.speed  
                else:
                    self.rect.x -= self.speed
                if self.rect.x > 0 and self.rect.x != 620:
                    self.rect.x -= self.speed

        if keys[K_d] and self.rect.x < WINDOW_WIDTH - self.rect.width:
            if not self.right_collided:
                if bg.rect.x + bg.rect.width > WINDOW_WIDTH:
                    bg.rect.x -= self.speed
                    for block in blocks:
                        block.rect.x -= self.speed  
                else:
                    self.rect.x += self.speed
                if self.rect.x < WINDOW_WIDTH - self.rect.width and self.rect.x != 620:
                    self.rect.x += self.speed

class Wall(GameSprite):
    def __init__(self, img, position, size, speed):
        super().__init__(img, position, size, speed)

bg = GameSprite(img="C:/Users/1202v/OneDrive/Рабочий стол/Hero in another world/pictures/bg/bg.png",
                position=(0, 0),
                size=(4000, 2000),
                speed=5)

school_form = Player(img="school_form.png",
                     img_back="school_form_back",
                     position=(620, 480),
                     size=(50, 70),
                     speed=7)
blocks = [Wall(img="school_form.png",
                position=(800, 550),
                size=(50, 70),
                speed=0)]

# Игровой цикл
while GAME_RUN:
    for ev in event.get():
        if ev.type == QUIT:
            GAME_RUN = False  
    
    # Отрисовка
    bg.reset()
    school_form.reset()
    for block in blocks:
        block.reset()

    # Логика игры (работает пока не проиграем/выиграем)
    if not GAME_FINISHED:
        school_form.update()  # Update players
 
    display.update()
    CLOCK.tick(FPS)