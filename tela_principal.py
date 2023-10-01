from tkinter import *
import algoritimo as a
from tkinter import messagebox

def diagnosticar():

    if a.Treinar(radio_Asma.get(), radio_Cardiopatia.get(), radio_Diabetes.get(), radio_Doenca_Hepatica.get(), 
        radio_Doenca_Neurologica.get(), radio_Doenca_Renal.get(), box_Idade.get(), radio_Obesidade.get(), 
        radio_Pneumopatia.get(), radio_Síndrome_De_Down.get()) == 1:
        messagebox.showwarning(title="Resultado do diagnóstico",
        message='Você possui maiores fatores de risco para a covid-19.')     
    else:
        messagebox.showinfo(title="Resultado do diagnóstico",
        message='Você não possui maiores fatores de risco para a covid-19.')
            
janela = Tk()

radio_Asma = IntVar()
radio_Cardiopatia = IntVar()
radio_Diabetes = IntVar()
radio_Doenca_Hepatica = IntVar()
radio_Doenca_Neurologica = IntVar()
radio_Doenca_Renal = IntVar()
box_Idade = IntVar()
radio_Obesidade = IntVar()
radio_Pneumopatia = IntVar()
radio_Síndrome_De_Down = IntVar()

janela.title("Fatores de risco para Covid-19")
largura = 800
altura = 600
pos_x = (janela.winfo_screenwidth() // 2) - (largura // 2)  # Centraliza horizontalmente
pos_y = (janela.winfo_screenheight() // 2) - (altura // 2)  # Centraliza verticalmente
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")  # Defina a geometria da janela

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

janela.title("Fatores de risco para Covid-19")

frame_principal = Frame(janela, bg="#C0C0C0")
frame_principal.pack(fill="both", expand=True)

canvas = Canvas(frame_principal, bg="#C0C0C0")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

frame_interno = Frame(canvas, bg="#C0C0C0")
canvas.create_window((0, 0), window=frame_interno, anchor="nw")

titulo1 = Label(frame_interno, 
                text="Fatores de risco para Covid-19",
                font=("Roboto", 20),
                bg="#C0C0C0",
                relief="groove",
                border=1
                )
titulo1.grid(column=0, row=0, columnspan=2, pady=(0, 17), padx=20, sticky="w")  # Alinhe à esquerda

perguntas_respostas = [
    ("Possui asma?", radio_Asma),
    ("Possui cardiopatia?", radio_Cardiopatia),
    ("Possui diabetes?", radio_Diabetes),
    ("Possui doença hepática?", radio_Doenca_Hepatica),
    ("Possui doença neurológica?", radio_Doenca_Neurologica),
    ("Possui doença renal?", radio_Doenca_Renal),
    ("Possui obesidade?", radio_Obesidade),
    ("Possui pneumopatia?", radio_Pneumopatia),
    ("Possui Síndrome de Down?", radio_Síndrome_De_Down),
    ("Idade:", box_Idade)
]

coluna = 0
linha = 1
largura_maxima_coluna = 800

for pergunta, variavel in perguntas_respostas:
    label_pergunta = Label(frame_interno, text=pergunta, font=("Roboto", 13), bg="#C0C0C0", anchor="w")
    label_pergunta.grid(column=coluna, row=linha, padx=20, pady=(10, 0), sticky="w")  # Alinhe à esquerda
    
    if pergunta == "Idade:":
        label_idade = Label(frame_interno, font=("Roboto", 13), bg="#C0C0C0", anchor="w")
        label_idade.grid(column=coluna, row=linha+1, padx=20, pady=(0, 5), sticky="w")
        
        entrada_idade = Entry(frame_interno, textvariable=box_Idade, font=("Roboto", 13))
        entrada_idade.grid(column=coluna, row=linha+2, padx=20, pady=(0, 10))
    
    else:
        radio_sim = Radiobutton(frame_interno, text="Sim", variable=variavel, value=1, font=("Roboto", 13), bg="#C0C0C0")
        radio_sim.grid(column=coluna, row=linha+1, padx=20, pady=(0, 10))
        
        radio_nao = Radiobutton(frame_interno, text="Não", variable=variavel, value=0, font=("Roboto", 13), bg="#C0C0C0")
        radio_nao.grid(column=coluna + 1, row=linha+1, padx=20, pady=(0, 10))
    

    coluna += 2
    
    if coluna * 800 >= largura_maxima_coluna:
        coluna = 0
        linha += 3
        
botaoDiagnostico = Button(frame_interno,
                          text='Realizar Diagnóstico',
                          fg='white',
                          bg='green',
                          command=diagnosticar,
                          font=("Roboto", 13),
                          relief="ridge",
                          border=2,
                          )
botaoDiagnostico.grid(column=0, row=linha+3, columnspan=2, pady=20, padx=20)

botaoFechar = Button(frame_interno,
                     text='Fechar',
                     fg='white',
                     bg='Red',
                     command=janela.quit,  # Use janela.quit para fechar a janela principal
                     font=("Roboto", 13),
                     relief="ridge",
                     border=2,
                     )
botaoFechar.grid(column=0, row=linha+4, columnspan=2, sticky="w", padx=20)

canvas.bind("<Configure>", on_canvas_configure)

janela.mainloop()