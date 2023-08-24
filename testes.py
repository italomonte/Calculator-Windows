import tkinter as tk

def on_button_click():
    print("Button Clicked")

root = tk.Tk()
root.title("Sombreado em Button")

button_frame = tk.Frame(root)
button_frame.pack(padx=20, pady=20)

# Botão principal
button = tk.Button(button_frame, text="Click Me", command=on_button_click, relief="flat", bg="#dcdcdc")
button.pack(padx=10, pady=10)

# Botão sobreposto para criar sombreado
shadow_button = tk.Button(button_frame, text=" ", command=on_button_click, relief="flat", bg="#9e9e9e")
shadow_button.place(in_=button, relx=1, rely=1, anchor="se")

root.mainloop()
