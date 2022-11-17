

import tkinter as tk
from PIL import Image,ImageTk
import time

# 基础设定
screem_size = "1280x720" #分辨率
FPS = 600 # 帧数

# 初始化 图片 数据
image_win = Image.open(r"winner.png")
image_zhujiangL = Image.open(r"zhujiangL.png")
image_zhujiangR = Image.open(r"zhujiangR.png")
image_phone = Image.open(r"phone.png")

# 数据库
phones = [] # 手机数据组

porson = { # 人物数据组
    # 位置
    'x': 320.0,
    'dir': 2,
    
    # 属性
    'v' : 6.0,
    'exp': 0,
    'lv': 0
}

# ----------

# 暂存数据 （系统内修改）
dir = 0

# 数据自动运算
width = 1280 #宽
height = 720 #高

MS = int(1000/FPS) #刷新时间/ms


# ----------

class APP():
    def __init__(self):
        """
        初始化
        """
        # 主窗口 初始化
        self.win= tk.Tk()
        self.win.geometry("1280x720")
        self.win.resizable(width=0,height=0)
        self.win.title("本游戏没有任何一个渚江受到伤害！")

        # 主画布 初始化
        self.canvas = tk.Canvas(self.win, width=width, height=height)
        self.canvas.pack()

        # 图片 初始化
        global bg
        bg = ImageTk.PhotoImage(image_win)
        bgi = self.canvas.create_image(0,0,anchor = "nw",image = bg)

        global image_porsonR
        image_porsonR = ImageTk.PhotoImage(image_zhujiangR)
        global image_porsonL
        image_porsonL = ImageTk.PhotoImage(image_zhujiangL)

        global image_phone
        image_phone = ImageTk.PhotoImage(image_phone)

        # 按键绑定 初始化 
        def key(event): 
            global dir
            if event.keysym == "a":
                dir = 1
            elif event.keysym == "d":
                dir = 2
        self.canvas.bind("<KeyPress-a>", key)
        self.canvas.bind("<KeyPress-d>", key)
        self.canvas.focus_set()




    # 显示功能
    def show_bg(self,x=0,y=0):
        """ 背景 """
        bgi = self.canvas.create_image(x,y,anchor = "nw",image = bg)
    def show_porson(self,x = 640,y = 320):
        """ 人物 """
        if porson['dir'] == 1:
            porsoni = self.canvas.create_image(x,y,anchor = "center",image = image_porsonL)
        elif porson['dir'] == 2:
            porsoni = self.canvas.create_image(x,y,anchor = "center",image = image_porsonR)
    def show_phone(self,x,y):
        """ 手机 """
        phonei = self.canvas.create_image(x,y,anchor = "nw",image = bg)
        phones.append(phonei)
    def show_text(self,x,y,text,color = "black",size = 32,place = "nw"):
        """ 文字 """
        self.canvas.create_text(x,y,text=text, fill = color, anchor = place, font =('微软雅黑',size,'bold'))


def core_porson():
    """
    人物相关 所有核心运算
    """
    global dir
    if dir == 0:
        return
    elif dir == 1:
        porson['x'] -= porson['v']
    elif dir == 2:
        porson['x'] += porson['v']
    porson['dir'] = dir
    dir = 0 
def show_porson():
    """
    人物相关 所有显示
    """
    app.show_porson(x = int(porson['x']))

def core_exp():
    pass
def show_exp():
    app.show_text(640, 680, "50/100", size=30, place="center")

def core_phone():
    pass
def show_phone():
    pass



def core():
    """
    运算 核心
    """
    core_porson()

def show():
    """
    显示 核心
    """
    app.canvas.delete("all")
    app.show_bg()
    

    show_porson()
    show_exp()



def game_loop():
    """
    主游戏 页面
    """
    core()
    show()
    app.win.update()
    print(porson['x'])
    app.win.after(MS, game_loop)


app = APP()
game_loop()
app.win.mainloop()



