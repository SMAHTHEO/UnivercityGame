# 问题 ： 太卡，运行后出问题

import tkinter as tk
from PIL import Image,ImageTk
import time


# 数据定义
screem_size = "1280x720" #分辨率





# 名称申明
FPS = 0
time1 = 0
time2 = 0

# 主程序

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
        self.win.title("飞行中")

        # 主画布 初始化
        self.canvas = tk.Canvas(self.win, width=1280, height=720,bg="black",bd=0)
        self.canvas.pack()

        # 按键绑定 初始化 
        def key(event): 
            pass
        # self.canvas.bind("<KeyPress-a>", key)
        self.canvas.focus_set()


    
    # 显示功能
    def show_text(self,x,y,text,color = "white",size = 32,place = "nw"):
        """ 文字 """
        self.canvas.create_text(x,y,text=text, fill = color, anchor = place, font =('微软雅黑',size,'bold'),width=0)
    def clear_text(self,x,y,l,color = "black"):
        self.canvas.create_rectangle(x, y, x+l, y+40,fill=color,width=0)



def show_FPS():
    # app.canvas.create_rectangle(10,10,160,50,fill="black",width=0)
    # app.show_text(10,10,"FPS "+FPS)
    pass

def core_FPS():
    global time1,time0,time2,FPS
    time2 = time.time()
    time0 = time2 - time1
    FPS = str(int(1/time0))
    # if int(FPS) > 120:
    #     time.sleep(0.005)
    time1 = time.time()



a = 100
clear = 0

def game_loop():
    core_FPS()


    show_FPS()
    global a
    app.clear_text(a,100,200)
    app.show_text(a,100,"[XMeng]")
    
    a = a + 1
    app.win.update()
    global clear
    # print(a)
    clear = clear + 1
    if clear == 100:
        app.canvas.delete("all")
        print("\nn\n\n\n\n\nn\n")
    app.win.after(1000,game_loop())
app = APP()

game_loop()

app.win.mainloop()

