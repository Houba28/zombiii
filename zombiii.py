import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
from player import player
import enemy
import game
import math
from time import sleep
import drawing
import os

def exit_game():
    pygame.quit()
    sys.exit()

def draw_player(player, X, Y):  
    #pygame.draw.line(window,(50,200,0),(X,Y),(X+(player.left_x*player.left_c),Y+(player.left_y*player.left_c)),1)
    #pygame.draw.line(window,(50,200,0),(X,Y),(X+(player.top_x*player.top_c),Y+(player.top_y*player.top_c)),1)
    #pygame.draw.line(window,(50,200,0),(X,Y), (X+(player.right_x*player.right_c),Y+(player.right_y*player.right_c)),1)
    pygame.draw.aalines(window,player.color, True, ((X+(player.left_x*player.left_c),Y+(player.left_y*player.left_c)), 
                                                (X+(player.top_x*player.top_c),Y+(player.top_y*player.top_c)),
                                                (X+(player.right_x*player.right_c),Y+(player.right_y*player.right_c))), 2)

def draw_bullet(bullet, X, Y):
    pygame.draw.aaline(window, bullet.color, (bullet.x, bullet.y), (X + bullet.x_end, Y + bullet.y_end), 2)

def draw_enemy(enemy):
    pygame.draw.circle(window, enemy.color, (math.ceil(enemy.x), math.ceil(enemy.y)), 20 ,4)

def update_game(game, enemy_list):
    window.fill((0,0,0))
    time = GAME_TIME.get_ticks()
    draw_player(player, game.screen_x/2, game.screen_y/2)
    
    for bullet in player.bullets:
        bullet.move()
        draw_bullet(bullet, game.screen_x/2, game.screen_y/2)

    for idx, zombi in enumerate(enemy_list):
        zombi.move(player, time)
        zombi.check_player_reachable(50, player, time)
        draw_enemy(zombi)
        if player.check_enemy_hit(zombi):
            del enemy_list[idx]
    game.level = int(game.score/(game.level*10) + 1)
    if game.level > game.max_level:
        game.level = game.max_level

def show_HUD(player, game):
    #score
    size = 30
    color = (255,255,255)
    thickness = 3
    space = 10
    drawing.print_text(window, str(game.score), (space,space), thickness, size, color)
    # lives
    for live in range(player.lives):
        pygame.draw.aalines(window,(255,0,0), True, [(5+space+(30+space)*live,0+(game.screen_y-space-30)),((10+space)+(30+space)*live,0+(game.screen_y-space-30)),
            ((15+space)+(30+space)*live,5+(game.screen_y-space-30)),((20+space)+(30+space)*live,0+(game.screen_y-space-30)),((25+space)+(30+space)*live,0+(game.screen_y-space-30)),
            ((30+space)+(30+space)*live,5+(game.screen_y-space-30)),((30+space)+(30+space)*live,10+(game.screen_y-space-30)),((15+space)+(30+space)*live,25+(game.screen_y-space-30)),
            ((0+space)+(30+space)*live,10+(game.screen_y-space-30)),((0+space)+(30+space)*live,5+(game.screen_y-space-30))], thickness)
    # developer
    if(game.show_dev):
        enemies_cnt = str(len(game.enemies))
        bullets_cnt = str(len(player.bullets))
        drawing.print_text(window, "ENEMIES: "+enemies_cnt, (game.screen_x - size*(15) + space,10), thickness, size, color)
        drawing.print_text(window, "BULLETS: "+bullets_cnt, (game.screen_x - size*(15) + space,10+size+space), thickness, size, color)
        drawing.print_text(window, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.!:?", (space,game.screen_y-(size+space)*3), thickness, size, color)
        drawing.print_text(window, "LIVES: "+str(player.lives), (space,game.screen_y-(size+space)*2), thickness, size, color)
        drawing.print_text(window, "LEVEL: "+str(game.level)+"TIME: "+str(game.intervals[game.level]), (space,(size+space)*2), thickness, size, color)

def show_settings():
    pass

def show_scores():
    pass

def show_menu(game, name, items):
    space = 10
    name_color = (0,255,0)
    name_thickness = 8
    name_size = 50
    size = 30
    color = (255,255,255)
    chosen_color = (20,255,20)
    chosen_thickness = 4
    thickness = 3
    chosen = 0

    while True:
        window.fill((0,0,0))
        drawing.print_text(window, name, ((game.screen_x-(len(name)*name_size))/2,((game.screen_y)/2-name_size-(len(items)*(size+space)-space))), name_thickness, name_size, name_color)

        for idx, item in enumerate(items):
            if idx == chosen:
                drawing.print_text(window, item["label"], ((game.screen_x-(len(item["label"])*size))/2,((game.screen_y)/2-name_size-(len(items)*(size+space))+space)+name_size+space*2+ (size+space)*idx), chosen_thickness, size, chosen_color)
            else:
                drawing.print_text(window, item["label"], ((game.screen_x-(len(item["label"])*size))/2,((game.screen_y)/2-name_size-(len(items)*(size+space))+space)+name_size+space*2+ (size+space)*idx), thickness, size, color)

        for event in GAME_EVENTS.get():    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_RETURN:
                    if chosen > 0:
                        items[chosen]["callback"]()
                    else:
                        return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    chosen +=1
                    if chosen >= len(items):
                        chosen = 0
                if event.key == pygame.K_UP:
                    chosen -= 1
                    if chosen < 0:
                        chosen = len(items)-1

            if event.type == GAME_GLOBALS.QUIT:
                    pygame.quit()
                    sys.exit()

        clock.tick(60)
        pygame.display.update()



def pause_game(game, enemy_time,pause):
    time = GAME_TIME.get_ticks() - enemy_time
    menu = [{"label":"return", "callback":lambda: None },{"label":"settings", "callback":show_settings},{"label":"high score", "callback":show_scores},{"label":"exit", "callback":exit_game}]
    show_menu(game, "PAUSE", menu)
    enemy_time = (GAME_TIME.get_ticks() + time)

def classic():
    pass

def survival():
    player.rotate((45+180)*(math.pi/180))
    last_enemy_ctime = 0
    gameStarted = False
    pause = False
    left = False
    right = False
    show_dev = False
    while True:
        gameStarted = True
        update_game(game, game.enemies)

        if (GAME_TIME.get_ticks() - last_enemy_ctime > game.intervals[int(game.level)-1]) and (gameStarted is True):
            game.enemies.append( enemy.enemy(game) )
            last_enemy_ctime= GAME_TIME.get_ticks()
        
        if left:
            player.all_rotate_left()
        if right:
            player.all_rotate_right()

        for event in GAME_EVENTS.get():
            if event.type == GAME_GLOBALS.QUIT:
               exit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True
                if event.key == pygame.K_LEFT:    
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_SPACE:
                    player.shoot(game.screen_x/2, game.screen_y/2)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pause_game(game, last_enemy_ctime, pause)
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_SEMICOLON:
                    if game.show_dev:
                        game.show_dev = False
                    else:
                        game.show_dev = True
        if player.lives == 0:
            #save score,etc 
            break
        clock.tick(60)
        
        show_HUD(player, game)

        pygame.display.update()


if __name__ == "__main__":
    global game
    game = game.game()
    global player
    player = player(game)
    pygame.init()
    pygame.display.set_caption('Zombiii')
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((game.screen_x,game.screen_y))
    volume = 1.0
    pygame.mixer.init()
    # pygame.mixer.music.load(os.path.join(os.getcwd(),'assets/music.ogg'))
    # pygame.mixer.music.play(-1)
    

    menu = [{"label":"Classic game", "callback":classic },{"label":"Survival game", "callback":survival },{"label":"settings", "callback":show_settings},{"label":"high score", "callback":show_scores},{"label":"exit", "callback":exit_game}]
    show_menu(game, "ZOMBIII", menu)
    