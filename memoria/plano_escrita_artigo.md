# Plano de escrita do artigo

Ordem pensada pra escrever do que já tá pronto/mecânico pro que precisa de
mais síntese, deixando o Resumo por último (só dá pra resumir o que já
existe).

1. **Metodologia** — mais rápido de todos. Puxa direto de
   `memoria/conceitos/*.md`: justificativa de cada método já escrita (por
   que qui-quadrado, por que regressão logística com interação, por que
   log-linear). Só formalizar em prosa + fórmulas.

2. **Resultados** — cola as Tabelas A-D de
   `memoria/resultados/achados_resultados.md`, formata em `booktabs`
   (mesmo padrão da Tabela 1 que já existe no `entrega1/main.tex`). Zero
   interpretação aqui, só apresentação. Rápido porque a curadoria já foi
   feita.

3. **Discussão** — a parte que exige mais lapidação de texto, mas os 8
   achados de `memoria/resultados/achados_discussao.md` já vêm com número
   + citação + trecho pronto. Trabalho aqui é costurar em narrativa, não
   pesquisar. Nessa etapa, ir adicionando ao `entrega1/ref.bib` as 7
   chaves pendentes conforme forem citadas (`alonso2010ead`,
   `durham2003ensinosuperior`, `pinto2004acesso`,
   `segenreichcastanheira2009expansao`, `martins2002setorprivado`,
   `moraes2025cstgq`/`schonarth2016cstgq`,
   `benevidessoares2023satisfacao`) — não deixar pra depois, gera trabalho
   de rastrear depois.

4. **Revisar Introdução/Dados** — já escritos na Etapa 1
   (`entrega1/main.tex`), só ajuste leve: confirmar que a pergunta de
   pesquisa ainda bate com o que os métodos 1-3 responderam de fato (bateu:
   modalidade é o eixo mais forte, não área isolada — vale ajustar uma
   frase da Introdução se ela sugeria só "área").

5. **Conclusão** — curta, direto do que virou Discussão. Só depois dela
   existir.

6. **Resumo** — por último, ~150 palavras, puxa da "lista de números
   citáveis" que já tá em `memoria/resultados/achados_resultados.md`.

7. **Apêndice (código R)** — mecânico, colar os 3 scripts
   (`metodo1_qui_quadrado.R`, `metodo2_regressao_logistica.R`,
   `metodo3_log_linear.R`), fazer a qualquer momento, não bloqueia nada.

8. **Passada final** — checar contagem de páginas (guia pede 15-20 no
   `instrucao_trabalho.pdf`), compilar PDF, conferir citações resolvidas
   no `.bib`.

## Contexto pra retomar em outra sessão/modelo

- Repo real do trabalho: `dados_categoricos_final` (remote
  `github.com/joaogtrm/dados_categoricos_final`), branch `nath`.
- Wiki de apoio em `memoria/` (schema em `memoria/CLAUDE.md`,
  índice em `memoria/index.md`).
- Prazo do artigo (Etapa 2): 15/07/2026. Seminário: 17/07/2026.
- Métodos já implementados e validados contra os dados reais: 1 (qui-
  quadrado/V de Cramér/resíduos), 2 (regressão logística com interação
  grau×modalidade), 3 (log-linear, interação tripla).
