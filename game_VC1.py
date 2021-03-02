import tkinter as tk

root=tk.Tk()
root.geometry('600x600')
root.title('welcome gamer')
canvas=tk.Canvas()
PosX = 60
PosY = 60


Box_X = 180
Box_Y = 180

Flag=""
Box=""
player=""
player_win=""
player_loose=""
Image_enemy1=Image_enemy2=Image_enemy3=Image_enemy4=Image_enemy5=""
# oval=""
# Move_Box=""
background = tk.PhotoImage(file="background.gif")
canvas.create_image(300,300,image=background )

Strat_game = tk.PhotoImage(file="strat_game.gif")
canvas.create_image(300,300,image=Strat_game )
canvas.create_text(300, 100, text='Press letter "s" to Start', font=('Time New Roman', 30), fill='black')
def grid():
    global Flag, Box, player,PosY, PosX, Box_X, Box_Y,Move_Box,oval,Image_enemy1,Image_enemy2,Image_enemy3,Image_enemy4,Image_enemy5
    for index in range(12):
                
        for i in range(12):
                    
            canvas.create_rectangle(60+(i*40),60+(index*40),100+(i*40),100+(index*40), fill="#AED6F1")


    Image_enemy1 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(320,320,image=Image_enemy1 )
    Image_enemy2 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(360,400,image=Image_enemy2 )
    Image_enemy3 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(160,240,image=Image_enemy3 )
    Image_enemy4 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(120,440,image=Image_enemy4 )
    Image_enemy5 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(440,120,image=Image_enemy5 )

    Flag = tk.PhotoImage(file="Flag.png")
    canvas.create_image(440,440,image=Flag )

    Box = tk.PhotoImage(file="box.png")
    Move_Box =  canvas.create_image(240,240,image=Box )

    player = tk.PhotoImage(file="player.png")
    oval=canvas.create_image(80,80,image=player )
    
    
    moveBox()
def ClickOnEnter(event):
    canvas.after(50, lambda:grid())
    

def moveLeft(event):
    global PosX, Box_X,Box_Y,player_loose,player_win
    if PosX >= 70 and not(PosY==Box_Y and PosX-40==Box_X and Box_X <70) :
        PosX -= 40
        print("PosX: ", PosX)
        
        if PosX==Box_X and PosY==Box_Y and Box_X >= 70:
            Box_X -=40
            print("Box_X_L:", Box_X)
            if Box_X==420 and Box_Y==420:
                
                player_win = tk.PhotoImage(file="win2.png")
                canvas.create_image(300,300,image=player_win )
            elif Box_X==60:
                player_loose= tk.PhotoImage(file="player_loose.png")
                canvas.create_image(300,300,image=player_loose)
            moveBox()
    
    moveCircle()
def moveRight(event):
    global PosX,Box_X,Box_Y,player_win,player_loose
    if PosX <= 490 and not(PosY==Box_Y and PosX+40==Box_X and Box_X > 490) :
        PosX += 40
        print("PosX: ", PosX)
        if PosX==Box_X and PosY==Box_Y and Box_X <= 490:
            Box_X +=40
            print("Box_X_R:", Box_X)
            
            if Box_X==420 and Box_Y==420:
                
                player_win = tk.PhotoImage(file="win2.png")
                canvas.create_image(300,300,image=player_win )
            elif Box_X==500:
                player_loose= tk.PhotoImage(file="player_loose.png")
                canvas.create_image(300,300,image=player_loose)
                
            moveBox()
    
    moveCircle()
def moveUp(event):
    global PosY, Box_Y,Box_X,player_loose,player_win
    if PosY >= 70 and not(PosY-40==Box_Y and PosX==Box_X and Box_Y < 70) :
        PosY -= 40
        print("PosY: ", PosY)
        if PosY==Box_Y and PosX==Box_X and Box_Y >= 70:
            Box_Y -=40
            print("Box_Y_U:", Box_Y)
            if Box_X==420 and Box_Y==420:
               
                player_win = tk.PhotoImage(file="win2.png")
                canvas.create_image(300,300,image=player_win )
            elif Box_Y==60:
                player_loose= tk.PhotoImage(file="player_loose.png")
                canvas.create_image(300,300,image=player_loose)
            moveBox()
    
    moveCircle()
def moveDown(event):
    global PosY,Box_Y,Box_X,player_win,player_loose
    if PosY <= 490 and not(PosY+40==Box_Y and PosX==Box_X and Box_Y > 490) :
        PosY += 40
        print("PosY: ", PosY)
        if PosY==Box_Y and PosX==Box_X and Box_Y <= 490:
            Box_Y +=40
            print("Box_Y_D:", Box_Y)
            if Box_X==420 and Box_Y==420:
               
                player_win = tk.PhotoImage(file="win2.png")
                canvas.create_image(300,300,image=player_win )
            elif Box_Y==500:
                player_loose= tk.PhotoImage(file="player_loose.png")
                canvas.create_image(300,300,image=player_loose)
            moveBox()
    
    moveCircle()
def moveCircle():
    canvas.moveto(oval, PosX, PosY)

def moveBox():
    canvas.moveto(Move_Box,Box_X,Box_Y)
    
    moveCircle()

root.bind("<s>", ClickOnEnter)
root.bind("<Right>" , moveRight)
root.bind("<Left>" , moveLeft)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)


root.resizable(False,False)
canvas.pack()
canvas.pack(expand=True,fill='both')
root.mainloop()