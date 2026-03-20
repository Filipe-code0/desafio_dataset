# desafio_dataset

## Arquivos

    "dataset_desafio_tainees_excel.xlsx" = Arquivo de planilha com as formulas
    "dataset_desafio_tainees_excel.xlsx" = Arquivo de planilha usado no codigo
    "dataset.py" = Arquivo .py do programa

## Conclusões

### Estatística Descritiva

Foi possível notar que a diferença entre a média e a mediana não é muito alta, o que indica que a distribuição dos dados é aproximadamente simétrica, significando que não existem muitos valores extremos que possam distorcer a análise. Esse fato tem mais respaldo com a análise dos quartis que têm uma distância parecida entre um e outro.

### Análise de Correlação

É possível notar que o coeficiente de correlação entre horas estudadas e notas é grande (0.9966), e que o mesmo acontece com aulas assistidas e notas (0.9947). Isto indica uma forte correlação positiva entre a quantidade de horas estudadas e a nota na prova, ou seja, no geral, as notas tendem a aumentar com mais horas de estudo e o contrário também. Porém, essa relação não necessariamente expressa causalidade.

### Teste de Hipótese

Para comprovar a hipótese, a análise foi dividida em dois grupos de alunos, os que estudaram 10 horas ou menos e os que estudaram mais de 10 horas. Utilizando a média da nota como métrica, foi aferido que alunos que estudaram menos de 10 horas se saíram pior na prova se comparado aos que estudaram mais de 10 horas, o que fornece evidências que apoiam a hipótese inicial.