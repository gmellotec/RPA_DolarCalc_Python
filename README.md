# Dolar Calc 2.0.0

### Este projeto foi criado utilizando Python e BotCity Web

O projeto consiste em capturar dados do mercado financeiro e depois realizar calculos matematicos para operacoes na Bolsa
de Valores brasileira, com Daytrade em Dolar Futuro.

- O Robo faz a captura das informacoes em 5 sites diferentes
  - Utilizado o framework web da BotCity para realizar a captura dos dados. O framework tem como base o Selenium.
- Realiza o calculo com as informacoes coletadas
- Armazena os calculos e os dados coletados em um banco de dados para manter um historico das informacoes
  - Foi Utilizado o banco de dados SQLite para armazenar os dados
- Envia por email todas as informacoes ja calculadas para o cliente, onde ele utiliza estas informacoes para tomadas de decisao em suas operacoes de DayTrade
  - Utilizado plugin da botcity para integrar o gmail e realizar o envio das informacoes. Para o corpo do email foi utilizado estrutura HTML.
  - As credenciais do email devem ser preenchidas no arquivo config.ini na secao [credentials]
  - No arquivo send_email ha uma variavel de lista onde deve ser adicionado os emails ao qual voce deseja que receba os dados.