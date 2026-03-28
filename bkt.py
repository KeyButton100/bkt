import pgzrun, random, pyautogui
WIDTH, HEIGHT=pyautogui.size()
TITLE= "bkt"

score=0
life=3
mo=[]
gamestate="start"

BKT=Actor("bucket.png")
BKT.scale=0.5
BKT.pos= WIDTH//2, HEIGHT-100
music.play("sunsaimenu.wav")
#sunsai
music.set_volume(0.7)
element=["money", "banpeel", "coin"]
def create_elements():
    if gamestate=="play":
        A=Actor(random.choice(element))
        A.pos= random.randint(0, WIDTH-50), 0
        mo.append(A)
def draw():
    screen.blit("space.jpg", (0, 0))
    BKT.draw()
    if gamestate=="start":
        message="Press space to start \n Control the bucket with left & right arrow keys \n Collect money, avoid trash \n You have 3 lives \n If you touch trash, you lose a life"
        screen.draw.text(message, center=(WIDTH//2, HEIGHT//2))
    elif gamestate=="play":
        screen.draw.text("Score:"+str(score), (50, 50), fontsize= 40)
        screen.draw.text("Life:"+str(life), (50, 70), fontsize= 40)
        for i in mo:
            i.draw()
    else:
        screen.draw.text("Game End \n Press space to play again", center=(WIDTH/2, HEIGHT/2), fontsize= 40)


def update():
    global score, life, gamestate
    if keyboard.space and gamestate != "play":
        gamestate="play"
        score=0
        life=3
        BKT.pos= WIDTH//2, HEIGHT-100
    if gamestate=="play":
        if keyboard.left:
            BKT.x=BKT.x-10
        if keyboard.right:
            BKT.x=BKT.x+10
        if BKT.x<0:
            BKT.x=WIDTH
        elif BKT.x>WIDTH:
            BKT.x=0
        for i in mo:
            i.y+=10
            if i.colliderect(BKT):
                if i.image=="money":
                    sounds.point.play()
                    #troy
                    score+=5
                elif i.image=="coin":
                    sounds.coin.play()
                    #simonadams
                    score+=10
                elif i.image=="banpeel":
 #         not work          sounds.trash.mp3.play()
                    #raclure
                    life-=1
                mo.remove(i)
        if life==0:
            gamestate="stop"
clock.schedule_interval(create_elements, 2)
pgzrun.go()