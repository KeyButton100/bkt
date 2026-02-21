import pgzrun, random, pyautogui
WIDTH, HEIGHT=pyautogui.size()
TITLE= "bkt"

mo=[]
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
    #screen.draw.rect(BKT.rect, "red")
    for i in mo:
        i.draw()

def update():
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
            mo.remove(i)
clock.schedule_interval(create_elements, 2)
pgzrun.go()