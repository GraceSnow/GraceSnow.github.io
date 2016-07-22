"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (700, 500)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
x = 350
y = 250
xspeed = random.randint(-10,10)
yspeed = random.randint(-10,10)
x2 = 350
y2 = 250
xspeed2 = random.randint(-10,10)
yspeed2 = random.randint(-10,10)
ballsize = random.randint(10,30)
ballcolors = [black, white, green, blue, red]

# BOUNCING BALL CLASS CODE  

class BouncingBall(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, y_speed, ball_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ball_size = ball_size 

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, ball_colors, screen_width, screen_height):

        #ball_color = random.choice(ball_colors) # This is outside because of variable scoping.

        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.ball_size)

# -------- Main Program Loop -----------
#OOP ball
x_location = 350
y_location = 250
x_speed = random.randint(-10,10)
y_speed = random.randint(-10,10)
ball_size = random.randint(10,30)
ball_colors = [black, white, green, blue, red]
ball_color = random.choice(ball_colors)
ball = BouncingBall(x_location, y_location, x_speed, y_speed, ball_size)

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    
    screen.fill(green)
    
    # --- Drawing code should go here
    ball.flashBounce(screen, ball_colors, screen_width, screen_height)
    
    #above OOP ball
    ballcolor = random.choice(ballcolors)
    pygame.draw.circle(screen, ballcolor, [x,y], ballsize)      
    if x <= 0 or x >= 700:
        xspeed = -xspeed
    if y <= 0 or y >= 500:
        yspeed = -yspeed
    x += xspeed
    y += yspeed

    pygame.draw.circle(screen, ballcolor, [x2,y2], ballsize)      
    if x2 <= 0 or x2 >= 700:
        xspeed2 = -xspeed2
    if y <= 0 or y >= 500:
        yspeed2 = -yspeed2
    x2 += xspeed2
    y2 += yspeed2
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
