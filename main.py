import pygame
from constants import *
from logger import log_state
from logger import log_event
from player import Player
from circleshape import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import *
from highscores import *
import sys
import random



def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    asteroidfield = AsteroidField()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    player.score += 3
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                add_score(player.score)
                print(f"saving score {player.score}")
                sys.exit()
                
                
        for thing in drawable:
            thing.draw(screen)
        score_text = font.render(f"Score: {player.score:.0f}", True, "white")
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
        

if __name__ == "__main__":
    main()
