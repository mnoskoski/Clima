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


# Armazenando Horário, Localização, Temperatura, Sensação Térmica e Umidade
# dentro da tupla getting

getting = info.get_info()

# Função responsável por atualizar os dados dos labels

def refresh():

    getting = info.get_info()
    local_label = Label(frm, text =f"Localização: {getting[1]}", font =("Segoe UI Variable",11)).grid(column = 0, row = 0)
    temp_label = Label(frm, text =f"Temperatura {getting[2]}ºC", font =("Segoe UI Variable",11)).grid(column = 0, row = 1)
    feels_label = Label(frm, text =f"Sensação: {getting[3]}ºC", font =("Segoe UI Variable",11)).grid(column = 0, row = 2)
    humid_label = Label(frm, text =f"Umidade: {getting[4]}", font =("Segoe UI Variable",11)).grid(column = 0, row = 3)
    lstupd_label = Label(frm, text =f"Última atualização: {getting[0]}", font =("Segoe UI Variable",7)).grid(column = 0, row = 7)

# Criação da estrutura e labels

local_label = Label(frm, text =f"Localização: {getting[1]}", font =("Segoe UI Variable",11)).grid(column = 0, row = 0)
temp_label = Label(frm, text =f"Temperatura {getting[2]}ºC", font =("Segoe UI Variable",11)).grid(column = 0, row = 1)
feels_label = Label(frm, text =f"Sensação: {getting[3]}ºC", font =("Segoe UI Variable",11)).grid(column = 0, row = 2)
humid_label = Label(frm, text =f"Umidade: {getting[4]}", font =("Segoe UI Variable",11)).grid(column = 0, row = 3)
Label(frm, text =f"", font =("Segoe UI Variable",7)).grid(column = 0, row = 4)
lstupd_label = Label(frm, text =f"Última atualização: {getting[0]}", font =("Segoe UI Variable",7)).grid(column = 0, row = 7)
Label(frm, text =f"", font =("Segoe UI Variable",7)).grid(column = 0, row = 6)
button = Button(frm, text = f"Atualizar", command = refresh, font = ("Segoe UI Variable", 11) ).grid(column = 0, row = 5)

root.mainloop()





