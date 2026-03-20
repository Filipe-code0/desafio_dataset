import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\futura\Desafio_dataset\dataset_desafio_trainees_python.csv", sep=';', decimal=',')
df = df.dropna(axis=1, how='all')

tmp = df.to_numpy()
nota = []
horas_estudo = []
aulas_assistidas = []

for i in range(0, tmp.shape[0]):
    for j in range(0, tmp.shape[1]):
        if j == 3:
            horas_estudo.append(tmp[i][j])
        if j == 4:
            aulas_assistidas.append(tmp[i][j])
        if j == 6:
            nota.append(tmp[i][j])


avg = np.average(nota)
med = np.median(nota)
des = np.std(nota)
qua_1 = np.quantile(nota,.25)
qua_2 = np.quantile(nota,.50)
qua_3 = np.quantile(nota,.75)

print(f'media: {avg}, mediana: {med}, desvio padrão: {des}\n1 quartil: {qua_1}, 1 quartil: {qua_2}, 1 quartil: {qua_3}')

#Correlações

cor_nota_horas = np.corrcoef(nota, horas_estudo)
cor_nota_aulas = np.corrcoef(nota, aulas_assistidas)

print(f'correlação entre notas e horas estudadas{cor_nota_horas}')
print(f'correlação entre notas e aulas assistidas{cor_nota_aulas}')
