# Version 2 of pong. In this version a ball spawns in a random location in the window moving in a random direction. Two paddles also spawn , the ball bounces off of the front of the paddles and the walls. The game terminates upon closing the window or upon either player reaching a score of 11 otherwise it will continue indefinitely.

import pygame, random, time
# main function where we call all other functions, start the game loop, quit pygame and clean up the window. Inside we create a game object, display surface, and start the game loop by calling the play method on the game object. There is also a set caption with the title of the game.
def main():
    pygame.init()
    size =(500,400)
    surface=pygame.display.set_mode(size)
    pygame.display.set_caption('Pong v2')
    game = Game(surface)
    game.play()
    #center_ball=self.ball.center
    pygame.quit()
    #return size
# This is where we define the class game    
class Game():
    # an object in this class represents a complete game
    
    # here we initialize a game. self is the game that is initialized surface is the display window surface object we also set default values for continuing the game and closing the window. we also define what fps we are running the game at, and define the velocity color position and radius of the ball
    def __init__(self,surface):
        
        # defining surface, fps, background color
        self.surface=surface
        self.FPS=120
        self.bg_color=pygame.Color('black')
        screen_width = surface.get_width()
        screen_height = surface.get_height()
        
        # defining ball attributes
        ball_radius=10
        ball_pos = [250, 
                    200]
        ball_color=pygame.Color('white')
        ball_velocity=[2,1]
        self.ball=Ball(ball_pos,ball_radius,ball_color,ball_velocity,surface)
        
        # defining paddle attributes
        
        rect_left=[50,450]
        rect_top=225
        rect_height=60
        rect_width=10
        self.Paddle1=Rect(rect_left[0],rect_top,rect_width,rect_height,surface)
        self.Paddle2=Rect(rect_left[1],rect_top,rect_width,rect_height,surface)

        
        self.game_Clock=pygame.time.Clock()
        self.close_clicked=False
        self.continue_game=True
        self.score1=0
        self.score2=0
        self.frame_counter=0
        #return ball_radius
        
    def play(self):
        # game is played until player clicks close and until score1/score2 reaches 11
        #self.draw()
        while not self.close_clicked:
            self.draw()
            self.handle_events()
            #while self.score1 <11 and self.score2 <11:  
                         
                #self.handle_events()
            
                #self.draw()
 
                
            # if nothing sets this to false the game will continue to update
            if self.continue_game==True:
                self.update()
            if self.continue_game==False:
                
                self.draw()
                #self.handle_events()
                
            self.game_Clock.tick(self.FPS)
    # score is drawn onto the screen (unimportant this is just playing with a feature for the next version), we define color font background etc of the score message and update score upon points being scored
    def draw_score(self):
        font_color = pygame.Color("white")
        font_bg    = pygame.Color("black")
        font       = pygame.font.SysFont("arial", 18)
        text_img   = font.render("Score for Player 1: " + str(self.score1) + '                                 Score for Player 2: ' + str(self.score2), True, font_color, font_bg)     
        text_pos   = (0,0)
        self.surface.blit(text_img, text_pos)
        
    # ball, surface, score, and two paddles are drawn, pygame also updates this drawing once per frame    
    def draw(self):
        self.surface.fill(self.bg_color)
        
        self.draw_score()

        self.Paddle1.draw()
        self.Paddle2.draw()
        
        self.ball.draw()
        
        
        pygame.display.update()
    # score value set to default of 0 we tell ball to move and add 1 to frame counter upon each update. update game object for the next frame 
    def update(self):
        self.ball.move()
        self.score=0
        
        
        get_self_center=self.ball.move()

        if get_self_center[0] - self.ball.radius <=0:
            self.score2+=1
            
        if get_self_center[0] + self.ball.radius>=500:
            self.score1+=1
            
        # check if ball is in either paddle if it is it is bounced off
        if self.Paddle1.collide_point(get_self_center[0]+self.ball.radius,get_self_center[1]+self.ball.radius)and self.ball.velocity[0]<0 or self.Paddle2.collide_point(get_self_center[0]+self.ball.radius,get_self_center[1]+self.ball.radius)and self.ball.velocity[0]>0:
            self.ball.bounce()

        

    
                    
            
        self.frame_counter+=self.frame_counter+1
        self.decide_continue()
    # check if we have reached a score of 11    
    def decide_continue(self):
        if self.score1==11 or self.score2==11:
            self.continue_game=False
        

            
            
        
        
        
 
        
    
        
        
    # here we setup an event loop and figure out if the action to end the game has been done
    def handle_events(self):
        events=pygame.event.get()
        for event in events:
            if event.type== pygame.QUIT:
                self.close_clicked=True
        
        # set keys to move each paddle, paddles aren't bounded by borders in case people feel like trolling
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]: self.Paddle1.move_ip(0,-2)
        if pressed[pygame.K_s]: self.Paddle1.move_ip(0,  2)
        if pressed[pygame.K_UP]: self.Paddle2.move_ip(0, -2)
        if pressed[pygame.K_DOWN]: self.Paddle2.move_ip(0,  2)
        
        

# user defined class ball            
class Ball:
    # self is the ball to intialize. color/center/radius are defined for the ball that is initialized
    def __init__(self,center,radius,color,velocity,surface):
        self.center=center
        self.radius=radius
        self.color=color
        self.velocity=velocity
        self.surface=surface
    # screen size is determined and edge of ball is checked that it is not touching the edge. if it is touching the edge it bounces and reverses velocity   
    def move(self):
        screen_width=self.surface.get_width()
        screen_height=self.surface.get_height()
        screen_size=(screen_width,screen_height)
        for i in range(0,len(self.center)):
            #print(self.center)
            self.center[i]+=self.velocity[i]
            if (self.center[i]<=0 + self.radius or self.center[i]>=screen_size[i] - self.radius):
                self.velocity[i]=-self.velocity[i]
        return self.center
    # simple method if we hit something we bounce off
    def bounce(self):
        for i in range(0,1):
        
            self.velocity[i]=-self.velocity[i]
    
        
    # ball is drawn            
    def draw(self):
        self.circle=pygame.draw.circle(self.surface,self.color,self.center,self.radius)
        
        
class Rect:
    
    def __init__(self,left,top,width,height,surface):
        # self is the rect to intialize and we put the rect on that surface
        self.surface=surface
        self.rect=pygame.Rect(left,top,width,height)
       
    # draw rect to surface   
    def draw(self):
        pygame.draw.rect(self.surface,pygame.Color('red'),self.rect)
    # checks if we collide    
    def collide_point(self,x,y):
        #get_self_center=self.ball.move()
        if self.rect.collidepoint(x,y):
            return True
        else:
            return False
    def move_ip(self,x,y):
       
        self.rect.move_ip(x,y)    
            
        #print(self.move())
        
        


        

        
            
            
        

            
            
        
        
           
    
        

        
        
        
main()