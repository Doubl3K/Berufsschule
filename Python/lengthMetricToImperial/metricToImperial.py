from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Calculation:
    def metricToImp(metValue):
        result = round(metValue / 2.54, 2)
        return str(result)

    def impToMetric(impValue):
        result = round(impValue * 2.54, 2)
        return str(result)

    #checks if the input numbers are floatingpoint
    def inputValidation(met, imp):
        try:
            float(met.get())
        except ValueError:
            messagebox.showerror("Not a Number", "The entered value of" + met.get() + "is not a Floatingpoint number!")
            return False
        try:
            float(imp.get())
        except ValueError:
            messagebox.showerror("Not a Number", "The entered value of" + imp.get() + "is not a Floatingpoint number!")
            return False

    #declares calulation direction
    def chooser(direction, met, imp, metChooser):
        if (Calculation.inputValidation(met, imp) == False):
            #returns to not change any values if userinput cant be used
            return
        direction = direction.get()
        if (direction == "metric -> imperial"):
            if (metChooser == "m"):
                imp.delete(0, "end");
                imp.insert(0 ,Calculation.metricToImp(float(met.get())*100)) 
            elif (metChooser == "km"):
                imp.delete(0, "end")
                imp.insert(0, Calculation.metricToImp(float(met.get())*100000))
            else:
                imp.delete(0, "end")
                imp.insert(0, Calculation.metricToImp(float(met.get())))

        elif (direction == "imperial -> metric"):
            if (metChooser == "m"):
                met.delete(0, "end");
                met.insert(0, Calculation.impToMetric(float(imp.get())/100))
            elif (metChooser == "km"):
                met.delete(0, "end")
                met.insert(0, Calculation.impToMetric(float(imp.get())/100000))
            else:
                met.delete(0, "end")
                met.insert(0, Calculation.impToMetric(float(imp.get())))

class Aplication():
    def window():

        #Window constraints
        root = Tk()
        root.title("Metric to Imperial")
        root.resizable(False, False)
        frm = ttk.Frame(root, padding=20)
        frm.grid()

        #Metric unit chooser
        metChooser = ttk.Combobox(frm,values=("cm", "m", "km"),justify="center",state="readonly");
        metChooser.grid(column=0, row=0)
        metChooser.current(0)
        

        #Metric user input / program output 
        metText = ttk.Entry(frm,justify="center")
        metText.grid(column=1, row=0)
        metText.insert(0,1)
        
        
        #Imperial user input/program output
        impText = ttk.Entry(frm,justify="center")
        impText.grid(column=2, row=0)
        impText.insert(0,0.39)
        

        #Imperial unit chooser
        impChooser = ttk.Combobox(frm, values=("inch"),justify="center",state="readonly")
        impChooser.grid(column=3, row=0)
        impChooser.current(0)

        #Choose in wich direction you want to convert
        directionChooser = ttk.Combobox(frm, values=("metric -> imperial","imperial -> metric"))
        directionChooser.grid(column=1, row=1, columnspan=2, pady=10)
        directionChooser.current(0)

        #Button to run calculation and give parameters to Calc class
        calcButton = ttk.Button(frm, text="calculate", command= lambda:Calculation.chooser(directionChooser, metText, impText, metChooser.get()))
        calcButton.grid(column=1, row=3, columnspan=2)

        root.mainloop()
    window()
