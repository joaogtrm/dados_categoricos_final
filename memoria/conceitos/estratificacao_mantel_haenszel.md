# Estratificação, Paradoxo de Simpson e Mantel-Haenszel

> **Nota sobre a fonte:** o arquivo de origem se chama `slide_concordancia.pdf`,
> mas o nome é enganoso — o conteúdo real do arquivo não trata de medidas de
> concordância (Kappa etc.). Ele é uma aula sobre estratificação, Paradoxo de
> Simpson, odds ratio ajustado de Mantel-Haenszel e teste de homogeneidade de
> Breslow-Day. Esta página documenta o conteúdo real do arquivo.

## 1. Definição

O **Paradoxo de Simpson** ocorre quando a associação entre duas variáveis,
medida numa tabela agregada (marginal), se inverte ou desaparece quando os
dados são estratificados por uma terceira variável. Isso acontece quando a
variável de estratificação está desbalanceadamente distribuída entre os
grupos comparados (confundimento) — a tabela agregada "mente" porque mistura
grupos com pesos amostrais muito diferentes.

O **método de Mantel-Haenszel** resolve isso combinando os estratos com um
peso apropriado, produzindo um odds ratio ajustado (θ_MH) que representa a
associação real, livre da distorção de confundimento. O **teste de
Breslow-Day**, por sua vez, verifica se é sequer válido resumir os estratos
num único OR ajustado: ele testa a hipótese de que o efeito (OR) é homogêneo
(igual) em todos os estratos. Se a homogeneidade é rejeitada, a variável de
estratificação não é apenas confundidora — ela é **modificadora de efeito**
(há interação), e um único OR combinado não descreve adequadamente o
fenômeno.

## 2. Quando usar

Usar quando há uma terceira variável categórica (K) que pode ser
**confundidora** da associação entre duas variáveis de interesse (X, exposição/
tratamento, e Y, desfecho) — isto é, quando a distribuição de K difere entre
os grupos de X e K também está associada a Y. Típico de estudos observacionais
ou quase-experimentais com alocação não uniforme entre estratos (ex.: um
tratamento aplicado preferencialmente a casos mais graves). A pergunta de
pesquisa é: "a associação bruta entre X e Y é real, ou é um artefato de K
estar desbalanceado entre os grupos?"

## 3. Pressupostos

- Tabelas 2x2 dentro de cada estrato de K (X binário, Y binário).
- Estratos devem ter tamanho amostral suficiente para estimativas estáveis
  (Mantel-Haenszel é robusto a estratos pequenos, mas não a zeros extremos).
- Para o OR combinado de Mantel-Haenszel fazer sentido como resumo único, o
  efeito deve ser razoavelmente homogêneo entre estratos — daí a necessidade
  de testar isso via Breslow-Day antes de reportar θ_MH como conclusão final.
- Independência das observações dentro e entre estratos.

## 4. Fórmula-chave

Para cada estrato *i* com células *a_i, b_i, c_i, d_i* (a = exposto/curado,
b = exposto/não curado, c = não exposto/curado, d = não exposto/não curado) e
total N_i:

**Odds Ratio de Mantel-Haenszel:**

θ_MH = ( Σ (a_i · d_i / N_i) ) / ( Σ (b_i · c_i / N_i) )

**Teste de Breslow-Day:** estatística qui-quadrado que compara, estrato a
estrato, o número observado de casos "a" com o esperado sob a hipótese de OR
comum (θ_MH), somando os desvios ponderados. Segue distribuição χ² com
(nº de estratos − 1) graus de liberdade sob H₀: OR homogêneo entre estratos.

## 5. Interpretação

- **OR bruto (crude) vs. OR ajustado (M-H):** se divergem muito, há indício
  de confundimento por K. No exemplo do slide (ensaio clínico: medicamento
  novo vs. padrão, estratificado por gravidade), o OR bruto era 0,08 (IC95%
  [0,06; 0,12]) — sugerindo que o medicamento novo era desastroso — enquanto
  o OR ajustado de Mantel-Haenszel subiu para 0,598 (p = 0,043). A causa: o
  medicamento novo foi aplicado predominantemente em casos graves (600 de
  800 pacientes), onde a cura é naturalmente rara, distorcendo a tabela
  agregada (viés de seleção/confundimento pela gravidade).
- **Teste de Breslow-Day:** no mesmo exemplo, X² = 35,599, df = 1,
  p = 2,424e-09 — rejeita-se a homogeneidade. Isso significa que mesmo o OR
  ajustado (0,598) é **inválido como resumo único**, porque o efeito do
  medicamento não é o mesmo nos dois estratos: OR = 1,20 em casos leves
  (medicamento aumenta a chance de cura em 20%) vs. OR = 0,069 em casos
  graves (medicamento é ineficaz/prejudicial). Ou seja, a gravidade não é
  apenas confundidora, é modificadora de efeito — a conclusão correta é
  reportar os OR por estrato separadamente, não uma média ponderada.
- Regra geral: comparar OR bruto x OR ajustado detecta confundimento;
  Breslow-Day decide se o ajuste único (M-H) é ou não apropriado, ou se a
  resposta certa é reportar por estrato.

## 6. Conexão com o trabalho

Essa técnica **não foi implementada diretamente** nos métodos 1/2/3 do
trabalho (qui-quadrado, regressão logística, log-linear), mas é o **análogo
formal, em tabela 2x2 estratificada, do que o método 3 (log-linear) já fez
de outro jeito** com uma tabela 3 vias.

O modelo log-linear ajustado (Rede × Grau × Modalidade, via `glm` com família
Poisson) testou a interação tripla e encontrou deviance = 654,13 com 2 graus
de liberdade, p < 2,2e-16 — ou seja, **o efeito de Modalidade sobre Rede não
é homogêneo entre os níveis de Grau Acadêmico** (mais pronunciado em
Tecnólogo: rede pública majoritariamente presencial, rede privada quase toda
EAD). Essa é conceitualmente a mesma pergunta que o teste de Breslow-Day
responde: "o efeito (aqui, a associação Rede×Modalidade) é igual em todos os
estratos (aqui, níveis de Grau)?" A rejeição da homogeneidade no log-linear
(interação tripla significativa) é equivalente, em espírito, à rejeição de
homogeneidade que o Breslow-Day sinalizaria.

Se o trabalho tivesse optado por estratificar em vez de modelar a três vias,
o caminho seria: calcular o OR de Rede×Modalidade separadamente por estrato
de Grau, combinar num θ_MH (OR ajustado) e testar sua validade com
Breslow-Day — que provavelmente rejeitaria a homogeneidade, replicando a
conclusão já obtida pelo log-linear de que Grau modifica o efeito, e que os
efeitos por estrato (por Grau) devem ser reportados separadamente em vez de
resumidos num único número.

## 7. Fonte

Arquivo: `slide_concordancia.pdf` (nome enganoso — conteúdo real é sobre
estratificação/Paradoxo de Simpson/Mantel-Haenszel/Breslow-Day, não sobre
medidas de concordância). 16 páginas, todas lidas e usadas como base desta
página.
