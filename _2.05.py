from tkinter import *
import time, random, pygame 

class Ball():
#создаеи объект
    def __init__(self, canvas, platform, color):
        self.canvas = canvas
        self.platform = platform
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.dir = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(self.dir)
        self.y = -1
        self.touch_bottom = False
# проверяем сталкивается ли мяча с платформой
    def touch_platform(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform.rect)
        if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                return True
        return False
 #рисуем что-то типо мяча
    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        pos = self.canvas.coords(self.oval)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= 400:
            self.touch_bottom = True
        if self.touch_platform(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 500:
            self.x = -3
# создаем класс платформы, чтобы был
class Platform():
#создаеи объект 2.0
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)
 # движение платформы влево
    def left(self, event):
        self.x = -4
# движение платформы вправо
    def right(self, event):
        self.x = 4
# отрисовываем платформу
    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
        pos=self.canvas.coords(self.rect)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= 500:
            self.x = 0

# создаем главное окно для расстрела 
window = Tk()
window.title("Аркада")
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)
#создание окна
canvas = Canvas(window, width=500, height=400)
canvas.pack()
#создаем цвета для "мяча" и "платформы"
platform = Platform(canvas, 'red')
ball = Ball(canvas, platform, 'pink')

while True:
    if ball.touch_bottom == False:
        ball.draw()
        platform.draw()
    else:
        break

    window.update()
    time.sleep(0.01)

window.mainloop()