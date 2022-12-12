

# Designed for training to improve typing speed and efficiency
# SMAH_YAN ------------

# KEYS
# = boss key
# tab show Top
# enter continue game
# a-z  gaming
# 0526 cheeting code



import tkinter as tk
from PIL import Image,ImageTk
import random
import time



# 数据定义
screem_size = "1280x720" #分辨率

diff = 0
chance = 0.005
t = 0
v = 1.0 # 速度

Tops = []
Words = []

egg = "0526"
Wordslib = ['int','float','list','ifelse','while','import','def']
# ,'youwilldeadinthis'
# 名称申明
FPSS = [120,0,0,0,10]
user = ""
point = 0
keys = 0
show_config = True

# 游戏0 top1 point2
win_now = 10
t0 = 0
t1 = 0
Top_str = ""
egg_i = 0
a = {}
As = []
xy = [100,100]

# 主窗口申明
app= tk.Tk()
app.geometry("1280x720")
app.resizable(width=0,height=0)
app.title("飞行中")

# 游戏窗口
win_game = tk.Canvas(app, width=1280, height=720,bg = "black",cursor='heart')
win_game.pack()



# 照片声明
image_start = Image.open(r"lib/start.png")
image_start = ImageTk.PhotoImage(image_start)

def button1():
    button_end.destroy()
    button_start.destroy()
    restart()
def button2():
    button_end.destroy()
    button_start.destroy()
    global t0, win_now
    t0, win_now = 0.1, 2
    Top_loop()

button_start = tk.Button(win_game,text="开始游戏",width=14,height=3,bg='#7CCD7C',command=button1)
button_end = tk.Button(win_game,text="排行榜",width=14,height=3,bg='#7CCD7C',command=button2)
button_start.place(x = 880,y = 210)
button_end.place(x = 880,y = 330)

# 按键申明
def key(event):
    print(event)
    if win_now == 10:
        if event.keysym == 'a':
            xy[0] -=2
        if event.keysym == 'w':
            xy[1] -=2
        if event.keysym == 's':
            xy[1] +=2
        if event.keysym == 'd':
            xy[0] +=2
    if win_now == 0:
        for i in Words:
            if i['key'] == "":
                continue
            if i['key'][0] == event.keysym:
                i['key'] = i['key'][1:]
                global keys
                keys +=1
def key_return(event):
    global win_now
    if win_now == 0:
        check_words()
        return
    elif win_now == 1:
        win_now = 0
        game_loop()
    elif win_now == 2:
        win_now = 0
        restart()
def key_period(event):
    global show_config
    show_config = ~show_config
def key_tab(event):
    global win_now
    win_now = 1
    Top_sort()
    Top_loop()
def key_slash(event):
    print(event)
    if win_now == 2:
        user_win()
def key_egg(event):
    global egg_i
    print(event)
    if t>300:
        return
    if win_now != 0:
        return
    if event.keysym == egg[egg_i]:
        egg_i+=1
        if egg_i == 4:
            global t0, point
            t0 = time.time()-300
            point += 10
            egg_i = 0
    else:
        egg_i = 0
    print(egg_i)
def key_equal(event):
    #boss key
    app.withdraw()
    print(2)
    time.sleep(6)
    print(1)
    app.deiconify()


all = 'abcdefghijklmnopqrstuvwxyz'
for i in all:
    i = "<KeyPress-" + i + ">"
    win_game.bind(i,key)
win_game.bind("<KeyPress-Return>", key_return)
win_game.bind("<KeyPress-period>", key_period)
win_game.bind("<KeyPress-Tab>", key_tab)
win_game.bind("<KeyPress-equal>", key_equal)
numbers = "0123456789"
for i in numbers:
    i = "<KeyPress-" + i + ">"
    win_game.bind(i,key_egg)
# win_game.bind("<KeyPress-Escape>", key_excape)
win_game.bind("<KeyPress-slash>", key_slash)
win_game.focus_set()


# 基础函数封装
def clear(canvas):
    canvas.delete("all")

def show_text(canvas,x,y,text,color = "white",size = 32,dir = 'nw'):
    return canvas.create_text(x,y,text=text,fill=color,font =('微软雅黑',size,'bold'),width=0,anchor=dir)
def create_box(canvas,x1,y1,x2,y2,color = "black"):
    canvas.create_rectangle(x1,y1,x2,y2, fill=color, width = 0)

def show_bg():
    for i in range(0,720,160):
        create_box(win_game,0,i,1280,i+80,color='#181818')



# 组合功能封装

def show_words():
    for i in Words:
        i['x'] = i['x'] - v
        show_text(win_game,int(i['x']),i['y'],i['show'],color='red',size=50,dir='ne')
        show_text(win_game,int(i['x']),i['y'],i['key'],size=50,dir='ne')

def check_words():
    for i in Words:
        if i['key'] == '':
            Words.remove(i)
            global point
            point += 1
            return

def create_words():
    if random.random() > chance:
        return
    y = random.randint(1,13)
    if y > 8:
        y = y - 5
    y = y*80 + 10
    word = random.choice(Wordslib)
    a = {
        'x': 1280,
        'y': y,
        'key': word,
        'show': word
    }
    Words.append(a)

def change_diff():
    global diff, chance, v
    if t < 30:
        return
    diff = t//30
    chance = 0.005 + 0.001*diff
    v = 1.0 + 0.2*diff

def check_end():
    for i in Words:
        if i['x'] < (0 + len(i['show'])*20):
            global win_now
            win_now = 2
            Point_loop()


def show_FPS(canvas):
    FPSS[2] = time.time()
    FPSS[3] = FPSS[2] - FPSS[1]
    FPSS[0] = int(1/FPSS[3])
    FPSS[1] = time.time()
    show_text(canvas,10,10,"FPS",size=16)
    show_text(canvas,60,10,str(FPSS[0]),size=16)
    # print(FPSS)

def show_times():
    global t
    t1 = time.time()
    t = t1 - t0
    t = round(t,2)
    show_text(win_game,10,40,"Time",size=16)
    show_text(win_game,60,40,str(t),size=16)
def show_keys():
    show_text(win_game,10,100,"Keys",size=16)
    show_text(win_game,60,100,str(keys),size=16)
def show_point():
    show_text(win_game,10,70,"Point",size=16)
    show_text(win_game,60,70,str(point),size=16)
def show_diff():
    show_text(win_game,10,130,"Diff",size=16)
    show_text(win_game,60,130,str(diff),size=16)
def Point():
    show_text(win_game,640,40,str(point),size=60,dir='center')



# Top_loop 
def show_top():
    show_text(win_game,640,80,'Top',dir='center',size=140)# top10
    for i in range(len(Tops)):
        if i == 10:
            break
        show_text(win_game,150,160+80*i,str(i+1),size=60)
        show_text(win_game,260,160+80*i,Tops[i]['name'],size=60)
        show_text(win_game,550,160+80*i,Tops[i]['point'],size=60)
        show_text(win_game,930,160+80*i,Tops[i]['keys'],size=60)


def Top_read():
    global Tops, Top_str
    f = open('lib/Top.txt')
    for i in range(30):
        Top_str = Top_str + f.readline()
    Top_str = Top_str.split()
    while Top_str != []:
        a = {
            'name':Top_str[0],
            'point':int(Top_str[1]),
            'keys':int(Top_str[2])
        }
        Tops.append(a)
        Top_str = Top_str[3:]

def Top_sort():
    Tops.sort(key=lambda i: i['point'])
    Tops.reverse()

def Top_save():
    global As
    f = open('lib/Top.txt','w+')
    Top_sort()
    for i in Tops:
        As.append(i['name'])
        As.append(str(i['point']))
        As.append(str(i['keys']))
    for i in As:
        f.write(i)
        f.write('\n')
    As = 0
    f.close()

def add_top():
    print(point)
    global a
    a = {
        'name':user,
        'point':point,
        'keys':keys
    }
    Tops.append(a)
    Top_sort()
    Top_save()



# Point_loop 
def restart():
    global t0, t, diff, point, keys, v, Words, win_now
    t0 = time.time()
    t = 0
    chance = 0.005
    diff = 0
    v = 1.0
    point = 0
    keys = 0
    Words = []
    win_now = 0
    game_loop()


def start_loop():
    if t0 > 0 :
        return
    win_game.delete("all")
    win_game.create_image(0,0,anchor = "nw",image = image_start)
    show_text(win_game,x = xy[0],y = xy[1],text='ERROW///')
    win_game.update()
    win_game.after(10,start_loop)

def user_loop():
    win_game.forget()
    random.randint(0,500)

def Point_loop():
    win_game.delete('all')

    show_text(win_game,450,180,'Point',dir='center',size=80)
    show_text(win_game,820,180,str(point),dir='center',size=80)
    show_text(win_game,450,300,'keys',dir='center',size=80)
    show_text(win_game,820,300,str(keys),dir='center',size=80)
    show_text(win_game,420,450,'Restart',size= 28)
    show_text(win_game,420,500,'Top',size= 28)
    show_text(win_game,700,450,'Return',size= 28)
    show_text(win_game,700,500,'Key - / ',size= 28)


    app.update()
    app.after(0,Point_loop)

def Top_loop():
    win_game.delete('all')
    show_bg()
    show_top()
    app.update()
    app.after(0,Top_loop)

def game_loop():
    win_game.delete('all')
    show_bg()
    create_words()
    Point()
    show_words()
    change_diff()
    check_end()
    if show_config ==1:
        show_FPS(win_game)
        show_times()
        show_point()
        show_keys()
        show_diff()
    app.update()
    app.after(0,game_loop)



def user_win():

    window = tk.Tk()
    window.title("[XMeng] 输入用户名以加入排行榜")
    window.geometry("300x150")
    
    user_enter = tk.Entry(window)
    user_enter.place(x=150, y=40,anchor='center')
    def but():
        global user
        user = user_enter.get()
        print(user)
        add_top()
        window.destroy()

    button_end = tk.Button(window,text="确认",bg='#7CCD7C',command=but)
    button_end.place(x=150,y=90,anchor='center')


Top_read()
start_loop()
app.mainloop()


# 用户移动物体能力



