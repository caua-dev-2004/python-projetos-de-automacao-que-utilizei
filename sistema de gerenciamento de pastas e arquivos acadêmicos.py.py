import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
import os
import pyperclip 

def encontrar_pasta_com_matricula(matricula, diretorio):
    try:
        pastas = os.listdir(diretorio)
        for pasta in pastas:
            if matricula in pasta:
                return os.path.join(diretorio, pasta)
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao tentar listar as pastas: {e}")
        return None

def acessar_pasta():
    matricula = name_entry.get().strip()
    if matricula:
        diretorio_matriculas = r"\\SERVIDOR\Rede Lab2\Alunos(atalhos)"
        pasta_encontrada = encontrar_pasta_com_matricula(matricula, diretorio_matriculas)
        if pasta_encontrada:
            os.startfile(pasta_encontrada)
        else:
            messagebox.showerror("Erro", "Pasta correspondente à matrícula não encontrada.")
    else:
        messagebox.showwarning("Aviso", "Por favor, insira a matrícula.")

def copiar_caminho():
    matricula = name_entry.get().strip()
    if matricula:
        diretorio_matriculas = r"\\SERVIDOR\Rede Lab2\Alunos(atalhos)"
        pasta_encontrada = encontrar_pasta_com_matricula(matricula, diretorio_matriculas)
        if pasta_encontrada:
            pyperclip.copy(pasta_encontrada)
            messagebox.showinfo("Caminho Copiado", f"O caminho da pasta foi copiado:\n{pasta_encontrada}")
        else:
            messagebox.showerror("Erro", "Pasta correspondente à matrícula não encontrada.")
    else:
        messagebox.showwarning("Aviso", "Por favor, insira a matrícula.")

root = tk.Tk()
root.title("Sistema Acadêmico")
root.geometry("650x250")
root.configure(bg="#084d6e")


try:
    img = Image.open("logo.png")
    img = img.resize((250, 80), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
except Exception as e:
    img_tk = None
    print(f"Erro ao carregar a imagem: {e}")

frame_top = tk.Frame(root)
frame_top.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
frame_top.configure(bg="#084d6e")

if img_tk:
    label_img = tk.Label(frame_top, image=img_tk, bg="#084d6e")
    label_img.pack(pady=5)
else:
    label = tk.Label(frame_top, bg="#084d6e", font=('impact', 20, 'bold'), fg='light blue', text="Onbyte Penha")
    label.pack(pady=5)

name_label = tk.Label(frame_top, text='Digite sua matrícula', font=('georgia', 15, 'bold'), foreground='white')
name_label.configure(background="#084d6e")
name_label.pack(pady=0)
name_entry = tk.Entry(frame_top, font=('arial black', 15, 'bold'), fg='white', width=15)
name_entry.configure(background="#084d6e")
name_entry.pack(pady=2)

frame_bottom = tk.Frame(root)
frame_bottom.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=20)
frame_bottom.configure(bg="#084d6e")

frame_bottom.grid_columnconfigure(0, weight=1)
frame_bottom.grid_columnconfigure(1, weight=1)

botao_pasta = tk.Button(frame_bottom, text="Acessar minha pasta", command=acessar_pasta, font=('calibri', 16, 'bold'), bg="#084d6e", fg='white')
botao_pasta.grid(row=0, column=0, padx=10, pady=2, sticky="ew")

botao_copiar_caminho = tk.Button(frame_bottom, text="Copiar caminho", command=copiar_caminho, font=('calibri', 16, 'bold'), bg="#084d6e", fg='white')
botao_copiar_caminho.grid(row=0, column=1, padx=10, pady=2, sticky="ew")

root.mainloop()
