import pygame as pg
from random import randrange

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE// 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE),randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir= (0,0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW]*2)
clock = pg.time.Clock()
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1,pg.K_d: 1 }
#los controles si borras o modificas esto sin saber la mierda no va a funcionar
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1,pg.K_d: 1 }
            if event.key == pg.K_s:
                snake_dir = (0, TILE_SIZE)
                dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1,pg.K_d: 1 }
            if event.key == pg.K_a:
                snake_dir = (-TILE_SIZE , 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1,pg.K_d: 0 }
            if event.key == pg.K_d:
                snake_dir = (TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0,pg.K_d: 1 }
        screen.fill('black')
        #si se xoca (con la pared y ella misma) la serpiente jaja que tonta
        self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
        if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
            snake.center, food.center = get_random_position(), get_random_position()
            length, snake_dir = 1, (0,0)
            segments = [snake.copy()]
        #check la food esa
        if snake.center == food.center:
            food.center = get_random_position()
            length += 1
        #Dibujar la manzana
        pg.draw.rect(screen, 'red',food)
        #Dibujar la serpiente
        [pg.draw.rect(screen, 'green', segment)for segment in segments]
        #Sin esto la mierda no se va a mover
        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]
        pg.display.flip()
        clock.tick(60)
