import pygame
import random

# Initialize Pygame
pygame.init()

# Set window dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define a class for your objects
class MyObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - 50)
        self.rect.y = random.randint(0, screen_height - 50)

# Create a group for the objects
objects = pygame.sprite.Group()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Spawn new objects randomly (adjust the probability as needed)
        if random.randint(0, 100) < 5:
            new_object = MyObject()
            objects.add(new_object)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the objects
    objects.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()