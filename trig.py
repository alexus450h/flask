from tkinter import *
import time

root=Tk()
root.geometry("600x480")
class Megogo:
    def __init__(self,base_left_x,base_left_y,
                 base_right_x,base_right_y,
                 base_back_left_x, base_back_left_y,
                 base_back_right_x, base_back_right_y):
        self.base_left_x=base_left_x
        self.base_left_y = base_left_y

        self.base_right_x = base_back_right_x
        self.base_right_y = base_right_y

        self.base_back_left_x=base_back_left_x
        self.base_back_left_y = base_back_left_y

        self.base_back_right_x = base_back_right_x
        self.base_back_right_y = base_back_right_y

    def base_display(self):
         self.adv='MEGOGo'
         c.create_line(self.base_left_x,self.base_left_y,self.base_right_x,self.base_right_y,width='3',
                       fill='cyan')

         c.create_line(self.base_left_x, self.base_left_y, self.base_back_left_x, self.base_back_left_y, width='3',
                  fill='cyan')
         c.create_line(self.base_back_left_x,self.base_back_left_y,self.base_back_right_x, self.base_back_right_y,width='3',
                       fill='cyan')

         c.create_line(self.base_right_x,self.base_right_y,self.base_back_right_x,self.base_back_right_y,
                  width='3',
                  fill='cyan')
         for el in range(50):

             c.create_text(self.base_right_x-el,self.base_left_y-35,text=self.adv,font='Verdana 34',fill='#FFFFFF')
             time.sleep(0.1)
# c.create_line(0,0,600,240,fill='white')
# c.create_oval(0,0,100,100,fill='red')
# c.create_rectangle(100,100,590,290,fill="orange")
c = Canvas(root, width=600, height=400, bg="Navy")
c.pack()
r=Megogo(100,300,300,300,100,230,500,230)
r.base_display()
root.mainloop()