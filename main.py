
import pygame
import os

#import gm, mains et up eveeyrhting
from modules.gameObjects.ball import Ball
from modules.gameObjects.drawable import Drawable
from modules.gameObjects.leftGoal import LeftGoal
from modules.gameObjects.player1 import Player1
from modules.gameObjects.player2 import Player2
from modules.gameObjects.powerUp import  PowerUp1, PowerUp2, PowerUp3, PowerUp4, PowerUp5
from modules.gameObjects.rightGoal import RightGoal
from modules.gameObjects.vector2D import Vector2
from modules.managers.soundManager import SoundManager
from modules.managers.gameManager import GameManager
from modules.managers.screenManager import ScreenManager
from modules.UI.screenInfo import SCREEN_SIZE, UPSCALED


import random



def main():

    # initialize the pygame module
    pygame.init()
    # load and set the logo

    pygame.display.set_caption("1 V 1 Soccer")

    screen = pygame.display.set_mode(list(SCREEN_SIZE))

    drawSurface = pygame.Surface(list(SCREEN_SIZE))

    screenManager = ScreenManager()

    # Make a game clock for nice, smooth animations
    gameClock = pygame.time.Clock()

    # define a variable to control the main loop
    RUNNING = True


    while RUNNING:

        # Draw everything        
      
        screenManager.draw(screen)

        #pygame.transform.scale(drawSurface, list(SCREEN_SIZE), screen)

        # Flip the display to the monitor
        pygame.display.flip()

        
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT or ESCAPE is pressed
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # change the value to False, to exit the main loop
                RUNNING = False
                break

            result = screenManager.handleEvent(event)

            if result == "exit":
                RUNNING = False
                break


        # Update everything

        # Let our game clock tick at 60 fps
        gameClock.tick(60)

        # Get some time in seconds
        seconds = min(0.1, gameClock.get_time() / 1000)

        screenManager.update(seconds)
        

        
        
 #Ask about collision, friction       

if __name__ == "__main__":
    main()

