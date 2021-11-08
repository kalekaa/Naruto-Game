#PyGame
# Enemies

import pygame
pygame.init()

# Displays Window Size
window = pygame.display.set_mode((1000, 500))

# Captions the Window
pygame.display.set_caption("Collision and Hit Boxes")

# Loads in images for walking
walkRight = [pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoRun0.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoRun1.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoRun2.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoRun3.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoRun4.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoRun5.png')]
walkLeft = [pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoLeft0.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoLeft1.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoLeft2.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoLeft3.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoLeft4.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoLeft5.png')]

# Background Image
bg = pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\bg.png')

# When character is jumping/standing
char = pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoIdle.png')
charLeft = pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\NarutoIdleLeft.png')
# Changes FPS in game
clock = pygame.time.Clock()


# Class for Character Attributes
class player(object):
    def __init__(self, x, y, width, height):

        # Starting Point
        self.x = x
        self.y = y

        # Height and Width of Character
        self.width = width
        self.height = height

        # Velocity of Character
        self.vel = 10

        # Indicates if Character is Jumping
        self.isJump = False
        self.jumpCount = 8
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

        # Defines Hit Box
                    # x-crd., y-crd., width, hieght of hit box
        self.hitbox = (self.x, self.y, 45, 70)

        
    def draw(self, window):
        # Displaying 6 Sprites within 3 frames
        if self.walkCount + 1 >= 18:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                window.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                window.blit(char, (self.x, self.y))
            else:
                window.blit(charLeft, (self.x, self.y))
        self.hitbox = (self.x, self.y, 45, 70)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

# Class to make an Enemy
class enemy(object):
    walkRight =[pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiR1.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiR2.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiR3.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiR4.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiR5.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiR6.png')]
    walkLeft = [pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiL1.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiL2.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiL3.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiL4.png'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiL5.png.'), pygame.image.load(r'C:\Users\zayas\OneDrive\Documents\Basic_Game\TobiL6.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3

        # Defines Enemy Hitbox
        self.hitbox = (self.x + 15, self.y, 40, 60)

    def draw(self, window):
        self.move()
        if self.walkCount + 1 >= 18:
            self.walkCount = 0

        if self.vel > 0:
            window.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1

    
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        self.hitbox = (self.x + 15, self.y, 40, 60)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    # Hit box Collision
    def hit(self):
        print("Hit")
        
    
        
        
# Class to create projectiles
class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 40 * facing

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

# Class to draw; don't draw in main loop
def redrawGameWindow():

    # Sets background image
    window.blit(bg, (0, 0))
    naruto.draw(window)
    tobi.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()

# Main Loop
naruto = player(0, 395, 70, 70)
tobi = enemy(100, 395, 64, 64, 450)
shootCap = 0
bullets = []
run = True

while run != False:

    # Time delay so events don't happen super quick; in-game clock
    clock.tick(27)

    if shootCap > 0:
        shootCap+= 1
    if shootCap > 3:
        shootCap = 0

    # Check for Events; User Key Input
    # List for all events that happen
    for event in pygame.event.get():
        # User quits program
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        # check if bullets are in the same y-crd.
        # Checks to see if bullet is above the bottom of the hitbox # Checks to see if bullet is below the top of hitbox
        if bullet.y - bullet.radius < tobi.hitbox[1] + tobi.hitbox[3] and bullet.y + bullet.radius > tobi.hitbox[1]:
            if bullet.x + bullet.radius > tobi.hitbox[0] and bullet.x - bullet.radius < tobi.hitbox[0] + tobi.hitbox[2]:
                tobi.hit()             
                bullets.pop(bullets.index(bullet))
        
        if bullet.x < 1000 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    # list for user input when keys are pressed
    keys = pygame.key.get_pressed()

    # if statements to move character by the velocity in direction
    if keys[pygame.K_SPACE] and shootCap == 0:
        if naruto.left:
            facing = -1
        else:
            facing = 1
        
        if len(bullets) < 3:
            bullets.append(projectile(round(naruto.x + naruto.width//2), round(naruto.y + naruto.height//2), 6, (0, 0, 0), facing))

        shootCap = 1
                        # Make sure character stays on screen
    if keys[pygame.K_LEFT] and naruto.x > naruto.vel:
        naruto.x -= naruto.vel

        # Image for running left
        naruto.left = True
        naruto.right = False
        naruto.standing = False
                        # Creates border line
    elif keys[pygame.K_RIGHT] and naruto.x < 1000 - naruto.width - naruto.vel:
        naruto.x += naruto.vel

        # Image for running right
        naruto.right = True
        naruto.left = False
        naruto.standing = False
        
    # idle image
    else:
       naruto.standing = True
       naruto.walkCount = 0
        
    if not(naruto.isJump):   

        # Character Jump
        if keys[pygame.K_UP]:
            naruto.isJump = True
            naruto.right = False
            naruto.left = False
            naruto.walkCount = 0
    else:
        if naruto.jumpCount >= -8:
            neg = 1
            if naruto.jumpCount < 0:
                neg = -1
            naruto.y -= (naruto.jumpCount**2) * 0.5 * neg
            naruto.jumpCount -= 1
        else:
            naruto.isJump = False
            naruto.jumpCount = 8

    redrawGameWindow()
            
pygame.quit()
