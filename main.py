from tkinter import *

root = Tk()
w = 800
h = 600

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = ws/2 - w/2
y = hs/2 - h/2

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.iconbitmap("assets/icons/Icon.ico")

root.resizable(False, False)
root.title("Training Conversions")
root.configure(background="grey")

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

title = Label(text="Training Conversions", font=("Arial", 20), bg="grey")
title.pack(side=TOP, pady=5)

buttons = Frame(width=800, height=20, bg="grey")
buttons.pack()

table = Frame(width=800, height=100, bg="grey")
table.pack()

def convertRun():
    error["text"] = ""
    ru = run.get(1.0, "end-1c").strip()
    if ru.startswith("-"):
        error["text"] = "Invalid input, must be a positive number."
    else:
        if isfloat(ru):
            error["text"] = ""
            ru = float(ru)
            ro = ru + ru/4
            b = 2*ru + ru/2
            s = 2*(ru/100)

            if str(ro).endswith(".0"):
                ro = int(ro)
            if str(b).endswith(".0"):
                b = int(b)
            if str(s).endswith(".0"):
                s = int(s)

            rowResult["text"] = str(ro)
            rowResult.grid(row=1, column=1)
            bikeResult["text"] = str(b)
            bikeResult.grid(row=1, column=2)
            stairsResult["text"] = str(s)
            stairsResult.grid(row=1, column=3)     
        else:
            error["text"] = "Invalid input, must be a positive number."

def convertRow():
    error["text"] = ""
    ro = row.get(1.0, "end-1c").strip()
    if ro.startswith("-"):
        error["text"] = "Invalid input, must be a positive number."
    else:
        if isfloat(ro):
            error["text"] = ""
            ro = float(ro)
            ru = ro - (ro/4)
            b = 2*ro
            s = ro/62.5

            if str(ru).endswith(".0"):
                ru = int(ru)
            if str(b).endswith(".0"):
                b = int(b)
            if str(s).endswith(".0"):
                s = int(s)

            runResult["text"] = str(ru)
            runResult.grid(row=1, column=0)
            bikeResult["text"] = str(b)
            bikeResult.grid(row=1, column=2)
            stairsResult["text"] = str(s)
            stairsResult.grid(row=1, column=3)     
        else:
            error["text"] = "Invalid input, must be a positive number."

def convertBike():
    error["text"] = ""
    b = bike.get(1.0, "end-1c").strip()
    if b.startswith("-"):
        error["text"] = "Invalid input, must be a positive number."
    else:
        if isfloat(b):
            error["text"] = ""
            b = float(b)
            ru = b/2.5
            ro = b/2
            s = b/125

            if str(ru).endswith(".0"):
                ru = int(ru)
            if str(ro).endswith(".0"):
                ro = int(ro)
            if str(s).endswith(".0"):
                s = int(s)

            runResult["text"] = str(ru)
            runResult.grid(row=1, column=0)
            rowResult["text"] = str(ro)
            rowResult.grid(row=1, column=1)
            stairsResult["text"] = str(s)
            stairsResult.grid(row=1, column=3)     
        else:
            error["text"] = "Invalid input, must be a positive number."

def convertStairs():
    error["text"] = ""
    s = stairs.get(1.0, "end-1c").strip()
    if s.startswith("-"):
        error["text"] = "Invalid input, must be a positive number."
    else:
        if isfloat(s):
            error["text"] = ""
            s = float(s)
            ru = s*50
            ro = s*62.5
            b = s*125

            if str(ru).endswith(".0"):
                ru = int(ru)
            if str(ro).endswith(".0"):
                ro = int(ro)
            if str(b).endswith(".0"):
                b = int(b)

            runResult["text"] = str(ru)
            runResult.grid(row=1, column=0)
            rowResult["text"] = str(ro)
            rowResult.grid(row=1, column=1)
            bikeResult["text"] = str(b)
            bikeResult.grid(row=1, column=2)     
        else:
            error["text"] = "Invalid input, must be a positive number."

def checkConversion():
    if run["state"] == "normal":
        convertRun()
    elif row["state"] == "normal":
        convertRow()
    elif bike["state"] == "normal":
        convertBike()
    elif stairs["state"] == "normal":
        convertStairs()

calculate = Button(root, text="Calculate", width=10, height=3, bg="grey", state="disabled", command=checkConversion)
calculate.pack(pady=20)

alt2 = Label(root, text="Check data directory for more info", font=("Arial", 7), bg="grey")
alt2.pack(side=BOTTOM, pady=10)

alt1 = Label(root, text="Data from: Functional Bodybuilding and Daybreak CrossFit", font=("Arial", 12), bg="grey")
alt1.pack(side=BOTTOM, pady=10)

error = Label(root, text="", font=("Arial", 10), bg="grey", fg="red")
error.pack()

runText = Label(table, text="Run Meters", font=("Arial", 12), width=20, bg="grey")
runText.grid(row=0, column=0)

run = Text(table, height=3, width=20)
run.grid(row=1, column=0)

runResult = Label(table, text="", font=("Arial", 10), fg="green", width=20, height=3)
runResult.grid_forget()

rowText = Label(table, text="Row Meters", font=("Arial", 12), width=20, bg="grey")
rowText.grid(row=0, column=1)

row = Text(table, height=3, width=20)
row.grid(row=1, column=1)

rowResult = Label(table, text="", font=("Arial", 10), fg="green", width=20, height=3)
rowResult.grid_forget()

bikeText = Label(table, text="Bike Meters", font=("Arial", 12), width=20, bg="grey")
bikeText.grid(row=0, column=2)

bike = Text(table, height=3, width=20)
bike.grid(row=1, column=2)

bikeResult = Label(table, text="", font=("Arial", 10), fg="green", width=20, height=3)
bikeResult.grid_forget()

stairsText = Label(table, text="Stair Flights", font=("Arial", 12), width=20, bg="grey")
stairsText.grid(row=0, column=3)

stairs = Text(table, height=3, width=20)
stairs.grid(row=1, column=3)

stairsResult = Label(table, text="", font=("Arial", 10), fg="green", width=20, height=3)
stairsResult.grid_forget()

def activate(active, e1, e2, e3, activeResults, e1Results, e2Results, e3Results):
    active.delete("1.0", "end")
    active["state"] = "normal"
    active["bg"] = "white"
    activeResults.grid_forget()
    e1Results.grid_forget()
    e2Results.grid_forget()
    e3Results.grid_forget()
    e1.delete("1.0", "end")
    e1["state"] = "disabled"
    e1["bg"] = "grey"
    e2.delete("1.0", "end")
    e2["state"] = "disabled"
    e2["bg"] = "grey"
    e3.delete("1.0", "end")
    e3["state"] = "disabled"
    e3["bg"] = "grey"
    calculate["state"] = "active"
    calculate["bg"] = "white"




runBtn = Button(buttons, width=20, height=3, bg = "darkgrey", text="From run to..", command=lambda: activate(run, row, bike, stairs, runResult, rowResult, bikeResult, stairsResult))
runBtn.grid(row=0, column=0)

rowBtn = Button(buttons, width=20, height=3, bg = "darkgrey", text="From row to..", command=lambda: activate(row, run, bike, stairs, rowResult, runResult, bikeResult, stairsResult))
rowBtn.grid(row=0, column=1)

bikeBtn = Button(buttons, width=20, height=3, bg = "darkgrey", text="From bike to..", command=lambda: activate(bike, run, row, stairs, bikeResult, runResult, rowResult, stairsResult))
bikeBtn.grid(row=0, column=2)

stairsBtn = Button(buttons, width=20, height=3, bg = "darkgrey", text="From stairs to..", command=lambda: activate(stairs, run, row, bike, stairsResult, runResult, rowResult, bikeResult))
stairsBtn.grid(row=0, column=3)


root.mainloop()
