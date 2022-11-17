

import tkinter as tk
from PIL import Image,ImageTk


# 数据定义
screem_size = "1280x720" #分辨率
# 640,360
FPS = 100 # 帧数





# 初始化数据
image_win = Image.open(r"winner.png")
image_zhujiangL = Image.open(r"zhujiangL.png")
image_zhujiangR = Image.open(r"zhujiangR.png")
image_phone = Image.open(r"phone.png")


phones = []


# 数据自动运算
screem_size1 = screem_size.split('x') # 运算中...
width = int(screem_size1[0]) #宽
height = int(screem_size1[1]) #高

MS = int(1000/FPS) #刷新时间/ms


Position = 50 #人物位置

Hall = 50 #大厅内宽度
Side = 50 #屏幕移动宽度
Max_move = Side + Hall + Side #总可移动宽度

witdh_bg = 1920 #背景宽度
Move_bg = witdh_bg - width #背景可移动宽度
hall_pre = Move_bg/Hall #1position/大厅移动
side_pre = width/Side/2 #1position/人物移动
# 两侧走像素 move = 像素
# hall走像素 move = 像素

dir = 0
dir_show = 0

class APP():
    """
    主程序
    """
    def __init__(self):
        """
        初始化
        """
        self.win= tk.Tk()
        self.win.geometry("1280x720")
        self.win.resizable(width=0,height=0)
        self.win.title("本游戏没有任何一个渚江受到伤害！")

        self.canvas = tk.Canvas(self.win, width=width, height=height)
        self.canvas.pack()

        def key(event):
            global dir
            if event.keysym == "a":
                dir = 1
            elif event.keysym == "d":
                dir = 2
        self.canvas.bind("<KeyPress-a>", key)
        self.canvas.bind("<KeyPress-d>", key)
        self.canvas.focus_set()



        global bg
        bg = ImageTk.PhotoImage(image_win)
        bgi = self.canvas.create_image(0,0,anchor = "nw",image = bg)

        global image_porsonR
        image_porsonR = ImageTk.PhotoImage(image_zhujiangR)
        global image_porsonL
        image_porsonL = ImageTk.PhotoImage(image_zhujiangL)
        porsoni = self.canvas.create_image(640,320,anchor = "center",image = bg)

        global image_phone
        image_phone = ImageTk.PhotoImage(image_phone)


    def show_bg(self,x,y):
        bgi = self.canvas.create_image(x,y,anchor = "nw",image = bg)
    def show_porson(self,x = 640,y = 320, dir = 2):
        if dir == 2:
            porsoni = self.canvas.create_image(x,y,anchor = "center",image = image_porsonR)
        else:
            porsoni = self.canvas.create_image(x,y,anchor = "center",image = image_porsonL)
    def show_phone(self,x,y):
        phonei = self.canvas.create_image(x,y,anchor = "nw",image = bg)
        phones.append(phonei)
    def change_bg(photo):
        bg = ImageTk.PhotoImage(photo)


def show_move():
    """
    显示 人物/背景 移动
    """
    global Position
    if 0 <= Position < Side:
        app.show_bg(0,0)
        app.show_porson(Position * side_pre, 320, dir_show)
    elif Hall + Side >= Position >= Side:
        app.show_bg(hall_pre * (Side - Position), 0)
        app.show_porson(dir=dir_show)
    elif Max_move >= Position > Hall + Side:
        app.show_bg(- Hall * hall_pre, 0)
        app.show_porson(640 + (Position-Side-Hall) * side_pre, 320, dir_show)
    else:
        Position = 0
    print(Position)


def move():
    """
    运算 人物/背景 移动
    """
    global dir, dir_show, Position
    if dir == 0:
        return
    elif dir == 1:
        dir_show = dir
        if Position > 0:
            Position = Position - 2
    elif dir == 2:
        dir_show = dir
        if Position < Max_move:
            Position = Position + 2
    dir = 0

def create_phone():
    phone = {
        'v': 2,
        'end': 150,
        'now': 1
    }

def show_phone():
    pass




def core():
    """
    运算 核心
    """
    move()

def show():
    app.canvas.delete("all")
    """
    显示 核心
    """
    show_move()

def game_loop():
    """
    主游戏循环
    """
    app.win.update()
    core()
    show()
    # global Position
    # Position = Position + 1
    app.win.after(MS, game_loop)





# core    

app = APP()
game_loop()
app.win.mainloop()







# 窗口
#     游戏
#         显示
#             boss bar 
#             人物血量
#             怪物
#             人物光环
#             经验条
#             侧边栏
#                 等级
#                 通告
#                 任务
#         运算
#             boss血量 
#             个人血量
#             获得物品/经验/金钱

#         功能
#             隐藏/复现游戏
#     装备 E
#         显示
#             物品 数量     两侧显示
#             放上面 物品介绍
#             排序
#             个人属性
        

#     兑换商人 R
#         显示
#             兑换
#             点击兑换

#     设置 exc 
#         功能
#             退出保存
#             修改功能键


