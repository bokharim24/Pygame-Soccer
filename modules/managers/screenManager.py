from .basicManager import BasicManager
from .gameManager import GameManager
from .soundManager import SoundManager

from ..FSMs.screenFSM import ScreenState
from ..UI.entries import Text
from ..UI.displays import *
from ..gameObjects.vector2D import Vector2
from ..UI.screenInfo import SCREEN_SIZE
import pygame


class ScreenManager(BasicManager):
   #Initializing screen and sounds for the different events   
   def __init__(self):
      super().__init__()
      self._game = GameManager(SCREEN_SIZE)
      self._state = ScreenState()
      
      self._pausedText = Text(Vector2(0,0),"Paused")
      #Text for goals
      self._goalP1Text = Text(SCREEN_SIZE // 2 - Vector2(175,50),"Player 1 Scored!")
      self._goalP2Text = Text(SCREEN_SIZE // 2 - Vector2(175,50),"Player 2 Scored!")

      #Loading the sounds to be used
      self._loadScreenNoise = SoundManager.getInstance().playSound("loadScreen.mp3")
      self._crowdNoise = SoundManager.getInstance().playSound("regularPlay.wav")
      self._goalSound = SoundManager.getInstance().playSound("goalScored.wav")
      self._crossBarNoise = SoundManager.getInstance().playSound("crossbarCollision.mp3")

      
      SoundManager.getInstance().pauseChannel(self._goalSound)
      SoundManager.getInstance().pauseChannel(self._crowdNoise)
      SoundManager.getInstance().pauseChannel(self._crossBarNoise)
      
      size = self._pausedText.getSize()
      midPointX = SCREEN_SIZE.x // 2 - size[0] // 2
      midPointY = SCREEN_SIZE.y // 2 - size[1] // 2
      
      self._pausedText.setPosition(Vector2(midPointX, midPointY))
      
      #Adding a goalMenu to ask for input
      self._goalMenu = HoverClickMenu("finalPitch.png", fontName="default8")
      self._goalMenu.addText("How many Goals do you want to play upto?", SCREEN_SIZE // 2 - Vector2(350,250))
      self._goalMenu.addOption("three", "3",
                               SCREEN_SIZE // 2 + Vector2(-80,100),
                               )
      self._goalMenu.addOption("four", "4",
                               SCREEN_SIZE // 2 + Vector2(-10,100),
                               )
      self._goalMenu.addOption("five", "5",
                               SCREEN_SIZE // 2 + Vector2(60,100),
                               )
      self._goalMenu.addOption("six", "6",
                               SCREEN_SIZE // 2 + Vector2(130,100),
                               )

      self._mainMenu = HoverClickMenu("finalPitch.png", fontName="default8")
      self._mainMenu.addText("1 VS 1 Soccer", SCREEN_SIZE // 2 - Vector2(120,250))
      self._mainMenu.addOption("start", "Start Game",
                               SCREEN_SIZE // 2 + Vector2(0,100),
                               center="both")
      self._mainMenu.addOption("exit", "Exit Game",
                               SCREEN_SIZE // 2 + Vector2(0,190),
                               center="both")
   
      
      #Adding a finishing screen if player 1 wins
      self._gameOverP1 = HoverClickMenu("p2win.png", fontName="default8")
      self._gameOverP1.addText("Game Over",
                                Vector2(550,50),
                               center="both")
      self._gameOverP1.addText("Player 2 wins!",
                                Vector2(550,100),
                               center="both")

      self._gameOverP1.addOption("exit", "Exit Game",
                                Vector2(550,150),
                               center="both")
      
      #Adding a finishing screen if player 2 wins
      
      self._gameOverP2 = HoverClickMenu("p1win.png", fontName="default8")
      self._gameOverP2.addText("Game Over",
                                Vector2(550,50),
                               center="both")
      self._gameOverP2.addText("Player 1 Wins!",
                                 Vector2(550, 100),
                               center="both")
      self._gameOverP2.addOption("exit", "Exit Game",
                               Vector2(550, 150),
                               center="both")
   
   def setMainMenu(self, menuType):
      if menuType == "event":
         self._mainMenu = self._eventMenu
      elif menuType == "cursor":
         self._mainMenu = self._cursorMenu      
      elif menuType == "hoverclick":
         self._mainMenu = self._hoverClickMenu
   
   def draw(self, drawSurf):
      if self._state == "game":
         self._game.draw(drawSurf)
      
         #Displaying text when a goal is scored
         if self._game._goalP1 == True:
            self._goalP1Text.draw(drawSurf)
         
         if self._game._goalP2 == True:
            self._goalP2Text.draw(drawSurf)

         if self._state.isPaused():
            self._pausedText.draw(drawSurf)
         
         
      elif self._state == "mainMenu":
         self._mainMenu.draw(drawSurf)

      elif self._state == "goalMenu":
         self._goalMenu.draw(drawSurf)
      
      elif self._state == "gameOverP1":
         self._gameOverP1.draw(drawSurf)
      
      elif self._state == "gameOverP2":
         self._gameOverP2.draw(drawSurf)
   
   def handleEvent(self, event):
      # Handle screen-changing events first
      if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
         self._state.manageState("pause", self)
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
         self._state.manageState("mainMenu", self)
      else:
         if self._state == "game" and (not self._game._goalP1 and not self._game._goalP2) :
            self._game.handleEvent(event)
            
         if self._state == "game" and self._game._goal1 == self._game._scoreToWin:
            self._state.manageState("gameOverP1", self)       
         if self._state == "game" and self._game._goal2 == self._game._scoreToWin:
            self._state.manageState("gameOverP2", self)

         #Allowing users to choose number of goals to play upto
         elif self._state == "goalMenu":
            goalChoice = self._goalMenu.handleEvent(event)
            if goalChoice == "three":
               self._game._scoreToWin = 3
            elif goalChoice == "four":
               self._game._scoreToWin = 4
            elif goalChoice == "five":
               self._game._scoreToWin = 5
            elif goalChoice == "six":
               self._game._scoreToWin = 6
            if goalChoice != None:
               self._state.manageState("startGame", self)
         
         elif self._state == "mainMenu":

            choice = self._mainMenu.handleEvent(event)
            if choice == "start":
               self._state.manageState("goalMenu", self)
            
            elif choice == "exit":
               return "exit"
         
         elif self._state == "gameOverP1":
            choiceP1 = self._gameOverP1.handleEvent(event)
            if choiceP1 == "exit":
               return "exit"
         
         elif self._state == "gameOverP2":
            choiceP2 = self._gameOverP2.handleEvent(event)
            if choiceP2 == "exit":
               return "exit"
   
   def update(self, seconds):  
      #Pausing and unpausing music based on updates in the game    
      if self._state == "game" :
         status = self._game.update(seconds, SCREEN_SIZE)
         SoundManager.getInstance().pauseChannel(self._loadScreenNoise)
         SoundManager.getInstance().unpauseChannel(self._crowdNoise)
         SoundManager.getInstance().pauseChannel(self._goalSound)
         SoundManager.getInstance().pauseChannel(self._crossBarNoise)


         if self._game._collideBar ==True:
            SoundManager().getInstance().unpauseChannel(self._crossBarNoise)

         
         if self._game._goalP1 == True or self._game._goalP2 == True:
            SoundManager.getInstance().unpauseChannel(self._goalSound)
            SoundManager.getInstance().pauseChannel(self._crowdNoise)
            SoundManager.getInstance().pauseChannel(self._crossBarNoise)

      
      elif self._state == "game" and self._state.isPaused():
         SoundManager.getInstance().unpauseChannel(self._loadScreenNoise)
         SoundManager.getInstance().pauseChannel(self._crowdNoise)
         SoundManager.getInstance().pauseChannel(self._goalSound)
         SoundManager.getInstance().pauseChannel(self._crossBarNoise)



    
      elif self._state == "mainMenu":
         self._mainMenu.update(seconds)
      
      elif self._state == "goalMenu":
         self._goalMenu.update(seconds)
      
      elif self._state == "gameOverP1":
         self._gameOverP1.update(seconds)
         SoundManager.getInstance().unpauseChannel(self._loadScreenNoise)

      
      elif self._state == "gameOverP2":
         self._gameOverP2.update(seconds)
         SoundManager.getInstance().unpauseChannel(self._loadScreenNoise)
      
      if self._state == "gameOverP1" or self._state == "gameOverP2":
         SoundManager.getInstance().pauseChannel(self._crowdNoise)
         SoundManager.getInstance().pauseChannel(self._goalSound)
         SoundManager.getInstance().pauseChannel(self._crossBarNoise)

        
   
    
   def transitionState(self, state):
      pass
  