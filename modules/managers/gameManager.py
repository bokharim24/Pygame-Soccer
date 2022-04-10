import pygame
from .basicManager import BasicManager
from ..gameObjects.player1 import Player1
from ..gameObjects.player2 import Player2
from ..gameObjects.ball import Ball
from ..gameObjects.rightGoal import RightGoal
from ..gameObjects.leftGoal import LeftGoal
from ..gameObjects.drawable import Drawable
from ..gameObjects.powerUp import *
from ..gameObjects.vector2D import Vector2
from .frameManager import FrameManager
from .soundManager import SoundManager

import random

#Class which has everything going on in the game
class GameManager(BasicManager):
   
   _DEBUG = True
   
   def __init__(self, screenSize):
      #Initializing all the drawables and variables
      self._background = Drawable("finalPitch.png", Vector2(0, 0))
      self._leftGoal = LeftGoal(Vector2(0, 452))
      self._rightGoal = RightGoal(Vector2(1012, 452))
      self._rightGoal = RightGoal(Vector2(1012, 452))
      self._ball = Ball(Vector2(510, 614))
      self._player1 = Player1(Vector2(90, 570))
      self._player2 = Player2(Vector2(900,570))
      self._ground = pygame.Rect(-50, 650, 1200, 50)
      self._leftCrossBar = pygame.Rect(-10, 450, 93, 16)
      self._rightCrossBar = pygame.Rect(1018, 450, 93, 16)
      self._rightGoalRect = pygame.Rect(1055, 468, 88, 220)
      self._leftGoalRect = pygame.Rect(-48, 468, 88, 220)
      self._powerUps = []
      self._goalP1 = False
      self._goalP2 = False
      self._collideBar = False
      self._goal1 = 0
      self._goal2 = 0
      self._scoreToWin = 2
      self._crossTimer = 2.2
      self._font = pygame.font.Font('freesansbold.ttf', 50)
      self._scores = self._font.render(str(self._goal1) + "-" + str(self._goal2),
               False, (255, 255, 255))
      self._text = self._font.render("Score 0-0",
               False, (255, 255, 255))
      self._gameOver = self._font.render("Game Over",
               False, (0,0,0))
      self._p1Win = self._font.render("Player 2 wins!",
               False, (255,255,0))
      self._p2Win = self._font.render("Player 1 wins!",
               False, (0,255,0))
      
      self._powerUpTimer = 6
      
   
   #Checks for ball colliding with the goal post
   def collisionCrossBar(self,ball, rightCrossBar, leftCrossBar):
        if ball.getCollisionRect().colliderect(rightCrossBar):
            ball._velocity = Vector2(
                random.randint(-200, 0), random.randint(-200, 0))
            self._collideBar = True
        if ball.getCollisionRect().colliderect(leftCrossBar):
            ball._velocity = Vector2(
                random.randint(0, 200), random.randint(-200, 0))
            self._collideBar = True
   
   
   
   # Draw everything

   def draw(self, drawSurface):
      
      drawSurface.fill((255,0,255))
      
      self._background.draw(drawSurface)
      self._leftGoal.draw(drawSurface)
      self._rightGoal.draw(drawSurface)
      self._ball.draw(drawSurface)
      self._player1.draw(drawSurface)
      self._player2.draw(drawSurface)
      for power in self._powerUps:
         if power._isUsed != True:
            power.draw(drawSurface)
      
      # Displaying text till the game is going on
      if self._goal1 != self._scoreToWin and self._goal2 !=self._scoreToWin:
         drawSurface.blit(self._text, (460, 30))
      

      # Indicating when the game is over and displaying it
      if self._goal1 == self._scoreToWin or self._goal2 ==self._scoreToWin:
         drawSurface.blit(self._gameOver,(400,30))
      if self._goal1 == self._scoreToWin:
         drawSurface.blit(self._p1Win,(370,80))
      elif self._goal2 == self._scoreToWin:
         drawSurface.blit(self._p2Win,(370,80))

     
      
      #Testing out the collision boxes
      #pygame.draw.rect(drawSurface, (255, 255, 0),collision1Rect, 2)
      #pygame.draw.rect(drawSurface, (255, 255, 0),collision2Rect,2)  
      #pygame.draw.rect(drawSurface, (255, 255, 0), self._ball.getCollisionRect(),2)  

   
   #Handling certain events for the balls and players
   def handleEvent(self, event):      
      self._player1.handleEvent(event)
      self._player2.handleEvent(event)
      self._ball.handleEvent(event)
   
   
   def update(self, seconds, screenSize):
   
      #Changing players rectangle to match it to the sprite
      player1Rect = pygame.Rect.inflate(
         self._player1.getCollisionRect(), -35, -10)
      player2Rect = pygame.Rect.inflate(
         self._player2.getCollisionRect(), -25, 0)
      
      #Rects for condition when players collide with the ball at the same time
      collision1Rect =  pygame.Rect.inflate(
         self._player1.getCollisionRect(), -25, -10)
      collision2Rect = pygame.Rect.inflate(
         self._player2.getCollisionRect(), -15, 0)
      #Changing the players rectangle based on them sliding
      if self._player1._row == 2:
         player1Rect = pygame.Rect.inflate(
         self._player1.getCollisionRect(), -20, -17)
      if self._player2._row == 2:
         player2Rect = pygame.Rect.inflate(
         self._player2.getCollisionRect(), -9, -30)
      
      if self._player1._power1 == True:
         player1Rect =  pygame.Rect.inflate(
            self._player1.getCollisionRect(), -70, -10)
      
      if self._player2._power1 == True:
         player2Rect =  pygame.Rect.inflate(
            self._player2.getCollisionRect(), -70, -8)

      
      #Updating the movement of the players and the ball
      self._player1.update(seconds, screenSize)
      self._player2.update(seconds,screenSize)
      self._ball.update(screenSize, seconds,self._ground)
   
      #Appending powerups to the game
      for power in self._powerUps:
         power.update(seconds,player1Rect,player2Rect)
         power.power(seconds,self._player1,self._player2,player1Rect,player2Rect,self._ball)
         if power.isDead():
               self._powerUps.remove(power)
      
      self._powerUpTimer -=seconds
      
      # Creating PowerUps after the powerup timer is reset
      if self._powerUpTimer <=0:
         choice = random.randint(0,5)

         if choice == 0:  
            power1 = PowerUp1(Vector2(random.randint(200,700),random.randint(470,550)))
            self._powerUps.append(power1)
         elif choice ==1:
            power2 = PowerUp2(Vector2(random.randint(200,700),random.randint(470,550)))
            self._powerUps.append(power2)

         elif choice ==2:
            power3 = PowerUp3(Vector2(random.randint(200,700),random.randint(470,550)))
            self._powerUps.append(power3)

         elif choice ==3:         
            power4 = PowerUp4(Vector2(random.randint(200,700),random.randint(470,550)))
            self._powerUps.append(power4)

         elif choice ==4:
            power5 = PowerUp5(Vector2(random.randint(200,700),random.randint(470,550)))
            self._powerUps.append(power5)

         elif choice ==5:
            power6 = PowerUp6(Vector2(random.randint(200,700),random.randint(470,550)))
            self._powerUps.append(power6)

         self._powerUpTimer = 15
   
      # Updating the movement of the ball if it collides with a player
   
      #If both players run into the ball at the same time, the ball just goes up else normal bounce behavior
      if self._ball.getCollisionRect().colliderect(collision1Rect) and self._ball.getCollisionRect().colliderect(collision2Rect):      
         self._ball._velocity.x = random.randint(-100,100)
         self._ball._velocity.y = -300
      else:
         self._ball.collider(self._player1,player1Rect)
         self._ball.collider(self._player2,player2Rect)
      
      # Updating every time a goal is scored
      if self._ball.getCollisionRect().colliderect(self._rightGoalRect):
         self._goal1 += 1
        
      if self._ball.getCollisionRect().colliderect(self._leftGoalRect):
         self._goal2 +=1
        
      #Resetting the positions of the player if a goal is scored
      if  self._ball.getCollisionRect().colliderect(self._rightGoalRect) or self._ball.getCollisionRect().colliderect(self._leftGoalRect):
         if  self._ball.getCollisionRect().colliderect(self._rightGoalRect):
            self._goalP2 = True
            self._goalTimer = 4
         elif self._ball.getCollisionRect().colliderect(self._leftGoalRect):
            self._goalP1 = True
            self._goalTimer = 4
         
         self._player1.setPosition(Vector2(90,570))
         self._player2.setPosition(Vector2(900,570))
         self._ball.setPosition(Vector2(510, 616))
         self._ball._velocity = (Vector2(0,0))
         self._player1._state.manageState("ground",self._player1)
         self._player1._state.manageState("stopleft",self._player1) 
         self._player1._state.manageState("stopright",self._player1)
         self._player1._state.manageState("stopsliding",self._player1) 
         self._player1.transitionState("standing")

         self._player2._state.manageState("ground",self._player2)
         self._player2._state.manageState("stopleft",self._player2) 
         self._player2._state.manageState("stopright",self._player2)
         self._player2._state.manageState("stopsliding",self._player1)
         self._player2.transitionState("standing")



      #Pausing the screen momentarily
      if self._goalP2  or self._goalP1 :
         self._goalTimer -= seconds
         if self._goalTimer <=0:
            self._goalP1 = False
            self._goalP2 = False
      
      #For hitting the crossbar sound
      if self._collideBar:
         self._crossTimer -= seconds
         if self._crossTimer <=0:
            self._collideBar = False
            self._crossTimer = 2.2
      
      #Updating the balls position after its collision with the goal post
      self.collisionCrossBar(self._ball,self._rightCrossBar,self._leftCrossBar)

    
      #Updating the score and displaying it
      self._text = self._font.render("Score " + str(self._goal1) + "-" + str(self._goal2),
            False, (0, 0, 0))
        
        
      
      
      # Detect collision
      
      if self._player1._power1 == True:
         clipRect = pygame.Rect.inflate(
          self._player1.getCollisionRect(), 40, -10).clip(self._ground)
      else:
         clipRect = pygame.Rect.inflate(
         self._player1.getCollisionRect(), -35, -10).clip(self._ground)
      
      if self._player2._power1 == True:
         clipRect2 = pygame.Rect.inflate(self._player2.getCollisionRect() ,10,-10).clip(self._ground)
      else:
         clipRect2 = pygame.Rect.inflate(self._player2.getCollisionRect() ,-25,0).clip(self._ground)

      clipRect3 = self._ball.getCollisionRect().clip(self._ground)
      
      if clipRect.width > 0:
         self._player1.collideGround(clipRect.height)
      if clipRect2.width > 0:
         self._player2.collideGround(clipRect2.height)
      if clipRect3.width > 0:
         self._ball.collideGround(clipRect3.height)
      
