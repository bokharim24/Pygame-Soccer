"""
A PowerUp class
Author: Danish Bokhari

Provides certain powerups to help the players

"""
from .drawable import Drawable
import pygame
from ..managers.frameManager import FrameManager


class PowerUp(Drawable):
    
    def update(self, seconds,player1,player2):
        
        if self._activeTime <= 0 or self._lifeTime<=0:
            self._isDead = True
  
    
    def isDead(self):
        return self._isDead
    
    def isUsed(self):
        return self._isUsed        

"""Powerup to make the player bigger in size"""
class PowerUp1(PowerUp):
    
    #Blue
    def __init__(self, position):
        super().__init__("powerUp2.png", position, (1, 1))
        self._isDead = False
        self._lifeTime = 8
        self._activeTime = 5

        self._isUsed = False   
    
    def power(self,seconds,player1,player2,player1Rect,player2Rect,ball):
        if self.getCollisionRect().colliderect(player1Rect) or self.getCollisionRect().colliderect(player2Rect):
            self._isUsed = True 
            
            if self.getCollisionRect().colliderect(player1Rect):
                player1._power1 = True

            if self.getCollisionRect().colliderect(player2Rect):
                player2._power1 = True
        
        if self._isUsed:
            self._lifeTime -= seconds        
        
        if self._isUsed == False:
            self._activeTime -= seconds
        


        if self._lifeTime <= 0:
            if player1._power1== True:
                player1._power1 = False
            if player2._power1 == True:
                player2._power1 = False


   
"""PowerUp to increase the velocity of a player"""
class PowerUp2(PowerUp):

    def __init__(self, position):
        super().__init__("powerUp2.png", position, (2,0))
        self._isDead = False
        self._lifeTime = 9
        self._activeTime = 5

        self._isUsed = False   
    
    def power(self,seconds,player1,player2,player1Rect,player2Rect,ball):
        if self.getCollisionRect().colliderect(player1Rect) or self.getCollisionRect().colliderect(player2Rect):
            self._isUsed = True 
            
            if self.getCollisionRect().colliderect(player1Rect):
                player1._power2 = True

            if self.getCollisionRect().colliderect(player2Rect):
                player2._power2 = True
        
        if self._isUsed:
            self._lifeTime -= seconds        
        
        if self._isUsed == False:
            self._activeTime -= seconds
        


        if self._lifeTime <= 0:
            if player1._power2 == True:
                player1._power2 = False
            if player2._power2 == True:
                player2._power2 = False

        

"""PowerUp to increase the jump of a player """
class PowerUp3(PowerUp):
    #Red
    def __init__(self, position):
        super().__init__("powerUps.png", position, (0, 1))
        self._isDead = False
        self._lifeTime = 9
        self._activeTime = 5
        self._isUsed = False
    
    def power(self,seconds,player1,player2,player1Rect,player2Rect,ball):
        
        if self.getCollisionRect().colliderect(player1Rect) or self.getCollisionRect().colliderect(player2Rect):
            self._isUsed = True 
            
            if self.getCollisionRect().colliderect(player1Rect):
                player1._power3 = True

            if self.getCollisionRect().colliderect(player2Rect):
                player2._power3 = True          
        
        if self._isUsed:
            self._lifeTime -= seconds        
        
        if self._isUsed == False:
            self._activeTime -= seconds
        
        if self._lifeTime <= 0:
            if player1._power3 == True:
                player1._power3 = False
            if player2._power3 == True:
                player2._power3 = False

"""Powerup to freeze the opposing player"""
class PowerUp4(PowerUp):
    
    #Purple
    def __init__(self, position):
        super().__init__("powerUps.png", position, (1, 0))
        self._isDead = False
        self._lifeTime = 6
        self._isUsed = False 
        self._activeTime = 5
   
    def power(self,seconds,player1,player2,player1Rect,player2Rect,ball):
        if self.getCollisionRect().colliderect(player1Rect) or self.getCollisionRect().colliderect(player2Rect):
            self._isUsed = True 
        
            if self.getCollisionRect().colliderect(player1Rect):
                player2._power4 = True

        
            if self.getCollisionRect().colliderect(player2Rect):
                player1._power4 = True
    
         
        if self._isUsed:
            self._lifeTime -= seconds        
        
        if self._isUsed == False:
            self._activeTime -= seconds
        


        if self._lifeTime <= 0:
            if player1._power4 == True:
                player1._power4 = False
            if player2._power4 == True:
                player2._power4 = False
"""Powerup to increase the velocity and bounce behavior of the balls"""

class PowerUp5(PowerUp):
    
    #Blue
    def __init__(self, position):
        super().__init__("powerUps.png", position, (1, 1))
        self._isDead = False
        self._lifeTime = 7
        self._isUsed = False  
        self._activeTime = 5
 
    
    def power(self,seconds,player1,player2,player1Rect,player2Rect,ball):
        if self.getCollisionRect().colliderect(player1Rect) or self.getCollisionRect().colliderect(player2Rect):
            ball._power5 = True
            self._isUsed = True 
        
        if self._isUsed:
            self._lifeTime -= seconds        
        
        if self._isUsed == False:
            self._activeTime -= seconds
        
        if self._lifeTime <= 0:
            ball._power5 = False
        
        
"""Powerup to increase the gravity of the ball"""

class PowerUp6(PowerUp):
    
    #Grey
    def __init__(self, position):
        super().__init__("powerUps.png", position, (0, 0))
        self._isDead = False
        self._lifeTime = 7
        self._isUsed = False   
        self._activeTime = 5
    
    def power(self,seconds,player1,player2,player1Rect,player2Rect,ball):
        if self.getCollisionRect().colliderect(player1Rect) or self.getCollisionRect().colliderect(player2Rect):
            self._isUsed = True 
            ball._power6 = True
        
        if self._isUsed:
            self._lifeTime -= seconds        
        
        if self._isUsed == False:
            self._activeTime -= seconds
        
        if self._lifeTime <= 0:
            ball._power6 = False
        
        