# Testes de Hipótese em Tabelas de Contingência

## Definição

Testes em tabelas de contingência avaliam se a distribuição de frequências observadas
numa tabela cruzando duas (ou mais) variáveis categóricas se "ajusta" a um modelo
teórico esperado — tipicamente o modelo de independência entre as variáveis. A
pergunta fundamental é: as diferenças entre o que foi observado ($n_{ij}$) e o que
seria esperado sob independência ($e_{ij}$) são fruto apenas do acaso, ou indicam uma
associação real entre as variáveis?

O teste mais usado nesse contexto é o qui-quadrado de Pearson, mas a família inclui
variações — correção de Yates, teste exato de Fisher, teste de McNemar — que se aplicam
conforme o tamanho amostral, a magnitude das frequências esperadas e se as observações
são independentes ou pareadas.

## Quando usar

- Duas variáveis categóricas (nominais ou ordinais) organizadas em tabela $I \times J$,
  e a pergunta é "essas variáveis são independentes ou associadas?".
- O delineamento amostral pode ser de três tipos, o que muda a interpretação (mas não o
  cálculo) do teste:
  1. **Produto de Binomiais**: os totais de linha são fixados de antemão (ex.: 100
     pacientes no grupo Tratamento, 100 no Controle); o foco é testar
     **homogeneidade** de proporções entre os grupos.
  2. **Multinomial**: só o total amostral $n$ é fixo; uma única amostra é classificada
     simultaneamente em duas variáveis; o foco é testar **independência**.
  3. **Poisson**: nem os totais de linha nem o total geral são fixos — apenas o
     tempo/espaço de observação; o foco é testar **ausência de interação**.
- Quando as observações são **pareadas** (mesmo indivíduo medido duas vezes — ex.:
  antes/depois, olho esquerdo/direito), usa-se o teste de McNemar em vez do
  qui-quadrado de Pearson.

## Pressupostos

- **Qui-quadrado de Pearson** (`correct = FALSE`): amostras grandes; todas as
  frequências esperadas $e_{ij} \geq 5$ (regra de bolso; alguns autores toleram até 10
  para amostras moderadas).
- **Correção de Yates** (`correct = TRUE`, default do R): amostras moderadas, algum
  $e_{ij}$ entre 5 e 10, tabelas $2\times2$; evita erro Tipo I inflado.
- **Teste exato de Fisher**: qualquer $e_{ij} < 5$; não depende de aproximação
  assintótica, calcula a probabilidade exata via distribuição hipergeométrica; é a
  escolha mais segura para tabelas com frequências observadas muito baixas.
- **Teste de McNemar**: exige observações pareadas/dependentes (o mesmo indivíduo nas
  duas medições); aplicar o teste de Pearson em dados pareados ignora a correlação
  intraclasse e leva a conclusões inválidas.
- Independência entre as unidades amostrais (exceto no caso de McNemar, que existe
  justamente para tratar a dependência intra-par).

## Fórmula-chave

**Estatística de Pearson**, somando sobre todas as células $(i,j)$ da tabela:

$$\chi^2_{calc} = \sum_{i=1}^{I} \sum_{j=1}^{J} \frac{(n_{ij} - e_{ij})^2}{e_{ij}}$$

Segue distribuição $\chi^2$ com $(I-1)(J-1)$ graus de liberdade. A frequência esperada
sob $H_0$ (independência) é estimada por

$$e_{ij} = \frac{n_{i+} \cdot n_{+j}}{n}$$

**Correção de Yates** (tabelas $2\times2$, amostras pequenas):

$$\chi^2_{corr} = \sum_{i,j} \frac{(|n_{ij}-e_{ij}| - 0{,}5)^2}{e_{ij}}$$

**Teste exato de Fisher** (probabilidade exata de $n_{11}$ dada a tabela $2\times2$ com
marginais fixas):

$$P(n_{11}) = \frac{\binom{n_{1+}}{n_{11}}\binom{n_{2+}}{n_{+1}-n_{11}}}{\binom{n}{n_{+1}}}
= \frac{n_{1+}!\,n_{2+}!\,n_{+1}!\,n_{+2}!}{n!\,n_{11}!\,n_{12}!\,n_{21}!\,n_{22}!}$$

**Estatística de McNemar** (baseada só nas células discordantes $n_{12}$ e $n_{21}$):

$$\chi^2_{Mc} = \frac{(n_{12}-n_{21})^2}{n_{12}+n_{21}} \sim \chi^2_1$$

## Interpretação

- Quanto **maior** a discrepância entre observados e esperados, maior o $\chi^2$ e
  **menor** o p-valor, levando à rejeição de $H_0$ (independência/homogeneidade).
- $H_0$ de independência: $\pi_{ij} = \pi_{i+}\pi_{+j}$ para todo $i,j$; $H_1$: essa
  igualdade falha para pelo menos um par.
- $H_0$ de McNemar: $p_{12} = p_{21}$ (simetria — probabilidade de mudar numa direção é
  igual à de mudar na outra); rejeitar indica mudança sistemática (ex.: treinamento
  teve efeito).
- Escolha do teste conforme os $e_{ij}$: Pearson se todos $e_{ij} \geq 5$; Yates se
  algum $e_{ij}$ entre 5 e 10 em tabela $2\times2$; Fisher se algum $e_{ij} < 5$.
- Numericamente, o cálculo do $\chi^2$ é idêntico nos três delineamentos amostrais
  (Binomial, Multinomial, Poisson) — a diferença entre eles é conceitual (o que está
  fixo por desenho vs. o que é aleatório), não o valor da estatística.
- p-valor sozinho não mede **força** da associação, só a evidência contra $H_0$; para
  isso usam-se medidas complementares como resíduos padronizados (qual célula puxa a
  associação) e V de Cramér (magnitude da associação, ver página de medidas de
  associação).

## Conexão com o trabalho

O **método 1** (`metodo1_qui_quadrado.R`) implementa diretamente o teste de Pearson
descrito aqui: cruza Rede de Ensino (Pública/Privada) com Área Geral CINE, Grau
Acadêmico e Modalidade de Ensino, rodando `chisq.test()` sobre cada tabela de
contingência. A base tem cerca de 706 mil observações (Censo da Educação Superior
2024/INEP), volume muito acima do mínimo de $e_{ij} \geq 5$ exigido pelo qui-quadrado —
não há necessidade de correção de Yates ou teste de Fisher aqui, ao contrário do que
esses métodos alternativos serviriam para tabelas pequenas.

Com N tão grande, a estatística $\chi^2$ fica inflada e o p-valor tende a ficar
praticamente zero (`< 2.2e-16`) em todas as tabelas testadas — ou seja, qualquer
associação, por menor que seja, é "estatisticamente significativa". Por isso o texto do
trabalho não se apoia só na significância: usa o **V de Cramér** (calculado em
`cramer_v()`, a partir de $\chi^2$ e da dimensão da tabela) como medida de **força** da
associação, e os **resíduos padronizados de Pearson** (`teste$stdres`, salvos em
`resultados/metodo1_residuos_*.csv`) para identificar quais células (quais
combinações rede × categoria) mais "puxam" a associação — célula com resíduo
$|>2|$ é interpretada como contribuindo significativamente para o desvio de
independência.

Os métodos 2 (regressão logística/odds ratio) e 3 (log-linear em tabela de 3 vias) não
usam diretamente a estatística de Pearson, mas herdam a mesma lógica de comparação
observado-vs-esperado sob independência: o log-linear, em particular, generaliza a
ideia de "ausência de interação" (delineamento de Poisson deste slide) para três
variáveis simultâneas.

## Fonte

`slide/slide_testes.pdf` — 17 páginas (slide "Testes em tabelas de contingência",
disciplina Dados Categóricos).
