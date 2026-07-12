# Tabelas de Contingência S x R

## Definição

Uma tabela de contingência $S \times R$ (também chamada tabela de dupla entrada ou
tabela de associação) cruza duas variáveis categóricas — uma com $S$ categorias
dispostas em linha, outra com $R$ categorias dispostas em coluna — e registra, em cada
célula $(i,j)$, a frequência absoluta observada $n_{ij}$ de indivíduos que caem
simultaneamente nas categorias $i$ e $j$. É a estrutura de dados básica para investigar
se duas variáveis qualitativas estão associadas.

A partir dessa mesma estrutura de tabela, quatro perguntas distintas podem ser feitas,
cada uma com seu próprio teste: (1) **independência** — as duas variáveis são
independentes numa única amostra? (2) **homogeneidade** — diferentes populações têm a
mesma distribuição de uma variável categórica? (3) **simetria** — numa tabela quadrada
com dados pareados, a probabilidade de cair em $(i,j)$ é igual à de cair em $(j,i)$? (4)
**homogeneidade marginal** — as distribuições marginais de linha e coluna de uma tabela
pareada são iguais? Os quatro se apoiam no mesmo modelo probabilístico (multinomial) e,
com exceção da simetria/homogeneidade marginal, levam à mesma estatística de teste —
mudando apenas o desenho amostral e a interpretação das margens.

## Quando usar

- **Independência**: uma única amostra, classificada simultaneamente em duas variáveis
  categóricas $X$ (S categorias) e $Y$ (R categorias); pergunta: "$X$ e $Y$ estão
  associadas?".
- **Homogeneidade**: $S$ populações (grupos) amostradas independentemente, cada uma
  classificada em $R$ categorias de uma mesma variável resposta; pergunta: "os grupos
  têm o mesmo perfil de distribuição?". Matematicamente idêntico ao teste de
  independência, mas as margens de linha são fixadas pelo desenho amostral (não
  observadas livremente).
- **Simetria (Bowker)**: tabela quadrada $R \times R$ com **dados pareados/emparelhados**
  (mesmo indivíduo classificado duas vezes nas mesmas $R$ categorias — ex.: antes/depois,
  avaliador A/avaliador B); pergunta: "a chance de migrar de $i$ para $j$ é igual à de
  migrar de $j$ para $i$?".
- **Homogeneidade marginal**: mesmo desenho pareado da simetria, mas a pergunta é mais
  fraca: "a distribuição geral (marginal) mudou entre a 1ª e a 2ª medição?", sem exigir
  simetria célula a célula. É a generalização do teste de McNemar para tabelas maiores
  que $2\times2$.

## Pressupostos

- Frequências esperadas $E_{ij}$ suficientemente grandes para a aproximação
  $\chi^2$ ser válida (amostras grandes); com contagens pequenas a aproximação assintótica
  fica instável — para tabelas $2\times2$ com frequências baixas, o slide recomenda o
  teste exato de Fisher (ver [[testes_hipotese]] para a fórmula).
- **Independência/homogeneidade**: unidades amostrais independentes entre si; no caso de
  homogeneidade, os $S$ grupos são amostras multinomiais independentes, podendo ter
  tamanhos $n_i$ diferentes.
- **Simetria e homogeneidade marginal**: exigem tabela quadrada ($R=S$, mesmas categorias
  nas duas dimensões) e dados **pareados** — a mesma unidade contribui para a linha e para
  a coluna. Aplicar o teste de independência/homogeneidade padrão nesse tipo de dado
  ignora a dependência intra-par e invalida a conclusão.
- Homogeneidade marginal é uma condição **menos restrita** que simetria: toda tabela
  simétrica tem homogeneidade marginal, mas o inverso não é necessariamente verdadeiro.

## Fórmula-chave

**Teste de independência / homogeneidade** — estatística de Pearson:

$$X^2 = \sum_{i=1}^{S}\sum_{j=1}^{R} \frac{(n_{ij}-E_{ij})^2}{E_{ij}}, \qquad
E_{ij} = \frac{n_{i+}\,n_{+j}}{n}$$

Sob $H_0$ (independência: $\pi_{ij}=\pi_{i+}\pi_{+j}$; ou homogeneidade:
$\pi_{1j}=\cdots=\pi_{Sj}$ para todo $j$), $X^2 \sim \chi^2_{(S-1)(R-1)}$. Alternativa
equivalente assintoticamente: razão de verossimilhança
$G^2 = 2\sum_{i,j} n_{ij}\log(n_{ij}/E_{ij})$, também $\chi^2_{(S-1)(R-1)}$ sob $H_0$.

**Resíduo padronizado de Pearson**, para localizar onde está a associação:

$$r_{ij} = \frac{n_{ij}-E_{ij}}{\sqrt{E_{ij}}}$$

**Teste de simetria de Bowker** (extensão do McNemar para $R\times R$), somando só sobre
os pares fora da diagonal ($i<j$):

$$X^2 = \sum_{i<j} \frac{(n_{ij}-n_{ji})^2}{n_{ij}+n_{ji}} \sim \chi^2_{R(R-1)/2} \text{ sob } H_0:\ \pi_{ij}=\pi_{ji}\ \forall i\neq j$$

**Teste de homogeneidade marginal** — estatística de Wald sobre o vetor de diferenças das
proporções marginais $\mathbf{d} = (\hat\pi_{1+}-\hat\pi_{+1}, \ldots, \hat\pi_{R+}-\hat\pi_{+R})$:

$$W = \mathbf{d}^\top \widehat{\mathrm{Var}}(\mathbf{d})^{-1} \mathbf{d} \sim \chi^2_{R-1} \text{ sob } H_0:\ \pi_{i+}=\pi_{+i}\ \forall i$$

No caso particular $R=2$ essa estatística coincide com o McNemar clássico,
$X^2=(n_{12}-n_{21})^2/(n_{12}+n_{21})$.

## Interpretação

- **$X^2$ (ou $G^2$) grande + p-valor baixo** → rejeita $H_0$: há evidência de
  associação (independência/homogeneidade) ou de assimetria/heterogeneidade marginal
  (Bowker/Wald), conforme o teste.
- **Resíduo padronizado $r_{ij}$**: $\approx 0$ é o esperado sob $H_0$; $|r_{ij}|>2$ (ou o
  limiar $\pm1{,}96$, aproximadamente 5% de significância) sinaliza célula com desvio
  relevante; $r_{ij}>0$ indica **mais** casos que o esperado naquela célula (associação
  positiva local); $r_{ij}<0$ indica **menos** casos que o esperado (associação
  negativa local). O teste global diz "há associação"; os resíduos dizem "onde".
- No teste de independência vs. homogeneidade, o **cálculo é idêntico**; a diferença é
  só conceitual — em independência as margens vêm todas da mesma amostra conjunta, em
  homogeneidade as margens de linha são fixas por desenho (grupos pré-definidos) e a
  hipótese recai sobre a igualdade das distribuições de coluna entre esses grupos.
- No teste de Bowker, $X^2$ alto = assimetria sistemática (migração mais forte num
  sentido do que no outro entre um par de categorias). No teste de homogeneidade
  marginal, $W$ alto = pelo menos uma categoria mudou de proporção global entre a 1ª e a
  2ª medição, mesmo que célula a célula a tabela pareça razoavelmente simétrica.
- Bowker é **mais restrito** que homogeneidade marginal: uma tabela pode ter margens
  homogêneas sem ser simétrica célula a célula; o inverso (simetria ⟹ homogeneidade
  marginal) sempre vale.

## Conexão com o trabalho

O **método 1** (`metodo1_qui_quadrado.R`) usa exatamente a lógica do teste de
independência/homogeneidade deste slide: cruza Rede de Ensino (Pública/Privada, $S=2$)
com Área Geral CINE (11 categorias, $R=11$), rodando `chisq.test()`. Como Pública e
Privada funcionam como duas populações pré-definidas cada uma distribuída entre as
áreas CINE, o desenho é, estritamente, de **homogeneidade** (margens de linha fixadas
pelas duas redes) — mas, como o slide explica, o cálculo é idêntico ao de independência,
por isso `chisq.test()` serve para os dois casos sem distinção de código.

Resultado obtido: $X^2 = 11846{,}4$ com $10$ graus de liberdade (($S-1)(R-1) = 1\times10$)
e p-valor $< 2{,}2\times10^{-16}$ — evidência esmagadora contra $H_0$ de que rede e área
CINE são independentes/homogêneas. Como o $N$ é enorme (Censo da Educação Superior
2024/INEP, ~706 mil observações), esse p-valor extremo não surpreende e não mede força
de associação — por isso o trabalho reporta também o **V de Cramér** ($V=0{,}128$, uma
métrica não coberta neste slide, ver [[testes_hipotese]]), indicando associação
estatisticamente significativa mas de magnitude fraca a moderada.

Os **resíduos padronizados de Pearson** ($r_{ij}$, fórmula desta página) identificam onde
a associação se concentra: a célula Pública×Educação tem resíduo $+83{,}57$ — muito acima
do limiar $|2|$, indicando forte excesso de matrículas em cursos de Educação na rede
pública frente ao esperado sob independência — enquanto Pública×Negócios tem resíduo
$-46{,}19$, indicando déficit acentuado (Negócios concentra-se na rede privada). A mesma
lógica de teste + V de Cramér + resíduos é repetida para Rede × Grau Acadêmico
($V=0{,}132$) e Rede × Modalidade de Ensino ($V=0{,}395$, a associação mais forte entre as
três, sugerindo que EAD vs. presencial é o fator mais distintivo entre rede pública e
privada nesta base).

Os testes de **simetria (Bowker)** e **homogeneidade marginal** deste slide não se
aplicam ao trabalho: exigem dados pareados (mesmo indivíduo medido duas vezes em
categorias idênticas nas duas dimensões), e a base do Censo é uma amostra transversal de
matrículas, sem essa estrutura de pareamento. Ficam registrados aqui por completude do
referencial teórico da disciplina, não por uso direto nos métodos 1/2/3.

## Fonte

`slide/slide_contingencia.pdf` — 68 páginas (slide "Tabelas de contingência S x R",
Prof. Ana Julia Alves Câmara, disciplina Análise de Dados Categorizados).
