from tkinter import *
from tkinter import ttk
import info
import time


# Janela

root = Tk()
root.title("Clima")
root.configure(width=500, height=500, bg="lightgray")

frm = ttk.Frame(root, padding = 10)
frm.grid()

getting = info.get_info()

def refresh():

    getting = info.get_info()
    local_label = Label(frm, text =f"Localização: {getting[1]}", font =("Segoe UI Variable",12)).grid(column = 0, row = 0)
    temp_label = Label(frm, text =f"Temperatura {getting[2]}ºC", font =("Segoe UI Variable",12)).grid(column = 0, row = 1)
    feels_label = Label(frm, text =f"Sensação: {getting[3]}ºC", font =("Segoe UI Variable",12)).grid(column = 0, row = 2)
    humid_label = Label(frm, text =f"Umidade: {getting[4]}", font =("Segoe UI Variable",12)).grid(column = 0, row = 3)
    lstupd_label = Label(frm, text =f"Última atualização: {getting[0]}", font =("Segoe UI Variable",12)).grid(column = 0, row = 7)

local_label = Label(frm, text =f"Localização: {getting[1]}", font =("Segoe UI Variable",12)).grid(column = 0, row = 0)
temp_label = Label(frm, text =f"Temperatura {getting[2]}ºC", font =("Segoe UI Variable",12)).grid(column = 0, row = 1)
feels_label = Label(frm, text =f"Sensação: {getting[3]}ºC", font =("Segoe UI Variable",12)).grid(column = 0, row = 2)
humid_label = Label(frm, text =f"Umidade: {getting[4]}", font =("Segoe UI Variable",12)).grid(column = 0, row = 3)
Label(frm, text =f"", font =("Segoe UI Variable",8)).grid(column = 0, row = 4)
lstupd_label = Label(frm, text =f"Última atualização: {getting[0]}", font =("Segoe UI Variable",8)).grid(column = 0, row = 7)
Label(frm, text =f"", font =("Segoe UI Variable",8)).grid(column = 0, row = 6)
button = Button(frm, text = f"Atualizar", command = refresh, font = ("Segoe UI Variable", 12) ).grid(column = 0, row = 5)

root.mainloop()





