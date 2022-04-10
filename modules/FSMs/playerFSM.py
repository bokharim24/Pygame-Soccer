

class BasicState(object):
    def __init__(self, facing="none"):
        self._facing = facing

    def getFacing(self):
        return self._facing

    def _setFacing(self, direction):
        self._facing = direction


#Handles the fsm for the player
class PlayerState(object):
    def __init__(self, state="falling"):
        self._state = state

        self._movement = {
            "left": False,
            "right": False,
            "sliding": False
        }

        self._lastFacing = "right"

    def isMoving(self):
        return True in self._movement.values()

    def isGrounded(self):
        return self._state == "running" or self._state == "standing" or self._state == "sliding"

    def getFacing(self):
        if self._movement["left"] == True:
            self._lastFacing = "left"
        elif self._movement["right"] == True:
            self._lastFacing = "right"

        return self._lastFacing

    def manageState(self, action, player):
        if action in self._movement.keys():
            if self._movement[action] == False:
                if (self._state == "falling" and action in ["left", "right"]) or self.isGrounded():#!!! To prevent sliding in air movement
                    self._movement[action] = True
                    
                    
                if self._state == "standing":
                    if action == "left" or action == "right":
                        self._state = "running"
                        player.transitionState(self._state)  
                    else:
                        self._state = "sliding"
                        player.transitionState(self._state)
                elif action == "sliding" and self._state != "sliding" and self.isGrounded(): # !!!
                    self._state = "sliding"# !!!
                    player.transitionState(self._state)# !!!
                    

        elif action.startswith("stop") and action[4:] in self._movement.keys():
            direction = action[4:]
            if direction == "sliding" and self._state == "sliding":
                self._movement["sliding"] = False # !!!
                if self._movement["left"] == True or self._movement["right"] == True:
                    self._state = "running"
                    player.transitionState(self._state)
                else:
                    self._state = "standing"
                    player.transitionState(self._state)
            elif self._movement[direction] == True and (direction == "left" or direction == "right"):
                self._movement[direction] = False
                allStop = True
                for move in ["left", "right"]:
                    if self._movement[move] == True:
                        allStop = False
                        break

                if allStop and self._state not in ["falling", "jumping", "sliding"]: # !!!!
                    self._state = "standing" # !!!
                    player.transitionState(self._state)

        elif action == "jump" and self.isGrounded() and self._state != "sliding":  # (self._state == "standing" or self._state == "sliding"): !!!
            self._state = "jumping"
            player.transitionState(self._state)

        elif action == "fall" and not self.isGrounded(): #self._state != "falling": !!!
            self._state = "falling"
            player.transitionState(self._state)

        elif action == "ground" and self._state == "falling":

            # self._state = "standing" # !!! 
            # player.transitionState(self._state) # !!!

            if self.isMoving() and (self._movement["left"] == True or self._movement["right"] == True):
                #if player._power4 == True:
                #    self._state = "standing"
                #    player.transitionState(self._state)
                
                self._state = "running" # !!!
                player.transitionState(self._state) # !!!
            elif self.isMoving() and self._movement["sliding"] == True:
                self._state = "sliding" # !!!
                player.transitionState(self._state)
            else:
                self._state = "standing" # !!!
                player.transitionState(self._state)

    def getState(self):
        return self._state
  


