# Regressão Logística Binária

## 1. Definição

A regressão logística binária modela a probabilidade de um evento com resposta
dicotômica Y ∈ {0,1} em função de um ou mais preditores (contínuos e/ou
categóricos). Em vez de modelar π(x) diretamente — o que poderia gerar valores
fora do intervalo [0,1] — o modelo aplica a transformação logito (log-odds):

log( π(x) / (1 − π(x)) ) = β₀ + β₁x₁ + ... + βₚxₚ

Essa função de ligação garante que a probabilidade estimada π(x) = eᵝ /(1+eᵝ)
esteja sempre entre 0 e 1: a reta η = β₀+β₁x é "espremida" numa curva em S
(função logística). Os parâmetros são estimados por Máxima Verossimilhança (EMV);
como não há solução fechada, usam-se métodos iterativos (Newton-Raphson ou Fisher
scoring).

É a extensão natural, para variáveis explicativas contínuas e múltiplas
covariáveis simultâneas, do que a Odds Ratio faz numa tabela 2x2: o coeficiente
de cada preditor, exponenciado, é uma razão de chances.

## 2. Quando usar

- A variável resposta é binária (sucesso/fracasso, sim/não, pertence/não pertence
  a um grupo).
- Quer-se estimar o efeito de múltiplos preditores (contínuos, binários ou
  categóricos com vários níveis) simultaneamente sobre a chance do evento,
  controlando uns pelos outros — diferente do qui-quadrado ou de OR/RR simples,
  que tratam uma associação por vez.
- A pergunta de pesquisa é do tipo "controlando por X₂, X₃, ..., qual o efeito de
  X₁ na chance do evento Y=1?" — inclusive permitindo estratificação (efeito de
  uma covariável dentro de níveis de um fator de confusão) e termos de interação
  quando o efeito de um preditor muda conforme outro.

## 3. Pressupostos

- **Linearidade no logito**: o logito da probabilidade é uma função linear das
  covariáveis (não a probabilidade em si, que é curva em S).
- **Independência das observações**.
- **Ausência de multicolinearidade severa** entre preditores — verificável com
  VIF (Variance Inflation Factor via `car::vif()`); VIFs < 5 indicam ausência de
  colinearidade forte. Quando dois preditores categóricos se sobrepõem quase
  perfeitamente, o efeito aparece como erro padrão inflado e IC muito largo,
  mesmo com sinal do coeficiente correto.
- **Amostra grande o suficiente** para que as aproximações assintóticas (teste de
  Wald, EMV) sejam válidas.
- Preditores categóricos entram via codificação dummy, com uma categoria de
  referência; níveis sem nenhuma observação em algum cruzamento levam o `glm` a
  "aliasar" o coeficiente correspondente — ele simplesmente some da tabela de
  saída, sem aviso explícito.

## 4. Fórmula-chave

**Probabilidade do sucesso / função logística:**

π(x) = eᵝ⁰⁺ᵝ¹ˣ¹⁺...⁺ᵝᵖˣᵖ / (1 + eᵝ⁰⁺ᵝ¹ˣ¹⁺...⁺ᵝᵖˣᵖ)

**Logito (função de ligação):**

log( π(x) / (1 − π(x)) ) = β₀ + β₁x₁ + ... + βₚxₚ

**Log-verossimilhança maximizada na estimação:**

ℓ(β) = Σᵢ [ yᵢ log(π(xᵢ)) + (1 − yᵢ) log(1 − π(xᵢ)) ]

**Erro padrão e teste de Wald** (para cada coeficiente βⱼ):

Var(β̂) = (XᵀWX)⁻¹, z = β̂ⱼ / EP(β̂ⱼ) ~ N(0,1)

**Razão de chances (odds ratio):**

ORⱼ = exp(βⱼ)

**IC de Wald para a OR:**

( exp(β̂ⱼ − z_{α/2}·EP), exp(β̂ⱼ + z_{α/2}·EP) )

**Teste de razão de verossimilhança** (compara modelo completo vs. reduzido/nulo,
útil para testar múltiplos coeficientes de uma vez, ex.: todos os níveis de um
fator categórico):

G² = −2 [ ℓ_reduzido − ℓ_completo ] ~ χ²_gl, gl = diferença no nº de parâmetros

**Pseudo-R² (ex.: McFadden):**

R²_McFadden = 1 − (deviance do modelo / deviance nula)

## 5. Interpretação

- **Coeficiente βⱼ (escala do logito)**: variação no log-odds do evento para
  cada unidade de aumento em xⱼ, mantendo as demais variáveis constantes.
  Positivo aumenta a chance, negativo diminui — mas a magnitude só é
  diretamente interpretável na escala log; por isso se exponencia.
- **Odds Ratio (exp(βⱼ))**: variação multiplicativa na chance do evento por
  unidade de xⱼ (ou, para dummy de categórica, a chance da categoria em
  relação à categoria de referência). OR=1 → sem associação; OR>1 → a variável
  aumenta a chance; OR<1 → diminui a chance. Não deve ser lido como "aumenta o
  risco em X vezes" (isso é RR) — é sempre chance (odds), não probabilidade.
- **IC 95% da OR**: se o intervalo não contém 1, o efeito é estatisticamente
  significativo ao nível de 5%. Quanto mais largo o IC, menos precisa é a
  estimativa da magnitude do efeito (mesmo que a direção seja clara) — sinal
  típico de amostra pequena no estrato ou de colinearidade entre preditores.
- **P-valor** (teste de Wald, z = β̂/EP): testa H₀: βⱼ=0, isto é, se aquele
  preditor específico tem efeito nulo controlando pelos demais. Em amostras
  pequenas, o teste de razão de verossimilhança (LRT) é mais confiável que Wald.
- **Pseudo-R² (McFadden, Nagelkerke, Cox-Snell)**: mede qualidade de ajuste,
  varia de 0 a 1 (quanto maior, melhor), mas não é comparável em escala ao R²
  da regressão linear — mesmo modelos bons costumam ter valores bem abaixo de 1.
- **Deviance e resíduos de deviance**: medem discrepância entre observado e
  ajustado, comparando com o modelo saturado; usados em gráficos de diagnóstico
  (Q-Q dos resíduos deviance, resíduos vs. ajustados, distância de Cook) para
  checar outliers e pontos de alta influência.
- **Curva ROC / AUC e estatística KS**: avaliam a capacidade discriminativa do
  modelo (não apenas o ajuste). AUC varia de 0,5 (modelo aleatório) a 1 (perfeito);
  KS mede a maior distância vertical entre as CDFs das probabilidades preditas
  nos grupos evento/não-evento — ambos usados para avaliar separação de classes,
  não significância de coeficientes.

## 6. Conexão com o trabalho

O método 2 do trabalho ajusta exatamente o modelo logístico múltiplo descrito
aqui:

```r
glm(rede_bin ~ area_geral + grau + modalidade + regiao, data = df_modelo, family = binomial)
```

com `rede_bin` = 1 para rede pública (evento de interesse), sobre 706.556 casos
completos do Censo da Educação Superior 2024. Pontos de conexão direta com a
teoria do slide:

- **Casos completos e aliasing silencioso**: a área "Programas básicos" (2.042
  cursos) tem 100% de valores ausentes em Grau Acadêmico. O script filtra
  `complete.cases()` e aplica `droplevels()` **antes** de criar os fatores
  justamente porque, se um nível ficasse sem nenhuma observação completa, o
  `glm` aliasaria o coeficiente correspondente — ele desapareceria da tabela de
  saída sem gerar erro, exatamente o comportamento descrito na seção de
  pressupostos sobre preditores categóricos.
- **Releveling**: `relevel()` é usado para trocar a categoria de referência de
  cada fator para a mais frequente (Negócios/administração/direito, Bacharelado,
  Presencial, Sudeste), tornando os coeficientes mais interpretáveis — mesma
  técnica do exemplo do slide (`relevel(dados$x3, ref = "B")`).
- **IC de Wald em vez de perfil**: com N=706.556, o IC de verossimilhança-perfil
  seria computacionalmente caro sem ganho prático; o script usa
  `confint.default()` (Wald), coerente com a seção de inferência do slide (teste
  de Wald e IC β̂ⱼ ± z_{α/2}·EP).
- **Qualidade de ajuste**: pseudo-R² de McFadden = 0,322 e teste de razão de
  verossimilhança (modelo completo vs. nulo) com qui-quadrado = 56.679,3, 16 gl,
  p<2,2e-16 — o conjunto de preditores é conjuntamente muito significativo,
  exatamente o G² = −2(ℓ_reduzido − ℓ_completo) descrito na fórmula-chave.
- **Multicolinearidade como achado prático**: `grauLicenciatura` saiu com
  OR=39,16 e IC muito largo (19,6–78,4). Isso não é um erro do modelo — é o
  sintoma clássico de multicolinearidade severa mencionado nos pressupostos:
  Grau Acadêmico "Licenciatura" e Área Geral "Educação" praticamente coincidem
  nos dados (quase todo curso de Licenciatura está na área Educação), então o
  modelo tem dificuldade de separar o efeito de um do outro, inflando o erro
  padrão desse coeficiente específico. O teste geral do modelo (LRT,
  qui-quadrado=56679,3, p<2,2e-16) continua válido — a colinearidade degrada a
  precisão de coeficientes individuais, não a validade do ajuste global. Isso é
  citado no próprio script (`cat(...)` de aviso) como ponto a tratar com cautela
  na Discussão do artigo, e ilustra por que checar VIF (ou, quando VIF não é
  aplicável por causa de fatores quase colineares, observar diretamente a
  magnitude/largura do IC) é parte necessária do diagnóstico do modelo.

## 7. Fonte

`slide/slide_regressao_logistica.pdf` — 72 páginas.
