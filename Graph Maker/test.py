from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import messagebox
import csv

# import csv file for barchart ploting
def importbcsv():#bar chart
    bcsvpane = PanedWindow(width=300,height=150)
    bcsvpane.place(x=19,y=279)
    global filename
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    print(filename)
    f = filename.split("/")
    print(f)
    dot = filename.split(".")
    if dot[-1]!="csv":
        messagebox.showinfo("File Not Supported", "Please Select a csv File")

    else:
        fname = Label(window,text="Imported File: "+f[-1])
        fname.place(x=20,y=280)
        
        generate = Button(window,text = "Generate Graph",command = bgeneratefromcsv,relief=FLAT,bg="#5EABEF",fg="white")
        generate.place(x=20,y=310)

        save = Button(window,text = "Save Graph",command = savegraph,relief=FLAT,bg="#5EABEF",fg="white")
        save.place(x=130,y=310)

# import csv file for histogram ploting
def importhcsv():#Histogram
    hcsvpane = PanedWindow(width=300,height=150)
    hcsvpane.place(x=19,y=279)
    global filename
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    print(filename)
    f = filename.split("/")
    print(f)
    dot = filename.split(".")
    if dot[-1]!="csv":
        messagebox.showinfo("File Not Supported", "Please Select a csv File")
    else:
        fname = Label(window,text="Imported File: "+f[-1])
        fname.place(x=20,y=280)

        global ycsvh
        ycsvh = Label(window,text="Interval:")
        ycsvh.place(x=20,y=310)
        ycsvh = Entry(window, bd =5, relief=GROOVE)
        ycsvh.place(x=90,y=310)
        
        generate = Button(window,text = "Generate Graph",command = hgeneratefromcsv,relief=FLAT,bg="#5EABEF",fg="white")
        generate.place(x=20,y=340)

        save = Button(window,text = "Save Graph",command = savegraph,relief=FLAT,bg="#5EABEF",fg="white")
        save.place(x=130,y=340)

# import csv file for Pie Chart ploting
def importpcsv():#Pie Chart
    pcsvpane = PanedWindow(width=300,height=150)
    pcsvpane.place(x=19,y=279)
    global filename
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    print(filename)
    f = filename.split("/")
    print(f)
    dot = filename.split(".")
    if dot[-1]!="csv":
        messagebox.showinfo("File Not Supported", "Please Select a csv File")
    else:
        fname = Label(window,text="Imported File: "+f[-1])
        fname.place(x=20,y=280)

        generate = Button(window,text = "Generate Graph",command = pgeneratefromcsv,relief=FLAT,bg="#5EABEF",fg="white")
        generate.place(x=20,y=310)

        global save
        save = Button(window,text = "Save Graph",command = savegraph,relief=FLAT,bg="#5EABEF",fg="white")
        save.place(x=130,y=310)
     
def pgeneratefromcsv():
    if len(etitle.get()) ==0:
        messagebox.showinfo("Empty Text Fields", "Please Fill All Text Fields")
    else:
        reader = csv.reader(open(filename))
        xpcsv = []
        newxpcsv = []
        labelpcsv = []
        for raw in reader:
            xpcsv.append(raw[0])
            labelpcsv.append(raw[1])
        print(xpcsv,labelpcsv)

        for xele in xpcsv:
            xele = int(xele)
            newxpcsv.append(xele)

        print(newxpcsv,labelpcsv)
        plt.pie(newxpcsv, labels = labelpcsv,startangle=90, shadow = True, explode = (0, 0, 0.1, 0), radius = 1.2, autopct = '%1.1f%%')
        plt.legend()
        plt.title(etitle.get())
        plt.show()
        
def hgeneratefromcsv():
    if len(xetitle.get() or yetitle.get() or etitle.get()) ==0:
        messagebox.showinfo("Empty Text Fields", "Please Fill All Text Fields")
    else:
        reader = csv.reader(open(filename))
        xcsv = []
        newxcsv = []
        for raw in reader:
            print(raw[0])
            xcsv.append(raw[0])
        for xele in xcsv:
            xele = int(xele)
            newxcsv.append(xele)

        newycsvh = int(ycsvh.get())

        plt.hist(newxcsv, newycsvh, color = 'green')
        plt.xlabel(xetitle.get()) 
        plt.ylabel(yetitle.get()) 
        plt.title(etitle.get())
        plt.show()
        
    
def bgeneratefromcsv():
    if len(xetitle.get() or yetitle.get() or etitle.get()) ==0:
        messagebox.showinfo("Empty Text Fields", "Please Fill All Text Fields")
    else:
        reader = csv.reader(open(filename))
        xcsv = []
        ycsv = []
        newxcsv = []
        newycsv = []
        labelcvs = []
        for raw in reader:
            print(raw[0],raw[1],raw[2])
            xcsv.append(raw[0])
            ycsv.append(raw[1])
            labelcvs.append(raw[2])

        print(xcsv,ycsv)
        for xcsvele in xcsv:
            xcsvele = int(xcsvele)
            newxcsv.append(xcsvele)

        for ycsvele in ycsv:
            ycsvele = int(ycsvele)
            newycsv.append(ycsvele)

        print(newxcsv,newycsv,labelcvs)
        plt.bar(newxcsv, newycsv, tick_label = labelcvs, width = 0.8, color = ['red', 'green']) 
        plt.xlabel(xetitle.get()) 
        plt.ylabel(yetitle.get()) 
        plt.title(etitle.get())
        plt.show()
         
def mgenerate():
    if len(x.get() or y.get()or le.get()or xetitle.get() or yetitle.get() or etitle.get()) ==0:
        messagebox.showinfo("Empty Text Fields", "Please Fill All Text Fields")

    else:
        newxval = []
        newyval = []
        xval = x.get()
        xval = xval.split(",")
        #print(xval)
        for xele in xval:
            xele = int(xele)
            newxval.append(xele)
        print(newxval)
        yval = y.get()
        yval = yval.split(",")
        #print(yval)
        for yele in yval:
            yele = int(yele)
            newyval.append(yele)
        print(newyval)
        tick_label = le.get()
        tick_label = tick_label.split(",")
        plt.bar(newxval, newyval, tick_label = tick_label, width = 0.8, color = ['red', 'green']) 
        plt.xlabel(xetitle.get()) 
        plt.ylabel(yetitle.get()) 
        plt.title(etitle.get())
        plt.show()

def savegraph():
        file = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
        if file:
            plt.savefig(file)
            messagebox.showinfo("Saved", "Image Saved at \n"+file)
        
def hgenerate():
    if len(xh.get() or yh.get() or xetitle.get() or yetitle.get() or etitle.get()) ==0:
        messagebox.showinfo("Empty Text Fields", "Please Fill All Text Fields")
    else:
        newxval = []
        xval = xh.get()
        xval = xval.split(",")
        for xele in xval:
            xele = int(xele)
            newxval.append(xele)
        yhval = int(yh.get())
        #print(type(yh.get()),yhval)

        plt.hist(newxval, yhval, color = 'green')
        plt.xlabel(xetitle.get()) 
        plt.ylabel(yetitle.get()) 
        plt.title(etitle.get())
        plt.show()
    
def bmanually():
    bpane = PanedWindow(width=300,height=150)
    bpane.place(x=19,y=279)
    
    global x
    x = Label(window,text="X-Axis:",font='Helvetica 8 bold')
    x.place(x=20,y=280)
    x = Entry(window, bd =5, relief=GROOVE)
    x.place(x=70,y=280)

    global y
    y = Label(window,text="Y-Axis:",font='Helvetica 8 bold')
    y.place(x=20,y=310)
    y = Entry(window, bd =5, relief=GROOVE)
    y.place(x=70,y=310)

    global le
    ll = Label(window,text="Labels:",font='Helvetica 8 bold')
    ll.place(x=20,y=340)
    le = Entry(window, bd =5, relief=GROOVE)
    le.place(x=70,y=340)
    
    generate = Button(window,text = "Generate Graph",command = mgenerate,relief=FLAT,bg="#5EABEF",fg="white")
    generate.place(x=20,y=380)

    save = Button(window,text = "Save Graph",command = savegraph,relief=FLAT,bg="#5EABEF",fg="white")
    save.place(x=130,y=380)

def hmanually():
    hpane = PanedWindow(width=300,height=150)
    hpane.place(x=19,y=279)
    global xh
    xh = Label(window,text="Frequencies:",font='Helvetica 8 bold')
    xh.place(x=20,y=280)
    xh = Entry(window, bd =5, relief=GROOVE)
    xh.place(x=100,y=280)

    global yh
    yh = Label(window,text="Interval:",font='Helvetica 8 bold')
    yh.place(x=20,y=310)
    yh = Entry(window, bd =5, relief=GROOVE)
    yh.place(x=100,y=310)

    generate = Button(window,text = "Generate Graph",command = hgenerate,relief=FLAT,bg="#5EABEF",fg="white")
    generate.place(x=30,y=340)
    
    save = Button(window,text = "Save Graph",command = savegraph,relief=FLAT,bg="#5EABEF",fg="white")
    save.place(x=140,y=340)


def pgenerate():
    if len(xp.get() or yp.get())==0:
        messagebox.showinfo("Empty Text Fields", "Please Fill All Text Fields")
    else:
        newxpval = []
        newypval = []
        xpval = xp.get()
        xpval = xpval.split(",")
        #print(xval)
        for xpele in xpval:
            xpele = int(xpele)
            newxpval.append(xpele)
        print(newxpval)
        ypval = yp.get()
        ypval = ypval.split(",")
            #print(yval)
        for ypele in ypval:
            newypval.append(ypele)
        print(newypval)
        plt.pie(newxpval, labels = newypval,startangle=90, shadow = True, explode = (0, 0, 0.1, 0), radius = 1.2, autopct = '%1.1f%%')
        plt.legend() 
        plt.show() 

def pmanually():
    bpane = PanedWindow(width=300,height=150)
    bpane.place(x=19,y=279)
    global xp
    xp = Label(window,text="Portions:",font='Helvetica 8 bold')
    xp.place(x=20,y=280)
    xp = Entry(window, bd =5, relief=GROOVE)
    xp.place(x=100,y=280)

    global yp
    yp = Label(window,text="Labels:",font='Helvetica 8 bold')
    yp.place(x=20,y=310)
    yp = Entry(window, bd =5, relief=GROOVE)
    yp.place(x=100,y=310)

    generate = Button(window,text = "Generate Graph",command = pgenerate,relief=FLAT,bg="#5EABEF",fg="white")
    generate.place(x=30,y=340)
    
    save = Button(window,text = "Save Graph",command = savegraph,relief=FLAT,bg="#5EABEF",fg="white")
    save.place(x=140,y=340)

def barchart():
    try:
        xetitle['state']='normal'
        yetitle['state']='normal'
        btn1 = Button(window,text="Insert Manually",command=bmanually,relief=FLAT,bg="#5EABEF",fg="white")
        btn1.pack()
        btn1.place(x=20,y=250)

        btn2 = Button(window,text="Import CSV",command=importbcsv,relief=FLAT,bg="#5EABEF",fg="white")
        btn2.place(x=130,y=250)
    except:
        print("Something went wrong...")

def histogram():
    xetitle['state']='normal'
    yetitle['state']='normal'
    btn1 = Button(window,text="Insert Manually",command=hmanually,relief=FLAT,bg="#5EABEF",fg="white")
    btn1.pack()
    btn1.place(x=20,y=250)
    btn2 = Button(window,text="Import CSV",command=importhcsv,relief=FLAT,bg="#5EABEF",fg="white")
    btn2.place(x=130,y=250)

def piechart():
    xetitle['state']='disabled'
    yetitle['state']='disabled'
    btn1 = Button(window,text="Insert Manually",command=pmanually,relief=FLAT,bg="#5EABEF",fg="white")
    btn1.pack()
    btn1.place(x=20,y=250)
    btn2 = Button(window,text="Import CSV",command=importpcsv,relief=FLAT,bg="#5EABEF",fg="white")
    btn2.place(x=130,y=250)
 
if __name__ == '__main__':
    window = Tk()
    window.iconbitmap('graphs.ico')
    window.title("Graph Maker")

    pane = PanedWindow(bg="#5EABEF",width=300,height=60)
    pane.place(x=0,y=0)

    title = Label(window,text="Graph Maker",justify="center",font='Helvetica 18 bold',bg="#5EABEF",fg="white")
    title.place(x=90,y=10)

    lbimg = PhotoImage(file="315191-48.png")
    imglb = Label(window,image=lbimg,bg="#5EABEF")
    imglb.place(x=8,y=4)
    
    global etitle
    ltitle = Label(window,text="Enter Title of Graph:",font='Helvetica 8 bold')
    ltitle.place(x=20,y=70)#10 & 50
    etitle = Entry(window, bd =5, relief=GROOVE)
    etitle.place(x=140,y=70)
    
    global xetitle
    xtitle = Label(window,text="X-Axis Label:",font='Helvetica 8 bold')
    xtitle.place(x=20,y=100)
    xetitle = Entry(window, bd =5, relief=GROOVE)
    xetitle.place(x=140,y=100)
   
    global yetitle
    ytitle = Label(window,text="Y-Axis Label:",font='Helvetica 8 bold')
    ytitle.place(x=20,y=130)
    yetitle = Entry(window, bd =5, relief=GROOVE)
    yetitle.place(x=140,y=130)

    global var
    var = IntVar()
    R1 = Radiobutton(window, text="Bar Chart", variable=var, value=1,command=barchart,font='Helvetica 8 bold')
    R1.place(x=20,y=160)

    R2 = Radiobutton(window, text="Histogram", variable=var, value=2,command=histogram,font='Helvetica 8 bold')
    R2.place(x=20,y=190)

    R3 = Radiobutton(window, text="Pie Chart", variable=var, value=3,command=piechart,font='Helvetica 8 bold')
    R3.place(x=20,y=220)

    
    window.geometry("300x420")
    window.resizable(False, False)
    window.mainloop()
