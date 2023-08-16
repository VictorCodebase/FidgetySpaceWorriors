
#? Enemies increase in complexity as player plays. New enemy is generated when preceding one is shot down
#? Enemy resistance, Enemy relative speed, deviation from standard dimensions
#? Enemy assult type


import pygame;
import random;

pygame.init()

class EnemyMothership:
        def __init__(self, EnemyLevel: int, HitCount: int) -> None:
                self.EnemyLevel = EnemyLevel
                self.HitCount = HitCount
                self.Damage = ""

                self.SaucerX = 0
                self.SaucerY = 0

        def shipManagement(self):
                self.Damage = self.damageAssesment()  
                if self.Damage != "Vanguished":
                        self.redeploySaucer(self.Damage)
        
        def damageAssesment(self) -> str:
                if self.EnemyLevel - self.HitCount == 0:
                        return "Vanguished"
                if self.EnemyLevel - self.HitCount == 1:
                        return "Unbeliveble"
                if self.EnemyLevel / self.HitCount > 1.5 and self.EnemyLevel / self.HitCount < 2.5:
                        return "looks fine to me 🤷🏽‍♂️"
                else:
                        return "Fit as fiddle"
        def redeploySaucer(self, Assessment: str)-> None:
                screenWidth = 1400
                screenHeight = 600
                self.SaucerX.append(random.randint(0, screenWidth))
                self.SaucerY.append(random.randint(50, 250))
