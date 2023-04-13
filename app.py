# Modulos importados
from tkinter import *
import os
from pathlib import Path
from glob import glob
from tkinter.filedialog import askopenfilename


# Funcao principal
def find_text():
    filePath = caminho.get()
    if filePath == "":
        texto_resultado['text'] = "destino vazio"
    else:
        lista = [item for item in termo.get().split(',')]
        lista = apagar_duplicatas(lista)

        buscas_linhas(lista, filePath)


# Chamar funcao que faz a indexacao e a comparacao dos termos com os arquivos
def buscas_linhas(lista, filePath):
    s = ""
    for x in lista:
        s += '\n termo "'+x+'", encontrado em: '
        for file in glob(filePath):
            cont = 0
            with open(file, 'r') as f:
                line_no = 0
                for lines in f:
                    line_no += 1
                    if x == "":
                        texto_resultado['text'] = "termo vazio"
                    else:
                        if x.lower() in lines.lower():
                            cont += 1
                            fileName = Path(file)
                            if (cont == 1):
                                s += (fileName.name+' \n')
                                texto_resultado['text'] = s


# Chamar funcao quando o usuario digitar os termos
def apagar_duplicatas(lista):
    return list(dict.fromkeys(lista))


# Apagar terminal
def apagar_terminal():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


# Chamar funcao quando clicar no botao
def zerar_result():
    texto_resultado["text"] = ""


# Chamar funcao para apagar placeholder quando usuario clicar na caixa de entrada
def on_click_termo(event):
    termo.configure(state=NORMAL)
    termo.delete(0, END)

    termo.unbind('<Button-1>', on_click_id_termo)


# Function para procurar os arquivos
def search_file():
    caminho.delete(0, END)
    filename = askopenfilename()
    caminho.insert(0, filename)


# Objeto Tkinter criado
root = Tk()

# Titulo criado
root.title("Buscar termos")

# Ajustando tamanho
root.geometry("901x501")

# Frame criado e posicionado
fr_quadro = Frame(root, borderwidth=2, relief="solid", background='black')
fr_quadro.place(width=900, height=500)

# Rótulo de texto do caminho adicionado
botao_search = Button(fr_quadro, width=20, text="Selecionar",
                      background='white', font=("Arial", 18), command=lambda: [zerar_result(), search_file()])
botao_search.grid(column=1, row=1)

# Caixa de entrada do caminho adicionada
caminho = Entry(fr_quadro, width=40, font=("Arial", 16))
caminho.grid(column=2, row=1, padx=10, pady=10)


# Rótulo de texto do termo adicionado
texto_termo = Label(fr_quadro, text="Digite o termo:",
                    background='white', width=20, font=("Arial", 18))
texto_termo.grid(column=1, row=2)

# Caixa de entrada do termo adicionado
termo = Entry(fr_quadro, width=40, font=("Arial", 16))
termo.grid(column=2, row=2, padx=10, pady=10)

# Criacao do Placeholder caminho
termo.insert(0, "Exemplo: a,gato,sapato,nossa senhora")
termo.configure(state=DISABLED)

# Botao criado com as definições
botao = Button(fr_quadro, text="Buscar", background='grey', font=("Arial", 14), command=lambda: [
    zerar_result(), apagar_terminal(), find_text()])
botao.grid(column=1, row=3, padx=10, pady=10)

# Resultado mostrado na janela
texto_resultado = Label(fr_quadro, background='black', foreground='white')
texto_resultado.grid(column=1, row=5)

# id on_click
on_click_id_termo = termo.bind('<Button-1>', on_click_termo)

# Executar Tkinter
root.mainloop()
