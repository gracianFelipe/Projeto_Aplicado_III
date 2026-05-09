# Pasta `data/`

Esta pasta é destinada à documentação da base de dados utilizada no projeto.

## Dataset utilizado

- **Nome:** iFood Restaurants Data
- **Fonte:** Kaggle
- **Link:** https://www.kaggle.com/datasets/ricardotachinardi/ifood-restaurants-data

## Arquivo principal utilizado no projeto

- **Arquivo:** `ifood-restaurants-february-2021.csv`

## Observação importante

O arquivo CSV utilizado no projeto **não foi incluído diretamente neste repositório**, pois possui tamanho elevado (mais de 300 MB), o que dificulta seu versionamento no GitHub.

Para reproduzir os experimentos, o arquivo deve ser obtido diretamente na fonte original indicada acima e, em seguida, colocado no ambiente de execução local ou no Google Colab, conforme utilizado no desenvolvimento do projeto.

## Uso no projeto

O dataset foi utilizado para:

- análise exploratória dos dados;
- limpeza e preparação da base;
- construção da representação textual dos restaurantes;
- vetorização com TF-IDF;
- cálculo de similaridade entre estabelecimentos;
- geração e avaliação das recomendações.

## Estrutura esperada

Caso o usuário deseje reproduzir o projeto localmente, recomenda-se manter o arquivo CSV com o seguinte nome:

```text
ifood-restaurants-february-2021.csv

## Licenciamento e uso

O uso do dataset deve respeitar as condições definidas pela plataforma Kaggle e pelo autor responsável pela disponibilização da base.