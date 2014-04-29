# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 10
PAD_HEIGHT = 90
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos=HEIGHT/2
paddle2_pos=HEIGHT/2
paddle1_vel=0
paddle2_vel=0
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[random.randrange(2,8),random.randrange(2,6)];
score2=score1=0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel,hits # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]

    if(direction==True):
        ball_vel=[random.randrange(2,8),random.randrange(2, 6)]
    else:
        ball_vel=[-random.randrange(2,8),random.randrange(2, 6)]
      

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    ch=random.randrange(0,2)
    if(ch==1):
        spawn_ball(False)
    else:
        spawn_ball(True)
    #paddle values
    paddle2_pos=HEIGHT/2
    paddle1_pos=HEIGHT/2
    paddle1_vel=paddle2_vel=0;
    #scores
    score1=score2=0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,hits
 
    # update paddle's vertical position, keep paddle on the screen
    paddle1pv=paddle1_pos+paddle1_vel 
    if (paddle1pv<HALF_PAD_HEIGHT):
        paddle1pv=HALF_PAD_HEIGHT
    elif (paddle1pv>HEIGHT-HALF_PAD_HEIGHT-1):    
        paddle1pv=HEIGHT-1-HALF_PAD_HEIGHT
    #paddle2
    paddle2pv=paddle2_pos+paddle2_vel
    if (paddle2pv<HALF_PAD_HEIGHT):
        paddle2pv=HALF_PAD_HEIGHT
    elif (paddle2pv>HEIGHT-HALF_PAD_HEIGHT-1):
        paddle2pv=HEIGHT-1-HALF_PAD_HEIGHT
    paddle1_pos=paddle1pv
    paddle2_pos=paddle2pv     
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos+HALF_PAD_HEIGHT], [PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT ], [PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT],[0,paddle1_pos-HALF_PAD_HEIGHT]], 3, "Blue", "White")
    canvas.draw_polygon([[WIDTH-1, paddle2_pos+HALF_PAD_HEIGHT], [WIDTH-1-PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT ], [WIDTH-1-PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT],[WIDTH-1,paddle2_pos-HALF_PAD_HEIGHT]], 3, "Blue", "White")
    # update ball
    paddle1pv=ball_pos[0]+ball_vel[0]
    paddle2pv=ball_pos[1]+ball_vel[1]
   
    if(paddle2pv<BALL_RADIUS):
        paddle2pv=BALL_RADIUS
        ball_vel[1]=-ball_vel[1]
    elif(paddle2pv>HEIGHT-1-BALL_RADIUS):
        paddle2pv=HEIGHT-1-BALL_RADIUS
        ball_vel[1]=-ball_vel[1]
    if(paddle1pv<BALL_RADIUS+PAD_WIDTH):
       if(paddle2pv<paddle1_pos+HALF_PAD_HEIGHT and paddle2pv > paddle1_pos-HALF_PAD_HEIGHT):
            paddle1pv=BALL_RADIUS+PAD_WIDTH+5
            ball_vel[0]=-ball_vel[0]*1.1
            ball_vel[1]=ball_vel[1]*1.1
       else:
            score2=score2+1
            ch=random.randrange(0,2)
            if(ch==0):
                spawn_ball(False)
                spawn_ball(True)
            return;    
    elif(paddle1pv> WIDTH-1-BALL_RADIUS-PAD_WIDTH) :  
        if(paddle2pv<paddle2_pos+HALF_PAD_HEIGHT and paddle2pv > paddle2_pos-HALF_PAD_HEIGHT):
            paddle1pv=WIDTH-1-BALL_RADIUS-PAD_WIDTH-5
            ball_vel[0]=-ball_vel[0]*1.1
            ball_vel[1]=ball_vel[1]*1.1
        else:
            score1=score1+1;
            ch=random.randrange(0,2)
            if(ch==0):
                spawn_ball(False)
            else:
                spawn_ball(True)
            return;        
   
    ball_pos[0]=paddle1pv
    ball_pos[1]=paddle2pv    
    
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"Red","White")
    canvas.draw_text(str(score1),[WIDTH/4,80],40,"White")
    canvas.draw_text(str(score2),[WIDTH-WIDTH/4,80],40,"White")
    
               
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    temp=10
    #user1 paddle
    if (key==simplegui.KEY_MAP["w"]):
        paddle1_vel=-temp
    if (key==simplegui.KEY_MAP["S"]):
        paddle1_vel=temp
    #user2Paddle
    if (key==simplegui.KEY_MAP["up"]):
        paddle2_vel=-temp
    if (key==simplegui.KEY_MAP["down"]):
        paddle2_vel=temp    
def keyup(key):
    global paddle1_vel, paddle2_vel
    #player1
    if(key==simplegui.KEY_MAP["W"]):
        paddle1_vel=0
    if(key==simplegui.KEY_MAP["S"]):
        paddle1_vel=0
    #player2
    if(key==simplegui.KEY_MAP["up"]):
        paddle2_vel=0
    if(key==simplegui.KEY_MAP["down"]):
        paddle2_vel=0
def pause():
    global ball_pos, ball_vel,hits
    ball_pos=[WIDTH/2,HEIGHT/2]
    ball_vel=[0,0];
def resume():
    global ball_pos, ball_vel,hits
    ball_pos=[WIDTH/2,HEIGHT/2]
    ball_vel=[random.randrange(2,8),random.randrange(2, 6)];
    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('Black')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game",new_game, 150)
frame.add_button("Pause",pause, 150)
frame.add_button("Resume",resume,150)

# start frame
new_game()
frame.start()
