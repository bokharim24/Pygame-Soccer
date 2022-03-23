

from .mobile import Mobile
from .FSM import PlayerState

import pygame


class Player1(Mobile):
    def __init__(self, position):
        super().__init__("playerF.png", position)
#power1active boolean to represent whether or not something is active
        self._jumpTime = 0.2
        self._vSpeed = 100
        self._jSpeed = 100
        
        self._power1 = False
        self._power2 = False
        self._power3 = False
        self._power4 = False


        """self._powerups ={
        1 :False,
        2:False,
        3:False,
        4 : False
        }
        
        self._powerTimer = {
            1:5,
            2:5,
            3:5,
            4:5
        }"""
        #When true set it to time, in update, if true decrease the timer.
        self._nFrames = 2
        self._framesPerSecond = 2

        self._nFramesList = {
            #"walking": 2,
            "running": 5,
            "jumping": 1,
            "sliding": 1,
            "falling": 1,
            "standing": 2
        }

        self._rowList = {
            #"walking": 3,
            "running": 1,
            "jumping": 0,
            "sliding": 2,
            "falling": 4,
            "standing": 3
        }

        self._framesPerSecondList = {
            #"walking": 8,
            "standing": 2,
            "jumping": 3,
            "sliding": 8,
            "falling": 3,
            "running": 8
        }

        self._state = PlayerState()

        self.transitionState("standing")

    def getVSpeed(self):
        if self._power2 == True:
            return super().getVSpeed() *2
        elif self._power2 == False:
            return super().getVSpeed()
    
    def getJSpeed(self):
        if self._power3 == True:
            return super().getJSpeed() *1.75
        elif self._power3 == False:
            return super().getJSpeed() 
           
    """def getCollisionRect(self):
        if self._row == 2:
            newRect = pygame.Rect.inflate(
            self.getCollisionRect(), -20, -17)
        else:
            newRect =  pygame.Rect.inflate(
            self.getCollisionRect(), -35, -10)
        return newRect"""
    
    def handleEvent(self, event):            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    self._state.manageState("jump", self)

                elif event.key == pygame.K_a:
                    self._state.manageState("left", self)

                elif event.key == pygame.K_d:
                    self._state.manageState("right", self)

                elif event.key == pygame.K_s:
                    self._state.manageState("sliding", self)

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_w:
                    self._state.manageState("fall", self)

                elif event.key == pygame.K_a:   
                    self._state.manageState("stopleft", self)

                elif event.key == pygame.K_d:
                    self._state.manageState("stopright", self)

                elif event.key == pygame.K_s:
                    self._state.manageState("stopsliding", self)
       

    def collideGround(self, yClip):
        self._state.manageState("ground", self)
        self._position.y -= yClip
    
    