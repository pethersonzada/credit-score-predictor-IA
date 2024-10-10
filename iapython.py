# Importando bibliotecas.

import pandas as pd # Análise e tratamento de dados.
from sklearn.preprocessing import LabelEncoder # Treino para IA.
from sklearn.model_selection import train_test_split # Treino para IA.
from sklearn.ensemble import RandomForestClassifier # Importando a IA.
from sklearn.neighbors import KNeighborsClassifier # Importando a IA.
from sklearn.metrics import accuracy_score # Avaliando a IA.

tabela = pd.read_csv("projetos-python/python-com-ia/clientes.csv") # Importando a base de dados (CASO NÃO FUNCIONAR, TENTE ALTERAR O DIRETÓRIO!!).

print(tabela.info()) # Verificando as informações da base de dados, mais especificamente o tipo de dados de cada coluna (Dtype).

codificador = LabelEncoder() # Criando um objeto do tipo LabelEncoder (Transforma os dados de texto em números).

tabela["profissao"] = codificador.fit_transform(tabela["profissao"]) # Usando o codificador para transformar o texto em número.

codificador2 = LabelEncoder() # Criando um novo objeto do tipo LabelEncoder (Transforma os dados de texto em números).

tabela["mix_credito"] = codificador2.fit_transform(tabela["mix_credito"]) # Usando o codificador para transformar o texto em número.

codificador3 = LabelEncoder() # Criando um novo objeto do tipo LabelEncoder (Transforma os dados de texto em números).

tabela["comportamento_pagamento"] = codificador3.fit_transform(tabela["comportamento_pagamento"]) # Usando o codificador para transformar o texto em número.

print(tabela.info())

y = tabela["score_credito"] 
x = tabela.drop(columns=["score_credito", "id_cliente"]) 

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

# Cria a IA.
modelo_arvoreDecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

# Treina a IA.
modelo_arvoreDecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

# Avaliar qual o melhor modelo de IA.

previsao_arvoreDecisao = modelo_arvoreDecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

# Comparando as previsões com o y_teste (PODE DEMORAR UM POUCO PARA RODAR!).

print("Acurácia da Arvore de Decisão: ", accuracy_score(y_teste, previsao_arvoreDecisao)) # Comparando as previsões com o y_teste.
print("Acurácia do KNN: ", accuracy_score(y_teste, previsao_knn)) # Comparando as previsões com o y_teste.

# Acurácia da Arvore de Decisão:  0.824... ou >> 82% << 
# Acurácia do KNN:  0.732... ou >> 73% <<

# Fazendo novas previsões.

tabelas_novos_clientes = pd.read_csv("projetos-python/python-com-ia/novos_clientes.csv") # Importando a base de dados (CASO NAO FUNCIONAR, TENTE ALTERAR O DIRETÓRIO!!).
print(tabelas_novos_clientes)

tabelas_novos_clientes["profissao"] = codificador.fit_transform(tabelas_novos_clientes["profissao"]) # Usando o codificador para transformar o texto em número.
tabelas_novos_clientes["mix_credito"] = codificador2.fit_transform(tabelas_novos_clientes["mix_credito"]) # Usando o codificador para transformar o texto em número.
tabelas_novos_clientes["comportamento_pagamento"] = codificador3.fit_transform(tabelas_novos_clientes["comportamento_pagamento"]) # Usando o codificador para transformar o texto em número.

# Previsão do score.

previsao = modelo_arvoreDecisao.predict(tabelas_novos_clientes)
print(previsao)

# 1 Cliente - Score 'Poor'
# 2 Cliente - Score 'Good'
# 3 Cliente - Score 'Standard'