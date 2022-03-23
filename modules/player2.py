

from sympy import N
from modules.animated import Animated
from .mobile import Mobile
from .FSM import PlayerState

import pygame


class Player2(Mobile):
    def __init__(self, position):
        super().__init__("pp.png", position)

        self._jumpTime = 0.2
        self._vSpeed = 100
        self._jSpeed = 100

        self._power1 = False
        self._power2 = False
        self._power3 = False
        self._power4 = False


        self._nFrames = 2
        self._framesPerSecond = 2

        self._nFramesList = {
            #"walking": 2,
            "running": 4,
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
        else:
            return super().getVSpeed()
    
    def getJSpeed(self):
        if self._power3 == True:
            return super().getJSpeed() *1.75
        else:
            return super().getJSpeed()
            #return 100
    
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
    
    """def update(self, seconds, boundaries):

        super().update(seconds)
    
        # if self._state.isMoving(): # !!!
        if self._state._movement["sliding"]:
            self._velocity.x = -self._vSpeed *2# !!!
        elif self._state._movement["left"]:
            self._velocity.x = -self._vSpeed
        elif self._state._movement["right"]:
            self._velocity.x = self._vSpeed
            # elif self._state._movement["sliding"]:
            #    self._velocity.x = self._vSpeed
        else:
            self._velocity.x = 0

        if self._state.isGrounded(): #getState() == "standing" or self._state.getState() == "sliding": !!!
            self._velocity.y = 0
        elif self._state.getState() == "jumping":
            self._velocity.y = -self._jSpeed
            self._jumpTimer -= seconds
            if self._jumpTimer < 0:
                self._state.manageState("fall", self)
        elif self._state.getState() == "falling":
            self._velocity.y += self._jSpeed * seconds

        newPosition = self.getPosition() + self._velocity * seconds

        if newPosition.x < 0 or newPosition.x > boundaries.x - self.getSize()[0]:
            self._velocity.x = -self._velocity.x

        newPosition = self.getPosition() + self._velocity * seconds

        self.setPosition(newPosition)"""