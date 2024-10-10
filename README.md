Este projeto utiliza algoritmos de inteligência artificial para prever o score de crédito de clientes com base em variáveis como profissão, mix de crédito e comportamento de pagamento. Através de dois modelos de IA – Random Forest e KNN – foram treinados para identificar padrões nos dados e gerar previsões precisas sobre o perfil de crédito dos clientes.
Objetivo do Projeto

O objetivo é prever o score de crédito de novos clientes com base em variáveis previamente analisadas, facilitando a tomada de decisões sobre a concessão de crédito.
Ferramentas e Bibliotecas Utilizadas

    pandas: Para manipulação e análise de dados.
    scikit-learn (sklearn): Para implementação e treino dos modelos de IA.
        LabelEncoder: Transformação de variáveis categóricas em numéricas.
        train_test_split: Divisão dos dados em treino e teste.
        RandomForestClassifier: Modelo de árvore de decisão para classificação.
        KNeighborsClassifier: Modelo KNN (K-Nearest Neighbors) para classificação.
        accuracy_score: Avaliação da acurácia dos modelos.
    Jupyter Notebook ou IDE Python: Para desenvolvimento e execução do projeto.

Etapas do Projeto
1. Preparação dos Dados

    Os dados foram carregados de arquivos CSV contendo informações dos clientes.
    Colunas categóricas como "profissão", "mix_credito" e "comportamento_pagamento" foram convertidas em valores numéricos utilizando LabelEncoder.
    A coluna de saída (target) é o score_credito, que foi usada para treinar os modelos.

2. Treinamento dos Modelos de IA

    Dois modelos de IA foram criados:
        Random Forest: Um modelo baseado em árvores de decisão.
        KNN (K-Nearest Neighbors): Um modelo que classifica baseado nos vizinhos mais próximos.
    Os dados foram divididos em 70% para treino e 30% para teste utilizando a função train_test_split.
    Ambos os modelos foram treinados com os dados de treino e avaliados com os dados de teste.

3. Avaliação dos Modelos

    Após o treino, foi calculada a acurácia dos dois modelos:
        Random Forest: 82% de acurácia.
        KNN: 73% de acurácia.
    O modelo Random Forest demonstrou ser mais eficiente para essa tarefa.

4. Previsão para Novos Clientes

    Após treinar o modelo, utilizamos o Random Forest para prever o score de novos clientes, com base em dados já transformados de profissão, mix de crédito e comportamento de pagamento.

Previsão Gerada:

    Exemplo de previsões geradas para novos clientes:
        Cliente 1: Score 'Poor'
        Cliente 2: Score 'Good'
        Cliente 3: Score 'Standard'

Como Executar o Projeto

    Instale as bibliotecas necessárias:

    bash

pip install pandas scikit-learn

Execute o script Python que faz a leitura dos dados, treino dos modelos, e avaliação das previsões.

Para prever novos clientes, utilize o arquivo CSV de "novos_clientes.csv" e execute o código para ver as previsões de score de crédito.
