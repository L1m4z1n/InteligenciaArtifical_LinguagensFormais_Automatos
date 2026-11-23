# Assistente de divulgação — Instituto Noah

**Aluno:** Gabriel Lima — 38180812
**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos
**Professora:** Kadidja Valéria

## Sobre o projeto

O trabalho foi inspirado no sistema de ingressos que desenvolvi
para o Instituto Noah.

O protótipo prevê a faixa de ocupação final de uma sessão
e aplica regras para recomendar ações de divulgação à equipe.

## Dados utilizados

O treinamento utiliza 300 sessões simuladas, com capacidade
adotada de 95 lugares por sessão.

O relatório real do instituto serve como contexto do projeto.
Ele não é a base de treinamento do modelo.

## Funcionamento

A árvore de decisão recebe:
- Ocupação atual;
- Vendas nos últimos sete dias;
- Dias restantes até o espetáculo.

Ela prevê a ocupação final como Baixa, Média ou Alta.

Depois, quatro regras usam a previsão e os dados da sessão
para recomendar uma ação. As vagas na outra sessão também
participam dessa decisão.

## Resultado

O modelo obteve 76% de acurácia nos 75 exemplos de teste
da base simulada.

Esse resultado ainda não comprova o desempenho em eventos reais.

## Arquivos

- [Notebook completo](A1_Sistema_Especialista_Instituto_Noah.ipynb)
- [Dataset simulado](sessoes_simuladas_noah.csv)
- [Apresentação em PowerPoint](Instituto Noah_Assistente de divulgação_A1.pptx)
- [Apresentação em PDF](Apresentacao_Instituto_Noah.pdf)

## Demonstração

[Abrir no Google Colab](https://colab.research.google.com/drive/1uRvCXXI1x0TKLpW0ZDVLbggMZeVbIRKS?usp=sharing)

Para utilizar, execute todas as células na ordem.
Ao final, ajuste os controles e clique em “Analisar sessão”.

## Limitações

Os dados são simulados e as regras utilizam critérios
propostos para o protótipo. Uma próxima etapa é validar
esses critérios com a equipe e avaliar o modelo com
histórico real de vendas.
