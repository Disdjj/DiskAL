import re
import matplotlib

matplotlib.use('TkAgg')

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

from matplotlib.figure import Figure

import tkinter as tk

class myDiskShow(tk.Tk):

    def fcfs(self):
        if len(self.fcfs_s) == 0:
            return 0

        self.nowindex_fcfs = self.fcfs_s.pop(0)
        return self.nowindex_fcfs

    def sstf(self):

        if len(self.sstf_s) == 0:
            return 0

        index = self.nowindex_sstf
        self.sstf_s.sort(key=lambda x: int(abs(x - index)))
        self.nowindex_sstf = self.sstf_s.pop(0)
        return self.nowindex_sstf

    def scan(self):
        if len(self.scan_s) == 0:
            return 0

        index = self.nowindex_scan
        dire = self.dire

        if dire:
            self.scan_s.sort(key=lambda x: 1000 + abs(index - x) if x < index else x)
            if self.scan_s[0] < index:

                self.nowindex_scan = self.scan_s.pop(0)
                self.dire = False

            else:
                self.nowindex_scan = self.scan_s.pop(0)


        else:
            self.scan_s.sort(key=lambda x: 1000 + abs(index - x) if x > index else -1 * x)
            if self.scan_s[0] > index:
                self.nowindex_scan = self.scan_s.pop(0)
                self.dire = True

            else:
                self.nowindex_scan = self.scan_s.pop(0)

        return self.nowindex_scan

    def c_scan(self):
        if len(self.c_scan_s) == 0:
            return 0

        index = self.nowindex_c_scan
        self.c_scan_s.sort(key=lambda x: 1000 - abs(index - x) if x > index else -1 * x)
        self.nowindex_c_scan = self.c_scan_s.pop(0)
        return self.nowindex_c_scan

    def __init__(self):
        super().__init__()

        self.nowindex_fcfs = 0
        self.nowindex_sstf = 0
        self.nowindex_scan = 0
        self.nowindex_c_scan = 0

        self.dire = True
        self.fcfs_s = []
        self.sstf_s = []
        self.scan_s = []
        self.c_scan_s = []

        self.fcfs_pts = []
        self.sstf_pts = []
        self.scan_pts = []
        self.c_scan_pts = []

        self.create()

    def create(self):
        self.title("代建昊--磁盘调度算法")

        f1 = tk.Frame(self)
        f1.grid(row=1,column=0)

        fig1 = Figure(figsize=(5,4), dpi=80)
        self.ax1 = fig1.add_subplot(111)
        self.canvas1 = FigureCanvasTkAgg(fig1, master=f1)
        self.canvas1.get_tk_widget().grid(row=1, column=1)
        #self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        fig2 = Figure(figsize=(5,4), dpi=80)

        self.ax2 = fig2.add_subplot(111)
        self.canvas2 = FigureCanvasTkAgg(fig2, master=f1)
        self.canvas2.get_tk_widget().grid(row=1, column=2)
        #self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        fig3 = Figure(figsize=(5,4), dpi=80)
        self.ax3 = fig3.add_subplot(111)
        self.canvas3 = FigureCanvasTkAgg(fig3, master=f1)
        self.canvas3.get_tk_widget().grid(row=2, column=1)
        #self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        fig4 = Figure(figsize=(5,4), dpi=80)
        self.ax4 = fig4.add_subplot(111)
        self.canvas4 = FigureCanvasTkAgg(fig4, master=f1)
        self.canvas4.get_tk_widget().grid(row=2, column=2)
        #self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


        f2 = tk.Frame(self)
        f2.grid(row=2,column=0)

        l1 = tk.Label(f2,text="输入数据:",font=('Arial', 12))
        l1.grid(row=1,column=1)

        e1 = tk.Entry(f2)
        e1.insert(0,'1 23 90 76 56 12 34 44 2 9 45 78 32 4 65 87 24 ')
        e1.grid(row=1, column=2)

        def b1f(self=self):
            s = e1.get()
            s = re.split("\s+",s)
            s = [int(x) for x in s if x != ""]


            self.fcfs_s = s[:]
            self.sstf_s = s[:]
            self.scan_s = s[:]
            self.c_scan_s = s[:]

        b1 = tk.Button(f2,text="确认",command=b1f,relief="raised", width=10)
        b1.grid(row=1,column=3)



        l2 = tk.Label(f2, text="添加:", font=('Arial', 12))
        l2.grid(row=2, column=1)

        e2 = tk.Entry(f2)
        e2.grid(row=2, column=2)

        def b2f(self=self):
            s = e2.get()
            s = re.split("\s+", s)
            s = [int(x) for x in s if x != ""]

            self.fcfs_s += s[:]
            self.sstf_s += s[:]
            self.scan_s += s[:]
            self.c_scan_s += s[:]





        b2= tk.Button(f2, text="确认",command=b2f,relief="raised", width=10)
        b2.grid(row=2, column=3)


        b3 = tk.Button(f2,text="下一步",command=self.drawpic)
        b3.grid(row=3,column=2)

    def drawpic(self):

        ax = [self.ax1,self.ax2,self.ax3,self.ax4]
        can = [self.canvas1,self.canvas2,self.canvas3,self.canvas4]


        for i in ax:
            i.clear()

        self.fcfs_pts.append(self.fcfs())
        self.ax1.plot(self.fcfs_pts,range(1,len(self.fcfs_pts)+1))

        self.sstf_pts.append(self.sstf())
        self.ax2.plot(self.sstf_pts, range(1, len(self.sstf_pts)+1))

        self.scan_pts.append(self.scan())
        self.ax3.plot(self.scan_pts, range(1, len(self.scan_pts)+1))

        self.c_scan_pts.append(self.c_scan())
        self.ax4.plot(self.c_scan_pts, range(1, len(self.c_scan_pts)+1))


        for i in can:
            i.draw()

        #print(self.sstf_s)
        #print(self.sstf_s)
        #print(self.scan_s)
        print(self.c_scan_s)



if __name__ == "__main__":
    a = myDiskShow()
    a.mainloop()
