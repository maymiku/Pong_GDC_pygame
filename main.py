import sys, pygame
import paddle
import ball

pygame.init()

pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
#Lets take a screen specification
SCR_WTH = 800
SCR_HTH = 500

FontSize = 150      #for the size of score displayed

paddle_offset = 15      #the gray space visible on screen ,i.e., the width of the boundaries
paddle_width = 20       #how long the paddle is

screen = pygame.display.set_mode((SCR_WTH, SCR_HTH))        #first load the screen of our game
#now generating game objects(2 paddles and 1 ball)
paddL = paddle.Paddle(paddle_offset,SCR_HTH/2 - 55, 110,paddle_width, (0, 154, 231, 1),screen, SCR_HTH,SCR_WTH, paddle_offset)
paddR = paddle.Paddle(SCR_WTH - paddle_offset - paddle_width,SCR_HTH/2 - 55, 110, paddle_width,(196, 11, 23, 1),screen, SCR_HTH, SCR_WTH,paddle_offset)
#lets refer from paddle code
ball = ball.Ball(10,SCR_WTH/2 , SCR_HTH/2,screen,SCR_HTH, SCR_WTH)
#lets refer form ball code

while 1:  #an infinite loop that only stops when we want to exit the game
    deltatime = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            #paddL.checkInp(event.key, True)
            paddR.checkInp(event.key, True) # here we pass the event key as we know that the key is pressed
            pass

        elif event.type == pygame.KEYUP:
            #paddL.checkInp(event.key, False)
            paddR.checkInp(event.key, False)
            pass


    pygame.draw.line(screen, (196, 196, 196, 0.12), (SCR_WTH/2,0),(SCR_WTH/2,SCR_HTH),paddle_offset)
    pygame.draw.rect(screen, (196, 196, 196, 0.12),pygame.Rect(0,0,SCR_WTH, SCR_HTH), paddle_offset)

    font = pygame.font.SysFont(None, FontSize)

    Lscore = font.render(str(paddL.score), True, (196, 196, 196, 0.12))
    screen.blit(Lscore, (SCR_WTH/4, SCR_HTH/2 - FontSize/2))

    Rscore = font.render(str(paddR.score), True, (196, 196, 196, 0.12))
    screen.blit(Rscore, (SCR_WTH * 3/4, SCR_HTH/2 - FontSize/2))

    paddL.activatebot(ball, True)                 #how do you activate the right side bot?
    paddR.activatebot(ball, False)

    ball.checkCollision(paddL.rect, paddR.rect, paddle_offset)
    paddL.draw(deltatime)
    paddR.draw(deltatime)
    ball.draw(deltatime, paddle_offset, paddL, paddR)

    pygame.display.flip()

    screen.fill((0,0,0))

pygame.quit()
    