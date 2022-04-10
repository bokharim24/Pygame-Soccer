from ..gameObjects.vector2D import Vector2
from ..gameObjects.drawable import Drawable


SCREEN_SIZE = Vector2(1100, 650)

SCALE = 1
UPSCALED = SCREEN_SIZE * SCALE

def adjustMousePos(mousePos):
   return Vector2(*mousePos) // SCALE 