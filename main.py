#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On importe les fichiers dont on a besoin
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import imports
import loader
import Objects
import constantes
import spriteManager
import menu
import GIF
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On initialise pygame
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
imports.pygame.init()

#On initialise nos variables objets globalement, pour éviter les erreurs de scope ...
boss = None
enemy = None

missile = None
enemyMissile = None

lifeBarBoss = None

explo = None
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On créé notre vaisseau et on l'ajoute à la liste de vaisseau et à la liste de sprite
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ship = Objects.newShip()
spriteManager.groupShip.add(ship)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On créé la barre de vie du vaisseau
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
lifeBarShip = Objects.newLifeBar(ship)
spriteManager.groupLifeBar.add(lifeBarShip)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On créé les premiers asteroide et on les ajoute à la liste d'ennemi et a la liste de sprite
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
for i in range(imports.random.randint(3, 9)):
    enemy = Objects.newEnemy()
    spriteManager.groupEnemy.add(enemy)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On créé notre background, une simple image (le faire defiler ? ...) et on l'ajoute a la liste de background
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
background = Objects.newBackground()
spriteManager.groupBackground.add(background)


#########################################################################################################################################################################
#########################################################################################################################################################################

menu.splashScreen()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Boucle principale
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while constantes.loop:
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On gere les evenements du clavier : appuyer sur une touche
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for event in imports.pygame.event.get():
        if event.type == imports.QUIT:
            constantes.loop = False
        if (imports.pygame.key.get_pressed()[imports.pygame.K_p] == True):
            menu.pause()
        if (imports.pygame.key.get_pressed()[imports.pygame.K_SPACE] == True):
            missile = Objects.newShipMissile(ship)
            spriteManager.groupShipMissile.add(missile)
            imports.pygame.mixer.music.load('SFX/missile.wav')
            imports.pygame.mixer.music.play(0)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On gere les collisions entre notre missile et l'ennemi
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for shipMissile in spriteManager.groupShipMissile:
        #Si un missile dépasse l'ecran, on detruit l'objet
        if shipMissile.rect.y < 0:
            spriteManager.groupShipMissile.remove(shipMissile)
        for enemy in spriteManager.groupEnemy:
            #Si un ennemi et un missile entrent en collision, on détruit les deux objets
            if imports.pygame.sprite.collide_rect(enemy, shipMissile):
                explo = GIF.explosionAnimation(enemy, shipMissile)
                spriteManager.explosionGroup.add(explo)
                imports.pygame.mixer.music.load('SFX/explosion.wav')
                imports.pygame.mixer.music.play(0)

                spriteManager.groupShipMissile.remove(shipMissile)

                enemy.life -=1
                if enemy.life <= 0:
                    #Quand on touche un ennemi on incremente le score de 1
                    constantes.score += 100
                    spriteManager.groupEnemy.remove(enemy)
                #Si pas assez d'ennemis, on en créé d'autre pour plus de fun
                if len(spriteManager.groupEnemy) <= 3:
                    for i in range(imports.random.randint(3, 6)):
                        enemy = Objects.newEnemy()
                        spriteManager.groupEnemy.add(enemy)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On gere les collisions entre notre missile et le boss
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if len(spriteManager.groupBoss) != 0:
        for shipMissile in spriteManager.groupShipMissile:
            if shipMissile.rect.y < 0:
                spriteManager.groupShipMissile.remove(shipMissile)
            for boss in spriteManager.groupBoss:
                if imports.pygame.sprite.collide_rect(boss, shipMissile):
                    explo = GIF.explosionAnimation(boss, shipMissile)
                    spriteManager.explosionGroup.add(explo)

                    spriteManager.groupShipMissile.remove(shipMissile)
                    boss.life -=1
                    if boss.life <= 0:
                        constantes.score += 10000
                        spriteManager.groupeBossLifeBar.remove(lifeBarBoss)
                        spriteManager.groupBoss.remove(boss)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On gere les collisions entre un missile ennemi ou boss et notre vaisseau
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for enemyMissile in spriteManager.groupEnemyMissile:
        for ship in spriteManager.groupShip:
            if imports.pygame.sprite.collide_rect(enemyMissile, ship):
                explo = GIF.explosionAnimation(ship, enemyMissile)
                spriteManager.explosionGroup.add(explo)

                spriteManager.groupEnemyMissile.remove(enemyMissile)
                ship.life -= 1
                #Si le joueur n'a plus de vie le jeu se termine
                if ship.life <= 0:
                    menu.gameOver()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On gere les collisions entre un missile ennemi ou boss et notre missile
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for enemyMissile in spriteManager.groupEnemyMissile:
        for shipMissile in spriteManager.groupShipMissile:
            if imports.pygame.sprite.collide_rect(enemyMissile, shipMissile):
                explo = GIF.explosionAnimation(enemyMissile, shipMissile)
                spriteManager.explosionGroup.add(explo)

                spriteManager.groupShipMissile.remove(shipMissile)
                spriteManager.groupEnemyMissile.remove(enemyMissile)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On gere les collisions entre notre vaisseau et l'ennemi
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for ship in spriteManager.groupShip:
        for enemy in spriteManager.groupEnemy:
            #Si il y a une collision on supprime l'ennemi et on enleve un point de vie au joueur
            if imports.pygame.sprite.collide_rect(enemy, ship):
                spriteManager.groupEnemy.remove(enemy)
                ship.life -= 1
                #Si le joueur n'a plus de vie le jeu se termine
                if ship.life <= 0:
                    spriteManager.groupLifeBar.remove(lifeBarShip)
                    menu.gameOver()
            #Si pas assez d'ennemis, on en créé d'autre pour plus de fun
            if len(spriteManager.groupEnemy) <= 3:
                for i in range(imports.random.randint(3, 6)):
                    enemy = Objects.newEnemy()
                    spriteManager.groupEnemy.add(enemy)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Les ennemis tirent des missiles aleatoirement avec une probabilité de 1/20
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    randMissile = imports.random.randint(1, 20)
    if randMissile == 1:
        #On choisit un ennemi aleatoirement qui va tirer un missile
        enemy = imports.random.choice(spriteManager.groupEnemy.sprites())
        if enemy.rect.y < constantes.screenWidth/2 and enemy.rect.y > 10:
            missileEnemy = Objects.newEnemyMissile(enemy)
            spriteManager.groupEnemyMissile.add(missileEnemy)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Le boss tire aléatoirement des missiles avec une probabilité de 1/40 a chaque frame
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    randBossMissile = imports.random.randint(1, 100)
    if (randBossMissile == 1) and (len(spriteManager.groupBoss) != 0):
        #On choisit un boss aleatoirement qui va tirer un missile (
        if boss.rect.y < constantes.screenWidth/2 and boss.rect.y > 10:
            bossMissile = Objects.newBossMissile(boss)
            spriteManager.groupEnemyMissile.add(bossMissile)


    randPowerUp = imports.random.randint(1, 250)
    if (randPowerUp == 1):
        powerUp = Objects.powerUp()
        spriteManager.groupPowerUp.add(powerUp)

    if len(spriteManager.groupPowerUp) != 0:
        for ship in spriteManager.groupShip:
            for powerUp in spriteManager.groupPowerUp:
                if powerUp.rect.bottom > constantes.screenHeight:
                    spriteManager.groupPowerUp.remove(powerUp)
                if imports.pygame.sprite.collide_rect(ship, powerUp):
                    spriteManager.groupPowerUp.remove(powerUp)
                    ship.life += 1
                    if ship.life > 10:
                        ship.life = 10



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On créer un boss apres avoir atteint un score minimum et on utilise un booleen pour eviter d'en creer plusieurs lorsque que le score ne change pas entre deux frames
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if (constantes.score == 100) and (constantes.spawnBoss == True):
            boss = Objects.newBoss()
            spriteManager.groupBoss.add(boss)
            lifeBarBoss = Objects.newBossLifeBar(boss)
            spriteManager.groupeBossLifeBar.add(lifeBarBoss)
            constantes.spawnBoss = False
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On supprime l'explosion si l'index se trouve sur la derniere frame de l'animation
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if len(spriteManager.explosionGroup) != 0:
        for explosion in spriteManager.explosionGroup:
            if explosion.index == 17:
                spriteManager.explosionGroup.remove(explosion)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Quelques statistiques, affichage console
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if constantes.debug == True:
        constantes.counterFrame += 1
        if constantes.counterFrame == constantes.FPS:
            print "nombre d'ennemis = ", len(spriteManager.groupEnemy)
            print "nombre de missiles = ", len(spriteManager.groupShipMissile)
            print "nombre d'objets = ", (len(spriteManager.groupShip)+len(spriteManager.groupEnemy)+len(spriteManager.groupBoss)+len(spriteManager.groupEnemyMissile)+len(spriteManager.groupShipMissile))
            print "SCORE = ", constantes.score
            print "life = ", ship.life
            print "\n--------------------\n"
            constantes.counterFrame = 0
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On appelle les méthodes update() de chaque objet et de la barre de vie (parametre en plus -> update(ship))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    spriteManager.groupShip.update()
    spriteManager.groupEnemy.update()
    spriteManager.groupBoss.update()

    spriteManager.groupEnemyMissile.update()
    spriteManager.groupShipMissile.update()

    spriteManager.groupLifeBar.update(ship)
    spriteManager.groupeBossLifeBar.update(boss)

    spriteManager.explosionGroup.update()

    spriteManager.groupPowerUp.update()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On dessine nos objets avec les attributs image et position définit par les constructeurs et mis a jour par les methodes update()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    spriteManager.groupBackground.draw(loader.screen)

    spriteManager.groupShip.draw(loader.screen)
    spriteManager.groupEnemy.draw(loader.screen)
    spriteManager.groupBoss.draw(loader.screen)
    spriteManager.groupEnemyMissile.draw(loader.screen)
    spriteManager.groupShipMissile.draw(loader.screen)

    spriteManager.groupLifeBar.draw(loader.screen)
    spriteManager.groupeBossLifeBar.draw(loader.screen)

    spriteManager.explosionGroup.draw(loader.screen)

    spriteManager.groupPowerUp.draw(loader.screen)

    menu.displayStats()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #On rafraichit l'ecran et on limite ce rafraichissement à constantes.FPS = 60
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    imports.pygame.display.flip()
    constantes.clock.tick(constantes.FPS)