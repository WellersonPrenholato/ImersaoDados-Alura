# -*- coding: utf-8 -*-
import pandas as pd

fonte = "https://github.com/WellersonPrenholato/ImersaoDados-Alura/blob/main/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

dados = pd.read_csv(fonte)
dados.head()

dados.shape

dados["SG_UF_RESIDENCIA"]

dados.columns.values

dados[["SG_UF_RESIDENCIA", "Q025"]]

dados["SG_UF_RESIDENCIA"]

dados["SG_UF_RESIDENCIA"].unique()

len(dados["SG_UF_RESIDENCIA"].unique())

dados["SG_UF_RESIDENCIA"].value_counts()

dados["NU_IDADE"].value_counts()

dados["NU_IDADE"].value_counts().sort_index()

dados["NU_IDADE"].hist()

dados["NU_IDADE"].hist(bins = 20, figsize = (10,8))



dados.query("IN_TREINEIRO == 1")["NU_IDADE"].value_counts().sort_index()

dados["NU_NOTA_REDACAO"].hist(bins = 20, figsize=(8, 6))

dados["NU_NOTA_LC"].hist(bins = 20, figsize=(8, 6))

dados["NU_NOTA_REDACAO"].mean()

dados["NU_NOTA_REDACAO"].std()

provas = ["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_MT","NU_NOTA_LC","NU_NOTA_REDACAO"]

dados[provas].describe()

dados["NU_NOTA_LC"].quantile(0.1)

dados["NU_NOTA_LC"].plot.box(grid = True, figsize=(8,6))

dados[provas].boxplot(grid=True, figsize= (10,8))

"""Desafio01: Proporção dos inscritos por idade.

Desafio02: Descobrir de quais estados são os inscritos com 13 anos.

Desafio03: Adicionar título no gráfico

Desafio04: Plotar os Histogramas das idades dos do treineiro e não treineiros.

Desafio05: Comparar as distribuições das provas em inglês espanhol

Desafio06: Explorar a documentações e visualizações com matplotlib ou pandas e gerar novas visualizações.
"""

