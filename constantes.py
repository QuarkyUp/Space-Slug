#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imports

FPS = 60
screenWidth = 800
screenHeight = 600

lifeBoss = 50
lifeShip = 10
lifeEnemy = 3

speedShip = 10
speedEnemy = 1
speedBoss = 1
speedPowerUp = 1

speedMissile = 5
speedBossMissile = 2


score = 0
counterFrame = 0

loop = True
debug = True
spawnBoss = True

clock = imports.pygame.time.Clock()

