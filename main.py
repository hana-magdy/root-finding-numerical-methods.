import tkinter as tk
from tkinter import filedialog, StringVar
import array as arr
import bisection
import falseposition
import secant
import fixedpoint
import NewtonRaphson
import time

elapsed_time=0
LARGE_FONT = ("Verdana", 12)
expression = ""
popup=''
x0=0
x1=0

error = arr.array('d', [0.0])
xi = arr.array('d', [0.0])
xii = arr.array('d', [0.0])


global x2
class Intialization(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()





class StartPage(tk.Frame):

    equation: StringVar

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.equation=tk.StringVar()
        self.equation.set('enter your expression')
        method = 0


        expression_field = tk.Entry(self, textvariable=self.equation, bg='white')
        expression_field.grid(columnspan=50, ipadx=100)
        self.v = tk.IntVar()
        self.v.set("1")
        self.FromFile=tk.IntVar()
        self.FromFile.set("0")
        self.filename=tk.StringVar()
        tk.Radiobutton(self,
                       text="file",
                       padx=20,
                       variable=self.FromFile,
                       value=6, width=1, command=self.print_path, fg='black', bg='white').grid(row=0, column=4)

        button1 = tk.Button(self, text=' 1 ', fg='white', bg='black',
                            command=lambda: self.press(1), height=2, width=9)
        button1.grid(row=4, column=2)

        button2 = tk.Button(self, text=' 2 ', fg='white', bg='black',
                            command=lambda: self.press(2), height=2, width=9)
        button2.grid(row=4, column=3)

        button3 = tk.Button(self, text=' 3 ', fg='white', bg='black',
                            command=lambda: self.press(3), height=2, width=9)
        button3.grid(row=4, column=4)

        button4 = tk.Button(self, text=' 4 ', fg='white', bg='black',
                            command=lambda: self.press(4), height=2, width=9)
        button4.grid(row=5, column=2)

        button5 = tk.Button(self, text=' 5 ', fg='white', bg='black',
                            command=lambda: self.press(5), height=2, width=9)
        button5.grid(row=5, column=3)

        button6 = tk.Button(self, text=' 6 ', fg='white', bg='black',
                            command=lambda: self.press(6), height=2, width=9)
        button6.grid(row=5, column=4)

        button7 = tk.Button(self, text=' 7 ', fg='white', bg='black',
                            command=lambda: self.press(7), height=2, width=9)
        button7.grid(row=6, column=2)

        button8 = tk.Button(self, text=' 8 ', fg='white', bg='black',
                            command=lambda: self.press(8), height=2, width=9)
        button8.grid(row=6, column=3)

        button9 = tk.Button(self, text=' 9 ', fg='white', bg='black',
                            command=lambda: self.press(9), height=2, width=9)
        button9.grid(row=6, column=4)

        button0 = tk.Button(self, text=' 0 ', fg='white', bg='black',
                            command=lambda: self.press(0), height=2, width=9)
        button0.grid(row=7, column=3)

        plus = tk.Button(self, text=' + ', fg='white', bg='black',
                         command=lambda: self.press("+"), height=2, width=20)
        plus.grid(row=4, column=1)

        minus = tk.Button(self, text=' - ', fg='white', bg='black',
                          command=lambda: self.press("-"), height=2, width=20)
        minus.grid(row=5, column=1)

        multiply = tk.Button(self, text=' * ', fg='white', bg='black',
                             command=lambda: self.press("*"), height=2, width=20)
        multiply.grid(row=6, column=1)

        divide = tk.Button(self, text=' / ', fg='white', bg='black',
                           command=lambda: self.press("/"), height=2, width=20)
        divide.grid(row=7, column=1)

        Decimal = tk.Button(self, text='.', fg='white', bg='black',
                            command=lambda: self.press('.'), height=2, width=9)
        Decimal.grid(row=7, column=2)

        variable = tk.Button(self, text='x', fg='white', bg='black',
                             command=lambda: self.press('x'), height=2, width=9)
        variable.grid(row=7, column=4)

        exponential = tk.Button(self, text='exp', fg='white', bg='black',
                                command=lambda: self.press("E"), height=2, width=20)
        exponential.grid(row=8, column=1)

        sinfn = tk.Button(self, text='sin', fg='white', bg='black',
                          command=lambda: self.press("sin("), height=2, width=9)
        sinfn.grid(row=8, column=2)

        cosfn = tk.Button(self, text='cos', fg='white', bg='black',
                          command=lambda: self.press("cos("), height=2, width=9)
        cosfn.grid(row=8, column=3)

        polynomial = tk.Button(self, text='pow', fg='white', bg='black',
                               command=lambda: self.press("**"), height=2, width=9)
        polynomial.grid(row=8, column=4)

        clear = tk.Button(self, text='CLEAR', fg='white', bg='black',
                          command=self.clear, height=2, width=9)
        clear.grid(row=9, column=2)

        brachet1 = tk.Button(self, text='(', fg='white', bg='black',
                             command=lambda: self.press("("), height=2, width=9)
        brachet1.grid(row=9, column=3)
        brachet2 = tk.Button(self, text=')', fg='white', bg='black',
                             command=lambda: self.press(")"), height=2, width=9)
        brachet2.grid(row=9, column=4 , pady=10)

        tk.Label(self,
                 text="""Choose a method:""",
                 justify=tk.LEFT,
                 padx=18, fg='white', bg='black').grid(row=10, column=1)

        tk.Radiobutton(self,
                       text="Bisection",
                       padx=20,
                       variable=self.v,
                       value=1, width=12, bg='white').grid(row=11, column=1)

        tk.Radiobutton(self,
                       text="False position",
                       padx=20,
                       variable=self.v,
                       value=2, width=12, bg='white').grid(row=12, column=1)
        tk.Radiobutton(self,
                       text="Newton raphson",
                       padx=20,
                       variable=self.v,
                       value=3, width=12, bg='white').grid(row=13, column=1)

        tk.Radiobutton(self,
                       text="    Secant",
                       padx=20,
                       variable=self.v,
                       value=4, width=12, bg='white').grid(row=14, column=1)

        tk.Radiobutton(self,
                       text="Fixed Point",
                       padx=20,
                       variable=self.v,
                       value=5, width=12, bg='white').grid(row=15, column=1)

        lbl = tk.Label(self, text=" Enter Tolerence", fg='white', bg='black').grid(column=1, row=17 ,pady=10)
        lb2 = tk.Label(self, text="Number of iterations", fg='white', bg='black').grid(column=1, row=18)
        self.expression_field_1 = tk.Entry(self, width=9)
        self.expression_field_1.grid(row=17, column=2,pady=10)
        self.expression_field_2 =tk.Entry(self, width=9)
        self.expression_field_2.grid(row=18, column=2)

        SubmitButton=tk.Button(self, text=' Show Results ', fg='white', bg='black',
                            command=lambda:self.OnSubmit(), height=2, width=9)
        SubmitButton.grid(row=22,column=2,pady=10)


    def OnSubmit(self):

        if self.v.get() == 1:
            self.popupmsg("bisection")
        elif self.v.get() == 2:
            self.popupmsg("false position")
        elif self.v.get() == 4:
            self.popupmsg("secant")
        elif self.v.get() == 5:
            self.popupmsg("FixedPoint")
        elif self.v.get() == 3:
            self.popupmsg("Newton")






    def popupmsg(self,Type):
         if Type =='bisection' or Type =='false position' or Type=='secant':
            label = tk.Label(self, text="Add 2 Intial guesses")
            label.grid(row=23)
            label_Xl= tk.Label(self, text="xl", fg='white', bg='black').grid( row=24,column=0)
            label_Xu= tk.Label(self, text="xu", fg='white', bg='black').grid( row=25, pady=5,column=0)
            self.entry_xl= tk.Entry(self, width=5)
            self.entry_xl.grid(row=24, column=1)
            self.entry_xu = tk.Entry(self, width=5)
            self.entry_xu.grid(row=25, column=1)
            if Type == 'bisection':
             B1 = tk.Button(self, text="Okay", command=self.bisectionPopup,fg="white",bg="black")
             B1.grid(row=26,column=1)
            elif Type =='false position':
                B2 = tk.Button(self, text="Okay", command=self.FalsePostionPopup,fg="white",bg="black")
                B2.grid(row=26,column=1)
            elif Type == 'secant':
                B3 = tk.Button(self, text="Okay", command=self.SecantPopup,fg="white",bg="black")
                B3.grid(row=26,column=1)
         elif Type=='FixedPoint' or Type=='Newton':
             label = tk.Label(self, text="Add 1 Intial guess")
             label.grid(row=23)
             label_Xl = tk.Label(self, text="xl").grid(row=24, pady=5)
             self.entry_xl = tk.Entry(self, width=5)
             self.entry_xl.grid(row=24, column=1)
             if Type=='FixedPoint':
              B3 = tk.Button(self, text="Okay", command=self.FixedPointPopup,fg="white",bg="black")
              B3.grid(row=26,column=1)
             elif Type=='Newton':
              B4 = tk.Button(self, text="Okay", command=self.NewtonRaphsonPopup,fg="white",bg="black")
              B4.grid(row=26,column=1)






    def bisectionPopup(self):
        imax=50
        ea= 0.00001
        global elapsed_time
        global x0
        x0=float(self.entry_xl.get())
        global x1
        x1=float(self.entry_xu.get())
        if self.expression_field_1.get()!='':
            ea=float(self.expression_field_1.get())
        if self.expression_field_2.get()!='':
            imax=int(self.expression_field_2.get())
        if self.FromFile.get() == 6:
         start = time.perf_counter()
         bisection.ReadFromFile(self.filename, x0, x1, ea, imax)
         end = time.perf_counter()
         elapsed_time=end-start
         print(elapsed_time)
        else:
            start = time.perf_counter()
            bisection.body(self.equation.get(), x0, x1, ea, imax)
            end = time.perf_counter()
            elapsed_time = end - start
            print(elapsed_time)
        self.FromFile.set("0")
        self.PassDataToPage1()

    def FalsePostionPopup(self):
        imax = 50
        ea = 0.00001
        global elapsed_time
        global x0
        x0=float(self.entry_xl.get())
        global x1
        x1=float(self.entry_xu.get())
        if self.expression_field_1.get() != '':
            ea = float(self.expression_field_1.get())
        if self.expression_field_2.get() != '':
            imax = int(self.expression_field_2.get())
        if self.FromFile.get() == 6:
         start = time.perf_counter()
         falseposition.ReadFromFile(self.filename, x0, x1, ea, imax)
         end = time.perf_counter()
         elapsed_time = end - start
        else:
            start = time.perf_counter()
            falseposition.body(self.equation.get(), x0, x1, ea, imax)
            end = time.perf_counter()
            elapsed_time = end - start
        self.FromFile.set("0")
        self.PassDataToPage1()

    def SecantPopup(self):
        imax = 50
        ea = 0.00001
        global elapsed_time
        global x0
        x0 = float(self.entry_xl.get())
        global x1
        x1 = float(self.entry_xu.get())
        if self.expression_field_1.get() != '':
            ea = float(self.expression_field_1.get())
        if self.expression_field_2.get() != '':
            imax = int(self.expression_field_2.get())
        if self.FromFile.get() == 6:
            start = time.perf_counter()
            secant.ReadFromFile(self.filename, x0, x1, ea,
                                      imax)
            end = time.perf_counter()
            elapsed_time = end - start
        else:
            start = time.perf_counter()
            secant.body(self.equation.get(), x0, x1, ea,
                               imax)
            end = time.perf_counter()
            elapsed_time = end - start
        self.FromFile.set("0")
        self.PassDataToPage1()

    def FixedPointPopup(self):
        imax = 50
        ea = 0.00001
        global elapsed_time
        global x0
        x0 = float(self.entry_xl.get())
        if self.expression_field_1.get() != '':
            ea = float(self.expression_field_1.get())
        if self.expression_field_2.get() != '':
            imax = int(self.expression_field_2.get())
        if self.FromFile.get() == 6:
            start = time.perf_counter()
            fixedpoint.ReadFile(self.filename, x0, ea,
                               imax)
            end = time.perf_counter()
            elapsed_time = end - start
        else:
            start = time.perf_counter()
            fixedpoint.body(self.equation.get(), x0, ea,
                       imax)
            end = time.perf_counter()
            elapsed_time = end - start
        self.FromFile.set("0")
        self.PassDataToPage1()

    def NewtonRaphsonPopup(self):
        imax = 50
        ea = 0.00001
        global elapsed_time
        global x0
        x0 = float(self.entry_xl.get())
        if self.expression_field_1.get() != '':
            ea = float(self.expression_field_1.get())
        if self.expression_field_2.get() != '':
            imax = int(self.expression_field_2.get())
        if self.FromFile.get() == 6:
            start = time.perf_counter()
            NewtonRaphson.ReadFile(self.filename, x0, ea,
                               imax)
            end = time.perf_counter()
            elapsed_time = end - start
        else:
            start = time.perf_counter()
            NewtonRaphson.body(self.equation.get(), x0, ea,
                           imax)
            end = time.perf_counter()
            elapsed_time = end - start

        self.FromFile.set("0")
        self.PassDataToPage1()





    def PassDataToPage1(self):
        self.controller.method = self.v.get()
        self.controller.frames[PageOne].correct_label()  # call correct_label function
        self.controller.show_frame(PageOne)


    def press(self,num):
        global expression
        expression = expression + str(num)
        self.equation.set(expression)


    def clear(self):
        global expression
        expression = ""
        self.equation.set("")


    def submitFunction(self):
        print('Submit button is clicked.')

    def print_path(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("text file", ".txt"), ("all files", ".*")))

        self.configure(background="white")



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.LabelTitle = tk.Label(self,text="")
        self.LabelTabelIteration = tk.Label(self,text="")
        self.LabelTabelXi = tk.Label(self,text="")
        self.LabelTabelXii = tk.Label(self,text="")
        self.LabelTabelError = tk.Label(self,text="")
        self.LabelTabelROOT = tk.Label(self,text="")
        self.LabelTabelPrint = tk.Label(self,text="")
        self.LabelNumberIteration = tk.Label(self,text="")
        self.LabelTabelTime = tk.Label(self, text="")
      #  self.backbutton=tk.Button(self,text="Go Back",command=lambda: self.controller.show_frame(StartPage))
       # self.backbutton.grid(column=10)

    def correct_label(self):



     if self.controller.method == 1:
         if (bisection.string ==""):
            self.LabelTitle.config(text="Result of bisection method",font=("Helvetica", 12))
            self.LabelTitle.grid(row=0,column=0)
            self.LabelTabelIteration.config(text="Iteration" ,font=("Helvetica", 12))
            self.LabelTabelIteration.grid(row=1, column=0)
            self.LabelTabelXi.config(text="Xi" ,font=("Helvetica", 12))
            self.LabelTabelXi.grid(row=1, column=1)
            self.LabelTabelXii.config(text="Xii" ,font=("Helvetica", 12))
            self.LabelTabelXii.grid(row=1, column=4)
            self.LabelTabelError.config(text="ERROR" ,font=("Helvetica", 12))
            self.LabelTabelError.grid(row=1, column=8)

            # correct the label
            error = bisection.error
            xi = bisection.xi
            xii = bisection.xii
            X2 = bisection.x2
            self.total_rows = 4

            self.LabelTabelROOT.config(text="The Root", font=("Helvetica", 12))
            self.LabelTabelROOT.grid(row=len(xi)+6, column=0)
            self.LabelNumberIteration.config(text="The Number Of Iteration", font=("Helvetica", 12))
            self.LabelNumberIteration.grid(row=len(xi) + 7, column=0)
            self.LabelTabelTime.config(text="Elapsed_Time", font=("Helvetica", 12))
            self.LabelTabelTime.grid(row=len(xi) + 8, column=0)
            for i in range(1, len(xi)):
                label = tk.Label(self, text=i, font=("Helvetica", 12))
                label.grid(row=i+2, column=0)

            for i in range(1,len(xi)):
                label = tk.Label(self,text=xi[i],font=("Helvetica", 12))
                label.grid(row=i+2,column=1)
            for i in range(1,len(xii)):
                label = tk.Label(self,text=xii[i],font=("Helvetica", 12))
                label.grid(row=i+2,column=4)
            for i in range(1,len(error)):
                label = tk.Label(self,text=error[i], font=("Helvetica", 12))
                label.grid(row=i+2,column=8)

            label = tk.Label(self, text=X2,font=("Helvetica", 12))
            label.grid(row=len(xi)+6, column=1)
            label = tk.Label(self, text=bisection.it, font=("Helvetica", 12))
            label.grid(row=len(xi) + 7, column=1)
            label = tk.Label(self, text=elapsed_time,font=("Helvetica", 12))
            label.grid(row=len(xi) + 8, column=1)
         else:
            self.LabelTabelPrint.config(text=bisection.string,font=("Helvetica", 12))
            self.LabelTabelPrint.grid(row=0,column=0)


     if self.controller.method == 2:
         if (falseposition.string ==""):
                self.LabelTitle.config(text="Result of false position method", font=("Helvetica", 12))
                self.LabelTitle.grid(row=0, column=0)
                self.LabelTabelIteration.config(text="Iteration", font=("Helvetica", 12))
                self.LabelTabelIteration.grid(row=1, column=0)
                self.LabelTabelXi.config(text="Xi" , font=("Helvetica", 12))
                self.LabelTabelXi.grid(row=1, column=1)
                self.LabelTabelXii.config(text="Xii" , font=("Helvetica", 12))
                self.LabelTabelXii.grid(row=1, column=4)
                self.LabelTabelError.config(text="ERROR" , font=("Helvetica", 12))
                self.LabelTabelError.grid(row=1, column=8)

                # correct the label
                error = falseposition.error
                xi = falseposition.xi
                xii = falseposition.xii
                x2 = falseposition.x2
                self.total_rows = 4

                self.LabelTabelROOT.config(text="The Root" , font=("Helvetica", 12))
                self.LabelTabelROOT.grid(row=len(xi) + 6, column=0)
                self.LabelNumberIteration.config(text="The Number Of Iteration", font=("Helvetica", 12))
                self.LabelNumberIteration.grid(row=len(xi) + 7, column=0)
                self.LabelTabelTime.config(text="Elapsed_Time", font=("Helvetica", 12))
                self.LabelTabelTime.grid(row=len(xi) + 8, column=0)
                for i in range(1, len(xi)):
                    label = tk.Label(self, text=i, font=("Helvetica", 12))
                    label.grid(row=i + 2, column=0)

                for i in range(1, len(xi)):
                    label = tk.Label(self, text=xi[i], font=("Helvetica", 12))
                    label.grid(row=i + 2, column=1)
                for i in range(1, len(xii)):
                    label = tk.Label(self, text=xii[i], font=("Helvetica", 12))
                    label.grid(row=i + 2, column=4)
                for i in range(1, len(error)):
                    label = tk.Label(self, text=error[i], font=("Helvetica", 12))
                    label.grid(row=i + 2, column=8)

                label = tk.Label(self, text=x2, font=("Helvetica", 12))
                label.grid(row=len(xi) + 6, column=1)
                label = tk.Label(self, text=falseposition.it, font=("Helvetica", 12))
                label.grid(row=len(xi) + 7, column=1)
                label = tk.Label(self, text=elapsed_time, font=("Helvetica", 12))
                label.grid(row=len(xi) + 8, column=1)
         else:
                self.LabelTabelPrint.config(text=falseposition.string, font=("Helvetica", 12))
                self.LabelTabelPrint.grid(row=3, column=3)
     if self.controller.method == 4:
         if (secant.string ==""):

                    self.LabelTitle.config(text="Result of Secent method", font=("Helvetica", 12))
                    self.LabelTitle.grid(row=0, column=0)
                    self.LabelTabelIteration.config(text="Iteration" , font=("Helvetica", 12))
                    self.LabelTabelIteration.grid(row=1, column=0)
                    self.LabelTabelXi.config(text="Xi" , font=("Helvetica", 12))
                    self.LabelTabelXi.grid(row=1, column=1)
                    self.LabelTabelXii.config(text="Xii" , font=("Helvetica", 12))
                    self.LabelTabelXii.grid(row=1, column=4)
                    self.LabelTabelError.config(text="ERROR" , font=("Helvetica", 12))
                    self.LabelTabelError.grid(row=1, column=8)

                    # correct the label
                    error = secant.error
                    xi = secant.xi
                    xii = secant.xii
                    X2 = secant.x2
                    self.total_rows = 4

                    self.LabelTabelROOT.config(text="The Root" , font=("Helvetica", 12))
                    self.LabelTabelROOT.grid(row=len(xi) + 6, column=0)
                    self.LabelNumberIteration.config(text="The Number Of Iteration", font=("Helvetica", 12))
                    self.LabelNumberIteration.grid(row=len(xi) + 7, column=0)
                    self.LabelTabelTime.config(text="Elapsed_Time", font=("Helvetica", 12))
                    self.LabelTabelTime.grid(row=len(xi) + 8, column=0)
                    for i in range(1, len(xi)):
                        label = tk.Label(self, text=i, font=("Helvetica", 12))
                        label.grid(row=i + 2, column=0)

                    for i in range(1, len(xi)):
                        label = tk.Label(self, text=xi[i], font=("Helvetica", 12))
                        label.grid(row=i + 2, column=1)
                    for i in range(1, len(xii)):
                        label = tk.Label(self, text=xii[i], font=("Helvetica", 12))
                        label.grid(row=i + 2, column=4)
                    for i in range(1, len(error)):
                        label = tk.Label(self, text=error[i], font=("Helvetica", 12))
                        label.grid(row=i + 2, column=8)

                    label = tk.Label(self, text=X2, font=("Helvetica", 12))
                    label.grid(row=len(xi) + 6, column=1)
                    label = tk.Label(self, text=secant.it, font=("Helvetica", 12))
                    label.grid(row=len(xi) + 7, column=1)
                    label = tk.Label(self, text=elapsed_time, font=("Helvetica", 12))
                    label.grid(row=len(xi) + 8, column=1)
         else:
                self.LabelTabelPrint.config(text=secant.string, font=("Helvetica", 12))
                self.LabelTabelPrint.grid(row=0, column=0)

     if self.controller.method == 5:
         if (fixedpoint.string ==""):
             self.LabelTitle.config(text="Result of Fixed Point method", font=("Helvetica", 12))
             self.LabelTitle.grid(row=0, column=0)
             self.LabelTabelIteration.config(text="Iteration", font=("Helvetica", 12))
             self.LabelTabelIteration.grid(row=1, column=0)
             self.LabelTabelXi.config(text="Xi", font=("Helvetica", 12))
             self.LabelTabelXi.grid(row=1, column=1)
             self.LabelTabelXii.config(text="Xii", font=("Helvetica", 12))
             self.LabelTabelXii.grid(row=1, column=4)
             self.LabelTabelError.config(text="ERROR", font=("Helvetica", 12))
             self.LabelTabelError.grid(row=1, column=8)

             # correct the label
             error = fixedpoint.error
             xi = fixedpoint.xi
             xii = fixedpoint.xii
             X2 = fixedpoint.x1
             self.total_rows = 4

             self.LabelTabelROOT.config(text="The Root", font=("Helvetica", 12))
             self.LabelTabelROOT.grid(row=len(xi) + 6, column=0)
             self.LabelNumberIteration.config(text="The Number Of Iteration", font=("Helvetica", 12))
             self.LabelNumberIteration.grid(row=len(xi) + 7, column=0)
             self.LabelTabelTime.config(text="Elapsed_Time", font=("Helvetica", 12))
             self.LabelTabelTime.grid(row=len(xi) + 8, column=0)
             for i in range(1, len(xi)):
                 label = tk.Label(self, text=i, font=("Helvetica", 12))
                 label.grid(row=i + 2, column=0)

             for i in range(1, len(xi)):
                 label = tk.Label(self, text=xi[i], font=("Helvetica", 12))
                 label.grid(row=i + 2, column=1)
             for i in range(1, len(xii)):
                 label = tk.Label(self, text=xii[i], font=("Helvetica", 12))
                 label.grid(row=i + 2, column=4)
             for i in range(1, len(error)):
                 label = tk.Label(self, text=error[i], font=("Helvetica", 12))
                 label.grid(row=i + 2, column=8)

             label = tk.Label(self, text=X2, font=("Helvetica", 12))
             label.grid(row=len(xi) + 6, column=1)
             label = tk.Label(self, text=fixedpoint.it, font=("Helvetica", 12))
             label.grid(row=len(xi) + 7, column=1)
             label = tk.Label(self, text=elapsed_time, font=("Helvetica", 12))
             label.grid(row=len(xi) + 8, column=1)
         else:
             print("ANA GOWAAAA"+fixedpoint.string)
             self.LabelPrint=tk.Label(self,text=fixedpoint.string,font=("Helvetica", 12))
             self.LabelPrint.grid(row=3, column=3)

     if self.controller.method == 3:
         if (NewtonRaphson.string ==""):
             self.LabelTitle.config(text="Result of NewtonRaphson method", font=("Helvetica", 12))
             self.LabelTitle.grid(row=0, column=0)
             self.LabelTabelIteration.config(text="Iteration", font=("Helvetica", 12))
             self.LabelTabelIteration.grid(row=1, column=0)
             self.LabelTabelXi.config(text="Xi", font=("Helvetica", 12))
             self.LabelTabelXi.grid(row=1, column=1)
             self.LabelTabelXii.config(text="Xii", font=("Helvetica", 12))
             self.LabelTabelXii.grid(row=1, column=4)
             self.LabelTabelError.config(text="ERROR", font=("Helvetica", 12))
             self.LabelTabelError.grid(row=1, column=8)

             # correct the label
             error = NewtonRaphson.error
             xi = NewtonRaphson.xi
             xii = NewtonRaphson.xii
             X2 = NewtonRaphson.x1
             self.total_rows = 4

             self.LabelTabelROOT.config(text="The Root", font=("Helvetica", 12))
             self.LabelTabelROOT.grid(row=len(xi) + 6, column=0)
             self.LabelNumberIteration.config(text="The Number Of Iteration", font=("Helvetica", 12))
             self.LabelNumberIteration.grid(row=len(xi) + 7, column=0)
             self.LabelTabelTime.config(text="Elapsed_Time", font=("Helvetica", 12))
             self.LabelTabelTime.grid(row=len(xi) + 8, column=0)
             for i in range(1, len(xi)):
                 label = tk.Label(self, text=i, font=("Helvetica", 12))
                 label.grid(row=i + 2, column=0)

             for i in range(1, len(xi)):
                 label = tk.Label(self, text=xi[i], font=("Helvetica", 12))
                 label.grid(row=i + 2, column=1)
             for i in range(1, len(xii)):
                 label = tk.Label(self, text=xii[i], font=("Helvetica", 12))
                 label.grid(row=i + 2, column=4)
             for i in range(1, len(error)):
                 label = tk.Label(self, text=error[i], font=("Helvetica", 12))
                 label.grid(row=i + 2, column=8)

             label = tk.Label(self, text=X2, font=("Helvetica", 12))
             label.grid(row=len(xi) + 6, column=1)
             label = tk.Label(self, text=NewtonRaphson.it, font=("Helvetica", 12))
             label.grid(row=len(xi) + 7, column=1)
             label = tk.Label(self, text=elapsed_time, font=("Helvetica", 12))
             label.grid(row=len(xi) + 8, column=1)

         else:
             self.LabelTabelPrint.config(text=NewtonRaphson.string, font=("Helvetica", 12))
             self.LabelTabelPrint.grid(row=4, column=6)










app = Intialization()
app.geometry("550x700")
app.title("Numerical Analysis")
app.mainloop()
