# Modelos Log-lineares para Tabelas de Contingência Multivariadas

## 1. Definição

Um modelo log-linear modela o logaritmo da contagem esperada em cada célula de
uma tabela de contingência como uma soma de efeitos principais e termos de
interação entre as variáveis categóricas envolvidas — analogamente a uma ANOVA,
mas sobre frequências em vez de médias. Para uma tabela de duas vias com células
(i, j), o modelo saturado é ln(μᵢⱼ) = λ + λᵢˣ + λⱼʸ + λᵢⱼˣʸ; para três vias
(i, j, k), log(μᵢⱼₖ) = λ + λᵢˣ + λⱼʸ + λₖᶻ + λᵢⱼˣʸ + λᵢₖˣᶻ + λⱼₖʸᶻ + λᵢⱼₖˣʸᶻ.

A diferença central em relação à regressão logística é que nenhuma variável é
tratada como "resposta": todas entram simetricamente do lado direito da equação,
e o que se modela é a própria frequência esperada da célula. Isso torna o modelo
log-linear a ferramenta natural quando o interesse é a associação entre três ou
mais variáveis categóricas ao mesmo tempo, sem que exista uma hierarquia causal
clara entre elas.

## 2. Quando usar

- Tabelas de contingência com três ou mais variáveis categóricas (tabelas
  multiway), quando se quer entender como as associações entre pares de
  variáveis mudam (ou não) dependendo do nível de uma terceira variável —
  isto é, testar interação de segunda ordem ou superior.
- Quando nenhuma variável é naturalmente "resposta": o interesse é a
  **associação simétrica** entre todas as variáveis (ex.: "há associação entre
  Sexo, Renda e Escolaridade?"), e não prever uma variável específica em função
  das demais.
- Quando um modelo logístico já foi ajustado mas as variáveis preditoras têm
  colinearidade forte demais entre si para separar seus efeitos com clareza —
  o log-linear permite investigar diretamente se a interação entre duas
  preditoras muda em função de uma terceira, sem impor a assimetria de uma
  variável resposta.
- Casos clássicos: tabelas 2x2 (uso de cinto de segurança x sobrevivência),
  tabelas 3-way (cor de cabelo x cor dos olhos x sexo, dataset `HairEyeColor`
  do R) e tabelas maiores (fumante x exercício x doença).

## 3. Pressupostos

- Contagens de célula (frequências), não proporções ou médias — a resposta do
  GLM subjacente é sempre uma contagem.
- Distribuição de Poisson para as contagens, com função de ligação logarítmica
  (é um caso particular de GLM: `family = poisson`, `link = log`).
- **Hierarquia**: modelos log-lineares são hierárquicos — se uma interação de
  ordem k está incluída no modelo (ex.: A:B:C), todos os termos marginais dela
  também devem estar (A, B, C, A:B, A:C, B:C). Não se testa um termo de
  interação isolado sem seus efeitos principais e interações de ordem inferior.
- Comparações de deviance por razão de verossimilhança só são válidas entre
  **modelos aninhados** (um é caso particular do outro).
- Células com contagem esperada muito baixa (esparsidade) comprometem a
  aproximação qui-quadrado da distribuição da deviance — problema que cresce
  junto com o número de variáveis, pois o número de células da tabela cresce
  multiplicativamente enquanto o de parâmetros possíveis cresce
  exponencialmente (2^p − 1 termos possíveis para p variáveis).

## 4. Fórmula-chave

**Modelo saturado (tabela de 3 vias)**:

log(μᵢⱼₖ) = λ + λᵢˣ + λⱼʸ + λₖᶻ + λᵢⱼˣʸ + λᵢₖˣᶻ + λⱼₖʸᶻ + λᵢⱼₖˣʸᶻ

O modelo saturado tem exatamente tantos parâmetros quanto células da tabela —
não simplifica nada, apenas redesenha algebricamente as contagens observadas
(μ̂ᵢⱼₖ = nᵢⱼₖ, deviance = 0). O objetivo prático é sempre partir dele e testar
se termos de interação de ordem mais alta podem ser removidos sem prejuízo
significativo do ajuste (parcimônia).

**Deviance (G²)**, para comparar um modelo testado ao saturado:

G² = 2 Σᵢ Oᵢ · log(Oᵢ / Eᵢ)

onde Oᵢ são as contagens observadas e Eᵢ as contagens esperadas pelo modelo
ajustado. G² segue aproximadamente uma distribuição qui-quadrado, com graus de
liberdade iguais à diferença no número de parâmetros entre os dois modelos.

**Hierarquia de termos**: com p variáveis categóricas há 2^p − 1 termos
possíveis (efeitos principais + interações de todas as ordens, excluindo o
termo nulo). Para p=2 são 3 termos; p=3, 7 termos; p=4, 15 termos — o número de
*modelos hierárquicos* válidos cresce ainda mais rápido (3, 18, 84, 715, 9330
para p=2..6). Por isso a seleção de modelos usa teste de razão de
verossimilhanças entre modelos aninhados, critérios de informação (AIC, BIC) e,
em espaços grandes, seleção stepwise (`step()` no R) em vez de enumerar tudo.

No R, o atalho `glm(Freq ~ (A+B+C)^2, family=poisson)` ajusta efeitos
principais e todas as interações de 2ª ordem; `(A+B+C)^3` ou `A*B*C` dá o
modelo saturado.

## 5. Interpretação

- **Deviance**: mede a discrepância entre o modelo ajustado e o modelo
  saturado (que reproduz os dados perfeitamente, deviance = 0). Deviance
  grande → modelo mal ajustado.
- **Teste de razão de verossimilhança entre modelos aninhados** (via
  `anova(mod1, mod2, ..., test="Chisq")`): cada linha compara a queda de
  deviance entre um modelo e o seguinte, mais complexo. Uma queda
  estatisticamente significativa (p pequeno) indica que os termos adicionais
  melhoram o ajuste; se a queda não for significativa, o modelo mais simples é
  preferível (parcimônia).
- **AIC** = 2k − 2log(L̂): penaliza modelos mais complexos pelo número de
  parâmetros k. Menor AIC indica melhor equilíbrio entre ajuste e
  simplicidade; é a métrica usada para decidir entre modelos não
  necessariamente aninhados.
- **Resíduos**: erros de ajuste célula a célula (observado − esperado,
  padronizado). Usados para localizar *onde* o modelo reduzido falha em
  capturar o padrão dos dados — tipicamente a razão de existir uma interação
  significativa é que certas combinações de categorias têm contagens muito
  diferentes do que a ausência de interação preveria.
- **Odds ratio a partir do log-linear**: em uma tabela 2x2, o parâmetro de
  interação λᵢⱼˣʸ do modelo saturado se relaciona diretamente ao log da razão
  de chances (θ): sob a restrição de referência λ₁ˣ = λ₁ʸ = 0, tem-se
  ln(θ) = λ₂₂ˣʸ, ou seja, θ = e^(λ₂₂ˣʸ). Isso mostra que o log-linear e a
  regressão logística, quando aplicados à mesma tabela com uma variável
  tratada como resposta, são reparametrizações um do outro e chegam à mesma
  informação associativa — a diferença é só a categoria de referência e a
  simetria (ou não) da estrutura do modelo.

## 6. Conexão com o trabalho

O método 3 do trabalho ajusta um modelo log-linear à tabela de três vias Rede
(Pública/Privada) × Grau Acadêmico (Bacharelado/Licenciatura/Tecnológico) ×
Modalidade (Presencial/EAD), via
`glm(Freq ~ rede*grau*modalidade, family=poisson)` — o modelo saturado dessa
tabela 2×3×2.

A comparação entre o modelo saturado e o modelo reduzido sem o termo de
interação tripla (rede:grau:modalidade) foi feita por razão de
verossimilhança: deviance = 654,13 com 2 graus de liberdade, p < 2,2e-16.
Como manda a lógica de hierarquia de modelos descrita no slide, essa
diferença enorme e altamente significativa indica que a interação tripla
**não pode ser removida** — a associação entre rede e modalidade muda
dependendo do grau acadêmico do curso, e vice-versa. Isto é: o modelo mais
simples (apenas interações de 2ª ordem) falha sistematicamente em reproduzir
as contagens observadas.

Os resíduos padronizados do modelo reduzido (sem a tripla) localizam onde
essa falha é maior: na categoria Tecnólogo. Na rede pública, cursos
tecnológicos são majoritariamente presenciais (1.318 presenciais vs. 1.153
EAD), enquanto na rede privada são quase todos EAD (332.227 EAD vs. 3.876
presenciais) — um padrão de associação rede×modalidade que se **inverte** em
relação ao observado em Bacharelado. É exatamente esse tipo de "a associação
entre duas variáveis depende do nível de uma terceira" que só um termo de
interação tripla capta, e que uma tabela 2x2 ou um modelo aditivo não
conseguiriam expressar.

Esse resultado resolve uma ambiguidade deixada pelo método 2 (regressão
logística): ali, área, grau e modalidade mostravam colinearidade forte
demais para separar os efeitos individuais com clareza (seção 6 da página
[[medidas_associacao]] traz os OR obtidos). O modelo log-linear, por tratar
as três variáveis simetricamente em vez de forçar uma delas a ser "resposta",
permite testar diretamente se a interação entre rede e modalidade é
condicional ao grau — e confirma que sim, com a direção oposta em Tecnólogo
sendo o achado substantivo que a regressão logística, sozinha, não deixava
enxergar.

## 7. Fonte

`slide/slide_log_linear.pdf` — 55 páginas.
