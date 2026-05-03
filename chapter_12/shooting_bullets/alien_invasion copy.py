import sys

import pygame



class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((900,600))
        pygame.display.set_caption("Super Alien Invasion")
        self.bg_color = (230,230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()    
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(120)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

























































































































