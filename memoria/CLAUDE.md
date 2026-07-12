# Schema da Wiki — Referencial Teórico (Dados Categóricos)

Wiki de apoio pro trabalho final da disciplina. Alimenta a seção de Metodologia/
referencial teórico do artigo (`entrega1/main.tex` e o artigo final), embasando
as escolhas já implementadas em `metodo1_qui_quadrado.R`, `metodo2_regressao_logistica.R`
e `metodo3_log_linear.R`.

## Arquitetura

- **Fontes brutas (imutáveis)**: `slide/*.pdf` (slides teóricos da disciplina),
  `raw/*.pdf` (artigos temáticos sobre educação superior no Brasil, na raiz do
  projeto `trabalho-anajulia/`, fora deste repo). A LLM lê, nunca edita.
- **Wiki (`memoria/`)**: páginas .md geradas a partir das fontes. A LLM é dona
  dessa camada — cria, atualiza, mantém referências cruzadas.
- **`index.md`**: catálogo de todas as páginas, por categoria.
- **`log.md`**: histórico cronológico de ingestões, formato `## [AAAA-MM-DD] ingest | Título`.

## Convenções de página de conceito (`memoria/conceitos/*.md`)

Cada página de conceito estatístico segue esta estrutura:

1. **Definição** — o que é, em 1-2 parágrafos.
2. **Quando usar** — tipo de dado e pergunta de pesquisa que pede esse método.
3. **Pressupostos** — o que precisa valer pra ser válido.
4. **Fórmula-chave** — a estatística central, sem derivação longa.
5. **Interpretação** — como ler o resultado (p-valor, razão de chances, resíduo, etc).
6. **Conexão com o trabalho** — como isso aparece nos métodos 1/2/3 já rodados.
7. **Fonte** — arquivo e páginas de onde veio.

Referências cruzadas usam `[[nome-do-arquivo-sem-extensão]]`.

## Workflow de ingestão

1. Ler a fonte inteira (PDF pode exigir múltiplas chamadas de `pages` por causa
   do limite de 20 páginas por leitura).
2. Escrever/atualizar a(s) página(s) de conceito relevante(s).
3. Atualizar `index.md`.
4. Adicionar entrada em `log.md`.

## Status

- `slide/*.pdf` (6 arquivos): ingeridos — ver `index.md`.
- `raw/*.pdf` (9 artigos temáticos, já citados em parte no `ref.bib`): ainda
  não ingeridos nessa wiki. Ingerir quando formos escrever a Discussão do
  artigo final, cruzando achados estatísticos com a literatura sobre expansão/
  privatização da educação superior.
