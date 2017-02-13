import imports
import constantes
import loader

def pause():
    font = imports.pygame.font.SysFont("comicsansms", 72)
    font2 = imports.pygame.font.SysFont("comicsansms", 36)
    text = font.render("PAUSE", True, (255, 255, 255))
    text2 = font2.render("appuyer sur P pour reprendre", True, (255, 255, 255))

    while True:
        for event in imports.pygame.event.get():
            if event.type == imports.QUIT:
                imports.pygame.quit()
            if (imports.pygame.key.get_pressed()[imports.pygame.K_p] == True):
                return False
        loader.screen.blit(text, (constantes.screenWidth / 2 - text.get_rect().width / 2, constantes.screenHeight / 2 - text.get_rect().height))
        loader.screen.blit(text2, (constantes.screenWidth / 2 - text2.get_rect().width / 2, constantes.screenHeight / 2 + text.get_rect().height))
        imports.pygame.display.flip()
        constantes.clock.tick(constantes.FPS)


def gameOver():
    font = imports.pygame.font.SysFont("comicsansms", 72)
    text = font.render("Game Over", True, (255, 255, 255))

    while True:
        for event in imports.pygame.event.get():
            if event.type == imports.QUIT:
                imports.pygame.quit()
            if event.type == imports.KEYDOWN:
                if event.key == imports.K_ESCAPE:
                    imports.pygame.quit()
        loader.screen.fill((0, 0, 0))
        loader.screen.blit(text, (200, 200))
        imports.pygame.display.flip()
        constantes.clock.tick(constantes.FPS)

def displayStats():
    score = "Score : %d" %constantes.score
    font = imports.pygame.font.SysFont("comicsansms", 25)
    text = font.render(score, 1, (255, 255, 255))
    loader.screen.blit(text, (10, constantes.screenHeight - text.get_rect().height))

def splashScreen():
    splashLoop = True
    clockSplash = imports.pygame.time.Clock()
    counterSplash = 0

    while splashLoop:
        counterSplash += 1

        for event in imports.pygame.event.get():
                if event.type == imports.QUIT:
                    imports.pygame.quit()

        if counterSplash == 60*5:
            splashLoop = False

        loader.screen.blit(loader.imageSplash, (0, 0))
        imports.pygame.display.flip()
        clockSplash.tick(constantes.FPS)

    imports.pygame.mixer.music.load('SFX/start.wav')
    imports.pygame.mixer.music.play(0)
