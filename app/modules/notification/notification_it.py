import tkinter as tk


def mostrar_notificacao(titulo, mensagem):
    janela = tk.Tk()
    janela.title(titulo)

    # Tamanho da janela
    largura = 350
    altura = 100

    # Posição no canto inferior direito
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()

    x = tela_largura - largura - 20
    y = tela_altura - altura - 60

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

    # Mantém a janela na frente
    janela.attributes("-topmost", True)

    # Remove a barra de título
    janela.overrideredirect(True)

    # Conteúdo
    label_titulo = tk.Label(
        janela,
        text=titulo,
        font=("Arial", 12, "bold")
    )
    label_titulo.pack(pady=(15, 5))

    label_mensagem = tk.Label(
        janela,
        text=mensagem,
        font=("Arial", 10)
    )
    label_mensagem.pack()

    # Fecha automaticamente depois de 5 segundos
    janela.after(5000, janela.destroy)

    janela.mainloop()
