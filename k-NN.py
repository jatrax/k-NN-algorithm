from tkinter import *

ARR = []
SIZE = 1000
K = 5

class Nouns:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
        clr = type
        if clr == 0:
            canvas.create_oval(x-5, y-5, x+5 , y+5 , fill="lightgreen")
        if clr == 1:
            canvas.create_oval(x-5, y-5, x+5 , y+5 , fill="red")
        if clr == 2:
            canvas.create_rectangle(x-5, y-5, x+5 , y+5 , fill="lightgreen")
        if clr == 3:
            canvas.create_rectangle(x-5, y-5, x+5 , y+5 , fill="red")
        ARR.append([x,y,type])

def normalize(x,max,min):
    return (x-min)/(max-min)

import math
def new_node(x,y):
    values = []
    x_max = max([val[0] for val in ARR])
    x_min = min([val[0] for val in ARR])
    y_max = max([val[1] for val in ARR])
    y_min = min([val[1] for val in ARR])
    print(x_min)
    for i in ARR:
        x0 = normalize(i[0],x_max,x_min)
        x1 = normalize(x,x_max,x_min)
        y0 = normalize(i[1],y_max,y_min)
        y1 = normalize(y,y_max,y_min)
        range_to_data = math.pow(x0-x1,2) + math.pow(y0-y1,2) #karelerinin toplamını al
        range_to_data = math.sqrt(range_to_data) #kökünü al
        values.append([range_to_data,i[2],i[0],i[1]])
    values.sort()
    tmp = 0
    for i in range(0,K):
        if values[i][1] == 0:
            tmp -= 1
        elif values[i][1] == 1:
            tmp +=1
        canvas.create_line(x,y,values[i][2],values[i][3])
    if tmp < 0:
        Nouns(x,y,2)
    else:
        Nouns(x,y,3)

root = Tk()
root.config(width=SIZE,height=SIZE)
canvas = Canvas(root, width=SIZE, height=SIZE)
canvas.pack()

Nouns(111,111,0)
Nouns(12,133,0)
Nouns(300,20,0)
Nouns(888,50,0)
Nouns(555,200,0)
Nouns(700,200,0)
Nouns(588,288,0)
Nouns(451,451,0)
Nouns(488,288,0)
Nouns(900,155,0)
Nouns(451,411,0)
Nouns(200,411,0)
Nouns(45,411,0)
Nouns(799,477,0)
Nouns(488,400,0)
Nouns(444,491,1)
Nouns(333,877,1)
Nouns(222,910,1)
Nouns(740,910,1)
Nouns(581,844,1)
Nouns(699,788,1)
Nouns(777,641,1)
Nouns(210,580,1)
Nouns(240,680,1)
Nouns(155,550,1)
Nouns(15,580,1)

new_node(600,500)

root.mainloop()