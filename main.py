
from matplotlib.pyplot import draw
import pygame
import os

from modules.ball import Ball
from modules.drawable import Drawable
from modules.leftGoal import LeftGoal
from modules.player1 import Player1
from modules.player2 import Player2
from modules.powerUp import  PowerUp1, PowerUp2, PowerUp3, PowerUp4, PowerUp5
from modules.rightGoal import RightGoal
from modules.vector2D import Vector2
from modules.soundManager import SoundManager
# from modules.timer import TimerFunction
import random


SCREEN_SIZE = Vector2(1100, 650)
SCALE = 1
UPSCALED = SCREEN_SIZE * SCALE


def main():

    # initialize the pygame module
    pygame.init()
    # load and set the logo

    pygame.display.set_caption("1 V 1 Soccer")

    screen = pygame.display.set_mode(list(UPSCALED))

    drawSurface = pygame.Surface(list(SCREEN_SIZE))

    leftGoal = LeftGoal(Vector2(0, 452))
    rightGoal = RightGoal(Vector2(1012, 452))
    ball = Ball(Vector2(510, 614))
    player1 = Player1(Vector2(90, 570))
    player2 = Player2(Vector2(900,570))
    ground = pygame.Rect(-50, 650, 1200, 50)
    leftCrossBar = pygame.Rect(-10, 450, 93, 16)
    rightCrossBar = pygame.Rect(1018, 450, 93, 16)
    rightGoalRect = pygame.Rect(1055, 468, 88, 220)
    leftGoalRect = pygame.Rect(-48, 468, 88, 220)

    powerUps = []
    powerUpTimer = 5

    crowdNoise =  SoundManager.getInstance().playSound("long.wav")
    goalNoise =   SoundManager.getInstance().playSound("goalazo.wav")
    SoundManager.getInstance().pauseChannel(goalNoise)






    def collisionCrossBar(ball, rightCrossBar, leftCrossbar):
        if ball.getCollisionRect().colliderect(rightCrossBar):
            # newPosition = ball.getPosition() + ball._velocity * seconds
            ball._velocity = Vector2(
                random.randint(-200, 0), random.randint(-200, 0))
            # ball.setPosition(newPosition)
        if ball.getCollisionRect().colliderect(leftCrossBar):
            # newPosition = ball.getPosition() + ball._velocity * seconds
            # ball.setPosition(newPosition)
            ball._velocity = Vector2(
                random.randint(0, 200), random.randint(-200, 0))

    
    
    goalTimer = 0.8



    background = Drawable("finalPitch.png", Vector2(0, 0))

    goal1 = 0
    goal2 = 0
    
    font = pygame.font.Font('freesansbold.ttf', 50)
    scores = font.render(str(goal1) + "-" + str(goal2),
                False, (255, 255, 255))
    text = font.render("Score 0-0",
                       False, (0, 0, 0))
    gameOver = font.render("Game Over",
    False, (255,255,255))
    
    p1Win = font.render("Player 1 wins!",
    False, (255,255,255))
    p2Win = font.render("Player 2 wins!",
    False, (255,255,255))
    # Make a game clock for nice, smooth animations
    gameClock = pygame.time.Clock()

    # define a variable to control the main loop
    RUNNING = True
    
    # main loop
    while RUNNING:

        # Draw everything
        
        background.draw(drawSurface)
        leftGoal.draw(drawSurface)
        rightGoal.draw(drawSurface)
        ball.draw(drawSurface)
        player1.draw(drawSurface)
        player2.draw(drawSurface)
        for power in powerUps:
            power.draw(drawSurface)
        
        #power1.draw(drawSurface)
        #power2.draw(drawSurface)
        #power3.draw(drawSurface)



        scoreToWin = 1
        
        if goal1 !=scoreToWin and goal2 !=scoreToWin:
            drawSurface.blit(text, (460, 30))
        
        if goal1 ==scoreToWin or goal2 ==scoreToWin:
            drawSurface.blit(gameOver,(400,30))
        if goal1 == scoreToWin:
            drawSurface.blit(p1Win,(370,80))
        elif goal2 == scoreToWin:
            drawSurface.blit(p2Win,(370,80))

        

        player1Rect = pygame.Rect.inflate(
           player1.getCollisionRect(), -35, -10)

        player2Rect = pygame.Rect.inflate(
            player2.getCollisionRect(), -25, 0)
        
        
        if player1._row == 2:
            player1Rect = pygame.Rect.inflate(
            player1.getCollisionRect(), -20, -17)
        if player2._row == 2:
            player2Rect = pygame.Rect.inflate(
            player2.getCollisionRect(), -9, -30)
        
        
        #pygame.draw.rect(drawSurface, (255, 255, 0),player1Rect, 2)
        #pygame.draw.rect(drawSurface, (255, 255, 0), player2Rect,2)
        #pygame.draw.rect(drawSurface, (255, 255, 255), ground, 2)
        #pygame.draw.rect(drawSurface, (255, 0, 255), rightCrossBar, 2)
        #pygame.draw.rect(drawSurface, (255, 0, 255), power1.getCollisionRect(), 2)
        #pygame.draw.rect(drawSurface, (255, 0, 255), leftCrossBar, 2)
        #pygame.draw.rect(drawSurface, (255, 0, 255), rightGoalRect, 2)
        #pygame.draw.rect(drawSurface, (255, 0, 255), leftGoalRect, 2)
        #pygame.draw.rect(drawSurface, (255, 0, 255),
        #                ball.getCollisionRect(), 2)

      
        pygame.transform.scale(drawSurface, list(UPSCALED), screen)

        # Flip the display to the monitor
        pygame.display.flip()

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT or ESCAPE is pressed
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # change the value to False, to exit the main loop
                RUNNING = False

            player1.handleEvent(event)
            player2.handleEvent(event)
            ball.handleEvent(event)
        
        # Let our game clock tick at 60 fps
        gameClock.tick(60)
        # Get some time in seconds
        seconds = gameClock.get_time() / 1000
        
        powerUpTimer -=seconds
        if powerUpTimer <=0:
            power1 = PowerUp1(Vector2(random.randint(200,700),random.randint(470,550)))
            power2 = PowerUp2(Vector2(random.randint(200,700),random.randint(470,550)))
            power3 = PowerUp3(Vector2(random.randint(200,700),random.randint(470,550)))
            power4 = PowerUp4(Vector2(random.randint(200,700),random.randint(470,550)))
            power5 = PowerUp5(Vector2(random.randint(200,700),random.randint(470,550)))

            powers = [power1,power2,power3,power4,power5]
            #powerUps.append(power1)
            powerUps.append(powers[random.randint(2,5)])
            powerUpTimer = 20
        
   
        
        ball.collider(player1,player1Rect)
        ball.collider(player2,player2Rect)
        #ball.collider(leftCrossBar,leftCrossBar)
        
        #if seconds < 0.05:

        player1.update(seconds, SCREEN_SIZE)
        player2.update(seconds,SCREEN_SIZE)
        ball.update(SCREEN_SIZE, seconds,ground)
        for power in powerUps:
            power.power(seconds,player1,player2,player1Rect,player2Rect,ball)
            power.update(seconds,player1Rect,player2Rect)
            if power.isDead():
                powerUps.remove(power)

            
        if ball.getCollisionRect().colliderect(rightGoalRect):
            goal1 += 1
        
        if ball.getCollisionRect().colliderect(leftGoalRect):
            goal2 +=1
        
        if  ball.getCollisionRect().colliderect(rightGoalRect) or ball.getCollisionRect().colliderect(leftGoalRect):
                SoundManager.getInstance().pauseChannel(crowdNoise)
                SoundManager.getInstance().unpauseChannel(goalNoise)

                #Detect timer update nothing in the world if 0.

                player1.setPosition(Vector2(90,570))
                player2.setPosition(Vector2(900,570))
                ball.setPosition(Vector2(510, 616))
                ball._velocity = (Vector2(0,0))
                player1.transitionState("standing")
                player2.transitionState("standing")


                
                SoundManager.getInstance().pauseChannel(goalNoise)
                SoundManager.getInstance().unpauseChannel(goalNoise)
        
        


    
        collisionCrossBar(ball,rightCrossBar,leftCrossBar)
        
        #scores = font.render(str(goal1) + "-" + str(goal2),
        #        False, (255, 255, 255))
    
        text = font.render("Score " + str(goal1) + "-" + str(goal2),
                False, (255, 255, 255))
        
        
        
        # Detect collision
        clipRect = pygame.Rect.inflate(
            player1.getCollisionRect(), -35, -10).clip(ground)
        clipRect2 = pygame.Rect.inflate(player2.getCollisionRect() ,-25,0).clip(ground)
        clipRect3 = ball.getCollisionRect().clip(ground)

        if clipRect.width > 0:
            player1.collideGround(clipRect.height)
        if clipRect2.width > 0:
            player2.collideGround(clipRect2.height)
        if clipRect3.width > 0:
            ball.collideGround(clipRect3.height)
        
        
 #Ask about collision, friction       

if __name__ == "__main__":
    main()
