<h1 align="center">Conversor de Planilhas Google (Spreadsheet Conversor)</h1>

Esse script acessa uma planilha no Google Docs e efetua uma cópia do conteúdo para um arquivo local no formato CSV. O arquivo CSV recebe o conteúdo formatado (data, valores e porcentagens). O código foi feito em Python 3.9 e foi utilizada a biblioteca [gspread](https://gspread.readthedocs.io/en/latest/index.html).

## GSPREAD:

- Para conseguir conectar ao serviço do Google Docs, é preciso utilizar uma [Service Account](https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account);
- Para isso, é necessária uma autenticação através de credenciais com placeholders conforme o exemplo abaixo:

<p align="center">
  <img src="/img/json.png" />
</p>
