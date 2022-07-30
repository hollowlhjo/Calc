import tkinter as tk
import matplotlib.pyplot as plt
import math as mt


def math_calc(): 

    save = open("saves.txt", "w+")
    save.read()
    win = tk.Tk()
    win.title("Calc")
    win.geometry("330x300")
    win.resizable(False, False)
    entry_number3 = tk.Entry(win)
    entry_number2 = tk.Entry(win)
    entry_number = tk.Entry(win)
    entry_number.grid(row=0, column=1, sticky="nw")
    entry_number2.grid(row=0, column=2, sticky="nw")
    entry_number3.grid(row=1, column=2, sticky="nw")
    tk.Label(win, text="Entry number:").grid(row=0, column=0)

    btn_ico1 = tk.PhotoImage(file="img/png/plus.png")
    btn_ico2 = tk.PhotoImage(file="img/png/minus.png")
    btn_ico3 = tk.PhotoImage(file="img/png/root.png")
    btn_ico4 = tk.PhotoImage(file="img/png/multiply.png")
    btn_ico5 = tk.PhotoImage(file="img/png/divide.png")
    btn_ico1 = btn_ico1.subsample(3, 3)
    btn_ico2 = btn_ico2.subsample(3, 3)
    btn_ico3 = btn_ico3.subsample(9, 6)
    btn_ico4 = btn_ico4.subsample(6, 6)
    btn_ico5 = btn_ico5.subsample(6, 9)


    def result_lb(result):
        result_lb = tk.Label(win, text=result)
        result_lb.grid(row=5, column=1)
        save.write(str(result))

        def clear():

            def remove_button():
                clear_button.grid_remove()
            remove_button()
            result_lb.destroy()
            entry_number2.delete(0, tk.END)
            entry_number.delete(0, tk.END)
        clear_button = tk.Button(win, text="Стерти", command=clear)
        clear_button.grid(row=3, column=2, sticky="eswn")
        
    def plus():
        a = float(entry_number.get())
        b = float(entry_number2.get())
        result = a + b
        result_lb(result)
        
    def minus():
        a = float(entry_number.get())
        b = float(entry_number2.get())
        result = a - b
        result_lb(result)

    def pomnoj():
        a = float(entry_number.get())
        b = float(entry_number2.get())
        result = a * b
        result_lb(result)

    def podili():
        a = float(entry_number.get())
        b = float(entry_number2.get())
        result = a / b
        result_lb(result)

    def stepin():
        a = float(entry_number.get())
        b = float(entry_number2.get())
        result = a ** b
        result_lb(result)

    def korin():
        a = float(entry_number.get())
        b = float(entry_number2.get())
        pok = 1 / b
        result = a ** pok
        result_lb(result)

    def factorial():
        a = int(entry_number.get())
        result = 1
        for i in range(1, a + 1):
            result = result * i
        result_lb(result)

    def x_found_2():
        b = int(entry_number2.get())
        a = int(entry_number.get())
        c = int(entry_number3.get())
        pok = 1 / 2
        d = b ** 2 - 4 * a * c
        result = (-1*b + d ** pok) / (2 * a)
        result2 = (-1*b - d ** pok) / (2 * a)
        result_lb = tk.Label(win, text=result)
        result_lb.grid(row=5, column=1)
        result_lb2 = tk.Label(win, text=result2)
        result_lb2.grid(row=5, column=2)
        

        def clear():

            def remove_button():
                clear_button.grid_remove()
            remove_button()
            result_lb.destroy()
            result_lb2.destroy()
            entry_number2.delete(0, tk.END)
            entry_number.delete(0, tk.END)
            entry_number3.delete(0, tk.END)
            save.write(str(result))
            save.write(str(result2))

        clear_button = tk.Button(win, text="Стерти", command=clear)
        clear_button.grid(row=3, column=2, sticky="eswn")

    def log():
        a = int(entry_number.get())
        b = int(entry_number2.get())
        result = mt.log(a, b)
        result_lb(result)

    def function_draw():
        x_list = []
        y_list = []
        a = int(entry_number.get())
        b = int(entry_number2.get())
        c = int(entry_number3.get())
        for x_l in range(0, c):
            y_l = b * x_l + a
            x_list.append(x_l)
            y_list.append(y_l)
        plt.plot(x_list, y_list)
        plt.show()

        def clear():

            def remove_button():
                clear_button.grid_remove()
            remove_button()
            result_lb.destroy()
            entry_number2.delete(0, tk.END)
            entry_number.delete(0, tk.END)

        clear_button = tk.Button(win, text="Стерти", command=clear)
        clear_button.grid(row=3, column=2, sticky="eswn")
        
        

    tk.Button(win, text="Квадратні рівн", command=x_found_2).grid(row=1, column=2, sticky="esw")
    tk.Button(win, image=btn_ico1, command=plus).grid(row=1, column=0, sticky="esnw")
    tk.Button(win, image=btn_ico2, command=minus).grid(row=1, column=1, sticky="eswn")
    tk.Button(win, image=btn_ico4, command=pomnoj).grid(row=2, column=0, sticky="eswn")
    tk.Button(win, image=btn_ico5, command=podili).grid(row=2, column=1, sticky="eswn")
    tk.Button(win, image=btn_ico3, command=korin).grid(row=2, column=2, sticky="eswn")
    tk.Button(win, text="Факторіал", command=factorial).grid(row=3, column=0, sticky="ewsn")
    tk.Button(win, text="Степінь", command=stepin).grid(row=3, column=1, sticky="ewsn")
    tk.Button(win, text="Графік", command=function_draw).grid(row=4, column=0, sticky="ewsn")
    tk.Button(win, text="log", command=log).grid(row=4, column=1, sticky='ewsn')

    win.mainloop()


math_calc()
