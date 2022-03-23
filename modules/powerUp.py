"""
A PowerUp class
Author: Danish Bokhari

Provides certain powerups to help the players

"""



import pygame
from .drawable import Drawable


class PowerUp(Drawable):
       
    #def __init__(self,position):
    #    self.lifetime = 5
    #    self._isDead = False
    
    """def update(self, seconds):
        if self._lifetime <= 0:
         self._isDead = True
        else:
         self._lifetime -= seconds
         super().update(seconds)"""
    def update(self, seconds,player1,player2):
        if self._lifeTime <= 0 or self.getCollisionRect().colliderect(player1) or self.getCollisionRect().colliderect(player2):
            self._isDead = True
        else:
            self._lifeTime -= seconds
    
    def isDead(self):
          return self._isDead
            
"""Powerup to make the player bigger in size"""
class PowerUp1(PowerUp):
    
    def __init__(self, position):
        super().__init__("powerUps.png", position, (0, 0))
        self._isDead = False
        self._lifeTime = 5
        self._powerTime = 5
    
    def power(self,seconds,player1,player2,player1Rect,player2Rect,ball):
        if self.getCollisionRect().colliderect(player1Rect):
            player1Rect =  pygame.Rect.inflate(
            player1.getCollisionRect(), -75, -20)
        
        if player1._power1 == True or player2._power1 == True:
            self._powerTime -= seconds
        
        if self._powerTime <= 0:
            if player1._power1 == True:
                player1._power1 = False
            if player2._power1 == True:
                player2._power1 = False
            self._powerTime = 5

"""PowerUp to increase the velocity of a player"""
class PowerUp2(PowerUp):
    def __init__(self, position):
        super().__init__("powerUps.png", position, (0, 1))
        self._isDead = False
        self._lifeTime = 5
        self._powerTime = 5
    
    def power(self,seconds,player1,player2,player1Rect,player2Rect,ball):
        if self.getCollisionRect().colliderect(player1Rect):
            player1._power2 = True
            #player1._powerups[1] = True
            #player1._powerups[1] = 5
            
        if self.getCollisionRect().colliderect(player2Rect):
            player2._power2 = True
        
        if player1._power2 == True or player2._power2 == True:
            self._powerTime -= seconds
        
        
        if self._powerTime < 0:
            if player1._power2 == True:
                player1._power2 = False
            if player2._power2 == True:
                player2._power2 = False
            #self._powerTime = 5
        
        
        """for key in player1._powerups:
            if player1._powerups[key]:
                player1._powerTimer[key] -= seconds
                if player1._powerTimer[key] <0:
                    player1._powerups[key] = False"""
        

"""PowerUp to increase the jump of a player """
class PowerUp3(PowerUp):
    def __init__(self, position):
        super().__init__("powerUps.png", position, (1, 0))
        self._isDead = False
        self._lifeTime = 5
        self._powerTime = 5
    
    def power(self,seconds,player1,player2,player1Rect,player2Rect,ball):
        if self.getCollisionRect().colliderect(player1Rect):
            player1._power3 = True

        if self.getCollisionRect().colliderect(player2Rect):
            player2._power3 = True
        
        if player1._power3 == True or player2._power3 == True:
            self._powerTime -= seconds
        
        if self._powerTime <= 0:
            if player1._power3 == True:
                player1._power3 = False
            if player2._power3 == True:
                player2._power3 = False
            #self._powerTime = 5


"""Powerup to freeze the opposing player"""
class PowerUp4(PowerUp):
    
    def __init__(self, position):
        super().__init__("powerUps.png", position, (0, 1))
        self._isDead = False
        self._lifeTime = 5
        self._powerTime = 5
    
    def power(self,seconds,player1,player2,player1Rect,player2Rect,ball):
        if self.getCollisionRect().colliderect(player1Rect):
            player2._power4 = True
        
        if self.getCollisionRect().colliderect(player2Rect):
            player1._power4 = True
        
        if player1._power4 == True or player2._power3 == True:
            self._powerTime -= seconds
        
        if self._powerTime <= 0:
            if player1._power4 == True:
                player1._power4 = False
            if player2._power4 == True:
                player2._power4 = False
            #self._powerTime = 1      


"""Powerup to increase the velocity and bounce behavior of the balls"""

class PowerUp5(PowerUp):
    
    def __init__(self, position):
        super().__init__("powerUps.png", position, (0, 1))
        self._isDead = False
        self._lifeTime = 5
        self._powerTime = 5
    
    def power(self,seconds,player1,player2,player1Rect,player2Rect,ball):
        if self.getCollisionRect().colliderect(player1Rect) or  self.getCollisionRect().colliderect(player2Rect):
            ball._power5 = True
        
        if ball._power5 == True: 
            self._powerTime -= seconds
        
        if self._powerTime <= 0:
            ball._power5 = False
            #self._powerTime = 1        