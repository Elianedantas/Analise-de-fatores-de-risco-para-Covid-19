import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import Perceptron

#importando a base de dados atraves do gitHub
url = 'https://raw.githubusercontent.com/Elianedantas/Analise-de-fatores-de-risco-para-Covid-19/main/Registros_Casos_e_obitos_ESP.csv'
base_Treinamento = pd.read_csv(url,sep=',', encoding = 'utf-8').values

#normalizando os dados
def normalizarDados(base_Treinamento):
    # Binarizador de rótulo
    lb = preprocessing.LabelBinarizer()

    #Transforma valores categóricos equidistantes em valores binários equidistantes.
    #Atributos categóricos com valores sim e não
    lb.fit(['SIM', 'NÃO'])
    Asma = lb.transform(base_Treinamento[:,0])
    Cardiopatia = lb.transform(base_Treinamento[:,1])
    Diabetes = lb.transform(base_Treinamento[:,3])
    Doenca_Hepatica = lb.transform(base_Treinamento[:,6])
    Doenca_Neurologica = lb.transform(base_Treinamento[:,7])
    Doenca_Renal = lb.transform(base_Treinamento[:,8])
    Obesidade = lb.transform(base_Treinamento[:,13])
    Pneumopatia = lb.transform(base_Treinamento[:,16])    
    Síndrome_De_Down = lb.transform(base_Treinamento[:,18])

    min_max = preprocessing.MinMaxScaler()
    Idade = min_max.fit_transform(base_Treinamento[:,10].reshape(-1, 1))

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
    diagnostico_norm = list(map(int, base_Treinamento[:, 14]))

    modelo = treinarRedePerceptron(dadosT, diagnostico_norm)

    teste = [[Asma, Cardiopatia, Diabetes, Doenca_Hepatica, Doenca_Neurologica, Doenca_Renal, Idade, Obesidade, Pneumopatia, Síndrome_De_Down]]

    min_max = preprocessing.MinMaxScaler()
    testeT = min_max.fit_transform(teste)
    return modelo.predict(testeT)
