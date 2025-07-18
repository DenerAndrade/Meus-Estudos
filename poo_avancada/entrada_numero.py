import tkinter as tk
from tkinter import simpledialog, messagebox

# Cria janela principal oculta
root = tk.Tk()
root.withdraw()

# Pede o número com caixa de diálogo
numero_str = simpledialog.askstring("Entrada", "Digite um número:")

if numero_str is not None:
    try:
        numero = float(numero_str)  # tenta converter para número
        messagebox.showinfo("Resultado", f"Você digitou o número: {numero}")
    except ValueError:
        messagebox.showerror("Erro", "Valor digitado não é um número válido!")
else:
    messagebox.showinfo("Cancelado", "Nenhum número foi digitado.")

# Fecha a janela principal
root.destroy()
