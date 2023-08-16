
#! Apologies - 16/08/2023
#! I have cancelled this project.
#! I will son start redeveloping it using flutter
#! This is due to public demand that it ought to be available on mobile

import pygame;
import random;
import Enemies;


pygame.init()

standardHeight = 80
standardwidth = 80

screenWidth = 1400;
screenHeight = 600;

direction = "rest"
Hit = False

screen = pygame.display.set_mode((screenWidth, screenHeight));
pygame.display.set_caption("Fidgety Space Warriors");



#!Player Images to set
Playerflying1 = pygame.image.load("FunImages/KithinjiRocket1.png")
Playerflying2 = pygame.image.load("FunImages/KithinjiRocket2_.png")
PlayerflyingLeft = pygame.image.load("FunImages/ShuttleLeft.png")
PlayerflyingRight = pygame.image.load("FunImages/ShuttleRight.png")
PrimaryBomb = pygame.image.load("FunImages/Bomb1.png")
EnemyImg = pygame.image.load("FunImages/BadBoy.png")

#! image alterations and animatons
Playerflying1 = pygame.transform.scale(Playerflying1, (standardwidth, standardHeight))
Playerflying2 = pygame.transform.scale(Playerflying2, (standardwidth, standardHeight))
PlayerflyingLeft = pygame.transform.scale(PlayerflyingLeft, (standardwidth, standardHeight))
PlayerflyingRight = pygame.transform.scale(PlayerflyingRight, (standardwidth, standardHeight))
EnemyImg = pygame.transform.scale(EnemyImg, (standardwidth, standardHeight))

PrimaryBombAngle = 0
prevPrimaryBombAngle = 0

# PrimaryBombLeft = pygame.transform.rotate(PrimaryBomb, (45))
# PrimaryBombRight = pygame.transform.rotate(PrimaryBomb, (-45))
# PrimaryBombDown = pygame.transform.rotate(PrimaryBomb, (180))
# PrimaryBombDownRight = pygame.transform.rotate(PrimaryBomb, (-135))
# PrimaryBombDownLeft = pygame.transform.rotate(PrimaryBomb, (225))


TIMER_EVENT = pygame.USEREVENT + 1;


#! My starting positions
playerX = screenWidth / 2;
playerY = 480;

#?Level 1
temp_hit_count = 0;

num_of_enemies = 5;
EnemyX = []
EnemyY = []
EnemyX_change = [];
EnemyY_change = [];
Enemy_rects = [];

for i in range(num_of_enemies):
    EnemyX.append(random.randint(0, screenWidth));
    EnemyY.append(random.randint(50, 150));
    EnemyX_change.append(0.5 + (i * 0.1));

    Enemy_rect = pygame.Rect(EnemyX[i], EnemyY[i], standardwidth, standardHeight)
    Enemy_rects.append(Enemy_rect)
    pygame.draw.rect(screen, (255, 0, 0), Enemy_rects[i], 2)

# EnemyX = random.randint(0, 800);
# EnemyY = random.randint(50, 150)

#! Enemy and player movements
playerX_change = 0;



#! Functions to get my good buddy and the good old bad guys on screen
currentPlayerImage = Playerflying1;

pygame.time.set_timer(TIMER_EVENT, 120)

def player(x, y, direction):
    global currentPlayerImage;
    if direction == "rest":
        screen.blit(currentPlayerImage, (x, y))
        
    elif direction == "left":
        screen.blit(PlayerflyingLeft, (x, y))
    elif direction == "right":
        screen.blit(PlayerflyingRight, (x, y))

def badGuys(x, y):
    screen.blit(EnemyImg, (x, y))



#! The fun part; BULLEEETTTTTSSS pyeww! pyew 🔫🔫
BulletX = 0
BulletY = 0
BulletX_change = 0
BulletY_change = 0
BulletActive = "none"
Bullet_collided = False;
standardX_change_per_frame = 0.6
standardY_change_per_frame = 0.6

Bullet_rect = pygame.Rect(BulletX, BulletY, standardwidth, standardHeight)

def Bullet(x, y, orientation):
    global BulletX_change, BulletY_change, standardX_change_per_frame, standardY_change_per_frame, PrimaryBombAngle, prevPrimaryBombAngle;    
    BulletY_change = standardY_change_per_frame;
    if orientation == "left":
        if standardX_change_per_frame > 0:
            standardX_change_per_frame *= -1
        BulletX_change = standardX_change_per_frame
        PrimaryBombAngle = 45
        GuidedBomb = pygame.transform.rotate(PrimaryBomb, (PrimaryBombAngle))
        screen.blit(GuidedBomb, (x, y))
        prevPrimaryBombAngle = PrimaryBombAngle
    elif orientation == "right":
        if standardX_change_per_frame < 0:
            standardX_change_per_frame *= -1
        BulletX_change = standardX_change_per_frame
        PrimaryBombAngle = -45
        GuidedBomb = pygame.transform.rotate(PrimaryBomb, (PrimaryBombAngle))
        screen.blit(GuidedBomb, (x, y))
        prevPrimaryBombAngle = PrimaryBombAngle
    elif orientation == "down":
        if prevPrimaryBombAngle == -45:
            PrimaryBombAngle = 225
        elif prevPrimaryBombAngle == 45:
            PrimaryBombAngle = 135
        else:
            PrimaryBombAngle = 180
        BulletY_change = standardY_change_per_frame
        GuidedBomb = pygame.transform.rotate(PrimaryBomb, (PrimaryBombAngle))
        screen.blit(GuidedBomb, (x, y))

    else: 
        BulletX_change = 0;
        screen.blit(PrimaryBomb, (x, y));


def bulletCollisions(HitLocation, x, y):
    global BulletY_change, BulletX_change, standardX_change_per_frame, standardY_change_per_frame, BulletActive, PrimaryBomb,temp_hit_count
    print(HitLocation)
    if HitLocation == "Hit":
        temp_hit_count += 1
        print(temp_hit_count)
    if HitLocation == "upperEdge":
        standardY_change_per_frame = -standardY_change_per_frame
        standardX_change_per_frame = -standardX_change_per_frame
        BulletActive = "down"
    if HitLocation == "lowerEdge":
        standardY_change_per_frame = -standardY_change_per_frame
        standardX_change_per_frame = -standardX_change_per_frame
    if HitLocation == "leftEdge":
        screen.blit(PrimaryBomb, (x, y))
        BulletActive = "right"
    if HitLocation == "rightEdge":
        screen.blit(PrimaryBomb, (x, y))
        BulletActive = "left"




def FIRE(direction):
    global BulletX, BulletY, BulletActive, standardY_change_per_frame;
    BulletX = playerX
    BulletY = playerY - 30
    print(BulletX, playerY,  BulletY)
    BulletActive = direction
    if standardY_change_per_frame < 0:
        standardY_change_per_frame = -standardY_change_per_frame
        print("throwback")



#!Game run loop
running = True;
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        
        if event.type == TIMER_EVENT:
            if currentPlayerImage == Playerflying1:
                currentPlayerImage = Playerflying2
            else:
                currentPlayerImage = Playerflying1

        #!Ensuring I get all keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2;
                direction = "left";
            if event.key == pygame.K_RIGHT:
                playerX_change = 2;
                direction = "right";
            if event.key == pygame.K_a:
                FIRE("left");
            elif event.key == pygame.K_s:
                PrimaryBombAngle = 0
                FIRE("up")
            elif event.key == pygame.K_d:
                FIRE("right")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                playerX_change = 0;
                direction = "rest";
    
    

    playerX += playerX_change;
    #!Keeping bounderies
    if playerX <= 0:
        playerX = 0;
    elif playerX >= screenWidth:
        playerX = screenWidth;
    
    if BulletActive != "none":
        if Bullet_rect.right >= screenWidth:
            bulletCollisions("rightEdge", BulletX, BulletY)
        elif Bullet_rect.top == 0:
            BulletY_change = -BulletY_change
            bulletCollisions("upperEdge", BulletX, BulletY)
        elif Bullet_rect.bottom == screenHeight:
            BulletY_change = -BulletY_change
            bulletCollisions("lowerEdge", BulletX, BulletY)
        elif Bullet_rect.left <= 0:
            BulletX_change = -BulletX_change 
            bulletCollisions("leftEdge", BulletX, BulletY)

    for i in range(num_of_enemies):
        EnemyX[i] += EnemyX_change[i]
        Enemy_rects[i].x = EnemyX[i]
        Enemy_rects[i].y = EnemyY[i]
        pygame.draw.rect(screen, (255, 0, 0), Enemy_rects[i], 2)

        if Bullet_rect.colliderect(Enemy_rects[i]):
            temp_hit_count += 1;
            bulletCollisions("Hit", BulletX, BulletY)
            
        
        if EnemyX[i] <= 0:
            EnemyX_change[i] = -EnemyX_change[i]
        elif EnemyX[i] >= screenWidth:
            EnemyX_change[i] = -EnemyX_change[i]
        
        


    if BulletActive != "none":
        BulletX += BulletX_change
        BulletY += BulletY_change
        Bullet_rect.x = BulletX
        Bullet_rect.y = BulletY
        pygame.draw.rect(screen, (0, 0, 255), Bullet_rect, 2)
        Bullet(BulletX, BulletY, BulletActive);


    #! Yooow people!!! Time to get on set!
    player(playerX, playerY, direction);
    for i in range(num_of_enemies):
        badGuys(EnemyX[i], EnemyY[i])

    pygame.display.update();