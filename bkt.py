import pgzrun, random, pyautogui
WIDTH, HEIGHT=pyautogui.size()
TITLE= "bkt"

BKT=Actor("bucket.png")
BKT.pos= WIDTH//2, HEIGHT-100
def draw():
    screen.clear()
    BKT.draw()

def update():
    if keyboard.left:
        BKT.x=BKT.x-10
    if keyboard.right:
        BKT.x=BKT.x+10
    if BKT.x<0:
        BKT.x=WIDTH
    elif BKT.x>WIDTH:
        BKT.x=0
pgzrun.go()