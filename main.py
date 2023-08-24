import tkinter as tk
from tkinter import ttk

# Criar raiz
root = tk.Tk()

# Definindo nome
root.title("Calculadora")

# Definindo tamanho da janela
root.geometry("340x550")

# Criando frame onde vai ficar o texto
display_frame = ttk.Frame(root)
display_frame.grid(row=0, column=0)

# Criando frame onde vão ficar os botões
button_frame = ttk.Frame(root)
button_frame.grid(row=1, column=0)

#DISPLAY
display = tk.Label(display_frame, text="a", height=12)
display.grid(row=0, column=0)

# BUTTONS

# Configuração dos botões para remover sombreado e foco
button_style = {"relief":"flat", "width":10, "height":3, "bg":"#dcdcdc"}

button1 = tk.Button(button_frame, text="%", **button_style)
button1.grid(row=0, column=0, pady=(2, 2), padx=(4,2))

button2 = tk.Button(button_frame, text="CE", **button_style)
button2.grid(row=0, column=1, pady=(2, 2), padx=(2,2))

button3 = tk.Button(button_frame, text="C", **button_style)
button3.grid(row=0, column=2, pady=(2, 2), padx=(2,2))

button4 = tk.Button(button_frame, text="<-", **button_style)
button4.grid(row=0, column=3, pady=(2, 2), padx=(2,2))

button5 = tk.Button(button_frame, text="1/x", **button_style)
button5.grid(row=1, column=0, pady=(2, 2), padx=(4,2))

button6 = tk.Button(button_frame, text="x²", **button_style)
button6.grid(row=1, column=1, pady=(2, 2), padx=(2,2))

button7 = tk.Button(button_frame, text="sqrt x", **button_style)
button7.grid(row=1, column=2, pady=(2, 2), padx=(2,2))

button8 = tk.Button(button_frame, text="/", **button_style)
button8.grid(row=1, column=3, pady=(2, 2), padx=(2,2))

button9 = tk.Button(button_frame, text="9", **button_style)
button9.grid(row=2, column=0, pady=(2, 2), padx=(4,2))

button10 = tk.Button(button_frame, text="8", **button_style)
button10.grid(row=2, column=1, pady=(2, 2), padx=(2,2))

button11 = tk.Button(button_frame, text="7", **button_style)
button11.grid(row=2, column=2, pady=(2, 2), padx=(2,2))

button12 = tk.Button(button_frame, text="X", **button_style)
button12.grid(row=2, column=3, pady=(2, 2), padx=(2,2))

button13 = tk.Button(button_frame, text="6", **button_style)
button13.grid(row=3, column=0, pady=(2, 2), padx=(4,2))

button14 = tk.Button(button_frame, text="5", **button_style)
button14.grid(row=3, column=1, pady=(2, 2), padx=(2,2))

button15 = tk.Button(button_frame, text="4", **button_style)
button15.grid(row=3, column=2, pady=(2, 2), padx=(2,2))

button16 = tk.Button(button_frame, text="-", **button_style)
button16.grid(row=3, column=3, pady=(2, 2), padx=(2,2))

button17 = tk.Button(button_frame, text="3", **button_style)
button17.grid(row=4, column=0, pady=(2, 2), padx=(4,2))

button18 = tk.Button(button_frame, text="2", **button_style)
button18.grid(row=4, column=1, pady=(2, 2), padx=(2,2))

button19 = tk.Button(button_frame, text="1", **button_style)
button19.grid(row=4, column=2, pady=(2, 2), padx=(2,2))

button20 = tk.Button(button_frame, text="+", **button_style)
button20.grid(row=4, column=3, pady=(2, 2), padx=(2,2))

button21 = tk.Button(button_frame, text="+/-", **button_style)
button21.grid(row=5, column=0, pady=(2, 2), padx=(4,2))

button22 = tk.Button(button_frame, text="0", **button_style)
button22.grid(row=5, column=1, pady=(2, 2), padx=(2,2))

button23 = tk.Button(button_frame, text=",", **button_style)
button23.grid(row=5, column=2, pady=(2, 2), padx=(2,2))

button24 = tk.Button(button_frame, text="=", relief="flat", width=10, height=3, bg="#107db2", fg="white")
button24.grid(row=5, column=3, pady=(2, 2), padx=(2,2))

root.mainloop()