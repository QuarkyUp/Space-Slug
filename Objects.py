#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imports
import constantes
import loader


def randSpeed(a, b):
    speed = imports.random.randint(a, b)
    while speed == 0:
        speed = imports.random.randint(a, b)
    return speed
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Classe du background
    #Class mère : Sprite
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class newBackground(imports.pygame.sprite.Sprite):
#Constructeur du backround, on hérite de la classe Sprite pour faciliter l'affichage grace aux methodes update() et draw() de la classe mere
    def __init__(self):
        #Constructeur de la classe Sprite
        imports.pygame.sprite.Sprite.__init__(self)
        #On définit l'image et le rectangle (qu'on utilisera pour la parallaxe, peut etre...)
        self.image = loader.imageBackground
        self.rect = loader.rectBackground
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Classe de la barre de vie
    #Class mère : Sprite
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class newLifeBar(imports.pygame.sprite.Sprite):
#Constructeur de la barre de vie, on hérite de la classe Sprite pour faciliter l'affichage grace aux methodes update() et draw() de la classe mere
    def __init__(self, sprite):
        #Constructeur de la classe Sprite
        imports.pygame.sprite.Sprite.__init__(self)
        #On définit l'image (une surface verte) et le rectangle
        #La largeur de la barre de vie est proportionnelle au nombre de point de vie
        self.image = imports.pygame.Surface([5 * sprite.life, 5])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        #On créé la barre de vie centré sur le vaisseau
        self.rect.x = sprite.rect.x
        self.rect.y = sprite.rect.bottom

    def update(self, sprite):
        #On actualise la taille de la barre de vie et on la recentre sur le vaisseau
        self.image = imports.pygame.Surface([5 * sprite.life, 5])
        self.image.fill((0, 255, 0))
        self.rect.x = sprite.rect.x
        self.rect.y = sprite.rect.bottom

class newBossLifeBar(imports.pygame.sprite.Sprite):
#Constructeur de la barre de vie, on hérite de la classe Sprite pour faciliter l'affichage grace aux methodes update() et draw() de la classe mere
    def __init__(self, sprite):
        #Constructeur de la classe Sprite
        imports.pygame.sprite.Sprite.__init__(self)
        #On définit l'image (une surface verte) et le rectangle
        #La largeur de la barre de vie est proportionnelle au nombre de point de vie
        self.image = imports.pygame.Surface([10, 12 * sprite.life])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        #On créé la barre de vie centré sur le vaisseau
        self.rect.x = constantes.screenWidth - self.rect.width
        self.rect.y = constantes.screenHeight - 12 * sprite.life

    def update(self, sprite):
        #On actualise la taille de la barre de vie et on la recentre sur le vaisseau
        self.image = imports.pygame.Surface([10, 12 * sprite.life])
        self.image.fill((255 , 0, 0))
        self.rect.x = constantes.screenWidth - self.rect.width
        self.rect.y = constantes.screenHeight - 12 * sprite.life
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Classe du vaisseau du joueur
    #Class mère : Sprite
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class newShip(imports.pygame.sprite.Sprite):
#Constructeur du vaisseau, on hérite de la classe Sprite pour faciliter l'affichage grace aux methodes update() et draw() de la classe mere
    def __init__(self):
        #Constructeur de la classe Sprite
        imports.pygame.sprite.Sprite.__init__(self)
        self.image = loader.imageShipRest
        self.rect = self.image.get_rect()
        self.rect.x = constantes.screenWidth/2 - self.rect.width/2
        self.rect.y = constantes.screenHeight - self.rect.height - 50
        self.life = constantes.lifeShip

    def moveUp(self):
        self.rect.y -= constantes.speedShip
    def moveDown(self):
        self.rect.y += constantes.speedShip
    def moveLeft(self):
        self.rect.x -= constantes.speedShip
    def moveRight(self):
        self.rect.x += constantes.speedShip

    def movementShip(self):
        if (imports.pygame.key.get_pressed()[imports.pygame.K_LEFT] == True):
            self.image = loader.imageShipLeft
            self.moveLeft()
        elif (imports.pygame.key.get_pressed()[imports.pygame.K_RIGHT] == True):
            self.image = loader.imageShipRight
            self.moveRight()
        elif (imports.pygame.key.get_pressed()[imports.pygame.K_UP] == True):
            self.moveUp()
        elif (imports.pygame.key.get_pressed()[imports.pygame.K_DOWN] == True):
            self.moveDown()

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > constantes.screenWidth - self.rect.width:
            self.rect.x = constantes.screenWidth - self.rect.width
        elif self.rect.y > constantes.screenHeight - self.rect.height - 50:
            self.rect.y = constantes.screenHeight - self.rect.height - 50
    def update(self):
        self.movementShip()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Classe de l'asteroide
    #Class mère : Sprite
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class newEnemy(imports.pygame.sprite.Sprite):
#Constructeur de l'asteroide, on hérite de la classe Sprite pour faciliter l'affichage grace aux methodes update() et draw() de la classe mere
    def __init__(self):
        #Constructeur de la classe Sprite
        imports.pygame.sprite.Sprite.__init__(self)
        #On définit l'image et le rectangle
        self.image = imports.random.choice(loader.enemyImageList)
        self.rect = self.image.get_rect()
        #Coordonnées aleatoire : Y au dessus de l'ecran pour laisser le joueur se preparer, et en X qui occupe toute la largeur de l'ecran
        self.rect.y = imports.random.randrange(-200, -50)
        self.rect.x = imports.random.randint(constantes.screenWidth/2 - 350, constantes.screenWidth/2 + 350)
        #Vitesse aleatoire
        self.speedY = randSpeed(constantes.speedEnemy, constantes.speedEnemy + 3)
        self.speedX = imports.random.randint(-3, 3)
        self.life = constantes.lifeEnemy
#Si l'asteroide depasse de l'ecran verticalement on le ramene en haut a une position horizontale aleatoire
    def resetPositionEnemyY(self):
        self.speedY = randSpeed(constantes.speedEnemy, constantes.speedEnemy + 3)
        self.rect.y = imports.random.randrange(-300, -20)
        self.rect.x = imports.random.randrange(constantes.screenWidth/2 - 350, constantes.screenWidth/2 + 350)
#On appelle cette methode dans la boucle principale, on déplace verticalement et horizontalement l'asteroide avec une vitesse aleatoire
#Si l'asteroide depasse de l'ecran, on appelle ResetPosition()
    def update(self):
        self.rect.y += self.speedY
        self.rect.x += self.speedX
        if self.rect.y > constantes.screenHeight - 35:
            self.resetPositionEnemyY()
        #On fait fait passer l'asteroides de gauche a droite et inversement quand il depasse
        if self.rect.x > constantes.screenWidth + 10:
            self.rect.x = -10
        if self.rect.x < -10:
            self.rect.x = constantes.screenWidth + 10
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Classe du missile
    #Class mère : Sprite
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class newShipMissile(imports.pygame.sprite.Sprite):
#Constructeur du missile, on hérite de la classe Sprite pour faciliter l'affichage grace aux methodes update() et draw() de la classe mere
    def __init__(self, ship):
        #Constructeur de la classe Sprite
        imports.pygame.sprite.Sprite.__init__(self)
        #On définit l'image, le rectangle et les coordonnées
        self.image = loader.imageShipMissile
        self.rect = self.image.get_rect()
        #On créé le missile centré sur le vaisseau du joueur
        self.rect.x = ship.rect.centerx - 5
        self.rect.y = ship.rect.top + 5
#On appelle cette methode dans la boucle principale, on déplace verticalement le missile
    def update(self):
        self.rect.y -= constantes.speedMissile
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Classe du missile
    #Class mère : Sprite
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class newEnemyMissile(imports.pygame.sprite.Sprite):
#Constructeur du missile, on hérite de la classe Sprite pour faciliter l'affichage grace aux methodes update() et draw() de la classe mere
    def __init__(self, enemy):
        #Constructeur de la classe Sprite
        imports.pygame.sprite.Sprite.__init__(self)
        #On définit l'image, le rectangle et les coordonnées
        self.image = loader.imageEnemyMissile
        self.rect = self.image.get_rect()
        #On créé le missile centré sur le vaisseau du joueur
        self.rect.x = enemy.rect.centerx
        self.rect.y = enemy.rect.y + 20
#On appelle cette methode dans la boucle principale, on déplace verticalement le missile
    def update(self):
        self.rect.y += constantes.speedMissile
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Classe du missile
    #Class mère : Sprite
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class newBossMissile(imports.pygame.sprite.Sprite):
#Constructeur du missile, on hérite de la classe Sprite pour faciliter l'affichage grace aux methodes update() et draw() de la classe mere
    def __init__(self, boss):
        #Constructeur de la classe Sprite
        imports.pygame.sprite.Sprite.__init__(self)
        #On définit l'image, le rectangle et les coordonnées
        self.image = loader.imageBossMissile
        ''' loader.rectBossMissile ne marche pas ... '''
        self.rect = self.image.get_rect()
        #On créé le missile centré sur le vaisseau du joueur
        self.rect.x = boss.rect.centerx
        self.rect.y = boss.rect.bottom + 20
#On appelle cette methode dans la boucle principale, on déplace verticalement le missile
    def update(self):
        self.rect.y += constantes.speedBossMissile


class newBoss(imports.pygame.sprite.Sprite):
#Constructeur de l'asteroide, on hérite de la classe Sprite pour faciliter l'affichage grace aux methodes update() et draw() de la classe mere
    def __init__(self):
        #Constructeur de la classe Sprite
        imports.pygame.sprite.Sprite.__init__(self)
        #On définit l'image et le rectangle
        self.image = loader.imageBoss
        self.rect = self.image.get_rect()
        #Coordonnées aleatoire : Y au dessus de l'ecran pour laisser le joueur se preparer, et en X qui occupe toute la largeur de l'ecran
        self.rect.y = 50
        self.rect.x = imports.random.randint(constantes.screenWidth/2 - 250, constantes.screenWidth/2 + 50)
        #Vitesse aleatoire
        self.speedY = randSpeed(constantes.speedBoss - 3, constantes.speedBoss + 1)
        self.speedX = randSpeed(constantes.speedBoss - 3, constantes.speedBoss + 1)
        self.life = constantes.lifeBoss

    def resetPositionBossY(self):
        self.speedY = -1 * randSpeed(constantes.speedBoss - 3, constantes.speedBoss + 1)

    def resetPositionBossX(self):
        self.speedX = -1 * randSpeed(constantes.speedBoss - 3, constantes.speedBoss + 1)

    def update(self):
        self.rect.y += self.speedY
        self.rect.x += self.speedX
        if (self.rect.top < 0):
            self.rect.top = 1
            self.resetPositionBossY()
        elif (self.rect.bottom > constantes.screenHeight - 100):
            self.rect.bottom = constantes.screenHeight - 101
            self.resetPositionBossY()
        elif (self.rect.left < 0):
            self.rect.left = 1
            self.resetPositionBossX()
        elif (self.rect.right > constantes.screenWidth ):
            self.rect.right = constantes.screenWidth - 1
            self.resetPositionBossX()

class powerUp(imports.pygame.sprite.Sprite):
#Constructeur du missile, on hérite de la classe Sprite pour faciliter l'affichage grace aux methodes update() et draw() de la classe mere
    def __init__(self):
        #Constructeur de la classe Sprite
        imports.pygame.sprite.Sprite.__init__(self)
        #On définit l'image, le rectangle et les coordonnées
        self.image = imports.random.choice(loader.powerUpImageList)
        self.rect = self.image.get_rect()
        #On créé le missile centré sur le vaisseau du joueur
        self.rect.x = imports.random.randint(constantes.screenWidth/2 - 250, constantes.screenWidth/2 + 250)
        self.rect.y = -10
#On appelle cette methode dans la boucle principale, on déplace verticalement le missile
    def update(self):
        self.rect.y += constantes.speedPowerUp

