import pygame
import math

#Setting the window
pygame.init()
screen = pygame.display.set_mode((800, 600))

#Setting the middle of the window
screen_center_x = 800/2
screen_center_y = 600/2

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

#Setting clock
clock = pygame.time.Clock()

#Check if player is alive
alive = True

class Player(object):
    def __init__(self):
        self.asset = pygame.image.load('images/ship1.png')
        self.w = self.asset.get_width()
        self.h = self.asset.get_height()
        self.x = screen_center_x
        self.y = screen_center_y
        self.angle = 0
        self.speed = 0
        self.max_speed = 5
        self.deceleration_rate = 0.08
        self.rotatedScreen = pygame.transform.rotate(self.asset, self.angle)
        self.rotatedRect = self.rotatedScreen.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)
        
    def draw(self, screen):
        #screen.blit(self.asset, [self.x, self.y, self.w, self.h])
        screen.blit(self.rotatedScreen, self.rotatedRect)
        
    def turnLeft(self):
        self.angle += 5
        
    def turnRight(self):
        self.angle -= 5
    
    def propulsion(self):
        self.speed = min(self.speed + 0.1, self.max_speed)
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

#Calling classes
player = Player()

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
                if event.key == pygame.K_SPACE:
                    break
            elif selected_button == "exit":
                # If Exit is pressed
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    exit()
        
        pygame.display.flip()
        
#Game Screen
def gameScreen():
    while True:
    # Handle events
        if alive:
            player.update()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.turnLeft()
            if keys[pygame.K_RIGHT]:
                player.turnRight()
            if keys[pygame.K_UP]:
                player.propulsion()
            if not keys[pygame.K_UP]:
                player.deceleration()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                exit()
            
        screen.fill(BLACK)
        player.draw(screen)
        
        pygame.display.flip()
        
        clock.tick(60)
                    
#Main Loop
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit() 
        exit()
    
    startScreen()
    gameScreen()