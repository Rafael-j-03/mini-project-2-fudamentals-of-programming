import pygame
import math
import random

#Setting the window
pygame.init()
screen = pygame.display.set_mode((800, 600))

#Caption
pygame.display.set_caption("Comets")

#Window stuff
screen_center_x = 800/2
screen_center_y = 600/2
screen_width = screen.get_width()
screen_height = screen.get_height()

#Assets
ship = pygame.image.load('images/ship1.png')
bigAsteroid = pygame.image.load('images/bigAsteroid.png')
mediumAsteroid = pygame.image.load('images/mediumAsteroid.png')
smallAsteroid = pygame.image.load('images/smallAsteroid.png')

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

#Setting clock
clock = pygame.time.Clock()

#Check if player is alive
alive = True

#Player Class
class Player(object):
    def __init__(self):
        self.asset = ship
        self.w = self.asset.get_width()
        self.h = self.asset.get_height()
        self.x = screen_center_x
        self.y = screen_center_y
        self.angle = 0
        self.speed = 0
        self.max_speed = 5
        self.deceleration_rate = 0.05
        self.rotatedScreen = pygame.transform.rotate(self.asset, self.angle)
        self.rotatedRect = self.rotatedScreen.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)
    
    def draw(self, screen):
        screen.blit(self.rotatedScreen, self.rotatedRect)
    
    def turnLeft(self):
        self.angle += 5
        
    def turnRight(self):
        self.angle -= 5
    
    def propulsion(self):
        self.speed = min(self.speed + 0.08, self.max_speed)
        self.x += self.speed * self.cosine
        self.y -= self.speed * self.sine
        
    def deceleration(self):
        self.speed = max(self.speed - self.deceleration_rate, 0)
        self.x += self.speed * self.cosine
        self.y -= self.speed * self.sine
        
    def update(self):
        self.rotatedScreen = pygame.transform.rotate(self.asset, self.angle)
        self.rotatedRect = self.rotatedScreen.get_rect()
        self.rotatedRect.center = (self.x , self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)
        # Check if the player has reached the edge of the screen and wrap around if necessary
        if self.x > screen_width + 25:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = screen_width
        elif self.y < -25:
            self.y = screen_height
        elif self.y > screen_height + 25:
            self.y = 0

#Bullet class
class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 5
        self.h = 5
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s * 10
        self.creation_time = pygame.time.get_ticks()
        
    def update(self):
        self.x += self.xv
        self.y -= self.yv
        current_time = pygame.time.get_ticks()
        if current_time - self.creation_time > 4000:  # Remove the bullet after 4 seconds
            playerBullets.remove(self)
        # Check if the bullet has reached the edge of the screen and wrap around if necessary
        if self.x > screen_width + 2.5:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = screen_width
        elif self.y < -2.5:
            self.y = screen_height
        elif self.y > screen_height + 2.5:
            self.y = 0
        
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, [self.x ,self.y , self.w, self.h])
        
#Class Asteroid
class Asteroid(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.asset = smallAsteroid
        if self.rank == 2:
            self.asset = mediumAsteroid
        if self.rank == 3:
            self.asset = bigAsteroid
        self.w = 50 * rank
        self.h = 50 * rank
        self.sPoint = random.choice([(random.randrange(0, screen_width - self.w), random.choice([-1 * self.h - 5, screen_height + 5])), (random.choice([-1 * self.w - 5, screen_width + 5]), random.randrange(0, screen_height - self.h))])
        self.x, self.y = self.sPoint
        if self.x < screen_width//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < screen_height//2:
            self.ydir = 1
        else:
            self.ydir = -1
        #Random Speed for each asteroid
        self.xv = self.xdir * random.randrange(1,3)
        self.yv = self.ydir * random.randrange(1,3)
        
    def update(self):
        self.x += self.xv
        self.y += self.yv
        # Check if the asteroid has reached the edge of the screen and wrap around if necessary
        if self.x + self.w < 0:
            self.x = screen_width
        elif self.x > screen_width:
            self.x = -self.w
        if self.y + self.h < 0:
            self.y = screen_height
        elif self.y > screen_height:
            self.y = -self.h
        
    def draw(self, screen):
        screen.blit(self.asset, (self.x, self.y))

#Calling essential stuff
player = Player()
playerBullets = []
bullet = Bullet()
asteroids = []

#Start Screen
def startScreen():
    # Create font objects
    font = pygame.font.Font(None, 50)
    title_font = pygame.font.Font(None, 150)
    
    # Create text labels for the tile, the start button and the exit button
    title_text = title_font.render("COMETS", True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (screen_center_x, screen_center_y - 200)
    start_text = font.render("START", True, WHITE)
    start_rect = start_text.get_rect()
    start_rect.center = (screen_center_x, screen_center_y - 25)
    exit_text = font.render("EXIT", True, WHITE)
    exit_rect = exit_text.get_rect()
    exit_rect.center = (screen_center_x, screen_center_y + 25)
    
    #Setting the loop to the start screen
    selected_button = "start"  # Start with the start button selected
    while True:
        # Draw the start and exit buttons on the screen
        screen.fill((0, 0, 0))
        screen.blit(title_text, title_rect)
        if selected_button == "start":
            screen.blit(font.render("START", True, RED), start_rect)
            screen.blit(exit_text, exit_rect)
        else:
            screen.blit(start_text, start_rect)
            screen.blit(font.render("EXIT", True, RED), exit_rect)

        # Wait for a keyboard event
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            # Highligh the selected button
            if event.key == pygame.K_UP:
                # Highlight the start button
                selected_button = "start"
            elif event.key == pygame.K_DOWN:
                # Highlight the exit button
                selected_button = "exit"
            
            # Pressed a button
            if selected_button == "start":
                # If start is pressed
                if event.key == pygame.K_RETURN:
                    break
            elif selected_button == "exit":
                # If Exit is pressed
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    exit()
        
        pygame.display.flip()
        
#Game Screen
def gameScreen():
    #Starting with 2 big Asteroids
    asteroids.append(Asteroid(3))
    asteroids.append(Asteroid(3))
    
    # Set the time interval between key press events (in milliseconds)
    time_interval = 1000
    
    # Set the time of the last key press event to 0
    last_key_time = 0
    
    # Setting a count
    count = 0

    while True:
        clock.tick(60)
        count += 1
    # Handle events
        if alive:
            activeBigAsteroids = asteroids.count(Asteroid(3))
            activeMediumAsteroids = asteroids.count(Asteroid(2))
            activeSmallAsteroids = asteroids.count(Asteroid(1))
            # Check if are too much asteroids in the screen to spawn more after
            if (activeBigAsteroids > 2) or (activeMediumAsteroids > 6) or (activeSmallAsteroids > 15):
                if count % 150 == 0:
                    asteroids.append(Asteroid(3))
                
            player.update()
            
            for b in playerBullets:
                b.update()
                
            for a in asteroids:
                a.update()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.turnLeft()
            if keys[pygame.K_RIGHT]:
                player.turnRight()
            if keys[pygame.K_UP]:
                player.propulsion()
            if not keys[pygame.K_UP]:
                player.deceleration()
            if keys[pygame.K_SPACE]:
                current_time = pygame.time.get_ticks()
                if current_time - last_key_time > time_interval:
                    playerBullets.append(Bullet())
                    last_key_time = current_time
                
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                exit()
                    
            
        screen.fill(BLACK)
        player.draw(screen)
        
        for b in playerBullets:
            b.draw(screen)
            
        for a in asteroids:
            a.draw(screen)
        
        pygame.display.flip()
                    
#Main Loop
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit() 
        exit()
    
    startScreen()
    gameScreen()