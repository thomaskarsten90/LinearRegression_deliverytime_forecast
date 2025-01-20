# Projeto de Previsão de Tempo de Entrega de Mercadorias de Delivery

No meu projeto de **previsão de tempo de entrega de mercadorias de delivery**, eu usei o algoritmo de **regressão linear** para prever o **Delivery_Time** (tempo de entrega), com base em várias variáveis, como **Agent_Age** (idade do agente), **Agent_Rating** (classificação do agente), **Wait_Time** (tempo de espera), **Weather** (clima), **Traffic** (tráfego), **Vehicle** (veículo), entre outras.

### Como Funciona a Regressão Linear?

A **regressão linear** é um algoritmo que tenta **prever** um valor com base em um conjunto de variáveis. Para isso, ele usa uma fórmula matemática simples:

\[ Y = m_1 X_1 + m_2 X_2 + \dots + m_n X_n + b \]

Onde:
- **Y** é a variável que queremos prever (no meu caso, o **Delivery_Time**),
- **X_1, X_2, ..., X_n** são as variáveis que usamos para fazer a previsão (como **Agent_Age**, **Wait_Time**, **Traffic**, etc.),
- **m_1, m_2, ..., m_n** são os coeficientes que o algoritmo calcula durante o treinamento para entender o impacto de cada variável,
- **b** é o intercepto da equação.

O objetivo do algoritmo é ajustar esses coeficientes e o intercepto para que a diferença entre o valor **real** do **Delivery_Time** e o valor **previsto** seja o menor possível.

### Como o Algoritmo Chegou aos Resultados?

Para prever o tempo de entrega, o algoritmo de **regressão linear** analisou os dados históricos e ajustou a equação que melhor se adequasse ao comportamento observado. Ele fez isso utilizando um processo chamado **mínimos quadrados**, que basicamente tenta minimizar o erro, ou seja, a diferença entre as previsões do modelo e os valores reais.

Por exemplo, para o primeiro caso, onde o **Delivery_Time** real foi 170 minutos, o algoritmo previu **166,75 minutos**. A diferença de apenas **3,25 minutos** entre a previsão e o valor real mostra que o modelo fez uma previsão bastante precisa.

### Como o Algoritmo Ajusta os Coeficientes?

Durante o treinamento, o algoritmo tenta ajustar os **coeficientes** de cada variável (como **Wait_Time**, **Agent_Age**, etc.) para **entender o impacto** que cada uma delas tem sobre o **Delivery_Time**. Isso é feito calculando as **derivadas** do erro (a diferença entre o valor real e o previsto) e ajustando os coeficientes para reduzir essa diferença.

No meu caso, as variáveis como **Wait_Time** e **Agent_Rating** provavelmente tiveram um impacto significativo na previsão, já que o modelo precisou considerar o tempo de espera e a classificação do agente para estimar corretamente o tempo de entrega.

### O Que Aprendi com o Projeto?

Ao finalizar o projeto, eu percebi que o modelo de **regressão linear** foi bastante eficiente. Com base nas variáveis que forneci, ele fez previsões de **Delivery_Time** com um erro relativamente pequeno, o que indica que ele conseguiu capturar bem os padrões presentes nos dados.

Em resumo, o modelo de **regressão linear** foi capaz de prever o tempo de entrega de mercadorias com base em variáveis como idade do agente, tempo de espera, clima, tipo de veículo e outros fatores. Ele fez isso ajustando os coeficientes das variáveis e minimizando a diferença entre as previsões e os valores reais.

Esse foi um ótimo exemplo de como a **matemática da regressão linear** pode ser usada para resolver problemas do mundo real, como prever o tempo de entrega em um sistema de delivery.
