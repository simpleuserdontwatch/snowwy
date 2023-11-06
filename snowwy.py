from tkinter import *
import random as rand
root = Tk()
root.title('Snowwy')
C = Canvas(bg='black',highlightthickness=-1,width=200,height=200)
C.pack(expand=True, fill=BOTH)
root.wait_visibility(root)
snowObj = []
def tick():
    for c,i in enumerate(snowObj,start=0):
        C.move(i, rand.randint(-5,5), 5)
        if C.coords(i)[1] > C.winfo_height():
            del snowObj[c]
            C.delete(i)
    root.after(25,tick)
def snow():
    x = rand.randint(10,root.winfo_width()-10)
    snowObj.append(C.create_rectangle(x,10,x+5,5,fill='white',outline='white'))
    root.after(rand.randint(300,400),snow)
snow()
root.after(100,snow)
tick()
root.attributes('-transparentcolor','black')
root.attributes('-fullscreen',True)
root.attributes('-topmost', True)
root.mainloop()
