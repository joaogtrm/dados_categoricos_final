# Resultado — Método 2: Regressão Logística (Rede ~ Área + Grau×Modalidade + Região)

## 1. O que foi testado

`glm(rede_bin ~ area_geral + grau * modalidade + regiao, family = binomial)`,
rede_bin = 1 se Pública. Script: `metodo2_regressao_logistica.R`. Casos
completos: 706.556 de 720.349 (13.793 descartados por NA; área "Programas
básicos", 2.042 cursos, sai do modelo por ter 100% de Grau Acadêmico
ausente). Categorias de referência: Negócios/administração/direito,
Bacharelado, Presencial, Sudeste.

## 2. Resultado bruto

- Pseudo-R² de McFadden = 0,324
- Razão de verossimilhança (modelo completo vs. nulo): χ²=57.174,8, 18 gl, p<2,2e-16
- Interação grau×modalidade: LRT χ²=495,43, 2 gl, p<2,2e-16 (AIC cai de 119.578,8 pra 119.087,4)

Odds ratios (IC 95% Wald) selecionados — tabela completa em
`resultados/metodo2_odds_ratios.csv`:

| Termo | OR | IC 95% | Leitura |
|---|---|---|---|
| area_geralEducação | 0,093 | [0,046; 0,186] | Educação associada a maior chance de pública (~11x, invertendo a referência) |
| area_geralCiências naturais... | 2,759 | [2,49; 3,06] | maior chance de pública |
| modalidadeEAD | 0,033 | [0,031; 0,034] | EAD fortemente associado a privada |
| grauLicenciatura | 52,23 | [26,0; 104,9] | instável — ver limitações |
| grauTecnológico | 0,793 | [0,736; 0,856] | leve associação a pública, mas ver interação |
| grauLicenciatura:modalidadeEAD | 0,684 | [0,632; 0,742] | efeito de EAD é menor dentro de Licenciatura que em Bacharelado |
| grauTecnológico:modalidadeEAD | 0,316 | [0,286; 0,350] | efeito de EAD é maior dentro de Tecnológico que em Bacharelado |
| regiaoNordeste | 1,264 | [1,213; 1,317] | leve associação a pública |
| regiaoSul | 0,611 | [0,582; 0,642] | associação a privada |

## 3. Leitura

Controlando por área, grau, modalidade e região simultaneamente, a
combinação que mais caracteriza a rede privada é EAD (OR=0,033, a mais
extrema do modelo) — muito mais forte que qualquer área isolada. Os termos
de interação confirmam o que o método 3 já mostrou de outro jeito: o efeito
de EAD sobre a chance de ser pública **não é uniforme por grau** — é mais
atenuado em Licenciatura (OR interação 0,684) e mais acentuado em
Tecnológico (OR interação 0,316) que o esperado pela soma dos efeitos
principais.

## 4. Limitações/cautelas

- **`grauLicenciatura` (OR=52,23, IC [26; 105]) não é interpretável como
  efeito parcial.** 100% dos cursos de Licenciatura estão na área Educação
  e 93,3% da área Educação é Licenciatura — colinearidade quase
  determinística pela taxonomia CINE, não corrigível adicionando mais
  termos ao modelo (testado: adicionar grau×modalidade piorou o IC, não
  melhorou). Reportar o sinal (positivo), não a magnitude.
- Modelo é pra inferência sobre associação/OR, não pra classificação — a
  classe "Pública" é 2,8% da base, desbalanceamento extremo que inviabiliza
  uso do modelo como preditor sem reamostragem.
- IC é de Wald (não perfil), escolha deliberada pelo custo computacional em
  N=706 mil; validade assintótica é excelente nesse tamanho de amostra.

## 5. Arquivo de saída

`resultados/metodo2_odds_ratios.csv` (tabela completa, 19 termos).
