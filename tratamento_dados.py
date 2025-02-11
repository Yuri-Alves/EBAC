from hmac import digest_size
from itertools import groupby

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from setuptools.command.rotate import rotate

df = pd.read_csv('MODULO7_PROJETOFINAL_BASE_SUPERMERCADO.csv')
print(df.head().to_string())

# 1(- criando variaveis para alocar os valores da media e mediana
media_categoria = df.groupby('Categoria')['Preco_Normal'].mean()
mediana_preco = df.groupby('Categoria')['Preco_Normal'].median()

#Cria novas colunas no DF abordando a media e a mediana
df['Media_Preco_Categoria'] = df['Categoria'].map(media_categoria)
df['MediaNA_Preco_Categoria'] = df['Categoria'].map(mediana_preco)
print(df.head().to_string())

#Cria nova coluna, se baseando na condição de ser acima da mediana
df['Acima_Mediana'] = df['Media_Preco_Categoria'] > df['MediaNA_Preco_Categoria']

#Para apresentar de forma mais limpa o DF sem necessitar ficar procurando por categorias -)
df_unique = df[['Categoria', 'Media_Preco_Categoria', 'MediaNA_Preco_Categoria', 'Acima_Mediana']].drop_duplicates(subset=['Categoria'])

print(df_unique.to_string(index=False))

#2 (- Criando a variavel para alocar o valor do Desvio Padrão
desvio_padrao = df.groupby('Categoria')['Preco_Normal'].std()

#Incluindo o desvio dentro do DF
df['Desvio_Padrao'] = df['Categoria'].map(desvio_padrao)

#Apresentando o DF da forma mais limpa com o Desvio Padrao
df_unique = df[['Categoria', 'Media_Preco_Categoria', 'MediaNA_Preco_Categoria', 'Desvio_Padrao']].drop_duplicates(subset=['Categoria'])
print(df_unique.to_string(index=False))
#Quanto mais próximo o valor da Média e da Mediana, menor o valor do Desvio Padrão -)

# 3 (- Filtrando apenas os valores da categoria lacteos
df_lacteos = df[df['Categoria'] == 'lacteos']

# Criando o boxplot para a coluna Preco Normal
plt.figure(figsize=(10, 8))
plt.boxplot(df_lacteos['Preco_Normal'], vert=True, patch_artist=True)
plt.title("Boxplot de Preço - Categoria: Lacteos")
plt.ylabel("Preço Normal")
plt.show()
#O gráfico apresenta uma grande quantidade de Ouliers -)

#4 Criado o gráfico de barras
plt.figure(figsize=(10,8))
desconto_por_categoria = df.groupby('Categoria')['Preco_Desconto'].mean()
plt.bar(desconto_por_categoria.index, desconto_por_categoria, color='orange')
plt.title('Distribuição de descontos por categoria', fontsize=16)
plt.xlabel('Categoria')
plt.ylabel('Média de descontos')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--',alpha=0.7)
plt.show()

#5- Criando o gráfico de mapas

desconto_por_marca_categoria = df.groupby(['Categoria', 'Marca'])['Preco_Desconto'].mean().reset_index()

fig= px.treemap(desconto_por_marca_categoria,path=['Categoria','Marca'],values='Preco_Desconto',title='Desconto por Categoria e Marca',
                color='Marca')

fig.show()