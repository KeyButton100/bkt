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
element=["money", "banpeel", "coin"]
def create_elements():
    A=Actor(random.choice(element))
    A.pos= random.randint(0, WIDTH-50), 0
    mo.append(A)
def draw():
    screen.blit("space.jpg", (0, 0))
    BKT.draw()
    if gamestate=="start":
        message="Press space to start \n Control the bucket with left & right arrow keys \n Collect money, avoid trash \n You have 3 lives \n If you touch trash, you lose a life"
        screen.draw.text(message, center=(WIDTH//2, HEIGHT//2))

    screen.draw.text("Score:"+str(score), (50, 50))
    screen.draw.text("Life:"+str(life), (50, 70))
    for i in mo:
        i.draw()

def update():
    global score, life, gamestate
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
                score+=5
            elif i.image=="coin":
                score+=10
            elif i.image=="banpeel":
                life-=1
            mo.remove(i)
    if life==0:
        gamestate="end"
clock.schedule_interval(create_elements, 2)
pgzrun.go()