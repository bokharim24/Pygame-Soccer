import pygame
from ..managers.frameManager import FrameManager
from ..FSMs.basicFSM import BasicState
from .vector2D import Vector2


class Drawable(object):

    def __init__(self, imageName, position, offset=None):
        self._imageName = imageName

        # Let frame manager handle loading the image
        if self._imageName != "":
            self._image = FrameManager.getInstance().getFrame(self._imageName, offset)
        self._position = Vector2(*position)

    def getPosition(self):
        return self._position

    def setPosition(self, newPosition):
        self._position = newPosition

    def getSize(self):
        return self._image.get_size()

    def getWidth(self):
        return self._image.get_width()
  
    def getHeight(self):
        return self._image.get_height()

    def setImage(self, surface):
        self._image = surface

    def getCollisionRect(self):
        newRect = self._position + self._image.get_rect()
        return newRect
    
    def getImage(self):
        return self._image
    
    def draw(self, surface):
        surface.blit(self.getImage(), (self.getPosition()[0], self.getPosition()[1]))
