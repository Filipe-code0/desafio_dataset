import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\futura\Desafio_dataset\dataset_desafio_trainees_python.csv", sep=';', decimal=',')
df = df.dropna(axis=1, how='all')

tmp = df.to_numpy()
dados = []
for i in range(0, tmp.shape[0]):
    for j in range(0, tmp.shape[1]):
        if j == 6:
            dados.append(tmp[i][j])

avg = np.average(dados)
med = np.median(dados)
des = np.std(dados)
print(avg, med, des)
