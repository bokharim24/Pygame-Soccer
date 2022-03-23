import random
import pygame

from modules.FSM import *

from .mobile import Mobile
from .animated import Animated
from .drawable import Drawable
from .vector2D import Vector2


class Ball(Mobile):
    def __init__(self, position):
        super().__init__("SoccerBall.png", position)

        self._position = Vector2(*position)
        self._velocity = Vector2(0, 0)
        self._gravity = 200
        self._frictionY = 45
        self._frictionX = 30
        self._power5 = False


    def collider(self, object, objectRect):
        if self.getCollisionRect().colliderect(objectRect):
    
            clipBox = objectRect.clip(self.getCollisionRect())
            if clipBox.width < clipBox.height:
                if self.getPosition().x < object.getPosition().x:
                    change = Vector2(-clipBox.width, 0)
                else:
                    change = Vector2(clipBox.width, 0)
            else:

                if self.getPosition().x < object.getPosition().y:
                    change = Vector2(0, -clipBox.height)
                else:
                    change = Vector2(0, clipBox.height)
            self.setPosition(self.getPosition() + change)
            
            ballCenter = self.getCollisionRect().center
            objectCenter = objectRect.center
            if self._power5 == True:
                self._velocity = (Vector2(*ballCenter) -Vector2(*objectCenter))*2.5
                if object._row == 2:
                    self._velocity.x *= 10
                    self._velocity.y *=15
                else:
                    self._velocity.x *= 5
                    self._velocity.y *=5 
            else:
                self._velocity = Vector2(*ballCenter) -Vector2(*objectCenter)
                if object._row == 2:
                    self._velocity.x *= 10
                    self._velocity.y *=15
                else:
                    self._velocity.x *= 5
                    self._velocity.y *=5 
                #Have to calculate veloctiy Over here for bouncing at specific points. Endpoint - startpoint. balls center and then players center.


    def getWidth(self):
        return self._image.get_width()

    # Returns the height of the image surface
    def getHeight(self):
        return self._image.get_height()

    def getPosition(self):
        return self._position

    def collideGround(self, yClip):
        self._position.y -= yClip

    def update(self, worldinfo, seconds,ground):
        self._velocity[1] += self._gravity * seconds
        newPosition = self.getPosition() + self._velocity * seconds
        if newPosition[0] < 0:
            self._velocity[0] = -self._velocity[0]
        elif newPosition[0] + self.getWidth() > worldinfo[0]:
            self._velocity[0] = -self._velocity[0]

        if newPosition[1] < 0:
            self._velocity[1] = -self._velocity[1]
        elif newPosition[1] + self.getHeight() > worldinfo[1]:
            self._velocity[1] *= self._frictionY * seconds
            self._velocity[0] *= self._frictionX * seconds

            self._velocity[1] = -self._velocity[1]

        newPosition = self.getPosition() + self._velocity * seconds

        self.setPosition(newPosition)
        

        # return self._position

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                self._velocity = Vector2(
                    random.randint(-300, 300), random.randint(-300, 300))