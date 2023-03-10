import pygame
import math
import random

# Setting the window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Caption
pygame.display.set_caption("Comets")

# Window stuff
screen_center_x = 800/2
screen_center_y = 600/2
screen_width = screen.get_width()
screen_height = screen.get_height()

# Assets
ship = pygame.image.load('images/ship1.png')
bigAsteroid = pygame.image.load('images/bigAsteroid.png')
mediumAsteroid = pygame.image.load('images/mediumAsteroid.png')
smallAsteroid = pygame.image.load('images/smallAsteroid.png')

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

# Setting clock
clock = pygame.time.Clock()

# Player Class
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
        self.score = 0
        self.initials = ''
    
    def get_score(self):
        return self.score
    
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
    
    def reset(self):
        # Reset the player object to its original state
        self.__init__()

# Bullet class
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
        
# Class Asteroid
class Asteroid(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.asset = smallAsteroid
            self.w = self.asset.get_width()
            self.h = self.asset.get_height()
        if self.rank == 2:
            self.asset = mediumAsteroid
            self.w = self.asset.get_width()
            self.h = self.asset.get_height()
        if self.rank == 3:
            self.asset = bigAsteroid
            self.w = self.asset.get_width()
            self.h = self.asset.get_height()
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
        # Random Speed for each asteroid
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

# Calling essential stuff
player = Player()
playerBullets = []
bullet = Bullet()
asteroids = []

# Start Screen
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
        screen.fill(BLACK)
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
        
# Game Screen
def gameScreen():
    # Check if player is alive
    alive = True
    # Starting with 2 big Asteroids
    asteroids = [Asteroid(3),Asteroid(3)]
    # Set the time interval between key press events (in milliseconds)
    time_interval = 1000
    # Set the time of the last key press event to 0
    last_key_time = 0
    # Setting a count
    count = 0
    # Setting the score font
    score_font = pygame.font.Font(None, 30)

    while alive:
        # Updating the score
        score_text = score_font.render("Score: " + str(player.score), 1, WHITE)
        # Set FPS
        clock.tick(60)
        # Clear the screen
        screen.fill(BLACK)
        # Handle events
        if alive:
            # Player Update
            player.update()
            # Bullets Update
            for b in playerBullets:
                b.update()
            # Asteroids update
            for a in asteroids:
                a.update()
                if (player.x >= a.x and player.x <= a.x + a.w) or (player.x + player.w >= a.x and player.x + player.w <= a.x + a.w):
                    if (player.y >= a.y and player.y <= a.y + a.h) or (player.y + player.h >= a.y and player.y + player.h <= a.y + a.h):
                        alive = False
                
                # Bullet Collission
                for b in playerBullets:
                    if (b.x >= a.x and b.x <= a.x + a.w) or (b.x + b.w >= a.x and b.x + b.w <= a.x + a.w):
                        if (b.y >= a.y and b.y <= a.y + a.h) or (b.y + b.h >= a.y and b.y + b.h <= a.y + a.h):
                            if a.rank == 3:
                                player.score += 10
                                new_asteroid1 = Asteroid(2)
                                new_asteroid2 = Asteroid(2)
                                new_asteroid3 = Asteroid(2)
                                new_asteroid1.x = a.x
                                new_asteroid2.x = a.x
                                new_asteroid3.x = a.x
                                new_asteroid1.y = a.y
                                new_asteroid2.y = a.y
                                new_asteroid3.y = a.y
                                asteroids.append(new_asteroid1)
                                asteroids.append(new_asteroid2)
                                asteroids.append(new_asteroid3)
                            elif a.rank == 2:
                                player.score += 20
                                new_asteroid1 = Asteroid(1)
                                new_asteroid2 = Asteroid(1)
                                new_asteroid3 = Asteroid(1)
                                new_asteroid4 = Asteroid(1)
                                new_asteroid5 = Asteroid(1)
                                new_asteroid1.x = a.x
                                new_asteroid2.x = a.x
                                new_asteroid3.x = a.x
                                new_asteroid4.x = a.x
                                new_asteroid5.x = a.x
                                new_asteroid1.y = a.y
                                new_asteroid2.y = a.y
                                new_asteroid3.y = a.y
                                new_asteroid4.y = a.y
                                new_asteroid5.y = a.y
                                asteroids.append(new_asteroid1)
                                asteroids.append(new_asteroid2)
                                asteroids.append(new_asteroid3)
                                asteroids.append(new_asteroid4)
                                asteroids.append(new_asteroid5)
                            else:
                                player.score += 30
                            asteroids.pop(asteroids.index(a))
                            playerBullets.pop(playerBullets.index(b))
                            
            # Count the number of asteroids from each level using a list comprehension
            num_bigAsteroids = len([a for a in asteroids if a.rank == 1])
            num_mediumAsteroids = len([a for a in asteroids if a.rank == 2])
            num_smallAsteroids = len([a for a in asteroids if a.rank == 3])
            # Check if are too much asteroids in the screen to spawn more after
            if (num_smallAsteroids < 2) and (num_mediumAsteroids < 6) and (num_bigAsteroids < 15):
                count += 1
                if count % 200 == 0:
                    asteroids.append(Asteroid(3))
            
            # Keyboard Inputs
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
        # If the player wants to close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                exit()            
        # Drawing
        player.draw(screen)
        #Bullets drawing
        for b in playerBullets:
            b.draw(screen)
        #Asteroids drawing
        for a in asteroids:
            a.draw(screen)
        # Shows the score
        screen.blit(score_text, (screen_width - score_text.get_width() - 25, 25))
        # Update the screen
        pygame.display.flip()

#Game Over Screen
def gameOverScreen():
    # Set the background color to black
    screen.fill(BLACK)
    # Display the game over message
    font = pygame.font.Font(None, 170)
    text = font.render("GAME OVER", True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen_center_x
    text_rect.centery = screen_center_y
    screen.blit(text, text_rect)
    # Update the display
    pygame.display.update()
    # Wait for 2 seconds
    pygame.time.delay(2000)

def write_to_leaderboard(player):
    # Read the scores from the leaderboard.txt file
    scores = []
    with open("leaderboard.txt", "r") as f:
        for line in f:
            score, initials = line.strip().split(",")
            scores.append((int(score), initials))
    # Sort the scores in descending order by score
    scores = sorted(scores, key=lambda x: x[0], reverse=True)
    # Prompt the player to enter their initials if their score is one of the top 10 scores
    if len(scores) < 10 or player.get_score() > scores[9][0]:
        while True:
            initials = input("\nEnter your initials (3 Characters only): ")
            # Convert the initials to uppercase
            initials = initials.upper()
            # Limit the length of the initials to 3 characters
            if len(initials) == 3:
                # Write the player's score and initials to the leaderboard.txt file
                with open("leaderboard.txt", "a") as f:
                    f.write(f"{player.get_score()},{initials}\n")
                break
            else:
                print("\nError: Initials must be 3 characters long.")
    # Update the display
    pygame.display.flip()

def display_scores(scores, screen):
    # Create a font object
    font = pygame.font.Font(None, 40)
    leaderboard_font = pygame.font.Font(None, 50)
    score_surfaces = []
    score_rects = []
    y_offset = 0
    for score in scores:
        # Create a surface with the leaderboard text
        leaderboard_text = leaderboard_font.render("Leaderboard", True, WHITE)
        # Get the dimensions of the surface
        leaderboard_rect = leaderboard_text.get_rect()
        # Set the position of the surface
        leaderboard_rect.center = (screen_center_x, 50)
        # Create a surface with the score
        score_surface = font.render(score, True, WHITE)
        # Get the dimensions of the surface
        score_rect = score_surface.get_rect()
        # Set the position of the surface
        score_rect.center = (screen_center_x, 100 + y_offset)
        # Add the surface and rect to the lists
        score_surfaces.append(score_surface)
        score_rects.append(score_rect)
        # Increment the y offset
        y_offset += 50
    # Clear the screen
    screen.fill(BLACK)
    # Draw the scores surfaces on the screen
    for score_surface, score_rect in zip(score_surfaces, score_rects):
        screen.blit(score_surface, score_rect)
    screen.blit(leaderboard_text, leaderboard_rect)
    # Update the display
    pygame.display.flip()

def display_leaderboard(player, screen):
    scores = []
    with open("leaderboard.txt", "r") as f:
        for line in f:
            score, initials = line.strip().split(",")
            scores.append((int(score), initials))
    # Sort the scores in descending order by score
    scores = sorted(scores, key=lambda x: x[0], reverse=True)
    # Keep track of the number of scores that have been added to the leaderboard
    num_scores_added = 0
    leaderboard_text = []
    for i, (score, initials) in enumerate(scores[:10]):
        leaderboard_text.append(f"{initials}: {score}")
        num_scores_added += 1
    # Add the player's score and initials to the leaderboard if it is one of the top 10 scores
    if num_scores_added < 10 and player.get_score() >= scores[num_scores_added][0]:
        leaderboard_text.append(f"{player.initials}: {player.get_score()}")
        num_scores_added += 1
    # Display the scores on the screen
    display_scores(leaderboard_text, screen)
    # Update the display
    pygame.display.update()
    # Wait for 6 seconds
    pygame.time.delay(6000)
                    
# Game main Loop
while True:
    # Show the start screen
    startScreen()
    # Show the game screen
    gameScreen()
    # Show the game over screen
    gameOverScreen()
    # Write the player's score and initials to the leaderboard
    write_to_leaderboard(player)
    # Display the leaderboard
    display_leaderboard(player, screen)
    # Reset the game variables and objects
    player.reset()
    playerBullets = []
    asteroids = []