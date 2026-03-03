# Projeto Aplicado III - Sistema de Recomendação de Restaurantes (iFood)

## 1. Apresentação

**Título do Trabalho:**  
Sistema de Recomendação de Restaurantes (iFood)

**Membros do Grupo:**  
- Cristiano Prado do Carmo – RA: 10720249  
- Felipe Graciano de Moura Ramos – RA: 10369992  
- Guilherme Santos Oliveira – RA: 10730679  

**Objetivo do Projeto:**  
Desenvolver um **sistema de recomendação de restaurantes** utilizando a base pública **iFood Restaurants Data** (Kaggle), capaz de sugerir estabelecimentos **similares** a um restaurante de referência e/ou **coerentes com preferências** (ex.: categoria culinária, características e outros atributos disponíveis), aplicando técnicas de recomendação e boas práticas de ciência de dados, com entregas reprodutíveis e documentadas.

---

## 2. Contexto de Estudo

Plataformas de delivery e descoberta de restaurantes oferecem um grande volume de opções, o que pode gerar sobrecarga de escolha e dificuldade para encontrar estabelecimentos alinhados ao perfil do usuário. Sistemas de recomendação buscam reduzir esse atrito ao **priorizar itens relevantes**, apresentando sugestões personalizadas ou contextualizadas.

Neste projeto, será utilizada a base **iFood Restaurants Data**, disponibilizada no Kaggle, contendo registros de restaurantes do iFood em snapshots de 2020/2021 (catálogo e atributos dos estabelecimentos). Como o conjunto de dados é orientado a **itens (restaurantes)** e seus atributos (em vez de histórico de interações usuário–item), o projeto dará ênfase a uma abordagem **baseada em conteúdo (content-based)**, com possibilidade de extensão para um modelo **híbrido** caso sejam incorporadas regras, perfis de preferência ou outras fontes de dados.

---

## 3. Premissas do Projeto

**Empresa de Referência:**  
**iFood**, plataforma brasileira de delivery e marketplace de alimentação.

**Problema de Estudo:**  
A diversidade de opções e a necessidade de filtragem manual dificultam a descoberta eficiente de restaurantes relevantes, especialmente quando o usuário deseja alternativas semelhantes a um restaurante que já conhece ou um conjunto de preferências.

**Objetivo Geral:**  
Construir um sistema de recomendação que gere um **ranking Top-N** de restaurantes recomendados, com base na **similaridade** entre estabelecimentos e/ou aderência a preferências informadas, utilizando as características presentes no dataset.

**Metas Específicas:**  
- Selecionar e compreender o dataset (estrutura, variáveis e limitações).  
- Realizar limpeza e preparação dos dados (padronizações, nulos, duplicidades).  
- Construir um **baseline** (recomendação simples por regras/atributos) para comparação.  
- Implementar recomendação **content-based** (ex.: vetorização de atributos e similaridade do cosseno; TF-IDF quando houver campos textuais).  
- Avaliar a qualidade das recomendações com métricas e validações adequadas ao contexto (ex.: análises qualitativas, testes de consistência, cobertura/diversidade; e, quando aplicável, métricas offline de ranking).  
- Implementar um **MVP** de entrega (relatório + demonstração: notebook, dashboard simples ou API).  
- Documentar decisões, resultados e limitações, garantindo reprodutibilidade.

### 3.1. Objetivo Extensionista (ODS/ONU)

O projeto incorpora um **objetivo extensionista** ao propor uma solução que, além do valor técnico, contribua para necessidades alinhadas aos **Objetivos de Desenvolvimento Sustentável (ODS) da ONU**. Em especial, o trabalho se conecta ao **ODS 12 (Consumo e Produção Responsáveis)** ao favorecer escolhas mais conscientes e eficientes, reduzindo desperdícios de tempo e recursos na busca e ampliando a visibilidade de estabelecimentos compatíveis com critérios de preferência e responsabilidade (quando tais atributos estiverem disponíveis ou puderem ser tratados de forma adequada).

De modo complementar, o projeto pode apoiar o **ODS 8 (Trabalho Decente e Crescimento Econômico)** e o **ODS 11 (Cidades e Comunidades Sustentáveis)** ao incentivar a descoberta de restaurantes locais e a distribuição de demanda, contribuindo para o fortalecimento de pequenos negócios e serviços nas comunidades.

---

## 4. Cronograma do Projeto

O cronograma abaixo apresenta as atividades previstas, com responsáveis e prazos estimados.  
**Marcos principais:** definição/ingestão do dataset, preparação e baseline, implementação do recomendador, MVP/demonstração e entrega final (relatório + apresentação/vídeo).

> Observação: datas podem ser ajustadas conforme o calendário oficial da disciplina.

Em andamento
---

## 5. Repositório

Repositório no GitHub: **https://github.com/gracianFelipe/Projeto_Aplicado_III**

---

## 6. Bibliografia

- TACHINARDI, Ricardo. *iFood Restaurants Data* [conjunto de dados]. Kaggle, 2021. Disponível em: https://www.kaggle.com/datasets/ricardotachinardi/ifood-restaurants-data. Acesso em: 03 mar. 2026.  
- NAÇÕES UNIDAS. *Transformando nosso mundo: a Agenda 2030 para o Desenvolvimento Sustentável*. 2015. Disponível em: https://brasil.un.org/sites/default/files/2020-09/agenda2030-pt-br.pdf. Acesso em: 03 mar. 2026.  
- NAÇÕES UNIDAS NO BRASIL. *Objetivos de Desenvolvimento Sustentável (ODS) no Brasil*. Disponível em: https://brasil.un.org/pt-br/sdgs. Acesso em: 03 mar. 2026.  
- NAÇÕES UNIDAS NO BRASIL. *ODS 12 — Consumo e produção responsáveis*. Disponível em: https://brasil.un.org/pt-br/sdgs/12. Acesso em: 03 mar. 2026.  
- RICCI, Francesco; ROKACH, Lior; SHAPIRA, Bracha. *Recommender Systems Handbook*. 2. ed. Boston: Springer, 2015.  
- AGGARWAL, Charu C. *Recommender Systems: The Textbook*. Cham: Springer, 2016.