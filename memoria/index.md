# Índice da Wiki — Referencial Teórico

## Conceitos estatísticos (de `slide/`)

- [Testes de hipótese](conceitos/testes_hipotese.md) — qui-quadrado de Pearson, correção de Yates, teste exato de Fisher, McNemar. Base do método 1.
- [Medidas de associação](conceitos/medidas_associacao.md) — Risco Relativo, Diferença de Proporções, Odds Ratio (coorte vs. caso-controle). Base do V de Cramér (método 1) e OR (método 2).
- [Tabelas de contingência](conceitos/tabelas_contingencia.md) — independência, homogeneidade, simetria de Bowker, homogeneidade marginal. Base direta do método 1.
- [Regressão logística](conceitos/regressao_logistica.md) — logito, EMV, odds ratio, pseudo-R² de McFadden. Base do método 2.
- [Modelos log-lineares](conceitos/modelos_log_lineares.md) — GLM Poisson sobre tabelas multi-way, hierarquia de termos, deviance. Base do método 3.
- [Estratificação e Mantel-Haenszel](conceitos/estratificacao_mantel_haenszel.md) — Paradoxo de Simpson, OR ajustado, Breslow-Day. Análogo conceitual ao método 3 (arquivo fonte mal nomeado, ver nota na página).

## Fontes ingeridas

| Arquivo | Páginas | Página(s) da wiki | Status |
|---|---|---|---|
| `slide/slide_testes.pdf` | 17 | testes_hipotese.md | ingerido 2026-07-11 |
| `slide/slide_associacao.pdf` | 12 | medidas_associacao.md | ingerido 2026-07-11 |
| `slide/slide_contingencia.pdf` | 68 | tabelas_contingencia.md | ingerido 2026-07-11 |
| `slide/slide_regressao_logistica.pdf` | 72 | regressao_logistica.md | ingerido 2026-07-11 |
| `slide/slide_log_linear.pdf` | 55 | modelos_log_lineares.md | ingerido 2026-07-11 |
| `slide/slide_estratificacao_mantel_haenszel.pdf` (renomeado; nome original `slide_concordancia.pdf` era enganoso) | 16 | estratificacao_mantel_haenszel.md | ingerido 2026-07-11 |

## Literatura temática (de `raw/`)

- [Alonso 2010 — Expansão e EaD](fontes/alonso2010ead.md) — lógica privatista/quantitativista da expansão, EaD nascente (2007-08) já concentrada na privada.
- [Benevides Soares et al. 2023 — Satisfação com o curso](fontes/benevidessoares2023satisfacao.md) — privados ligam satisfação a retorno financeiro/institucional; públicos, a envolvimento acadêmico.
- [Carvalho 2013 — Mercantilização](fontes/carvalho2013mercantilizacao.md) — já citado em `ref.bib` (`carvalho2013mercantilizacao`). Crescimento assimétrico das lucrativas, EAD puxada por elas já em 2008-09, financeirização.
- [Durham — Ensino superior público e privado](fontes/durham_ensino_publico_privado.md) — trajetória histórica 1808-2003, origem do "mass private sector" nos anos 70, vínculo público-pesquisa.
- [Martins 2002 — O setor privado](fontes/martins2002setorprivado.md) — resenha (não artigo original) sobre a tese do "mass private sector" como absorvedor de demanda de massa.
- [Moraes 2025 — CSTGQ Curitiba](fontes/moraes2025cstgq.md) — estudo de caso de tecnólogo presencial; pública e privadas convergem no currículo quando a modalidade é a mesma.
- [Mota e Anjos 2012 — Turismo no Nordeste](fontes/mota2012educacao.md) — já citado em `ref.bib` (`mota2012educacao`). 92% dos cursos de Turismo são privados; oferta federal 100% Tecnólogo.
- [Pinto 2004 — Acesso à educação superior](fontes/pinto2004acesso.md) — ângulo complementar (quem acessa, não o que é ofertado): pública é proporcionalmente menos elitizada.
- [Segenreich e Castanheira 2009 — Expansão pós-LDBEN96](fontes/segenreichcastanheira2009expansao.md) — EAD privada cresce 4.700% vs. 200% pública (1996-2006); tecnólogo privado salta de 23,5% pra 68,3%.

Chaves já em `entrega1/ref.bib`: `carvalho2013mercantilizacao`, `mota2012educacao`, `cunha2007universidade` (este último não está em `raw/`). As demais 7 fontes acima ainda não têm entrada no `.bib` — adicionar ao citar na Discussão do artigo final.

## Resultados estatísticos (dos scripts R)

- [Síntese dos 3 métodos](resultados/sintese.md) — narrativa consolidada pra Discussão: modalidade (não área) é o eixo mais forte de distinção, condicionado ao grau acadêmico.
- [Método 1 — Qui-quadrado](resultados/metodo1_qui_quadrado.md) — V de Cramér: Área 0,128, Grau 0,132, Modalidade 0,395.
- [Método 2 — Regressão logística](resultados/metodo2_regressao_logistica.md) — OR ajustados; achado de colinearidade quase determinística Educação×Licenciatura.
- [Método 3 — Log-linear](resultados/metodo3_log_linear.md) — interação tripla Rede×Grau×Modalidade significativa (p<2,2e-16), mais extrema em Tecnológico.
- [**Achados para a Discussão**](resultados/achados_discussao.md) — 8 achados cruzando estatística + literatura, prontos pra virar parágrafo do artigo. Destaque: inversão histórica da EAD (84% pública em 2002 → 96,6% privada em 2024).
- [**Achados para os Resultados**](resultados/achados_resultados.md) — tabelas A-D prontas (χ²/V de Cramér, resíduos, OR, contagens) + lista de números citáveis pro Resumo, sem interpretação (isso fica na Discussão).
