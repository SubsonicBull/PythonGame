import pygame
import sys

# pygame initialisieren
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600

# Fenster erstellen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mein Spiel")

# Hauptloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Hintergrundfarbe (RGB)
    screen.fill((30, 30, 30))

    # Fenster aktualisieren
    pygame.display.flip()