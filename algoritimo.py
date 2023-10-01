import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import Perceptron

#importando a base de dados atraves do gitHub
url = 'https://raw.githubusercontent.com/Elianedantas/Analise-de-fatores-de-risco-para-Covid-19/main/Registros_Casos_e_obitos_ESP.csv'
base_Treinamento = pd.read_csv(url,sep=',', encoding = 'latin1').values

#normalizando os dados
def normalizarDados(base_Treinamento):
    # Binarizador de rótulo
    lb = preprocessing.LabelBinarizer()

    #Transforma valores categóricos equidistantes em valores binários equidistantes.
    #Atributos categóricos com valores sim e não
    lb.fit(['SIM', 'IGNORADO', 'NÃO'])
    Asma = lb.transform(base_Treinamento[:,1])
    Cardiopatia = lb.transform(base_Treinamento[:,2])
    Diabetes = lb.transform(base_Treinamento[:,4])
    Doenca_Hepatica = lb.transform(base_Treinamento[:,7])
    Doenca_Neurologica = lb.transform(base_Treinamento[:,8])
    Doenca_Renal = lb.transform(base_Treinamento[:,9])
    Obesidade = lb.transform(base_Treinamento[:,14])
    Pneumopatia = lb.transform(base_Treinamento[:,17])    
    Síndrome_De_Down = lb.transform(base_Treinamento[:,19])

    min_max = preprocessing.MinMaxScaler()
    Idade = min_max.fit_transform(base_Treinamento[:,11])

    #Concatenação de Atributos (Colunas)
    atributos_norm = np.column_stack((Asma,Cardiopatia,Diabetes,Doenca_Hepatica,Doenca_Neurologica,Doenca_Renal,Idade,Obesidade,
                                      Pneumopatia,Síndrome_De_Down))
    return atributos_norm

def treinarRedePerceptron(atributos_norm, diagnostico_norm):
    modelo =  Perceptron()
    modelo.fit(atributos_norm, diagnostico_norm)
    return modelo

def Treinar(Asma,Cardiopatia,Diabetes,Doenca_Hepatica,Doenca_Neurologica,Doenca_Renal,Idade,Obesidade,Pneumopatia,Síndrome_De_Down):
    dadosT = normalizarDados(base_Treinamento)
    diagnostico_norm = base_Treinamento[:, 15]

    modelo = treinarRedePerceptron(dadosT, diagnostico_norm)

    teste = [[Asma, Cardiopatia, Diabetes, Doenca_Hepatica, Doenca_Neurologica, Doenca_Renal, Idade, Obesidade, Pneumopatia, Síndrome_De_Down]]

    min_max = preprocessing.MinMaxScaler()
    testeT = min_max.transform(teste)
    return modelo.predict(testeT)