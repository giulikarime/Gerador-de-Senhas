import tkinter as tk
from tkinter import ttk
import random, string

win = tk.Tk()
win.title("Interface")
win.geometry("340x300")
win.configure(bg="#8BA7A1")

#Listas
letras_minusculas = list(string.ascii_lowercase)
letras_maiusculas = list(string.ascii_uppercase)
especiais = [ '.', '+', '-', '@', '#', '*', '!', '?', '~']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Campo de exibição
Exi_senha = tk.Label(win, font=("Arial", 14), bg="#8BA7A1",text='')
Exi_senha.place(relx=0.5, y=80, anchor="center", width=250)

# Linha abaixo do campo
linha = tk.Frame(win, bg="#3d3d3d", height=2, width=250)
linha.place(relx=0.5, y=95, anchor="center")

#Label e Dig
TextDig = tk.Label(win, text="Num de Díg.", font=("Arial", 10), bg="#8BA7A1")
TextDig.place(x=50, y=130)

spin_var = tk.StringVar(value="12")
spinDig = ttk.Spinbox(win, from_=12, to=24, width=4, font=("Arial", 12),textvariable=spin_var)
spinDig.place(x=50, y=155)

#Gerar Senhas

def MostrarSenha():
    total_dígitos = int(spin_var.get())
    Senha = []
    i = 0

    while i < total_dígitos:
        Senha.append(random.choice(letras_minusculas))
        i += 1
        Senha.append(random.choice(letras_maiusculas))
        i += 1
        Senha.append(random.choice(especiais))
        i += 1
        Senha.append(random.choice(numeros))
        i += 1

    delimiter = ''
    ValorSenha = delimiter.join(Senha)
    Exi_senha['text'] = ValorSenha

#Botão
btn = tk.Button(win, text="gerar senha", font=("Arial", 12), bg="#cfcfcf",command=MostrarSenha)
btn.place(x=130, y=150, width=150, height=35)

win.mainloop()