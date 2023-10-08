import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

#importando a base de dados atraves do gitHub
url = 'https://raw.githubusercontent.com/Elianedantas/Analise-de-fatores-de-risco-para-Covid-19/main/Registros_Casos_e_obitos_ESP.csv'
base_Treinamento = pd.read_csv(url,sep=',', encoding = 'utf-8').values

#normalizando os dados
min_max = preprocessing.MinMaxScaler()
#normalizando os dados
def normalizarDados(base_Treinamento):
    return min_max.fit_transform(base_Treinamento[:,:9])

#treinando a rede Knn
def treinarRedeKNN(atributos_norm,diagnostico_norm):
    modelo = KNeighborsClassifier(n_neighbors = 7)
    modelo.fit(atributos_norm, diagnostico_norm)
    return modelo

def Treinar(Anemia,Cardiopatia,Diabetes,Doenca_Hematologica,Doenca_Hepatica,Doenca_Neurologica,Doenca_Renal,Idade,Obesidade,Pneumopatia):
    dadosT = normalizarDados(base_Treinamento)
    diagnostico_norm = base_Treinamento[:, 9]
    modelo = treinarRedeKNN(dadosT,diagnostico_norm)
    
    teste = [[Anemia,Cardiopatia,Diabetes,Doenca_Hematologica,Doenca_Hepatica,Doenca_Neurologica,Doenca_Renal,Idade,Obesidade,Pneumopatia]]
    testeT = min_max.transform(teste)
    return modelo.predict(testeT)
