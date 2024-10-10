Previsão de Score de Crédito com IA

Este projeto utiliza algoritmos de aprendizado de máquina, como Random Forest e K-Nearest Neighbors, para prever o score de crédito de clientes com base em variáveis como profissão, mix de crédito e comportamento de pagamento.
Bibliotecas usadas:

    pandas: Manipulação e análise de dados.
    sklearn: Ferramentas para aprendizado de máquina, incluindo codificação de dados, divisão de treino/teste, classificadores e avaliação de modelos.

Como usar:

    Instale as dependências necessárias:

    pip install pandas scikit-learn

    Certifique-se de ter os arquivos CSV (clientes.csv e novos_clientes.csv) com os dados corretos.
    Execute o script para treinar os modelos e fazer previsões de score de crédito.

Etapas do Processo:

    Preparação dos dados:
        Os dados categóricos de profissão, mix_credito e comportamento_pagamento são convertidos para valores numéricos usando LabelEncoder.
        
    Treinamento dos Modelos:
        Dois modelos são treinados: Random Forest e K-Nearest Neighbors.
        
    Avaliação dos Modelos:
        A acurácia de cada modelo é comparada usando o conjunto de teste.
        
    Previsão de Novos Scores:
        O modelo selecionado faz previsões para novos clientes com base em dados fornecidos.
