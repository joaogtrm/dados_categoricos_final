# Ordem de execução dos scripts

Execute a partir da raiz do projeto, nesta ordem. Os scripts Python usam
`pandas`/`scipy`/`matplotlib`; os `.R` usam apenas funções base do R (`glm`,
`chisq.test`, etc.), sem pacotes extras.

## 1. `scripts/merge_e_seleciona.py`
Lê `dados/MICRODADOS_CADASTRO_CURSOS_2024.CSV`, seleciona as variáveis
categóricas de interesse e salva `dados/base_categorica_2024.pkl`. Todos os
scripts seguintes dependem desse arquivo — rode este primeiro.

```
python scripts/merge_e_seleciona.py
```

## 2. `scripts/contagem_rede.py` (opcional)
Conferência rápida: imprime no console a contagem de ofertas por Rede de
Ensino (Pública vs Privada). Não gera arquivo, só checagem manual.

```
python scripts/contagem_rede.py
```

## 3. `scripts/analise_descritiva.py`
Medidas descritivas (univariadas e bivariadas contra `TP_REDE`) e os gráficos
da análise exploratória do artigo.

```
python scripts/analise_descritiva.py
```

Saídas em `resultados/descritiva/`:
- `resumo_univariado.csv`
- `tabelas/freq_<VAR>.csv`, `tabelas/crosstab_<VAR>_por_rede.csv`, `tabelas/crosstab_pct_<VAR>_por_rede.csv`
- `graficos/uni_<VAR>.png`, `graficos/bi_<VAR>_por_rede.png`, `graficos/heatmap_<VAR>_por_rede.png`

## 4. `scripts/metodo1_qui_quadrado.py`
Qui-quadrado de independência, V de Cramér e resíduos padronizados de Pearson
para Rede de Ensino x (Área Geral, Grau Acadêmico, Modalidade de Ensino). Lê o
`.pkl` diretamente.

```
python scripts/metodo1_qui_quadrado.py
```

Saídas em `resultados/metodo1/`:
- `residuos_area_geral.csv`, `residuos_grau.csv`, `residuos_modalidade.csv`

## 5. `scripts/converter_pkl_para_csv.py`
Converte `dados/base_categorica_2024.pkl` em `dados/base_categorica_2024.csv`.
Necessário só a partir daqui, pois os métodos 2 e 3 são em R e leem CSV.

```
python scripts/converter_pkl_para_csv.py
```

## 6. `scripts/metodo2_regressao_logistica.R`
Regressão logística: Rede (Pública=1) ~ Área Geral + Grau Acadêmico +
Modalidade + Região. Odds ratios com IC 95% (Wald) e pseudo-R² de McFadden.

```
Rscript scripts/metodo2_regressao_logistica.R
```

Saída: `resultados/metodo2_odds_ratios.csv`

## 7. `scripts/metodo3_log_linear.R`
Modelo log-linear (tabela 3 vias Rede x Grau Acadêmico x Modalidade),
testando se a interação tripla é necessária via razão de verossimilhança.

```
Rscript scripts/metodo3_log_linear.R
```

Saída: `resultados/metodo3_log_linear.csv`

---

Resumo da dependência de dados:

```
MICRODADOS_CADASTRO_CURSOS_2024.CSV
        │
        ▼ (1) merge_e_seleciona.py
base_categorica_2024.pkl
        │
        ├─▶ (2) contagem_rede.py            [checagem, sem saída]
        ├─▶ (3) analise_descritiva.py        → resultados/descritiva/
        ├─▶ (4) metodo1_qui_quadrado.py      → resultados/metodo1/
        │
        ▼ (5) converter_pkl_para_csv.py
base_categorica_2024.csv
        │
        ├─▶ (6) metodo2_regressao_logistica.R → resultados/metodo2_odds_ratios.csv
        └─▶ (7) metodo3_log_linear.R          → resultados/metodo3_log_linear.csv
```

Os passos 2–4 só precisam ser refeitos se a base (`.pkl`) mudar. Os passos
5–7 só precisam rodar de novo se o `.pkl` ou o próprio `.csv` mudarem. O
passo 1 só precisa rodar de novo se o CSV bruto do INEP mudar.
