# Resultado — Método 1: Qui-quadrado + V de Cramér + Resíduos

## 1. O que foi testado

Independência entre Rede de Ensino (Pública/Privada) e três variáveis: Área
Geral CINE (11 categorias), Grau Acadêmico (3 categorias), Modalidade de
Ensino (2 categorias). Script: `metodo1_qui_quadrado.R`. Base: Censo da
Educação Superior 2024/INEP, 720.349 cursos (sem filtro de casos completos
neste método — `chisq.test()` ignora `NA` via `table()`).

## 2. Resultado bruto

| Cruzamento | χ² | gl | p-valor | V de Cramér |
|---|---|---|---|---|
| Rede × Área Geral | 11.846,4 | 10 | < 2,2e-16 | 0,128 |
| Rede × Grau Acadêmico | 12.595,1 | 2 | < 2,2e-16 | 0,132 |
| Rede × Modalidade | 112.638,1 | 1 | < 2,2e-16 | 0,395 |

Resíduos padronizados de Pearson (maiores em módulo):

- **Pública × Educação**: +83,57 (excesso forte de Educação na pública)
- **Pública × Negócios/administração/direito**: −46,19 (déficit forte)
- **Pública × Presencial** / **Privada × EAD**: os dois maiores resíduos
  absolutos entre todos os cruzamentos (tabela 2×2, ver
  `resultados/metodo1_residuos_modalidade.csv`)
- **Pública × Tecnológico**: −99,43 / **Privada × Tecnológico**: +99,43
  (maior resíduo absoluto entre os três cruzamentos)

## 3. Leitura

As três associações são estatisticamente significativas, mas de magnitude
bem diferente: Área Geral e Grau Acadêmico têm associação **fraca a
moderada** com Rede (V≈0,13), enquanto Modalidade tem associação **forte**
(V=0,395) — é o fator isoladamente mais distintivo entre rede pública e
privada nesta base. Os resíduos confirmam o padrão já visto na análise
descritiva (Etapa 1): pública concentra Educação e presencial; privada
concentra Negócios/Tecnólogo e EAD.

## 4. Limitações/cautelas

- Com N=706-720 mil, p-valor baixo é esperado mesmo para associações
  fracas — a leitura deve se apoiar no V de Cramér, não no p-valor.
- V de Cramér é simétrico e não direcional: diz "quão associadas", não
  "o que causa o quê" nem controla por outras variáveis (isso é papel dos
  métodos 2 e 3).
- Dado é censo (população dos cursos registrados), não amostra probabilística
  de uma população maior — o enquadramento inferencial clássico (p-valor
  contra erro de amostragem) é uma simplificação; a leitura mais honesta é
  descritiva/de força de associação.

## 5. Arquivo de saída

`resultados/metodo1_residuos_area_geral.csv`, `resultados/metodo1_residuos_grau.csv`,
`resultados/metodo1_residuos_modalidade.csv`.
