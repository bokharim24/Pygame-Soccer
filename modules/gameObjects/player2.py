
from .mobile import Mobile
from .vector2D import Vector2

from ..FSMs.playerFSM import PlayerState
import pygame

#A class representing player 2, has all the powerups as well 

class Player2(Mobile):
    def __init__(self, position):
        super().__init__("pp.png", position)

        self._jumpTime = 0.12
        self._vSpeed = 100
        self._jSpeed = 100

        self._power1 = False
        self._power2 = False
        self._power3 = False
        self._power4 = False


        self._nFrames = 2
        self._framesPerSecond = 2

        self._nFramesList = {
            "running": 4,
            "jumping": 1,
            "sliding": 1,
            "falling": 1,
            "standing": 2
        }

        self._rowList = {
            "running": 1,
            "jumping": 0,
            "sliding": 2,
            "falling": 4,
            "standing": 3
        }

        self._framesPerSecondList = {
            "standing": 2,
            "jumping": 3,
            "sliding": 8,
            "falling": 3,
            "running": 8
        }

        self._state = PlayerState()

        self.transitionState("standing")

    
    #Overrides Drawable to work for power1
    def getPosition(self):
        if self._power1 == True:
            return super().getPosition() - Vector2(self.getWidth()//2, self.getHeight())
        elif self._power1 == False:
            return super().getPosition()
    
    #Overrides Drawable to work for power1
    def setPosition(self,newPosition):
        if self._power1 == True:
            return super().setPosition(newPosition + Vector2(self.getWidth()//2, self.getHeight())) 
        elif self._power1 == False:
            return super().setPosition(newPosition)
    

    #Overrides Drawable to work for power3
    def getCollisionRect(self):
        if self._power1 == True:
            newRect = self.getPosition() + self.getImage().get_rect()
            return newRect
        elif self._power1 == False:
            return super().getCollisionRect()


    #Overrides Drawable to work for power1
    def getImage(self):
        if self._power1 == True:
            return pygame.transform.scale(super().getImage(),list(Vector2(*self.getSize())*2))
        elif self._power1 == False:
            return super().getImage()
    
    #Overrides Drawable to work for power2
    def getVSpeed(self):
        if self._power2 == True:
            return super().getVSpeed() *2
        else:
            return super().getVSpeed()
    
   
   
    #Overrides Drawable to work for power3
    def getJSpeed(self):
        if self._power3 == True:
            return super().getJSpeed() *1.75
        else:
            return super().getJSpeed()
    
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                self._state.manageState("jump", self)

            elif event.key == pygame.K_LEFT:
                self._state.manageState("left", self)

            elif event.key == pygame.K_RIGHT:
                self._state.manageState("right", self)

            elif event.key == pygame.K_DOWN:
                self._state.manageState("sliding", self)

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                self._state.manageState("fall", self)

            elif event.key == pygame.K_LEFT:
                self._state.manageState("stopleft", self)

            elif event.key == pygame.K_RIGHT:
                self._state.manageState("stopright", self)

            elif event.key == pygame.K_DOWN:
                self._state.manageState("stopsliding", self)
    
    
    def collideGround(self, yClip):
        self._state.manageState("ground", self)
        self._position.y -= yClip
    
