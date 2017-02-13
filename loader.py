#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imports
import constantes

enemyImageList = []
powerUpImageList = []

#On créé la fenetre
screen = imports.pygame.display.set_mode((constantes.screenWidth, constantes.screenHeight))

#On charge les sprites
imageBackground = imports.pygame.image.load("Sprites/background.png").convert_alpha()

imageSplash = imports.pygame.image.load("Sprites/splash.png").convert_alpha()

imageShipRest = imports.pygame.image.load("Sprites/joueurNormal.png").convert_alpha()
imageShipRest = imports.pygame.transform.scale(imageShipRest, (51, 57))

imageShipRight = imports.pygame.image.load("Sprites/joueurDroite.png").convert_alpha()
imageShipRight = imports.pygame.transform.scale(imageShipRight, (51, 57))

imageShipLeft = imports.pygame.image.load("Sprites/joueurGauche.png").convert_alpha()
imageShipLeft = imports.pygame.transform.scale(imageShipLeft, (51, 57))

imageEnemy = imports.pygame.image.load("Sprites/ufo.png").convert_alpha()
imageEnemy = imports.pygame.transform.scale(imageEnemy, (28, 24))
imageEnemy2 = imports.pygame.image.load("Sprites/ufo2.png").convert_alpha()
imageEnemy2 = imports.pygame.transform.scale(imageEnemy2, (27, 16))
imageEnemy3 = imports.pygame.image.load("Sprites/ufo3.png").convert_alpha()
imageEnemy3 = imports.pygame.transform.scale(imageEnemy3, (24, 20))
imageEnemy4 = imports.pygame.image.load("Sprites/ufo4.png").convert_alpha()
imageEnemy4 = imports.pygame.transform.scale(imageEnemy4, (22, 19))

imageBoss = imports.pygame.image.load("Sprites/boss.png").convert_alpha()
imageBoss = imports.pygame.transform.scale(imageBoss, (136, 72))

imageShipMissile = imports.pygame.image.load("Sprites/missileJoueur.png").convert_alpha()
imageShipMissile = imports.pygame.transform.scale(imageShipMissile, (10, 20))

imageEnemyMissile = imports.pygame.image.load("Sprites/missileEnnemi.png").convert_alpha()
imageEnemyMissile = imports.pygame.transform.scale(imageEnemyMissile, (10, 20))

imageBossMissile = imports.pygame.image.load("Sprites/missileBoss.png").convert_alpha()
imageBossMissile = imports.pygame.transform.scale(imageBossMissile, (20, 40))

imagePowerUp = imports.pygame.image.load("Sprites/powerUp.png").convert_alpha()
imagePowerUp = imports.pygame.transform.scale(imagePowerUp, (20, 20))
imagePowerUp2 = imports.pygame.image.load("Sprites/powerUp2.png").convert_alpha()
imagePowerUp2 = imports.pygame.transform.scale(imagePowerUp2, (20, 30))


powerUpImageList.append(imagePowerUp)
powerUpImageList.append(imagePowerUp2)


enemyImageList.append(imageEnemy)
enemyImageList.append(imageEnemy2)
enemyImageList.append(imageEnemy3)
enemyImageList.append(imageEnemy4)

#Rectangles
rectShip = imageShipRest.get_rect()
rectEnemy = imageEnemy.get_rect()
rectShipMissile = imageShipMissile.get_rect()
rectEnemyMissile = imageEnemyMissile.get_rect()
rectBossMissile = imageBoss.get_rect()
rectBackground = imageBackground.get_rect()

#On créé le fond d'écran
screen.blit(imageBackground, (0, 0))