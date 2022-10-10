from re import I
import pygame
import os
import random


width ,height = 900, 500

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game!")




WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 255, 0)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 100
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
bullet_width, bullet_height = 35, 30
ENEMY_WIDTH, ENEMY_HEGIHT = 55 ,40
enemy_VEL = 2

barrier_width, barrier_height = 900, 5






YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

bullet_img = pygame.image.load(os.path.join("assets", "bullet.png"))
bullet_img = pygame.transform.scale(bullet_img, (bullet_width, bullet_height))

enemy_img = pygame.image.load(os.path.join("assets", "enemy.png"))
enemy_img= pygame.transform.scale(enemy_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))


barrier = pygame.Rect((450, 250), (900, 5))




def draw_window(yellow, bullets, enemys):

    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit
    for bullet in bullets:
        WIN.blit(bullet_img, (bullet.x, bullet.y))
    

    for enemy in enemys:
        WIN.blit(enemy_img, (enemy.x, enemy.y))
        
    
    WIN.blits(barrier, (barrier.x, barrier.y))

        
        
        
    
        
        
        
    pygame.display.update()


def yellow_handel_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL < 850:
         yellow.x += VEL  
    if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN] and yellow.y - VEL < 450:
        yellow.y += VEL
        


def moving_bullets(yellow_bullets):
    for bullet in yellow_bullets:
        bullet.y -= BULLET_VEL
        


def moving_enemy(moving_enemys):
    for enemy in moving_enemys:
        enemy.y += enemy_VEL



    
    
        



def main():
    
    yellow = pygame.Rect(500, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    


    
    yellow_bullets = []
    moving_enemys = []
    
    counter = 0
    
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        counter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5)
                    yellow_bullets.append(bullet)
                    
        if counter == 60:
            counter = 0
            for _ in range(1):
                random_enemy_x = random.randrange(0, 900, 1)
                new_enemy = pygame.Rect(random_enemy_x + yellow.width, 0 + yellow.height//2 -2, 10, 5)
                moving_enemys.append(new_enemy)
                
                
        for bullet in yellow_bullets:
            for enemy in moving_enemys: 
                if enemy.colliderect(bullet):
                    run = False
        
                   

            
            
            
        

        

                
    
    
        keys_pressed = pygame.key.get_pressed()
        yellow_handel_movement(keys_pressed, yellow)
        moving_bullets(yellow_bullets)
        moving_enemy(moving_enemys)
            
        draw_window(yellow, yellow_bullets, moving_enemys)
                

    
    pygame.quit()
    
    
if __name__ == "__main__":
    main()