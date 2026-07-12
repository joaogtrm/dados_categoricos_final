# Log da Wiki

## [2026-07-11] ingest | slide_testes.pdf
Qui-quadrado de Pearson, delineamentos amostrais, correção de Yates, Fisher exato, McNemar. -> conceitos/testes_hipotese.md

## [2026-07-11] ingest | slide_associacao.pdf
Risco Relativo, Diferença de Proporções, Odds Ratio (coorte vs. caso-controle). -> conceitos/medidas_associacao.md

## [2026-07-11] ingest | slide_contingencia.pdf
Independência, homogeneidade, simetria de Bowker, homogeneidade marginal. -> conceitos/tabelas_contingencia.md

## [2026-07-11] ingest | slide_regressao_logistica.pdf
Logito, EMV, odds ratio, pseudo-R² de McFadden, diagnóstico (VIF, ROC/AUC). -> conceitos/regressao_logistica.md

## [2026-07-11] ingest | slide_log_linear.pdf
GLM Poisson sobre tabelas multi-way, hierarquia de termos, deviance, G². -> conceitos/modelos_log_lineares.md

## [2026-07-11] ingest | slide_concordancia.pdf
Nome do arquivo enganoso: conteúdo real é Paradoxo de Simpson, OR ajustado de
Mantel-Haenszel, teste de Breslow-Day. Página escrita com o conteúdo real
encontrado, não com o que o nome do arquivo sugeria. -> conceitos/estratificacao_mantel_haenszel.md

## [2026-07-11] rename | slide_concordancia.pdf -> slide_estratificacao_mantel_haenszel.pdf
Arquivo renomeado em slide/ pra refletir o conteúdo real.

## [2026-07-11] rename | Moraes...pdf
Nome original em raw/ tinha quebras de linha literais (bug de arquivo),
renomeado pra nome de linha única sem alterar conteúdo.

## [2026-07-11] ingest | Alonso - 2010 - A expansão do ensino superior no Brasil e a EaD
Lógica privatista/quantitativista da expansão (INEP 2007-08), EaD nascente já concentrada na privada. -> fontes/alonso2010ead.md

## [2026-07-11] ingest | Benevides Soares et al. - 2023 - Satisfação com o curso
Privados ligam satisfação a retorno financeiro/institucional; públicos, a envolvimento acadêmico. -> fontes/benevidessoares2023satisfacao.md

## [2026-07-11] ingest | Carvalho - 2013 - Mercantilização da educação superior
Já citado em ref.bib (carvalho2013mercantilizacao). Aprofundado com achados empíricos: EAD puxada pelas lucrativas, financeirização, oligopolização. -> fontes/carvalho2013mercantilizacao.md

## [2026-07-11] ingest | Durham - O ensino superior no Brasil público e privado
Trajetória histórica 1808-2003, origem do "mass private sector" nos anos 70. -> fontes/durham_ensino_publico_privado.md

## [2026-07-11] ingest | Martins - 2002 - O setor privado
É resenha, não artigo original. Tese do "mass private sector" como absorvedor de demanda de massa. -> fontes/martins2002setorprivado.md

## [2026-07-11] ingest | Moraes - 2025 - CSTGQ Curitiba
Estudo de caso de tecnólogo presencial em Curitiba; convergência curricular pública/privada quando modalidade é a mesma. -> fontes/moraes2025cstgq.md

## [2026-07-11] ingest | Mota e Anjos - 2012 - Turismo no Nordeste
Já citado em ref.bib (mota2012educacao). 92% dos cursos de Turismo são privados. -> fontes/mota2012educacao.md

## [2026-07-11] ingest | Pinto - 2004 - O acesso à educação superior no Brasil
Ângulo complementar (acesso, não oferta): pública proporcionalmente menos elitizada. -> fontes/pinto2004acesso.md

## [2026-07-11] ingest | Segenreich e Castanheira - 2009 - Expansão pós-LDBEN96
EAD privada cresce 4.700% vs. 200% pública (1996-2006); tecnólogo privado salta de 23,5% pra 68,3%. -> fontes/segenreichcastanheira2009expansao.md

## [2026-07-11] resultado | metodo1_qui_quadrado.R
V de Cramér: Área 0,128, Grau 0,132, Modalidade 0,395 (mais forte). Resíduos: Pública x Educação +83,57. -> resultados/metodo1_qui_quadrado.md

## [2026-07-11] resultado | metodo2_regressao_logistica.R
OR ajustados com interação grau x modalidade. modalidadeEAD=0,033 (mais extremo). grauLicenciatura instável -- colinearidade quase determinística com área Educação (100%/93,3%). -> resultados/metodo2_regressao_logistica.md

## [2026-07-11] resultado | metodo3_log_linear.R
Interação tripla Rede:Grau:Modalidade significativa (deviance=654,13, 2 gl, p<2,2e-16), mais extrema em Tecnológico. -> resultados/metodo3_log_linear.md

## [2026-07-11] resultado | síntese
Narrativa consolidada dos 3 métodos pra Discussão do artigo. -> resultados/sintese.md
