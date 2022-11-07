from distutils.command.build import build
from logging import root
from msilib.schema import ComboBox
from optparse import Values
from pydoc import text
from tkinter import *
from tkinter import ttk
from turtle import title
from decimal import Decimal
import keyboard

metValue = 0
impValue = 0
metUnit = ""
impUnit = ""


class Calculation:
    def cmToInch():
        result = metValue / impValue
        return result

    def unitChooser():
        result = 0
        if metUnit == "cm" and impUnit == "inch":
            result = Calculation.cmToInch()
        
        return result


class Aplication:
    def window():
        #Window constraints
        root = Tk()
        root.title("Metric to Imperial")
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
        impText.insert(0,2.54)

        #Imperial unit chooser
        impChooser = ttk.Combobox(frm, values=("inch", "feet + inch"),justify="center",state="readonly")
        impChooser.grid(column=3, row=0)
        impChooser.current(0)

        #set global variables to user input on enter
        
        def keyPress():
            metValue = Decimal(metText.get())
            impValue = Decimal(impText.get())
            metUnit = metChooser.get()
            impUnit = impChooser.get()
            print(Calculation.unitChooser())
        root.mainloop()

    window()

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break
