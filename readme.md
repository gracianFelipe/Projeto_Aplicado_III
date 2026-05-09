# Projeto Aplicado III — Sistema de Recomendação de Restaurantes

## 1. Apresentação

**Título do Trabalho:**  
Sistema de Recomendação de Restaurantes (iFood)

**Membros do Grupo:**  
- Allana Silva Santana - RA: 10424950  
- Cristiano Prado do Carmo – RA: 10720249  
- Déborah Silvério Alves Morales – RA: 10728563  
- Maria Fernanda Salles Vasconcellos – RA: 10424791  

**Objetivo do Projeto:**  
Desenvolver um **sistema de recomendação de restaurantes** utilizando a base pública **iFood Restaurants Data** (Kaggle), capaz de sugerir estabelecimentos **similares** a um restaurante de referência e/ou **coerentes com preferências** (ex.: categoria culinária, características e outros atributos disponíveis), aplicando técnicas de recomendação e boas práticas de ciência de dados, com entregas reprodutíveis e documentadas.

---

## 2. Contexto de Estudo

Plataformas de delivery e descoberta de restaurantes oferecem um grande volume de opções, o que pode gerar sobrecarga de escolha e dificuldade para encontrar estabelecimentos alinhados ao perfil do usuário. Sistemas de recomendação buscam reduzir esse atrito ao **priorizar itens relevantes**, apresentando sugestões personalizadas ou contextualizadas.

Neste projeto, é utilizada a base **iFood Restaurants Data**, disponibilizada no Kaggle, contendo registros de restaurantes do iFood em snapshots de 2020/2021 (catálogo e atributos dos estabelecimentos). Como o conjunto de dados é orientado a **itens (restaurantes)** e seus atributos, e não a interações explícitas entre usuários e itens, o projeto dá ênfase a uma abordagem **baseada em conteúdo (content-based)**.

---

## 3. Premissas do Projeto

**Empresa de Referência:**  
**iFood**, plataforma brasileira de delivery e marketplace de alimentação.

**Problema de Estudo:**  
A diversidade de opções e a necessidade de filtragem manual dificultam a descoberta eficiente de restaurantes relevantes, especialmente quando o usuário deseja alternativas semelhantes a um restaurante que já conhece ou a um conjunto de preferências.

**Objetivo Geral:**  
Construir um sistema de recomendação que gere um **ranking Top-N** de restaurantes recomendados, com base na **similaridade** entre estabelecimentos e/ou aderência a preferências informadas, utilizando as características presentes no dataset.

**Metas Específicas:**  
- Selecionar e compreender o dataset (estrutura, variáveis e limitações).  
- Realizar limpeza e preparação dos dados (padronizações, nulos e duplicidades).  
- Construir um **baseline** para comparação.  
- Implementar recomendação **baseada em conteúdo**, com vetorização e similaridade.  
- Avaliar qualitativamente as recomendações geradas.  
- Implementar uma **prova de conceito** funcional.  
- Documentar decisões, resultados, limitações e possibilidades de evolução.

### 3.1 Objetivo Extensionista (ODS/ONU)

O projeto incorpora um **objetivo extensionista** ao propor uma solução que, além do valor técnico, contribui para necessidades alinhadas aos **Objetivos de Desenvolvimento Sustentável (ODS) da ONU**. Em especial, o trabalho se conecta ao **ODS 12 (Consumo e Produção Responsáveis)** ao favorecer escolhas mais conscientes e eficientes, reduzindo desperdícios de tempo e recursos na busca e ampliando a visibilidade de estabelecimentos compatíveis com critérios de preferência e responsabilidade.

De modo complementar, o projeto também dialoga com o **ODS 8 (Trabalho Decente e Crescimento Econômico)** e o **ODS 11 (Cidades e Comunidades Sustentáveis)**, ao incentivar a descoberta de restaurantes locais e contribuir para o fortalecimento de pequenos negócios e serviços nas comunidades.

---

## 4. Metodologia resumida

A solução foi desenvolvida com base nas seguintes etapas:

1. entendimento do problema e dos dados;  
2. coleta e seleção da base;  
3. pré-processamento e limpeza dos dados;  
4. construção da representação textual dos restaurantes;  
5. vetorização com **TF-IDF**;  
6. cálculo de similaridade com **similaridade do cosseno**;  
7. construção do **baseline**;  
8. avaliação qualitativa;  
9. ajustes e refinamento do pipeline.

---

## 5. Principais resultados

Os resultados mostraram que a abordagem baseada em conteúdo foi capaz de gerar recomendações coerentes com os restaurantes consultados, principalmente em termos de **categoria** e **faixa de preço**.

A comparação com o baseline indicou que o modelo principal apresentou maior flexibilidade e melhor capacidade de captar similaridades entre os estabelecimentos. Após o refinamento do pipeline, observou-se melhora na consistência das recomendações, reforçando a viabilidade da prova de conceito.

---

## 6. Cronograma do Projeto

| Etapa | Atividade | Início | Término | Responsável |
|------:|-----------|:------:|:-------:|-------------|
| 1 | Alinhamento do tema, escopo e objetivo extensionista | 02/03/2026 | 06/03/2026 | Todos |
| 2 | Definição do repositório e padrão de pastas | 05/03/2026 | 06/03/2026 | Todos |
| 3 | Download/ingestão do dataset + Data Card | 09/03/2026 | 13/03/2026 | Todos |
| 4 | Limpeza e preparação dos dados | 16/03/2026 | 27/03/2026 | Cristiano / Débora |
| 5 | EDA orientada ao problema | 30/03/2026 | 10/04/2026 | Allana / Maria Fernanda |
| 6 | Baseline e critérios de avaliação | 13/04/2026 | 17/04/2026 | Todos |
| 7 | Modelo baseado em conteúdo | 20/04/2026 | 15/05/2026 | Cristiano / Allana |
| 8 | Ajustes, análise e refinamento | 18/05/2026 | 29/05/2026 | Todos |
| 9 | MVP / documentação / apresentação | 01/06/2026 | 21/06/2026 | Todos |

---

## 7. Estrutura do repositório

```text
Projeto_Aplicado_III/
├── README.md
├── data/
├── docs/
├── notebooks/
├── scripts/
├── figures/
└── videos/