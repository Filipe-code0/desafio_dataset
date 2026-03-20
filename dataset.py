import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\futura\Desafio_dataset\dataset_desafio_trainees_python.csv", sep=';', decimal=',')

nota = df['nota_final']
horas_estudo = df['horas_estudo']
faltas = df['faltas']
aulas_assistidas = df['aulas_assistidas']

#Estatisticas Descritivas

avg = np.average(nota)
med = np.median(nota)
des = np.std(nota)
qua_1 = np.quantile(nota,.25)
qua_2 = np.quantile(nota,.50)
qua_3 = np.quantile(nota,.75)

print(f'media: {avg:.2f}, mediana: {med:.2f}, desvio padrão: {des:.2f}\n1 quartil: {qua_1:.2f}, 2 quartil: {qua_2:.2f}, 3 quartil: {qua_3:.2f}')

#Correlações

cor_nota_horas = np.corrcoef(nota, horas_estudo)[0][1]
cor_nota_aulas = np.corrcoef(nota, aulas_assistidas)[0][1]

print(f'correlação entre notas e horas estudadas: {cor_nota_horas:.4f}')
print(f'correlação entre notas e aulas assistidas: {cor_nota_aulas:.4f}')

#teste de hipotese

grupo_ate_10 = df[df['horas_estudo'] <= 10]
grupo_mais_10 = df[df['horas_estudo'] > 10]
notas_grupo_ate_10 = grupo_ate_10['nota_final']
notas_grupo_mais_10 = grupo_mais_10['nota_final']

med_grupo_ate_10 = np.average(notas_grupo_ate_10)
med_grupo_mais_10 = np.average(notas_grupo_mais_10)

print(f'media dos alunos com menos de 10 horas estudadas: {med_grupo_ate_10:.2f}')
print(f'media dos alunos com mais de 10 horas estudadas: {med_grupo_mais_10:.2f}')
