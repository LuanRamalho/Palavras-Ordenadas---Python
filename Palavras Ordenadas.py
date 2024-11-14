import tkinter as tk
from tkinter import messagebox

# Inicialização da janela principal
root = tk.Tk()
root.title("Gerenciador de Palavras")
root.geometry("500x500")
root.configure(bg="#f5f5f5")

# Lista para armazenar as palavras
words = []

# Função para atualizar a exibição das palavras na interface
def display_words():
    word_list.delete(0, tk.END)
    for word in words:
        word_list.insert(tk.END, word)

# Função para adicionar uma palavra
def add_word():
    word = word_input.get().strip()
    if word and word not in words:
        words.append(word)
        word_input.delete(0, tk.END)
        display_words()
    else:
        messagebox.showinfo("Info", "Palavra inválida ou já existe na lista.")

# Função para remover uma palavra
def remove_word():
    word = word_input.get().strip()
    if word in words:
        words.remove(word)
        word_input.delete(0, tk.END)
        display_words()
    else:
        messagebox.showinfo("Info", "Palavra não encontrada na lista.")

# Função para ordenar as palavras
def sort_words(order):
    words.sort(reverse=(order == 'desc'))
    display_words()

# Função para preencher a caixa de entrada com a palavra selecionada
def on_select(event):
    selected_word = word_list.get(word_list.curselection())
    word_input.delete(0, tk.END)
    word_input.insert(tk.END, selected_word)

# Interface gráfica
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=10)

word_input = tk.Entry(frame, font=("Segoe UI", 14), width=25, borderwidth=2, relief="solid")
word_input.pack(pady=5)

add_button = tk.Button(frame, text="Adicionar Palavra", font=("Segoe UI", 12), bg="#007bff", fg="#fff", width=15, command=add_word)
add_button.pack(pady=5)

remove_button = tk.Button(frame, text="Remover Palavra", font=("Segoe UI", 12), bg="#007bff", fg="#fff", width=15, command=remove_word)
remove_button.pack(pady=5)

word_list = tk.Listbox(root, font=("Segoe UI", 12), bg="#007bff", fg="#fff", width=30, height=10, selectbackground="#0056b3", borderwidth=0, highlightthickness=0)
word_list.pack(pady=10)
word_list.bind("<<ListboxSelect>>", on_select)  # Liga o evento de seleção à função on_select

sort_asc_button = tk.Button(root, text="Ordem Crescente", font=("Segoe UI", 12), bg="#007bff", fg="#fff", width=15, command=lambda: sort_words('asc'))
sort_asc_button.pack(pady=5)

sort_desc_button = tk.Button(root, text="Ordem Decrescente", font=("Segoe UI", 12), bg="#007bff", fg="#fff", width=15, command=lambda: sort_words('desc'))
sort_desc_button.pack(pady=5)

# Inicia o loop principal do tkinter
root.mainloop()
