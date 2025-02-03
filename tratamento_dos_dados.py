import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('ecommerce_preparados.csv')
print(df.head().to_string())

#Gráfico de Barras
plt.figure(figsize=(10,6))
df['Nota'].value_counts().plot(kind = 'bar', color = '#90ee70')
plt.title('Quantidade de Notas')
plt.xlabel('Notas')
plt.ylabel('Quantidade')
plt.xticks(rotation = 0)
plt.show()

#Gráfico de pizza
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values

plt.figure(figsize=(10,6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Gêneros dos Produtos')
plt.show()

#Gráfico de dispersão
plt.hexbin(df['Preço'], df['Qtd_Vendidos_Cod'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Preço')
plt.ylabel('Quantidade vendidos')
plt.title('Dispersão de Preço e Quantidade de vendas')
plt.show()


#Gráfico de Regressão
sns.regplot(x='Nota', y='N_Avaliações', data= df, color = '#278f65', scatter_kws={'alpha':0.5, 'color': '#34c289'})
plt.title('Regressão de Nota por Número de avaliações')
plt.xlabel('Nota')
plt.ylabel('Número de Avaliações')
plt.show()

#Grafico de densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
plt.title('Densidade de Preços')
plt.xlabel('Preços')
plt.show()

#Gráfico de calor
corr = df[['Preço', 'Qtd_Vendidos_Cod']].corr()
sns.heatmap(corr,annot = True, cmap='coolwarm')
plt.title('Correlação Preço e Qunatidade')
plt.show()

#Gráfico de Histograma
plt.hist(df['Nota'])
plt.title('Histograma de Notas')
plt.xlabel('Notas')
plt.ylabel('Nº de notas')
plt.show()