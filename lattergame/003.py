

import tkinter as tk
import random
import time

# 数据定义
screem_size = "1280x720" #分辨率

diff = 0
chance = 0.90
t = 0
v = 1.0 # 速度

Tops = [{
    'name':"Tom",
    'point':210,
    'keys':1290
},
{
    'name':"zj",
    'point':1,
    'keys':129
}]
Words = [{
    'x':1280,
    'y':250,
    'key':'hello',
    'show':'hello'
}]

Wordslib = ['int','float','list','ifelse','while']
# 名称申明
FPSS = [120,0,0,0,10]
point = 0
keys = 0
show_config = True
show_config = ~show_config
win_now = 0
t0 = 0
t1 = 0



# 主窗口申明
app= tk.Tk()
app.geometry("1280x720")
app.resizable(width=0,height=0)
app.title("飞行中")

# 游戏窗口
# 80*9
win_game = tk.Canvas(app, width=1280, height=720,bg = "black",cursor='heart')
win_game.pack()

# 按键申明
def key(event):
    print(event)
    for i in Words:
        if i['key'] == "":
            continue
        if i['key'][0] == event.keysym:
            i['key'] = i['key'][1:]
            global keys
            keys +=1
def key_return(event):
    check_words()
def key_period(event):
    global show_config
    show_config = ~show_config
def key_tab(event):
    global win_now
    win_now = 1
    Top_loop()
def key_excape(event):
    global win_now
    if win_now == 0:
        pass
    else:
        win_now = 0
        game_loop()
all = 'abcdefghijklmnopqrstuvwxyz'
for i in all:
    i = "<KeyPress-" + i + ">"
    win_game.bind(i,key)
win_game.bind("<KeyPress-Return>", key_return)
win_game.bind("<KeyPress-period>", key_period)
win_game.bind("<KeyPress-Tab>", key_tab)
win_game.bind("<KeyPress-Escape>", key_excape)

# win_game.bind("<KeyPress-period>", key_period)
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



# 组合功能封装
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

def change_diff():
    global diff, chance, v
    if t < 30:
        return
    diff = t//30
    chance = 0.005 + 0.001*diff
    v = 1.0 + 0.2*diff


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
    if show_config ==1:
        show_FPS(win_game)
        show_times()
        show_point()
        show_keys()
        show_diff()
    app.update()
    app.after(0,game_loop)

t0 = time.time()
game_loop()
app.mainloop()





# 登陆窗口

# 简单介绍窗口 

# 设置窗口 

# 开始窗口

# 暂停
