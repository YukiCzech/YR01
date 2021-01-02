import tkinter as tk
from tkinter import ttk
from tkinter import *
import csv
LARGE_MAIN_FONT= ("Courier", 40, "bold")
LARGE_FONT= ("Courier", 40)
BUTTON_FONT= ("Arial", 20, "bold")




class SeaofBTCapp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        self.geometry("500x500")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        self.winfo_toplevel().title("Yuki Robotics")
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Main menu", font=LARGE_MAIN_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Motion", font=BUTTON_FONT,
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Programing", font=BUTTON_FONT,
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
   
        


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Motion", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to main menu", font=BUTTON_FONT,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        def print_valuea(vara):
            print("a="+vara)
        def print_valueb(varb):
            print("b="+varb)
        def print_valuec(varc):
            print("c="+varc)
        def print_valued(vard):
            print("d="+vard)
        def print_valuee(vare):
            print("e="+vare)
        def print_valuef(varf):
            print("f="+varf)
        vara = DoubleVar()
        varb = DoubleVar()
        varc = DoubleVar()
        vard = DoubleVar()
        vare = DoubleVar()
        varf = DoubleVar()
        
        a = Scale(self, variable = vara, orient=HORIZONTAL, length=275, to=275, command=print_valuea, background='orange')
        a.pack()

        b = Scale(self, variable = varb, orient=HORIZONTAL, length=275, to=275, command=print_valueb, background='red')
        b.pack()

        c = Scale(self, variable = varc, orient=HORIZONTAL, length=275, to=275, command=print_valuec, background='blue')
        c.pack()

        d = Scale(self, variable = vard, orient=HORIZONTAL, length=275, to=275, command=print_valued, background='yellow')
        d.pack()

        e = Scale(self, variable = vare, orient=HORIZONTAL, length=275, to=275, command=print_valuee, background='green')
        e.pack()

        f = Scale(self, variable = varf, orient=HORIZONTAL, length=275, to=275, command=print_valuef, background='white')
        f.pack()
        
       


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Programing", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to main menu", font=BUTTON_FONT,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        def save():
            vara1=str(vara.get())
            print("a=" + vara1)
            varb1=str(varb.get())
            print("b=" + varb1)
            varc1=str(varc.get())
            print("c=" + varc1)
            vard1=str(vard.get())
            print("d=" + vard1)
            vare1=str(vare.get())
            print("e=" + vare1)
            varf1=str(varf.get())
            print("f=" + varf1)
            step=w.get()
            f = open('data.csv', 'a', newline="")
            with f:
    
                writer = csv.writer(f, delimiter=',')
                writer.writerow([step, vara1, varb1, varc1, vard1, vare1, varf1]) 
        vara = DoubleVar()
        varb = DoubleVar()
        varc = DoubleVar()
        vard = DoubleVar()
        vare = DoubleVar()
        varf = DoubleVar()
        
        def read():
            with open('data.csv') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')

                for row in readCSV:
                    step = row[0]
                    a = row[1]
                    b = row[2]
                    c = row[3]
                    d = row[4]
                    e = row[5]
                    f = row[6]
                    print("step" + step + "\n" +
                          "a= " + a +"\n" +
                          "b= " + b +"\n" +
                          "c= " + c +"\n" +
                          "d= " + d +"\n" +
                          "e= " + e +"\n" +
                          "f= " + f +"\n")  
        w = Spinbox(self, from_=0, to=999)
        w.pack()
        
        a = Scale(self, variable = vara, orient=HORIZONTAL, length=275, to=275, background='orange')
        a.pack()

        b = Scale(self, variable = varb, orient=HORIZONTAL, length=275, to=275, background='red')
        b.pack()

        c = Scale(self, variable = varc, orient=HORIZONTAL, length=275, to=275, background='blue')
        c.pack()

        d = Scale(self, variable = vard, orient=HORIZONTAL, length=275, to=275, background='yellow')
        d.pack()

        e = Scale(self, variable = vare, orient=HORIZONTAL, length=275, to=275, background='green')
        e.pack()

        f = Scale(self, variable = varf, orient=HORIZONTAL, length=275, to=275, background='white')
        f.pack()

        button2 = tk.Button(self, text="Save", font=BUTTON_FONT,
                            command=save)
        button2.pack()
        button3 = tk.Button(self, text="Read", font=BUTTON_FONT,
                            command=read)
        button3.pack()
        


app = SeaofBTCapp()
app.mainloop()
