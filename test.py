import pygame

class Write(pygame.sprite.Sprite):
    def __init__(self,size,text,color,center):
        pygame.sprite.Sprite.__init__(self)
        self.textObject = pygame.font.Font(r"C:\SimpleCipher\Data\Fonts\TrajanPro\TrajanPro-Regular.ttf",size)
        self.writeText = self.textObject.render(text,True,color)
        self.textRect = self.writeText.get_rect()
        self.textRect.center = center