
#? Enemies increase in complexity as player plays. New enemy is generated when preceding one is shot down
#? Enemy resistance, Enemy relative speed, deviation from standard dimensions
#? Enemy assult type


import pygame;
import random;

pygame.init()

class EnemyMothership:
        def __init__(self, EnemyLevel: int, HitCount: int, screenWidth) -> None:
                self.EnemyLevel = EnemyLevel
                self.HitCount = HitCount
                self.Damage = ""
                self.screenWidth = screenWidth

                self.SaucerX = 0
                self.SaucerY = 0

                self.X_change = 0
                self.Ychange = 0

        def shipManagement(self):
                self.Damage = self.damageAssesment()  
                if self.Damage != "Vanguished":
                        self.deploySaucer(self.Damage)
                else:
                        self.retractSaucer()
                        
        def damageAssesment(self) -> str:
                if self.EnemyLevel - self.HitCount == 0:
                        return "Vanguished"
                elif self.EnemyLevel - self.HitCount == 1:
                        return "Unbeliveble"
                elif self.EnemyLevel / self.HitCount > 1.5 and self.EnemyLevel / self.HitCount < 2.5:
                        return "looks fine to me 🤷🏽‍♂️"
                else:
                        return "Fit as fiddle"
        def deploySaucer(self, Assessment: str = "")-> None:
                self.SaucerX = (random.randint(0, self.screenWidth))
                self.SaucerY = (random.randint(50, 250))
        
        def retractSaucer(self)-> None:
                self.SaucerX = 0
                self.SaucerY = 0

        def controllSaucer(self):
                switcher = {
                        1: [1, 0],
                        2: [0.5, 1],
                        3: [1, 1]
                }
        
                self.SaucerX += switcher[self.EnemyLevel][0]
                self.SaucerY += switcher[self.EnemyLevel][1]
                return self.SaucerX, self.SaucerY
        
