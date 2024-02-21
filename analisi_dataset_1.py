# -*- coding: utf-8 -*-
"""ANALISI DATASET 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WOs2X1aiwm-j18ETicLbSEw9CyubsRFi

Importiamo le librerie di cui abbiamo bisogno per questa analisi:
"""

import pandas as pd
import seaborn as sns
import numpy as np

"""Scegliamo un Data Set dalla libreria Seaborn"""

sns.get_dataset_names()

"""Scegliamo il Data Set 'Titanic'"""

df = sns.load_dataset('titanic')

"""Analizziamo la composizione:"""

df.describe()

for x in df.columns:
  print(x)

df.rename(columns={'sex':'gender'}, inplace=True)

for x in df.columns:
  print(x)

"""**Iniziamo a compattare i dati per rendere il data seti più leggibile.**
Soppravisuuti per genere:
"""

df.groupby(['gender'])['survived'].sum()

graf_1 = sns.catplot(df,x='gender',y='survived', kind = 'bar')
graf_1.set(title = 'Soppravisuti per Genere')

"""Rappresentazione dell'età dei soppravisuti"""

graf_1 = sns.violinplot(df, x='gender',y='age')
graf_1.set(title = 'Soppravisuti per Età')
graf_1.set(xlabel='Soppravisuti')



df.groupby(['gender','pclass'])['survived'].sum()

graf_1 = sns.catplot(df,x='gender',y='survived', hue='pclass',kind = 'bar')
graf_1.set(title = 'Soppravisuti per Gender/Classe')
graf_1.set(xlabel='Genere')
graf_1.set(xlabel='Soppravisuti')

graf_1 = sns.swarmplot(df, x='gender',y='age', hue='pclass')
graf_1.set(title = 'Soppravisuti per Età/Classe')
graf_1.set(xlabel='Soppravisuti')

df.head(10)

"""Rielaboramo il Data frame originale per focalizzarci su una Pivot in particolare."""

df2 = df.groupby(['gender','who','alive'])['gender'].count()
df2.to_csv('pp.csv')
df2=pd.read_excel('poo.xlsx')
df_2=pd.DataFrame(df2)
print(df_2)

graf_2 = sns.catplot(df_2, x='who', y= 'Conta', hue = 'alive', kind='bar')
graf_2.set(xlabel='Categoria')
graf_2.set(ylabel='Somma')
graf_2.set(title='Conta Per Categoria')

"""Focalizziamoci su una nuova Pivot"""

df.groupby(['gender','embark_town','alive'])['alive'].count()