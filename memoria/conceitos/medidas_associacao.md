# Medidas de Associação: Risco Relativo, Diferença de Proporções e Odds Ratio

## 1. Definição

Medidas de associação quantificam o quanto duas variáveis categóricas (tipicamente
uma exposição/tratamento e um desfecho binário) estão relacionadas, além do teste
de significância. Enquanto o qui-quadrado só responde "existe associação?", essas
medidas respondem "qual o tamanho e o sentido dela?". O slide trata três medidas
para tabelas 2x2: Risco Relativo (RR), Diferença de Proporções/Risco Atribuível (DP)
e Odds Ratio (OR).

Risco Relativo e Diferença de Proporções exigem que se conheça a incidência real do
desfecho em cada grupo (isto é, os totais de linha são fixados pelo desenho do
estudo — coorte). Odds Ratio, por outro lado, compara chances (odds) em vez de
riscos, e é a medida indicada quando a incidência não pode ser calculada
diretamente, como em estudos caso-controle.

## 2. Quando usar

- **RR e Diferença de Proporções**: estudos de coorte, onde os grupos são definidos
  pela exposição (ex.: tratamento vs. placebo) e se acompanha a incidência do
  desfecho ao longo do tempo. Os totais de cada grupo (expostos/não expostos) são
  conhecidos e fixados de antemão.
- **Odds Ratio**: estudos caso-controle, onde os grupos são definidos pelo desfecho
  (casos vs. controles) e não é possível calcular incidência real, pois o
  pesquisador escolhe artificialmente quantos casos e controles entram no estudo.
  OR também é a medida natural quando o modelo estatístico usado é uma regressão
  logística, já que o coeficiente da regressão é, por construção, um log-odds.

## 3. Pressupostos

- Tabela de contingência 2x2 (exposição x desfecho, ambos binários).
- Para RR e DP: desenho de coorte — os totais de linha (expostos/não expostos)
  precisam refletir a incidência real na população, não uma amostragem
  desbalanceada artificialmente.
- Para OR em caso-controle: os totais de linha (casos/controles) são fixados pelo
  desenho, então RR e DP não podem ser calculados a partir deles — apenas OR é
  interpretável.
- Amostra suficientemente grande para que o intervalo de confiança seja informativo;
  amostras pequenas produzem IC largos (baixa precisão), mesmo quando a estimativa
  pontual é significativa.
- Em doenças/desfechos raros, OR se aproxima do RR; fora dessa condição, OR é
  sempre mais "extremo" (mais distante de 1) que o RR.

## 4. Fórmula-chave

Considerando uma tabela 2x2 com células a, b, c, d (a = expostos com desfecho,
b = expostos sem desfecho, c = não expostos com desfecho, d = não expostos sem
desfecho), n1 = a+b, n2 = c+d:

### Risco Relativo (RR)

RR = (a / n1) / (c / n2)

Razão entre a incidência no grupo exposto e a incidência no grupo não exposto.

### Diferença de Proporções (DP, Risco Atribuível)

DP = (a / n1) − (c / n2)

Diferença absoluta entre as duas incidências (Ie − Ine). Indica o excesso (ou
redução) de casos atribuível à exposição, em pontos percentuais.

### Odds Ratio (OR)

Em caso-controle, com a = casos expostos, b = controles expostos, c = casos não
expostos, d = controles não expostos:

OR = (a/c) / (b/d) = (a·d) / (b·c)

Razão entre a chance (odds) de exposição entre os casos e a chance de exposição
entre os controles — equivalente à razão de chances do desfecho entre expostos e
não expostos.

Em R, ambas podem ser obtidas com o pacote `epiR`, função `epi.2by2()`, usando
`method = "cohort.count"` (RR e DP) ou `method = "case.control"` (OR).

## 5. Interpretação

### Risco Relativo

- RR = 1: nenhuma associação.
- RR < 1: exposição é fator de proteção (reduz o risco).
- RR > 1: exposição é fator de risco (aumenta o risco).
- Exemplo do slide (medicamento vs. placebo, infarto): RR = 0,50, IC95% (0,29;
  0,87). Como o intervalo inteiro está abaixo de 1, o medicamento é fator de
  proteção estatisticamente significativo — o grupo tratado tem metade do risco do
  grupo placebo.

### Diferença de Proporções

- DP = 0: nenhuma diferença absoluta de risco.
- Sinal negativo: exposição reduz o risco em termos absolutos; sinal positivo,
  aumenta.
- Exemplo do slide: DP = −15,00 (por 100 pessoas), IC95% (−26,39; −3,61). Não
  inclui o zero, logo a redução absoluta de 15 casos a cada 100 pessoas tratadas é
  real na população, não apenas ruído amostral.

### Odds Ratio

- OR = 1: nenhuma associação entre exposição e desfecho.
- OR < 1: exposição associada a menor chance do desfecho (fator de proteção).
- OR > 1: exposição associada a maior chance do desfecho (fator de risco).
- Importante: OR não deve ser lido como "a exposição aumenta o risco em X vezes"
  (isso é RR) — deve ser lido como "a chance de exposição é X vezes maior entre
  quem tem o desfecho do que entre quem não tem" (ou, equivalentemente, a chance do
  desfecho é X vezes maior entre expostos).
- Exemplo do slide (pesticida vs. doença rara): OR = 9,33, IC95% (4,29; 20,33),
  p<0,001. Limite inferior bem acima de 1 → associação forte e significativa. Mas
  o IC é largo (4,29 a 20,33), sinal de baixa precisão, tipicamente por tamanho
  amostral pequeno (n=150) — a magnitude exata do efeito é incerta mesmo com a
  direção sendo clara.

## 6. Conexão com o trabalho

O trabalho não usa RR nem Diferença de Proporções diretamente (os dados do Censo
da Educação Superior não vêm de um desenho de coorte/caso-controle), mas o
princípio de "medida de associação além do teste de hipótese" é o mesmo que
sustenta duas medidas efetivamente usadas:

- **Método 1 (qui-quadrado + V de Cramér)**: V de Cramér cumpre, para tabelas
  maiores que 2x2, o mesmo papel que RR/OR cumprem em 2x2 — quantificar a força da
  associação depois que o qui-quadrado já indicou que ela existe. No trabalho, V de
  Cramér deu 0,128 para Rede x Área Geral, 0,132 para Rede x Grau, e 0,395 para
  Rede x Modalidade — a associação mais forte das três, indicando que a rede
  (pública/privada) está fortemente ligada à modalidade de ensino (presencial vs.
  EAD).
- **Método 2 (regressão logística)**: usa Odds Ratio exatamente como descrito neste
  slide — a chance de um curso ser da rede privada (ou do desfecho modelado) é
  comparada via razão de chances. No trabalho, `modalidadeEAD` teve OR = 0,023 e
  área "Educação" teve OR = 0,108 (com N = 706 mil observações), ambos muito
  abaixo de 1, ou seja, fatores fortemente associados a menor chance do desfecho de
  referência da regressão. A leitura desses OR segue a mesma lógica do exemplo do
  pesticida no slide: não se diz que a modalidade EAD "reduz o risco em 0,023
  vezes", mas que a chance do desfecho é cerca de 43 vezes menor (1/0,023) nessa
  categoria em comparação à categoria de referência.

## 7. Fonte

`slide/slide_associacao.pdf` — 12 páginas.
