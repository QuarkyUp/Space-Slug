import imports

class explosionAnimation(imports.pygame.sprite.Sprite):
    def __init__(self, sprite, missile):
        imports.pygame.sprite.Sprite.__init__(self)
        self.explosionImageList = []

        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion1.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion2.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion3.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion4.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion5.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion6.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion7.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion8.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion9.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion10.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion11.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion12.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion13.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion14.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion15.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion16.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion17.png").convert_alpha())
        self.explosionImageList.append(imports.pygame.image.load("Sprites/explosion/explosion18.png").convert_alpha())

        self.index = 0

        self.image = self.explosionImageList[self.index]

        if (missile == "enemyMissile") and (sprite == "ship"):
            self.rect = imports.pygame.Rect(missile.rect.centerx, sprite.rect.top, 30, 30)
        else:
            self.rect = imports.pygame.Rect(missile.rect.centerx, sprite.rect.bottom, 30, 30)

    def update(self):
        self.index += 1
        if self.index >= len(self.explosionImageList):
            self.index = 0
        self.image = self.explosionImageList[self.index]