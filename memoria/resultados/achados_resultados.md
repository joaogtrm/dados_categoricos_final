# Achados para a seção Resultados do artigo

Diferente de `achados_discussao.md` (que cruza estatística com literatura e
interpreta o "porquê"), esta página é só **estimativas e tabelas** —
apresentação, sem interpretação — pra bater com o que o guia do trabalho
pede pra seção Resultados ("apresentação das tabelas, gráficos e
estimativas obtidas"; interpretação fica pra Discussão). Números
verificados contra os `.csv` em `resultados/`.

---

## Tabela A — Resumo dos três testes de associação (Método 1)

| Cruzamento | χ² | gl | p-valor | V de Cramér |
|---|---|---|---|---|
| Rede × Área Geral CINE | 11.846,4 | 10 | < 2,2×10⁻¹⁶ | 0,128 |
| Rede × Grau Acadêmico | 12.595,1 | 2 | < 2,2×10⁻¹⁶ | 0,132 |
| Rede × Modalidade de Ensino | 112.638,1 | 1 | < 2,2×10⁻¹⁶ | **0,395** |

## Tabela B — Resíduos padronizados de Pearson mais extremos (Método 1)

| Cruzamento | Célula | Resíduo |
|---|---|---|
| Rede × Área Geral | Pública × Educação | **+83,57** |
| Rede × Área Geral | Pública × Negócios/administração/direito | −46,19 |
| Rede × Área Geral | Pública × Agricultura/silvicultura/pesca/vet. | +31,08 |
| Rede × Grau | Pública × Tecnológico | −99,43 |
| Rede × Grau | Pública × Licenciatura | +91,76 |
| Rede × Modalidade | (tabela 2×2 — ver `resultados/metodo1_residuos_modalidade.csv`) | maior módulo do trabalho |

## Tabela C — Odds ratios do modelo logístico final (Método 2)

`rede_bin ~ area_geral + grau*modalidade + regiao`, N=706.556, pseudo-R²
McFadden=0,324, LRT modelo completo vs. nulo: χ²=57.174,8, 18 gl, p<2,2×10⁻¹⁶.

| Termo | OR | IC 95% | p-valor |
|---|---|---|---|
| area_geralEducação | 0,093 | [0,046; 0,186] | 2,0×10⁻¹¹ |
| area_geralCiências naturais/matemática/estatística | 2,759 | [2,49; 3,06] | 1,1×10⁻⁸⁴ |
| area_geralAgricultura/silvicultura/pesca/vet. | 2,013 | [1,82; 2,23] | 4,9×10⁻⁴¹ |
| area_geralComputação/TIC | 2,064 | [1,93; 2,21] | 8,1×10⁻⁹³ |
| area_geralSaúde e bem-estar | 0,329 | [0,303; 0,356] | 5,1×10⁻¹⁶⁴ |
| grauLicenciatura | 52,231 | [26,0; 104,9] | 9,9×10⁻²⁹ |
| grauTecnológico | 0,793 | [0,736; 0,856] | 2,1×10⁻⁹ |
| **modalidadeEAD** | **0,033** | **[0,031; 0,034]** | ≈0 |
| grauLicenciatura:modalidadeEAD | 0,684 | [0,632; 0,742] | 2,1×10⁻²⁰ |
| grauTecnológico:modalidadeEAD | 0,316 | [0,286; 0,350] | 4,1×10⁻¹⁰⁹ |
| regiaoNordeste | 1,264 | [1,213; 1,317] | 3,1×10⁻²⁹ |
| regiaoSul | 0,611 | [0,582; 0,642] | 2,9×10⁻⁸⁷ |

(tabela completa com todas as 19 linhas em `resultados/metodo2_odds_ratios.csv`)

## Tabela D — Contagens observadas e teste da interação tripla (Método 3)

| Grau | Modalidade | Pública | Privada |
|---|---|---|---|
| Bacharelado | Presencial | 5.964 | 17.788 |
| Bacharelado | EAD | 2.664 | 216.794 |
| Licenciatura | Presencial | 3.500 | 2.029 |
| Licenciatura | EAD | 5.285 | 125.705 |
| Tecnológico | Presencial | 1.318 | 3.876 |
| Tecnológico | EAD | 1.153 | 332.227 |

Teste de razão de verossimilhança (modelo sem interação tripla vs.
saturado): deviance = 654,13, 2 gl, **p < 2,2×10⁻¹⁶**.

Resíduo padronizado mais extremo do modelo sem interação tripla: ±23,96,
em **Tecnológico × Presencial/EAD** (o maior de todo o trabalho neste
recorte).

---

## Lista dos números mais citáveis (pra Resumo/Abstract e abertura da Discussão)

1. Base: 720.349 cursos (Censo da Educação Superior 2024/INEP); 97,20%
   privada, 2,80% pública.
2. Associação mais forte encontrada: **Rede × Modalidade, V de Cramér =
   0,395** (método 1) — muito acima de Rede×Área (0,128) e Rede×Grau
   (0,132).
3. Odds ratio mais extremo do modelo ajustado: **modalidadeEAD = 0,033**
   (IC 95% [0,031; 0,034]) — controlando por área, grau e região.
4. Interação estatística confirmada por dois métodos independentes: OR de
   interação grau×modalidade significativo no método 2 (p<2,2×10⁻¹⁶) e
   deviance da interação tripla significativa no método 3 (654,13, 2 gl,
   p<2,2×10⁻¹⁶).
5. Maior resíduo padronizado do trabalho: Pública×Tecnológico/EAD-vs-
   Presencial, ±23,96 no método 3 (achado mais extremo que qualquer
   resíduo do método 1).
6. Pseudo-R² de McFadden do modelo final: 0,324 — ajuste substancial pra
   um modelo de ciências sociais aplicadas.

## Como usar

Tabelas A-D vão direto pra seção Resultados do artigo (formatar em
`booktabs`/`tabularx`, mesmo padrão da Tabela 1 já usada em
`entrega1/main.tex`). A "lista de números citáveis" serve tanto pro Resumo
(objetivo/base/métodos/principais resultados em ~150 palavras) quanto
pra frase de abertura da Discussão, antes de entrar nos achados
qualitativos de `achados_discussao.md`.
