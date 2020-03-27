import pygame

pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Cubes")

walkRight = [pygame.image.load('png/1/walk/1_terrorist_1_Walk_000.png'),
pygame.image.load('png/1/walk/1_terrorist_1_Walk_001.png'),
pygame.image.load('png/1/walk/1_terrorist_1_Walk_002.png'),
pygame.image.load('png/1/walk/1_terrorist_1_Walk_003.png'),
pygame.image.load('png/1/walk/1_terrorist_1_Walk_004.png'),
pygame.image.load('png/1/walk/1_terrorist_1_Walk_005.png')]
#pygame.image.load('png/1/walk/1_terrorist_1_Walk_006.png'),
#pygame.image.load('png/1/walk/1_terrorist_1_Walk_007.png')]

walkLeft = [pygame.image.load('png/1/walk/1_terrorist_1_Walk_000.png'),
pygame.image.load('png/1/walk/1_terrorist_1_Walk_001.png'),
pygame.image.load('png/1/walk/1_terrorist_1_Walk_002.png'),
pygame.image.load('png/1/walk/1_terrorist_1_Walk_003.png'),
pygame.image.load('png/1/walk/1_terrorist_1_Walk_004.png'),
pygame.image.load('png/1/walk/1_terrorist_1_Walk_005.png')]
#pygame.image.load('png/1/walk/1_terrorist_1_Walk_006.png'),
#pygame.image.load('png/1/walk/1_terrorist_1_Walk_007.png')]

bg = pygame.image.load('Cartoon_Forest_BG_01.png')
playerstand = pygame.image.load('png/1/idle/1_terrorist_1_Idle_000.png')

clock = pygame.time.Clock()

x = 50
y = 385
width = 0
height = 0
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = "right"


class snaryad():
    def __init__(self, x,y,radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win,self.color, (self.x,self.y),self.radius)

def drawwindow():
    global animCount
    win.blit(bg,(0,0))

    if animCount +1 >=30:
        animCount =0

    if left:
        win.blit(walkLeft[animCount //5], (x,y))
        animCount +=1
    elif right:
        win.blit(walkRight[animCount //5], (x,y))
        animCount +=1
    else:
        win.blit(playerstand,(x,y))

    for bullet in bullets:
        bullet.draw(win)

    pygame.draw.rect(win, (0,0,255), (x,y,width,height))
    pygame.display.update()


run = True

bullets=[]

while run:

    clock.tick(30)
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x +=bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:

        if lastMove == "right":
            facing = 1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(snaryad(round(x + width//2+50), round(y + height//2 +50), 5, (255,0,0), facing))



    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left= True
        right=False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
        left= False
        right=True
        lastMove = "right"
    else:
        left= False
        right=False
        animCount = 0

    if not(isJump):
        """if keys[pygame.K_UP] and y > 5:
            y -= speed
        if keys[pygame.K_DOWN] and y < 500 - height - 15:
            y += speed
        """
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount <0:
                y +=(jumpCount **2)/2
            else:
                y -=(jumpCount **2)/2
            jumpCount -=1

        else:
            isJump = False
            jumpCount = 10

    drawwindow()




pygame.quit()
