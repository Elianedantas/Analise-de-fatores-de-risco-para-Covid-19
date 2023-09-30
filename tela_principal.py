from tkinter import *
import algoritimo as a
from tkinter import messagebox

def diagnosticar():
    if a.Treinar(radio_Asma.get(),radio_Cardiopatia.get(),radio_Diabetes.get(),radio_Doenca_Hepatica.get(),
                 radio_Doenca_Neurologica.get(),radio_Doenca_Renal.get(),box_Idade.get(), radio_Obesidade.get(),
                 radio_Pneumopatia.get(),radio_Síndrome_De_Down.get()) == 1:
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
janela.geometry("%dx%d+%d+%d"% (520,300,400,200))
janela = Frame(janela,bg="#C0C0C0")
janela.pack() 
titulo1 = Label(janela, 
                   text="Fatores de risco para Covid-19",
                   font="Roboto 20",
                   bg = "#C0C0C0",
                   relief="groove",
                   border=1
                   )
titulo1.grid(column=0, row=0, columnspan=5, pady=17)

titulo2 = Label(janela, 
                   text="Possui asma?",
                   font="Roboto 13",
                   bg = "#C0C0C0"
                   )
radioSim2 = Radiobutton(janela, 
                        text="Sim",
                        variable=radio_Asma,
                        value=1,
                        font="Roboto 13",
                        bg = "#C0C0C0"
                        )
radioNao2 = Radiobutton(janela, 
                        text= "Não", 
                        variable=radio_Asma, 
                        value=0,
                        font="Roboto 13",
                        bg = "#C0C0C0"
                        )
titulo2.grid(column=0, row=1)
radioSim2.grid(column=0, row=2)
radioNao2.grid(column=1, row=2)


titulo3 = Label(janela, 
                   text="Possui Cardiopatia?",
                   font="Roboto 13",
                   bg = "#C0C0C0"
                   )
radioSim3 = Radiobutton(janela, 
                            text="Sim",
                            variable=radio_Cardiopatia,
                            value=1,
                            font="Roboto 13",
                            bg = "#C0C0C0"
                            )
radioNao3 = Radiobutton(janela, 
                           text= "Não", 
                           variable=radio_Cardiopatia, 
                           value=0,
                           font="Roboto 13",
                           bg = "#C0C0C0"
                           )
titulo3.grid(column=2, row=1,columnspan=5)
radioSim3.grid(column=2, row=2)
radioNao3.grid(column=3, row=2)

titulo4 = Label(janela, 
                   text="Possui Diabetes?",
                   font="Roboto 13",
                   bg = "#C0C0C0"
                   )
radioSim4 = Radiobutton(janela, 
                        text="Sim",
                        variable=radio_Diabetes,
                        value=1,
                        font="Roboto 13",
                        bg = "#C0C0C0"
                        )
radioNao4 = Radiobutton(janela, 
                       text= "Não", 
                       variable=radio_Diabetes, 
                       value=0,
                       font="Roboto 13",
                       bg = "#C0C0C0"
                       )
titulo4.grid(column=4, row=1,columnspan=5)
radioSim4.grid(column=2, row=2)
radioNao4.grid(column=3, row=2)

titulo5 = Label(janela, 
                   text="Possui Doença Hepática?",
                   font="Roboto 13",
                   bg = "#C0C0C0"
                   )
radioSim5 = Radiobutton(janela, 
                        text="Sim",
                        variable=radio_Doenca_Hepatica,
                        value=1,
                        font="Roboto 13",
                        bg = "#C0C0C0"
                        )
radioNao5 = Radiobutton(janela, 
                       text= "Não", 
                       variable=radio_Doenca_Hepatica, 
                       value=0,
                       font="Roboto 13",
                       bg = "#C0C0C0"
                       )
titulo5.grid(column=4, row=1,columnspan=5)
radioSim5.grid(column=2, row=2)
radioNao5.grid(column=3, row=2)

titulo6 = Label(janela, 
                   text="Possui Doença Neurológica?",
                   font="Roboto 13",
                   bg = "#C0C0C0"
                   )
radioSim6 = Radiobutton(janela, 
                        text="Sim",
                        variable=radio_Doenca_Hepatica,
                        value=1,
                        font="Roboto 13",
                        bg = "#C0C0C0"
                        )
radioNao6 = Radiobutton(janela, 
                       text= "Não", 
                       variable=radio_Doenca_Hepatica, 
                       value=0,
                       font="Roboto 13",
                       bg = "#C0C0C0"
                       )
titulo6.grid(column=4, row=1,columnspan=5)
radioSim6.grid(column=2, row=2)
radioNao6.grid(column=3, row=2)

titulo7 = Label(janela, 
                   text="Possui Doença Renal?",
                   font="Roboto 13",
                   bg = "#C0C0C0"
                   )
radioSim7 = Radiobutton(janela, 
                        text="Sim",
                        variable=radio_Doenca_Renal,
                        value=1,
                        font="Roboto 13",
                        bg = "#C0C0C0"
                        )
radioNao7 = Radiobutton(janela, 
                       text= "Não", 
                       variable=radio_Doenca_Renal, 
                       value=0,
                       font="Roboto 13",
                       bg = "#C0C0C0"
                       )
titulo7.grid(column=4, row=1,columnspan=5)
radioSim7.grid(column=2, row=2)
radioNao7.grid(column=3, row=2)

titulo8 = Label(janela, 
                   text="Possui Obesidade?",
                   font="Roboto 13",
                   bg = "#C0C0C0"
                   )
radioSim8 = Radiobutton(janela, 
                        text="Sim",
                        variable=radio_Obesidade,
                        value=1,
                        font="Roboto 13",
                        bg = "#C0C0C0"
                        )
radioNao8 = Radiobutton(janela, 
                       text= "Não", 
                       variable=radio_Obesidade, 
                       value=0,
                       font="Roboto 13",
                       bg = "#C0C0C0"
                       )
titulo8.grid(column=4, row=1,columnspan=5)
radioSim8.grid(column=2, row=2)
radioNao8.grid(column=3, row=2)

titulo9 = Label(janela, 
                   text="Possui Pneumopatia?",
                   font="Roboto 13",
                   bg = "#C0C0C0"
                   )
radioSim9 = Radiobutton(janela, 
                        text="Sim",
                        variable=radio_Pneumopatia,
                        value=1,
                        font="Roboto 13",
                        bg = "#C0C0C0"
                        )
radioNao9 = Radiobutton(janela, 
                       text= "Não", 
                       variable=radio_Pneumopatia, 
                       value=0,
                       font="Roboto 13",
                       bg = "#C0C0C0"
                       )
titulo9.grid(column=4, row=1,columnspan=5)
radioSim9.grid(column=2, row=2)
radioNao9.grid(column=3, row=2)

titulo10 = Label(janela, 
                   text="Possui Pneumopatia?",
                   font="Roboto 13",
                   bg = "#C0C0C0"
                   )
radioSim10 = Radiobutton(janela, 
                        text="Sim",
                        variable=radio_Pneumopatia,
                        value=1,
                        font="Roboto 13",
                        bg = "#C0C0C0"
                        )
radioNao10 = Radiobutton(janela, 
                       text= "Não", 
                       variable=radio_Pneumopatia, 
                       value=0,
                       font="Roboto 13",
                       bg = "#C0C0C0"
                       )
titulo10.grid(column=4, row=1,columnspan=5)
radioSim10.grid(column=2, row=2)
radioNao10.grid(column=3, row=2)

idade = Label(janela,
              text="Idade:",
              bg= "#C0C0C0"
            )
idade.grid(column= 0, row=4,columnspan=5, sticky="w")
valorIdade = Entry(janela,textvariable=box_Idade,relief="solid")
valorIdade.grid(column=0, row =5,padx=3)

botaoDiagnostico = Button(janela,
               text='Realizar Diagnóstico',
               fg = 'white', 
               bg = 'green',
               command=diagnosticar,
               font="Roboto 13",
               relief="ridge",
               border=2,
               )
botaoDiagnostico.grid(column=0, row=7,columnspan=5,pady=20)

botaoFechar = Button(janela,text='Fechar',
               fg = 'white', 
               bg = 'Red',
               command=quit,
               font="Roboto 13",
               relief="ridge",
               border=2,
               )
botaoFechar.grid(column=1, row=8,columnspan=5,sticky="w")

janela.mainloop()

