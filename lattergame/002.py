# 问题 按照画布进行更替



import tkinter as tk
import time


# 数据定义
screem_size = "1280x720" #分辨率

Tops = [{
    'name':"Tom",
    'point':210
},
{
    'name':"zj",
    'point':1
},
{
    'name':"zj",
    'point':1
},
{
    'name':"zj",
    'point':1
},
{
    'name':"zj",
    'point':1
},
{
    'name':"zj",
    'point':1
}]

# 名称申明
FPS = [120,0,0,0,10]

class APP():
    """
    主程序
    """
    def __init__(self):
        """
        初始化
        """
        # 主窗口申明
        self.win= tk.Tk()
        self.win.geometry("1280x720")
        self.win.resizable(width=0,height=0)
        self.win.title("飞行中")

        # 画布申明
        self.canvas = tk.Canvas(self.win, width=1280, height=720,bg = "black")
        self.canvas.pack()

        # 按键申明
        def key(event):
            pass
        # self.canvas.bind("<KeyPress-a>", key)
        self.canvas.focus_set()


    # 清除字符
    def clear_text(self,x0,y0,l,color = "black"):
        x1 = x0+l
        y1 = y0+40
        self.canvas.create_rectangle(x0,y0,x1,y1, fill=color, width = 0)
    
    # 创建字符
    def show_text(self,x,y,text,color = "white",size = 32,dir = 'nw'):
        self.canvas.create_text(x,y,text=text,fill="white",font =('微软雅黑',size,'bold'),width=0,anchor=dir)



def core_FPS():
    FPS[2] = time.time()
    FPS[3] = FPS[2] - FPS[1]
    FPS[0] = int(1/FPS[3])
    FPS[1] = time.time()
def show_FPS():
    app.clear_text(10,10,150)
    app.show_text(10,10,"FPS"+str(FPS[0]))
def win_FPS():
    core_FPS()
    show_FPS()

def core_top():
    pass
def show_top():
    app.show_text(640,50,'Top 10',dir='center',size=60)# top10
    for i in range(len(Tops)):
        if i == 10:
            break
        app.show_text(150,120+50*i,str(i+1))
        app.show_text(250,120+50*i,Tops[i]['name'])
        app.show_text(700,120+50*i,Tops[i]['point'])







# 🌟🌟🌟窗口定义

def top_loop():

    win_FPS()
    app.win.update()
    top_loop()

def game_loop():
    """
    主游戏 页面
    """
    app.canvas.delete("all")
    win_FPS()
    show_top()

    app.win.update()
    app.win.after(0,game_loop)


app = APP()
game_loop()
app.win.mainloop()




