# Amazon Delivery Time Prediction

## Problema de Negócio
As operações de entrega de produtos da Amazon enfrentam desafios relacionados ao cumprimento dos prazos estimados. Entregas atrasadas podem impactar negativamente a satisfação dos clientes e aumentar custos operacionais devido à necessidade de ajustes logísticos. O objetivo deste projeto é prever o tempo de entrega com maior precisão, auxiliando a otimização das operações logísticas e melhorando a experiência do cliente.

## Solução
Implementamos um modelo de Machine Learning para prever o tempo de entrega de pedidos, utilizando algoritmos de regressão linear e LightGBM. Este modelo permite identificar e mitigar possíveis atrasos antes que eles ocorram, melhorando a precisão das estimativas e otimizando o planejamento logístico.

## Impacto no Negócio
- **Melhoria na satisfação do cliente:** Previsões mais precisas reduzem expectativas frustradas e aumentam a confiança dos clientes.
- **Redução de custos:** A identificação proativa de problemas logísticos permite ajustes que evitam gastos adicionais.
- **Eficiência operacional:** O planejamento aprimorado com base em previsões confiáveis otimiza o uso de recursos.

## Algoritmo Utilizado
1. **LightGBM**  
   - Um algoritmo de aprendizado por gradiente baseado em árvores, projetado para alta eficiência e precisão.
   - É ideal para lidar com grandes volumes de dados e detectar relações não lineares complexas.

## Evidências de Performance do Modelo

Abaixo estão os resultados de performance do modelo LightGBM, mostrando como ele se comporta em relação às previsões de tempo de entrega.

![Print com os resultados do modelo](https://github.com/thomaskarsten90/LinearRegression_deliverytime_forecast/blob/feature/linearregression_deliveryforecast/predict_lr.png)

Os principais indicadores de performance utilizados para avaliar o modelo incluem:

- **R² (Coeficiente de Determinação):** Mede a qualidade do ajuste do modelo aos dados. Valores mais próximos de 1 indicam um bom ajuste.
- **MAE (Erro Absoluto Médio):** Mede a diferença média entre os valores previstos e os reais, com valores menores indicando maior precisão nas previsões.
- **RMSE (Raiz do Erro Quadrático Médio):** Penaliza mais fortemente os erros maiores, fornecendo uma medida robusta da precisão do modelo.

Você pode acessar os resultados completos e a análise de performance no arquivo Excel disponível no repositório [aqui](/home/thomas-linux/projects/deliverytime_forecast_linearregression/LinearRegression_deliverytime_forecast/resultados_prediction.xlsx).

## Possibilidades nos Negócios
Com regressão linear e LightGBM, é possível:
- Identificar fatores críticos que afetam o tempo de entrega.
- Criar estratégias preventivas para melhorar a eficiência logística.
- Desenvolver sistemas em tempo real para reajustar prazos com base em condições atuais.

## Próximos Passos
1. **Coletar mais dados:** Expandir o conjunto de dados com informações de clima, tráfego em tempo real e sazonalidade.
2. **Hiperparametrização:** Ajustar os hiperparâmetros do LightGBM para aumentar a precisão.
3. **Expansão para outros mercados:** Generalizar o modelo para prever tempos de entrega em diferentes regiões e países.
4. **Integração com sistemas:** Implementar o modelo em sistemas de gestão logística em tempo real para tomadas de decisão automáticas.
5. **Monitoramento de desempenho:** Criar dashboards para acompanhar a precisão do modelo e seu impacto nos KPIs do negócio.

---

Este projeto exemplifica como a inteligência artificial pode transformar a logística e gerar valor significativo para o negócio. Para mais detalhes, consulte o código e documentação neste repositório.

