# PONG 2.0 (single player)
# Abhilash Harpale 10/12/2010

from config_pong import *

class Ball:
    def __init__(self,x,y,radius,color,vx,vy):
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
        self.vx=vx
        self.vy=vy

    def move(self):
        self.x+=self.vx
        self.y+=self.vy

    def show(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

    def check_hit(self,surface,bat_lower,bat_upper):
        if surface.get_at((self.x,self.y+self.radius-1))!=self.color:
            self.vy*=-1
            self.vx=((self.x-bat_lower.x)*X_VELOCITY_SCALE)+(bat_lower.vel*bat_lower.direction*FRICTION_2)
            hit_sound.play()
        elif surface.get_at((self.x,self.y-self.radius+1))!=self.color:
            self.vy*=-1
            self.vx=((self.x-bat_upper.x)*X_VELOCITY_SCALE)+(bat_upper.vel*bat_upper.direction*FRICTION_2)
            hit_sound.play()
        elif self.x<self.radius or self.x>WIDTH-self.radius:
            self.vx*=-1
            hit_sound.play()
        else:
            pass
        
    def is_out(self):
        if self.y<self.radius+GAP or self.y>HEIGHT-(self.radius+GAP):
            return True
        else :
            return False

class Bat:
    def __init__(self,length,thickness,color,x,y,vel):
        self.length=length
        self.thickness=thickness
        self.color=color
        self.x=x
        self.y=y
        self.vel=vel
        self.is_left_pressed=False
        self.is_right_pressed=False

    def show(self,screen):
         pygame.draw.rect(screen,self.color,(self.x-self.length/2,self.y-self.thickness/2,self.length,self.thickness))

    def check_key_status(self,event,left_control,right_control):
        if event.type==pygame.KEYDOWN and event.key==left_control:
            self.is_left_pressed=True
        elif event.type==pygame.KEYUP and event.key==left_control:
            self.is_left_pressed=False
        elif event.type==pygame.KEYDOWN and event.key==right_control:
            self.is_right_pressed=True
        elif event.type==pygame.KEYUP and event.key==right_control:
            self.is_right_pressed=False
        else:
            pass

    def move_bat(self):
        if self.is_left_pressed and self.x>(self.length/2):
            self.direction=-1
            self.x+=(self.direction*self.vel)
        elif self.is_right_pressed and self.x<WIDTH-(self.length/2):
            self.direction=1
            self.x+=(self.direction*self.vel)
        elif self.is_left_pressed==self.is_right_pressed:
            self.direction=0
        else:
            pass
        

class Comp_bat(Bat):
    def move_bat(self,ball):
        if self.x>ball.x and self.x>(self.length/2):
            self.direction=-1
            self.x+=(self.direction*self.vel)
        elif self.x<ball.x and self.x<WIDTH-(self.length/2):
            self.direction=1
            self.x+=(self.direction*self.vel)
        elif self.x==ball.x:
            self.direction=0
        else:
            pass
        
        

#MAIN
screen=pygame.display.set_mode((WIDTH,HEIGHT))
running=1
clock=pygame.time.Clock()
ball=Ball(WIDTH/2,HEIGHT/2,RADIUS,RED,0,Y_SPEED)
bat_lower=Bat(LENGTH,THICKNESS,BLUE,WIDTH/2,HEIGHT-GAP,PLAYER_BAT_SPEED)
bat_upper=Comp_bat(LENGTH,THICKNESS,GREEN,WIDTH/2,GAP,DIFFICULTY)
while running:
    screen.fill(WHITE)
    ball.show(screen)
    bat_lower.show(screen)
    bat_upper.show(screen)
    pygame.display.flip()
    
    ball.check_hit(screen,bat_lower,bat_upper)
    ball.move()
    bat_lower.move_bat()
    bat_upper.move_bat(ball)
    
    event=pygame.event.poll()
    bat_lower.check_key_status(event,pygame.K_LEFT,pygame.K_RIGHT)
    if event.type==pygame.QUIT or ball.is_out() :
          running=0
    else:
        pass
    clock.tick(SPEED)

        
    

    
        

    
            
