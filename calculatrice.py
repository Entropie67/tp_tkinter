import tkinter as tk


# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice")

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + (str(number)))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Erreur")
 
# Pour les entrées
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4,
           padx=10, pady=10)

# Boutons
button_1 = tk.Button(root, text="1", padx=20, pady=20,
                     command=lambda:button_click(1))
button_1.grid(row=3, column=0)

button_2 = tk.Button(root, text="2", padx=20, pady=20,
                     command=lambda : button_click(2))
button_2.grid(row=3, column=1)

button_3 = tk.Button(root, text="3", padx=20, pady=20,
                     command=lambda : button_click(3))
button_3.grid(row=3, column=2)
button_4 = tk.Button(root, text="4", padx=20, pady=20,
                     command=lambda : button_click(4))
button_4.grid(row=4, column=0)
button_1 = tk.Button(root, text="5", padx=20, pady=20,
                     command=lambda : button_click(5))
button_1.grid(row=4, column=1)
button_1 = tk.Button(root, text="6", padx=20, pady=20,
                     command=lambda : button_click(6))
button_1.grid(row=4, column=2)
button_1 = tk.Button(root, text="7", padx=20, pady=20,
                     command=lambda : button_click(7))
button_1.grid(row=5, column=0)
button_1 = tk.Button(root, text="8", padx=20, pady=20,
                     command=lambda : button_click(8))
button_1.grid(row=5, column=1)
button_1 = tk.Button(root, text="9", padx=20, pady=20,
                     command=lambda : button_click(9))
button_1.grid(row=5, column=2)
button_1 = tk.Button(root, text="0", padx=20, pady=20,
                     command=lambda : button_click(0))
button_1.grid(row=6, column=1)
button_plus = tk.Button(root, text="+", padx=20, pady=20,
                     command=lambda : button_click("+"))
button_plus.grid(row=3, column=3)
button_egal = tk.Button(root, text="=", padx=20, pady=20,
                     command=lambda : button_equal())
button_egal.grid(row=6, column=3)
# Démarrage de la boucle principale de l'interface
root.mainloop()
