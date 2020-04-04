import pygame
import random
import os


pygame.init()

W = 400
H = 600
run = False
start = False
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Protect the world")

soap_img1 = pygame.image.load('images/player.png')
soap_img = pygame.transform.scale(soap_img1, (55, 37))
corona_img1 = pygame.image.load('images/corona.png')
corona_img = pygame.transform.scale(corona_img1, (50, 50))

retry = False

walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load(
    'images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png'), pygame.image.load('images/R10.png'), pygame.image.load('images/R11.png'), pygame.image.load('images/R12.png'), pygame.image.load('images/R13.png'), pygame.image.load(
    'images/R14.png'), pygame.image.load('images/R15.png'), pygame.image.load('images/R16.png')]

walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load(
    'images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png'), pygame.image.load('images/L10.png'), pygame.image.load('images/L11.png'), pygame.image.load('images/L12.png'), pygame.image.load('images/L13.png'), pygame.image.load(
    'images/L14.png'), pygame.image.load('images/L15.png'), pygame.image.load('images/L16.png')]

walkRight1 = [pygame.image.load('images/frame1.png'), pygame.image.load('images/frame2.png'), pygame.image.load('images/frame3.png'), pygame.image.load('images/frame4.png'), pygame.image.load(
    'images/frame5.png'), pygame.image.load('images/frame6.png'), pygame.image.load('images/frame7.png'), pygame.image.load('images/frame8.png'), pygame.image.load('images/frame9.png'), pygame.image.load('images/frame10.png'), pygame.image.load('images/frame11.png'), pygame.image.load('images/frame12.png'), pygame.image.load('images/frame13.png'), pygame.image.load(
    'images/frame14.png'), pygame.image.load('images/frame15.png'), pygame.image.load('images/frame16.png')]


walkLeft1 = [pygame.image.load('images/Lframe1.png'), pygame.image.load('images/Lframe2.png'), pygame.image.load('images/Lframe3.png'), pygame.image.load('images/Lframe4.png'), pygame.image.load(
    'images/Lframe5.png'), pygame.image.load('images/Lframe6.png'), pygame.image.load('images/Lframe7.png'), pygame.image.load('images/Lframe8.png'), pygame.image.load('images/Lframe9.png'), pygame.image.load('images/Lframe10.png'), pygame.image.load('images/Lframe11.png'), pygame.image.load('images/Lframe12.png'), pygame.image.load('images/Lframe13.png'), pygame.image.load(
    'images/Lframe14.png'), pygame.image.load('images/Lframe15.png'), pygame.image.load('images/Lframe16.png')]


walkRight2 = [pygame.image.load('images/Run_01.png'), pygame.image.load('images/Run_02.png'), pygame.image.load('images/Run_03.png'), pygame.image.load('images/Run_04.png'), pygame.image.load(
    'images/Run_05.png'), pygame.image.load('images/Run_06.png'), pygame.image.load('images/Run_07.png'), pygame.image.load('images/Run_08.png'), pygame.image.load('images/Run_09.png'), pygame.image.load('images/Run_10.png'), pygame.image.load('images/Run_11.png'), pygame.image.load('images/Run_12.png'), pygame.image.load('images/Run_13.png'), pygame.image.load(
    'images/Run_14.png'), pygame.image.load('images/Run_15.png'), pygame.image.load('images/Run_16.png')]

walkLeft2 = []

idle1 = pygame.image.load('images/idle1.png')
idle2_ = pygame.image.load('images/idle2.png')
idle2 = pygame.transform.scale(idle2_, (50, 50))
idle3_ = pygame.image.load('images/idle3.png')
idle3 = pygame.transform.scale(idle3_, (75, 75))


bg = pygame.image.load('images/background.png')
start_bg = pygame.image.load('images/start_bg.png')
end_bg = pygame.image.load('images/end_bg.png')



new_list1 = []
for i in walkRight1:
    i = pygame.transform.scale(i, (50, 50))
    new_list1.append(i)
walkRight1 = new_list1


new_list2 = []
for i in walkLeft1:
    i = pygame.transform.scale(i, (50, 50))
    new_list2.append(i)
walkLeft1 = new_list2

new_list3 = []
for i in walkRight2:
    i = pygame.transform.scale(i, (75, 75))
    new_list3.append(i)
walkRight2 = new_list3

new_list4 = []
for i in walkRight2:
    i = pygame.transform.flip(i, True, False)
    new_list4.append(i)
walkLeft2 = new_list4




fps = 120


class Player:
    IMG = soap_img

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 8
        self.radius = 20
        self.img = self.IMG
        self.tick_count = 0
        self.hitbox = None
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.width = 55
        self.height = 37


    def move(self):
        mouse = pygame.mouse.get_pos()
        self.x = mouse[0] - (self.width//2)
        self.y = mouse[1] - (self.height // 2)


    def draw(self, win):
        win.blit(self.img,(self.x, self.y))
        self.Hitbox(win)

    def Hitbox(self, win):
        self.hitbox = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0),
        #S                  self.hitbox, 2)





class Corona:
    IMG2 = corona_img
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.hitbox = None
        self.left = False
        self.right = True
        self.up = False
        self.down = True
        self.img = self.IMG2

    def draw(self, win):
        win.blit(self.img,(self.x, self.y))
        self.Hitbox(win)




    def Hitbox(self, win):
        self.hitbox = (self.x, self.y, self.width, self.height)
        # pygame.draw.rect(win, (0, 255, 0),
        #                  self.hitbox, 2)

    def collide(self, rect):
        # collision with the player:
        if self.hitbox[1] + 30 <= player.hitbox[1] <= self.hitbox[1]+self.hitbox[3]:
            if self.hitbox[0] < player.hitbox[0]+player.hitbox[2] and player.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                # print('collision down')
                player.y = self.y + self.height
                self.up = True
                self.down = False

        if self.hitbox[1]+10 >= player.hitbox[1] + player.hitbox[3] >= self.hitbox[1]:
            if self.hitbox[0] < player.hitbox[0]+player.hitbox[2] and player.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                # print('collision up')
                player.y = self.y - player.height
                self.down = True
                self.up = False

        if self.hitbox[0] + 25 >= player.hitbox[0]+player.hitbox[2] >= self.hitbox[0]:
            if self.hitbox[1]+self.hitbox[3] > player.hitbox[1] > self.hitbox[1] or self.hitbox[1] < player.hitbox[1]+player.hitbox[3] < self.hitbox[1]+self.hitbox[2]:
                # print("collision left")
                player.x = self.x - self.width
                self.right = True
                self.left = False

        if self.hitbox[0] + self.hitbox[2] >= player.hitbox[0] >= self.hitbox[0] + 15:
            if self.hitbox[1]+self.hitbox[3] > player.hitbox[1] > self.hitbox[1] or self.hitbox[1] < player.hitbox[1]+player.hitbox[3] < self.hitbox[1]+self.hitbox[3]:
                # print("collision right")
                player.x = self.x + self.width
                self.left = True
                self.right = False

        # collision with the map:
        if self.hitbox[0] <= 0:
            # print('9as l7ayt dyal liser')
            self.left = False
            self.right = True

        if self.hitbox[0] >= W-(self.width):
            # print('9as l7ayt dyal limen')
            self.left = True
            self.right = False

        if self.hitbox[1] <= 0:
            # print('9as l7ayt dyal lfo9')
            self.up = False
            self.down = True

        if self.hitbox[1] >= H-(self.height):
            # print('9as l7ayt dyal lt7t')
            self.up = True
            self.down = False


class People:
    def __init__(self,y):
        self.x = W//2-10
        self.y = y
        self.width = 20
        self.height = 50
        self.hitbox = None
        self.left = False
        self.right = False
        self.walkcount = 0
        self.collision = False
        self.dead = False

    def draw(self,win):
        self.move()
        self.Hitbox(win)



    def move(self):
        if self.walkcount + 1 >= 120:
            self.walkcount = 0

        if self.x == 0:
            self.right = True
            self.left = False
        if self.x == W - self.width:
            self.right = False
            self.left = True

        if self.right:
            win.blit(walkRight[self.walkcount//30], (self.x-25, self.y-18))
            self.walkcount += 1
            people_velL = 0
            people_velR = 1
            people.x += people_velR

        if self.left:
            win.blit(walkLeft[self.walkcount//30], (self.x-25, self.y-18))
            self.walkcount += 1
            people_velR = 0
            people_velL = 1
            people.x -= people_velL

        if self.dead:
            self.left = False
            self.right = False
            win.blit(idle1,(self.x-19, self.y-8))


    def Hitbox(self,win):
        self.hitbox = (self.x, self.y, self.width, self.height)
        # pygame.draw.rect(win, (255, 0, 0),
        #                   self.hitbox, 2)


    def collide(self,rect):
        if corona.hitbox[1] + corona.hitbox[3] >= self.hitbox[1]:
            if self.hitbox[0] <= corona.hitbox[0] <= self.hitbox[0]+self.hitbox[2] or self.hitbox[0]<corona.hitbox[0] + corona.hitbox[2]<self.hitbox[0]+self.hitbox[2]:
                self.collision = True
                self.dead = True



class People2:
    def __init__(self,y):
        self.x = W//2-10
        self.y = y
        self.width = 20
        self.height = 50
        self.hitbox = None
        self.left = False
        self.right = False
        self.walkcount = 0
        self.collision = False
        self.dead = False

    def draw(self,win):
        self.move()
        self.Hitbox(win)

    def move(self):
        if self.walkcount + 1 >= 120:
            self.walkcount = 0

        if self.x == 0:
            self.right = True
            self.left = False
        if self.x == W - self.width:
            self.right = False
            self.left = True

        if self.right:
            win.blit(walkRight1[self.walkcount//30], (self.x-15, self.y-2))
            self.walkcount += 1
            people_velL = 0
            people_velR = 1
            people2.x += people_velR

        if self.left:
            win.blit(walkLeft1[self.walkcount//30], (self.x-15, self.y-2))
            self.walkcount += 1
            people_velR = 0
            people_velL = 1
            people2.x -= people_velL

        if self.dead:
            self.left = False
            self.right = False
            win.blit(idle2,(self.x-19, self.y-8))



    def Hitbox(self,win):
        self.hitbox = (self.x, self.y, self.width, self.height)
        # pygame.draw.rect(win, (255, 0, 0),
        #                   self.hitbox, 2)


    def collide(self,rect):
        if corona.hitbox[1] + corona.hitbox[3] >= self.hitbox[1]:
            if self.hitbox[0] <= corona.hitbox[0] <= self.hitbox[0]+self.hitbox[2] or self.hitbox[0]<corona.hitbox[0] + corona.hitbox[2]<self.hitbox[0]+self.hitbox[2]:
                self.collision = True
                self.dead = True




class People3:
    def __init__(self,y):
        self.x = W-20
        self.y = y
        self.width = 20
        self.height = 50
        self.hitbox = None
        self.left = None
        self.right = None
        self.walkcount = 0
        self.collision = None
        self.dead = False

    def draw(self,win):
        self.move()
        self.Hitbox(win)

    def move(self):
        if self.walkcount + 1 >= 120:
            self.walkcount = 0

        if self.x == 0:
            self.right = True
            self.left = False
        if self.x == W - self.width:
            self.right = False
            self.left = True

        if self.right:
            win.blit(walkRight2[self.walkcount//30], (self.x-19, self.y-8))
            self.walkcount += 1
            people_velL = 0
            people_velR = 1
            people3.x += people_velR

        if self.left:
            win.blit(walkLeft2[self.walkcount//30], (self.x-19, self.y-8))
            self.walkcount += 1
            people_velR = 0
            people_velL = 1
            people3.x -= people_velL

        if self.dead:
            self.left = False
            self.right = False
            win.blit(idle3,(self.x-19, self.y-8))




    def Hitbox(self,win):
        self.hitbox = (self.x, self.y, self.width, self.height)
        # pygame.draw.rect(win, (255, 0, 0),
        #                   self.hitbox, 2)


    def collide(self,rect):
        if corona.hitbox[1] + corona.hitbox[3] >= self.hitbox[1]:
            if self.hitbox[0] <= corona.hitbox[0] <= self.hitbox[0]+self.hitbox[2] or self.hitbox[0]<corona.hitbox[0] + corona.hitbox[2]<self.hitbox[0]+self.hitbox[2]:
                self.collision = True
                self.dead = True




def start_screen(win):
    start = True
    clock = pygame.time.Clock()
    while start:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                start = False


        win.blit(start_bg,(0,0))
        pygame.display.update()


def end_screen(win,last_time,final_time,start_ticks2):
    last_time = round(final_time,1)
    end = True
    clock = pygame.time.Clock()
    while end:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
                pygame.quit()
                sys.exit()

        win.blit(end_bg,(0,0))
        Font = pygame.font.SysFont('lucidaconsole',20)
        survive_time = Font.render('You saved the world for : '+str(last_time)+'s', False, (255, 255, 255),(0,0,0))

        button3 = pygame.image.load('images/button4.png')
        button4 = pygame.image.load('images/button3.png')

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(mouse)
        if 275 > mouse[0] > 123 and 333 > mouse[1] > 270:
            win.blit(button3, (W/2-80, 270))
            if click[0] == 1:
                retry = True
                final_time = 0
                start_ticks = 0
                corona.x = random.randint(0,W)
                corona.y = 20
                people.right = True
                people.left = False
                people2.right = False
                people2.left = True
                people3.right = True
                people3.left = False
                people.x = W//2-10
                people2.x = W//2-10
                people3.x = W-20
                people.collision = False
                people2.collision = False
                people3.collision = False
                people.dead = False
                people2.dead = False
                people3.dead = False
                people.y = H - 67
                people2.y = H - 67
                people3.y = H - 67
                run = True
                main(win)

        else:
            win.blit(button4, (W/2-80, 270))

        win.blit(survive_time,(20,100))
        pygame.display.update()



def draw_window(win, Player, Corona,People,People2,People3,start_ticks):
    win.blit(bg,(0,0))
    player.draw(win)
    corona.draw(win)
    player.move()
    corona.collide(player.hitbox)
    people.draw(win)
    people.collide(corona.hitbox)
    people2.draw(win)
    people2.collide(corona.hitbox)
    people3.draw(win)
    people3.collide(corona.hitbox)
    seconds=round((pygame.time.get_ticks()-start_ticks)/1000,1)
    font = pygame.font.SysFont('lucidaconsole',20)
    timer = font.render('Time : '+str(seconds)+'s', False, (255, 255, 255),(0,0,0))
    win.blit(timer,(120,20))
    pygame.display.update()



start_screen(win)



player = Player(190, 500)
corona = Corona(random.randint(0,W), 100)
people = People(H - 67)
people2 = People2(H - 67)
people3 = People3(H - 67)


clock = pygame.time.Clock()


def main(win):
    people.right = True
    people.left = False
    people2.right = False
    people2.left = True
    people3.right = True
    people3.left = False
    corona_vel = 3
    run = True

    start_ticks=pygame.time.get_ticks()

    if not(retry):
        last_time = 0


    while run:
        clock.tick(fps)
        final_time=(pygame.time.get_ticks()-start_ticks)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if corona.up:
            corona.y -= corona_vel
            corona_vel += 0.0008

        if corona.down:
            corona.y += corona_vel
            corona_vel += 0.0008

        if corona.right:
            corona.x += corona_vel
            corona_vel += 0.0008

        if corona.left:
            corona.x -= corona_vel
            corona_vel += 0.0008


        if people.collision:
            people.y -= 2
            if people.y == 500:
                people.y += 3

        if people2.collision:
            people2.y -= 2
            if people2.y == 500:
                people2.y += 3

        if people3.collision:
            people3.y -= 2
            if people3.y == 500:
                people3.y += 3

        if people.dead and people2.dead and people3.dead:
            if people.y-people.height <0 and people2.y -people2.height <0 and people3.y<0-people3.height :
                corona.right = False
                corona.down = False
                corona.left = False
                corona.up = False
                corona.right = True
                corona.down = True
                corona_vel = 3
                start_ticks2 = start_ticks
                start_ticks = 0
                break


        draw_window(win, player, corona, People, People2,People3,start_ticks)
    last_time = final_time
    end_screen(win,last_time,final_time,start_ticks2)
main(win)
