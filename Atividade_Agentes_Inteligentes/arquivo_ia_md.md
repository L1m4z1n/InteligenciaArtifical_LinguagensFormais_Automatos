# Atividade — Agentes Inteligentes

> Disciplina: Inteligência Artificial, Linguagens Formais e Autômatos  
> Instituição: UDF | Aula: 19/10/2026  
> Professora: Kadidja Valéria  
> Estudante: Gabriel Lima Almeida | Turma: 2267209

## Objetivo

Analisar a racionalidade dos agentes inteligentes, modelar ambientes de tarefa pelo método **PEAS** (Performance, Environment, Actuators, Sensors) e distinguir as principais arquiteturas de agentes, relacionando-as a autômatos.

## Exercício 2.3 - Racionalidade e funções de agentes

### a) Um agente que detecta apenas informações parciais sobre o estado não pode ser perfeitamente racional.

**Resposta: Falso.**

**Justificativa:** A racionalidade exige escolher a ação de maior desempenho esperado com base nas informações disponíveis, não conhecer todo o estado real. Hipótese: existe uma política ótima diante da incerteza.

**Exemplo ou contraexemplo:** Um robô que só percebe a sujeira no cômodo atual pode decidir racionalmente limpar esse cômodo, mesmo ignorando os demais.

### b) Existem ambientes de tarefa nos quais nenhum agente reativo puro pode comportar-se racionalmente.

**Resposta: Verdadeiro.**

**Justificativa:** Um agente reativo puro usa somente a percepção atual. Quando a mesma percepção pede ações diferentes conforme o passado, ele não consegue adotar sempre a melhor escolha. Hipótese: o histórico influencia o resultado.

**Exemplo ou contraexemplo:** Um aspirador vê o cômodo A limpo, mas precisa saber se já limpou B: se não limpou, deve visitá-lo; se já limpou, deve parar para economizar energia.

### c) Existe um ambiente de tarefa em que todo agente é racional.

**Resposta: Verdadeiro.**

**Justificativa:** Se todas as ações disponíveis produzem exatamente a mesma medida de desempenho em todas as situações, qualquer escolha maximiza o resultado esperado. Hipótese: não há diferença de custo ou recompensa entre ações.

**Exemplo ou contraexemplo:** Em uma sala fictícia, apertar qualquer botão mantém a mesma pontuação e não altera o ambiente.

### d) A entrada para o programa de agente é a mesma que a entrada para a função de agente.

**Resposta: Falso.**

**Justificativa:** A função de agente é definida matematicamente sobre toda a sequência de percepções; já o programa normalmente recebe a percepção atual e usa memória interna quando necessário.

**Exemplo ou contraexemplo:** A função considera [A limpo, B sujo]; o programa recebe agora “B sujo” e pode consultar o histórico armazenado.

### e) Toda função de agente é implementável por uma combinação de programa/máquina.

**Resposta: Falso.**

**Justificativa:** Uma função abstrata pode especificar respostas para infinitas sequências de maneiras não computáveis; uma máquina com programa finito não consegue implementar qualquer mapeamento possível. Hipótese: programas executam procedimentos computáveis.

**Exemplo ou contraexemplo:** Uma função que exige decidir corretamente um problema não computável, como a parada de programas arbitrários, não pode ser implementada em geral.

### f) Suponha que um agente selecione sua ação uniformemente ao acaso do conjunto de ações possíveis. Existe um ambiente de tarefa determinista em que esse agente é racional.

**Resposta: Verdadeiro.**

**Justificativa:** Mesmo em um ambiente determinístico, escolher aleatoriamente pode ser racional quando todas as ações disponíveis têm resultado igualmente bom.

**Exemplo ou contraexemplo:** Um agente escolhe aleatoriamente entre duas rotas que levam deterministicamente ao mesmo destino, com mesmo custo e duração.

### g) É possível para um dado agente ser perfeitamente racional em dois ambientes de tarefa distintos.

**Resposta: Verdadeiro.**

**Justificativa:** A racionalidade depende das condições e medidas de desempenho de cada tarefa. A mesma política pode maximizar o resultado em dois ambientes diferentes.

**Exemplo ou contraexemplo:** Um agente que abre uma porta ao detectar presença pode ser racional em dois corredores distintos que usam o mesmo sensor e têm as mesmas exigências.

### h) Todo agente é racional em um ambiente não observável.

**Resposta: Falso.**

**Justificativa:** A ausência de observações não elimina diferenças de qualidade entre políticas. O agente ainda deve usar conhecimento prévio e escolher ações que maximizem o resultado esperado.

**Exemplo ou contraexemplo:** Em uma sala sem sensores, um robô que liga um aquecedor perigoso desnecessariamente pode agir pior do que outro que o mantém desligado.

### i) Um agente jogador de pôquer perfeitamente racional nunca perde.

**Resposta: Falso.**

**Justificativa:** Racionalidade não significa prever cartas ocultas ou garantir vitória. O agente maximiza o retorno esperado com as informações que possui, mas pode perder por acaso ou pelas decisões adversárias.

**Exemplo ou contraexemplo:** Um jogador faz uma aposta matematicamente vantajosa, mas perde após a última carta favorecer o adversário.

## Exercício 2.4 — Análise de ambientes por PEAS

As classificações consideram as hipóteses explicitadas para cada cenário.


### 1. Jogar futebol

- **Agente analisado:** Jogador de futebol com capacidade de observar e agir.
- **Objetivo e hipóteses:** Partida real com regras conhecidas, colegas e adversários, bola em movimento.
- **P - Medida de desempenho:** Contribuir para gols e vitória; evitar faltas; executar bons passes e defender.
- **E - Ambiente:** Campo, bola, traves, árbitro, companheiros, adversários e clima.
- **A - Atuadores:** Pernas, pés, corpo e voz para movimentar-se, chutar, marcar e comunicar.
- **S - Sensores:** Visão, audição, tato e propriocepção.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Nem todos os movimentos ou intenções dos demais são conhecidos. |
| Número de agentes | Multiagente: cooperativo e competitivo | Coopera com o time e disputa com adversários. |
| Previsibilidade | Estocástico/estratégico | Erros, desvios e escolhas de outros jogadores tornam resultados incertos. |
| Dependência entre decisões | Sequencial | Passe ou marcação atual altera jogadas futuras. |
| Mudança durante a decisão | Dinâmico | Bola e atletas seguem se movendo enquanto se decide. |
| Natureza dos elementos | Combinação, predominância contínua | Movimentos e tempo são contínuos; placar e regras incluem eventos discretos. |
| Conhecimento do funcionamento | Conhecido parcialmente | Regras conhecidas, embora a dinâmica exata das escolhas rivais não seja. |

### 2. Explorar os oceanos subterrâneos de Titã

- **Agente analisado:** Robô submarino autônomo hipotético.
- **Objetivo e hipóteses:** Missão simulada sob gelo, sem outros agentes decisores, mapa inicialmente desconhecido.
- **P - Medida de desempenho:** Coletar amostras e dados, mapear região, evitar danos e conservar energia.
- **E - Ambiente:** Oceano subterrâneo hipotético, gelo, rochas, correntes e obstáculos.
- **A - Atuadores:** Propulsores, braços mecânicos, coletor de amostras e transmissor.
- **S - Sensores:** Sonar, câmeras, sensores de pressão, temperatura, composição e navegação.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Sensores alcançam apenas regiões limitadas e podem apresentar ruído. |
| Número de agentes | Agente único | Não se supõe outro explorador autônomo na missão. |
| Previsibilidade | Estocástico | Correntes e medições incertas alteram o resultado das manobras. |
| Dependência entre decisões | Sequencial | Trajetos escolhidos afetam energia e acesso a regiões futuras. |
| Mudança durante a decisão | Dinâmico | Correntes e condições podem mudar durante o planejamento. |
| Natureza dos elementos | Combinação, predominância contínua | Posição, pressão e velocidade são contínuas; amostras e comandos podem ser discretos. |
| Conhecimento do funcionamento | Desconhecido | Mapa e efeitos locais das condições precisam ser descobertos. |

### 3. Comprar livros usados de IA na Internet

- **Agente analisado:** Agente de software comprador.
- **Objetivo e hipóteses:** Pesquisa lojas e escolhe oferta; vendedores e compradores podem agir durante a busca.
- **P - Medida de desempenho:** Comprar livro adequado e em bom estado, minimizando preço total e prazo.
- **E - Ambiente:** Sites, anúncios, vendedores, outros compradores, estoque, entrega e pagamento.
- **A - Atuadores:** Consultas web, filtros, mensagens, carrinho, pedidos e pagamentos autorizados.
- **S - Sensores:** Páginas, preços, fotos, descrições, avaliações e status de estoque.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Anúncios podem omitir desgaste, autenticidade e estoque real. |
| Número de agentes | Multiagente: misto | Vendedores negociam e outros compradores disputam ofertas. |
| Previsibilidade | Estocástico/estratégico | Preço, disponibilidade e entrega podem variar. |
| Dependência entre decisões | Sequencial | Pesquisa, comparação e compra se encadeiam. |
| Mudança durante a decisão | Dinâmico | Um anúncio pode ser alterado ou o exemplar vendido enquanto o agente compara. |
| Natureza dos elementos | Combinação | Ações de compra são discretas; preço e tempo admitem valores quantitativos. |
| Conhecimento do funcionamento | Parcialmente desconhecido | Fluxo do site pode ser conhecido, mas qualidade real e reações de vendedores não. |

### 4. Jogar uma partida de tênis

- **Agente analisado:** Tenista individual.
- **Objetivo e hipóteses:** Partida real contra oponente, com regras conhecidas.
- **P - Medida de desempenho:** Ganhar pontos e jogo, com acertos e eficiência nos movimentos.
- **E - Ambiente:** Quadra, bola, rede, linhas, adversário e condições físicas.
- **A - Atuadores:** Pernas, braços, raquete, corpo e comunicação.
- **S - Sensores:** Visão, audição, propriocepção e tato.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Não percebe perfeitamente rotação da bola e intenção rival. |
| Número de agentes | Multiagente: competitivo | O adversário busca vencer os pontos. |
| Previsibilidade | Estocástico/estratégico | Trajetórias reais e jogadas do rival são incertas. |
| Dependência entre decisões | Sequencial | Posicionamento após uma rebatida altera a próxima. |
| Mudança durante a decisão | Dinâmico | Bola e rival se movem continuamente. |
| Natureza dos elementos | Combinação, predominância contínua | Bola e corpo têm trajetórias contínuas; pontuação é discreta. |
| Conhecimento do funcionamento | Conhecido parcialmente | Regras conhecidas; desempenho e escolhas rivais não totalmente previstos. |

### 5. Praticar tênis contra uma parede

- **Agente analisado:** Pessoa treinando rebatidas.
- **Objetivo e hipóteses:** Parede fixa; não existe adversário com decisões próprias.
- **P - Medida de desempenho:** Manter sequência de acertos, melhorar precisão e evitar erros.
- **E - Ambiente:** Quadra de treino, parede, bola, raquete e piso.
- **A - Atuadores:** Pernas, braços, corpo e raquete.
- **S - Sensores:** Visão, audição, tato e propriocepção.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Velocidade e giro da bola não são percebidos com precisão perfeita. |
| Número de agentes | Agente único | Parede não toma decisões independentes. |
| Previsibilidade | Estocástico na prática | Ruído motor e pequenas irregularidades afetam rebatidas, embora uma física idealizada seja determinística. |
| Dependência entre decisões | Sequencial | Uma rebatida determina a próxima trajetória. |
| Mudança durante a decisão | Dinâmico | A bola continua em movimento durante a escolha do golpe. |
| Natureza dos elementos | Combinação, predominância contínua | Deslocamento e tempo contínuos; contagem de acertos discreta. |
| Conhecimento do funcionamento | Conhecido aproximadamente | Comportamento geral da parede é previsível, mas não perfeitamente modelado. |

### 6. Realizar um salto de altura

- **Agente analisado:** Atleta executando o salto.
- **Objetivo e hipóteses:** Tentativa individual, barra parada, pista real; análise apenas da execução do salto.
- **P - Medida de desempenho:** Superar a altura sem derrubar a barra e evitar lesões.
- **E - Ambiente:** Pista, sarrafo, suportes, colchão, gravidade e vento.
- **A - Atuadores:** Pernas, braços e movimentos corporais.
- **S - Sensores:** Visão, tato, equilíbrio e propriocepção.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Não há medida perfeita do próprio impulso e de perturbações físicas. |
| Número de agentes | Agente único | A execução não depende das ações de outro competidor. |
| Previsibilidade | Estocástico na prática | Variação de impulso e vento tornam o resultado incerto. |
| Dependência entre decisões | Sequencial | Corrida, impulsão e transposição dependem das fases anteriores. |
| Mudança durante a decisão | Dinâmico | O corpo se desloca enquanto o atleta ajusta movimentos. |
| Natureza dos elementos | Combinação, predominância contínua | Altura, velocidade e tempo contínuos; êxito ou falta são discretos. |
| Conhecimento do funcionamento | Conhecido aproximadamente | Princípios físicos conhecidos, mas execução exata incerta. |

### 7. Participar de um leilão de um item

- **Agente analisado:** Agente comprador que dá lances.
- **Objetivo e hipóteses:** Leilão online ascendente com prazo, orçamento e concorrentes.
- **P - Medida de desempenho:** Ganhar o item desejado sem ultrapassar valor máximo e reduzir custo.
- **E - Ambiente:** Plataforma, item, regras, tempo restante, concorrentes e preços.
- **A - Atuadores:** Enviar ou retirar lance quando permitido, consultar e confirmar compra.
- **S - Sensores:** Valor atual, histórico público, alertas, tempo restante e dados do item.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Lances futuros e limites de orçamento dos concorrentes são ocultos. |
| Número de agentes | Multiagente: competitivo | Outros interessados disputam o mesmo item. |
| Previsibilidade | Estocástico/estratégico | Novas ofertas e atitudes rivais são incertas. |
| Dependência entre decisões | Sequencial | Lance atual muda preço e possibilidades posteriores. |
| Mudança durante a decisão | Dinâmico | Concorrentes podem aumentar lances enquanto o agente calcula. |
| Natureza dos elementos | Combinação | Lances são eventos discretos; valores e tempo variam numericamente. |
| Conhecimento do funcionamento | Conhecido parcialmente | Regras públicas são conhecidas, estratégias e avaliações rivais não. |

### Comparação final

1. No tênis contra uma pessoa há um oponente que escolhe estratégias e tenta vencer; portanto é multiagente competitivo. Contra a parede não existe adversário decisor: o retorno da bola decorre sobretudo da física da rebatida. Ambos continuam sequenciais e dinâmicos.

2. Os anúncios de livros usados podem apresentar fotos insuficientes, condições não verificadas e estoque desatualizado. Por isso o agente compara avaliações, pede esclarecimentos e considera o risco antes de efetuar a compra.

3. No futebol, colegas cooperam em passes e cobertura enquanto adversários tentam impedir a vitória. Nos leilões, lances de concorrentes elevam o preço e modificam a estratégia; em ambos, não basta prever apenas o ambiente físico ou digital.

## Exercício 2.5 — Conceitos fundamentais

### Agente

**Definição:** Entidade capaz de receber informações do ambiente e praticar ações que modificam esse ambiente. Pode ser uma pessoa, robô ou sistema computacional.

**Exemplo:** Um robô aspirador detecta poeira e aciona o mecanismo de limpeza.

### Função de agente

**Definição:** Regra abstrata que relaciona cada histórico possível de percepções a uma ação. Descreve o comportamento sem exigir uma implementação específica.

**Exemplo:** Após perceber “sujo”, a função determina “aspirar”.

### Programa de agente

**Definição:** Código executado em uma arquitetura que realiza, de maneira concreta, as decisões previstas para o agente. Pode usar variáveis para guardar percepções anteriores.

**Exemplo:** Um script lê um sensor e envia um comando ao motor do aspirador.

### Racionalidade

**Definição:** Capacidade de escolher, com o conhecimento e histórico disponíveis, a ação que oferece o melhor desempenho esperado. Não significa acertar o resultado sempre.

**Exemplo:** Escolher uma rota normalmente mais rápida, mesmo que ocorra um congestionamento inesperado.

### Autonomia

**Definição:** Grau em que o comportamento depende das próprias percepções e experiências, em vez de somente instruções fixas de quem programou.

**Exemplo:** Um robô aprende quais corredores têm mais obstáculos após várias viagens.

### Agente reativo

**Definição:** Agente que responde à percepção atual usando regras condição–ação, sem precisar construir um histórico interno para cada decisão.

**Exemplo:** Se o sensor detecta sujeira, o aspirador liga a sucção.

### Agente baseado em modelo

**Definição:** Agente que mantém um estado interno para estimar partes do mundo que não consegue observar diretamente; atualiza esse estado com ações e percepções.

**Exemplo:** Um robô lembra quais salas já visitou mesmo sem enxergá-las agora.

### Agente baseado em objetivos

**Definição:** Agente que avalia alternativas segundo um estado desejado e pode planejar ações para alcançá-lo.

**Exemplo:** Um navegador calcula como chegar a um endereço.

### Agente baseado em utilidade

**Definição:** Agente que compara resultados por uma função que expressa preferências e trade-offs, não apenas chegada a um objetivo.

**Exemplo:** Um sistema escolhe a entrega que combina menor custo, tempo e risco.

### Agente com aprendizagem

**Definição:** Agente que ajusta seu modo de decidir a partir da experiência e do retorno de suas ações, melhorando a atuação com o tempo.

**Exemplo:** Um filtro de spam aprende com mensagens classificadas pelo usuário.

## Síntese com autômatos

- **Caso escolhido:** compra de livros usados de IA pela Internet. Modelagem simplificada de um agente comprador.
- **Estados internos:** E1 — pesquisando opções; E2 — oferta adequada encontrada; E3 — compra concluída.
- **Percepções:** P1 — anúncio encontrado; P2 — preço total dentro do orçamento e condições aceitas; P3 — confirmação de pagamento.
- **Ações:** A1 — continuar pesquisando; A2 — realizar pedido; A3 — registrar a compra e encerrar.

- **Regra 1:** `E1 + P2 → E2 e A2 (oferta aprovada e pedido realizado).`

- **Regra 2:** `E2 + P3 → E3 e A3 (pagamento confirmado e operação encerrada).`

O estado E2 guarda a informação de que uma oferta anterior já foi avaliada e aprovada, mesmo que a tela atual só mostre a confirmação de pagamento. Limitação: três estados não representam bem variações de frete, múltiplos vendedores, cancelamentos ou devoluções; um agente real precisaria de mais memória e tratamento de exceções.

## Referências

- RUSSELL, Stuart; NORVIG, Peter. **Inteligência Artificial: uma abordagem moderna**. Capítulo 2 — Agentes inteligentes. Material disponibilizado na disciplina.
- VALÉRIA, Kadidja. **Agentes Inteligentes**. Slides da aula de 19 de outubro de 2026, UDF.

---

*Atividade acadêmica — UDF, 2026.*
