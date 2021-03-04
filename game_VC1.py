import tkinter as tk
# Create an empty window
root=tk.Tk()
# Set TK window size
root.geometry('600x600')
# Set the title
root.title('welcome gamer')
canvas=tk.Canvas()
# set variable
Pos_Player_X = 60   
Pos_Player_Y = 60   

Box_X = 180 
Box_Y = 180 

condition = True
Flag=""
Box=""
player=""
player_win=""
player_loose=""

Image_enemy1=Image_enemy2=Image_enemy3=Image_enemy4=Image_enemy5=Image_enemy6=Image_enemy7=Image_enemy8=Image_enemy9=Image_enemy10=""
# Display background in window
background = tk.PhotoImage(file="background.gif")
canvas.create_image(300,300,image=background )
# create text and image
Strat_game = tk.PhotoImage(file="strat_game.gif")
canvas.create_image(300,300,image=Strat_game )
canvas.create_text(300, 100, text='Press letter "S" to Start', font=('Time New Roman', 30), fill='black')
##Function 
# Display  grid and image
def grid():
    global Flag, Box, player,Pos_Player_Y, Pos_Player_X, Box_X, Box_Y,Move_Box,moveplayer,Image_enemy1,Image_enemy2,Image_enemy3,Image_enemy4,Image_enemy5,Image_enemy6,Image_enemy7,Image_enemy8,Image_enemy9,Image_enemy10
    for index in range(12):
                
        for i in range(12):
                    
            canvas.create_rectangle(60+(i*40),60+(index*40),100+(i*40),100+(index*40), fill="#AED6F1")


    Image_enemy1 = tk.PhotoImage(file="enemy.png")
    move_Image_enemy1=canvas.create_image(320,320,image=Image_enemy1 )
    Image_enemy2 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(400,400,image=Image_enemy2 )
    Image_enemy3 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(160,240,image=Image_enemy3 )
    Image_enemy4 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(120,440,image=Image_enemy4 )
    Image_enemy5 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(440,120,image=Image_enemy5 )
    Image_enemy6 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(480,240,image=Image_enemy6 )
    Image_enemy7 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(240,520,image=Image_enemy7 )
    Image_enemy8 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(280,440,image=Image_enemy8 )
    Image_enemy9 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(200,360,image=Image_enemy9 )
    Image_enemy10 = tk.PhotoImage(file="enemy.png")
    canvas.create_image(440,280,image=Image_enemy10 )

    Flag = tk.PhotoImage(file="Flag.png")
    canvas.create_image(440,440,image=Flag )

    Box = tk.PhotoImage(file="box.png")
    Move_Box =  canvas.create_image(240,240,image=Box )

    player = tk.PhotoImage(file="player.png")
    moveplayer=canvas.create_image(80,80,image=player )
    
    
    moveBox()
# display grid and image after 50 second
def ClickOnS(event):
    canvas.after(50, lambda:grid())
    
# MoveLeft
def moveLeft(event):
    global condition,Pos_Player_X, Box_X,Box_Y,player_loose,player_win
    if condition:
        if Pos_Player_X >= 70 and not(Pos_Player_Y==Box_Y and Pos_Player_X-40==Box_X and Box_X <70) :
            Pos_Player_X -= 40
            print("PosX: ", Pos_Player_X)
            
            if (Pos_Player_X==420 and Pos_Player_Y==260) or (Pos_Player_X==180 and Pos_Player_Y==340) or (Pos_Player_X==300 and Pos_Player_Y==300) or (Pos_Player_X==260 and Pos_Player_Y==420) or (Pos_Player_X==380 and Pos_Player_Y==380) or (Pos_Player_X==140 and Pos_Player_Y==220) or (Pos_Player_X==100 and Pos_Player_Y==420) or (Pos_Player_X==420 and Pos_Player_Y==100) or (Pos_Player_X==460 and Pos_Player_Y==220) or (Pos_Player_X==220 and Pos_Player_Y==500):
                player_loose= tk.PhotoImage(file="player_loose.png")
                canvas.create_image(300,300,image=player_loose)
                condition = False
            
            elif Pos_Player_X==Box_X and Pos_Player_Y==Box_Y and Box_X >= 70:
                Box_X -=40
                print("Box_X_L:", Box_X)
                if Box_X==420 and Box_Y==420:
                    
                    player_win = tk.PhotoImage(file="win.png")
                    canvas.create_image(300,300,image=player_win )
                    condition = False
                elif Box_X==60 or (Box_X==420 and Box_Y==260) or (Box_X==180 and Box_Y==340) or (Box_X==260 and Box_Y==420) or (Box_X==300 and Box_Y==300) or (Box_X==380 and Box_Y==380) or (Box_X==140 and Box_Y==220) or (Box_X==100 and Box_Y==420) or (Box_X==420 and Box_Y==100) or (Box_X==460 and Box_Y==220) or (Box_X==220 and Box_Y==500):
                    player_loose= tk.PhotoImage(file="player_loose.png")
                    canvas.create_image(300,300,image=player_loose)
                    condition = False
                    
                moveBox()
        
        Move_Player()

# MoveRight
def moveRight(event):
    global condition,Pos_Player_X,Box_X,Box_Y,player_win,player_loose
    if condition:
        if Pos_Player_X <= 490 and not(Pos_Player_Y==Box_Y and Pos_Player_X+40==Box_X and Box_X > 490) :
            Pos_Player_X += 40
            print("PosX: ", Pos_Player_X)

            if (Pos_Player_X==420 and Pos_Player_Y==260) or (Pos_Player_X==180 and Pos_Player_Y==340) or (Pos_Player_X==300 and Pos_Player_Y==300) or (Pos_Player_X==260 and Pos_Player_Y==420) or (Pos_Player_X==380 and Pos_Player_Y==380) or (Pos_Player_X==140 and Pos_Player_Y==220) or (Pos_Player_X==100 and Pos_Player_Y==420) or (Pos_Player_X==420 and Pos_Player_Y==100) or (Pos_Player_X==460 and Pos_Player_Y==220) or (Pos_Player_X==220 and Pos_Player_Y==500):
                player_loose= tk.PhotoImage(file="player_loose.png")
                canvas.create_image(300,300,image=player_loose)
                condition = False

            if Pos_Player_X==Box_X and Pos_Player_Y==Box_Y and Box_X <= 490:
                Box_X +=40
                print("Box_X_R:", Box_X)
                
                if Box_X==420 and Box_Y==420:
                    
                    player_win = tk.PhotoImage(file="win.png")
                    canvas.create_image(300,300,image=player_win )
                    condition = False

                elif Box_X==500 or (Box_X==420 and Box_Y==260) or (Box_X==180 and Box_Y==340) or (Box_X==260 and Box_Y==420) or (Box_X==300 and Box_Y==300) or (Box_X==380 and Box_Y==380) or (Box_X==140 and Box_Y==220) or (Box_X==100 and Box_Y==420) or (Box_X==420 and Box_Y==100) or (Box_X==460 and Box_Y==220) or (Box_X==220 and Box_Y==500):
                    player_loose= tk.PhotoImage(file="player_loose.png")
                    canvas.create_image(300,300,image=player_loose)
                    condition = False
                    
                moveBox()
        
        Move_Player()

# MoveUp
def moveUp(event):
    global condition,Pos_Player_Y, Box_Y,Box_X,player_loose,player_win
    if condition:
        if Pos_Player_Y >= 70 and not(Pos_Player_Y-40==Box_Y and Pos_Player_X==Box_X and Box_Y < 70) :
            Pos_Player_Y -= 40
            print("PosY: ", Pos_Player_Y)

            if (Pos_Player_X==420 and Pos_Player_Y==260) or (Pos_Player_X==180 and Pos_Player_Y==340) or (Pos_Player_X==300 and Pos_Player_Y==300) or (Pos_Player_X==260 and Pos_Player_Y==420) or (Pos_Player_X==380 and Pos_Player_Y==380) or (Pos_Player_X==140 and Pos_Player_Y==220) or (Pos_Player_X==100 and Pos_Player_Y==420) or (Pos_Player_X==420 and Pos_Player_Y==100) or (Pos_Player_X==460 and Pos_Player_Y==220) or (Pos_Player_X==220 and Pos_Player_Y==500):
                player_loose= tk.PhotoImage(file="player_loose.png")
                canvas.create_image(300,300,image=player_loose)
                condition = False
            
            elif Pos_Player_Y==Box_Y and Pos_Player_X==Box_X and Box_Y >= 70:
                Box_Y -=40
                print("Box_Y_U:", Box_Y)

            
                if Box_X==420 and Box_Y==420:
                
                    player_win = tk.PhotoImage(file="win.png")
                    canvas.create_image(300,300,image=player_win )
                    condition = False
                elif Box_Y==60 or (Box_X==420 and Box_Y==260) or (Box_X==180 and Box_Y==340) or (Box_X==260 and Box_Y==420) or (Box_X==300 and Box_Y==300) or (Box_X==380 and Box_Y==380) or (Box_X==140 and Box_Y==220) or (Box_X==100 and Box_Y==420) or (Box_X==420 and Box_Y==100) or (Box_X==460 and Box_Y==220) or (Box_X==220 and Box_Y==500):
                    player_loose= tk.PhotoImage(file="player_loose.png")
                    canvas.create_image(300,300,image=player_loose)
                    condition = False
                moveBox()
        
        Move_Player()

# MoveDown
def moveDown(event):
    global condition,Pos_Player_Y,Box_Y,Box_X,player_win,player_loose
    if condition:
        if Pos_Player_Y <= 490 and not(Pos_Player_Y+40==Box_Y and Pos_Player_X==Box_X and Box_Y > 490) :
            Pos_Player_Y += 40
            print("PosY: ", Pos_Player_Y)

            if (Pos_Player_X==420 and Pos_Player_Y==260) or (Pos_Player_X==180 and Pos_Player_Y==340) or (Pos_Player_X==300 and Pos_Player_Y==300) or (Pos_Player_X==260 and Pos_Player_Y==420) or (Pos_Player_X==380 and Pos_Player_Y==380) or (Pos_Player_X==140 and Pos_Player_Y==220) or (Pos_Player_X==100 and Pos_Player_Y==420) or (Pos_Player_X==420 and Pos_Player_Y==100) or (Pos_Player_X==460 and Pos_Player_Y==220) or (Pos_Player_X==220 and Pos_Player_Y==500):
                player_loose= tk.PhotoImage(file="player_loose.png")
                canvas.create_image(300,300,image=player_loose)
                condition = False
                
            
            elif Pos_Player_Y==Box_Y and Pos_Player_X==Box_X and Box_Y <= 490:
                Box_Y +=40
                print("Box_Y_D:", Box_Y)
                if Box_X==420 and Box_Y==420:
                    player_win = tk.PhotoImage(file="win.png")
                    canvas.create_image(300,300,image=player_win )
                    condition = False
                elif Box_Y==500 or (Box_X==420 and Box_Y==260) or (Box_X==180 and Box_Y==340) or (Box_X==260 and Box_Y==420) or (Box_X==300 and Box_Y==300) or (Box_X==380 and Box_Y==380) or (Box_X==140 and Box_Y==220) or (Box_X==100 and Box_Y==420) or (Box_X==420 and Box_Y==100) or (Box_X==460 and Box_Y==220) or (Box_X==220 and Box_Y==500):
                    player_loose= tk.PhotoImage(file="player_loose.png")
                    canvas.create_image(300,300,image=player_loose)
                    condition = False
                moveBox()
        
        Move_Player()

# Move Player
def Move_Player():
    
    canvas.moveto(moveplayer, Pos_Player_X, Pos_Player_Y)

# Move Box
def moveBox():
    
    canvas.moveto(Move_Box,Box_X,Box_Y)
    
    Move_Player()

      
root.bind("<S>", ClickOnS)
root.bind("<Right>" , moveRight)
root.bind("<Left>" , moveLeft)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)


root.resizable(False,False)
canvas.pack()
canvas.pack(expand=True,fill='both')
root.mainloop()