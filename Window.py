import pygame

class Window:

    def __init__(self, title="Wack-A-Mole", colorRGB=False):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(title)
        self.color = (0, 0, 0)
        if colorRGB:
            self.color = colorRGB
        self.screen.fill(self.color)

    def setColor(self, colorRGB):
        self.screen.fill(colorRGB)

  
    def update(self, screenObj=False):
        if screenObj:
            self.screen.fill(screenObj.color)
            screenObj.display()

        else:
            self.screen.fill(self.color)
        screenObj.display()
        pygame.display.flip()

    def checkForInput(self, screen):
        #check for inputs
        for event in pygame.event.get():
            #handle various inputs
            ##quit type    
            if event.type == pygame.QUIT: 
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clickLoc = pygame.mouse.get_pos()
                for e in screen.elements[::-1]:
                    if e.wasClicked(clickLoc):
                        e.onClick(screen)
                        return

