# Resultado — Método 3: Modelo Log-linear (Rede × Grau × Modalidade)

## 1. O que foi testado

Tabela 3 vias Rede (Pública/Privada) × Grau Acadêmico (Bacharelado/
Licenciatura/Tecnológico) × Modalidade (Presencial/EAD), 2×3×2=12 células.
`glm(Freq ~ rede*grau*modalidade, family=poisson)` (saturado) comparado via
razão de verossimilhança com `glm(Freq ~ (rede+grau+modalidade)^2, family=poisson)`
(sem interação tripla). Script: `metodo3_log_linear.R`. Casos completos:
718.303 de 720.349 (2.046 descartados por NA em Grau Acadêmico).

## 2. Resultado bruto

Teste da interação tripla: deviance = 654,13, 2 gl, **p < 2,2e-16** —
interação tripla necessária, modelo saturado é o que descreve os dados.

Tabela observada (Freq):

| Grau | Modalidade | Pública | Privada |
|---|---|---|---|
| Bacharelado | Presencial | 5.964 | 17.788 |
| Bacharelado | EAD | 2.664 | 216.794 |
| Licenciatura | Presencial | 3.500 | 2.029 |
| Licenciatura | EAD | 5.285 | 125.705 |
| Tecnológico | Presencial | 1.318 | 3.876 |
| Tecnológico | EAD | 1.153 | 332.227 |

Resíduos padronizados do modelo **sem** interação tripla (onde ele mais erra):

| Rede | Grau | Modalidade | Resíduo |
|---|---|---|---|
| Pública/Privada | Tecnológico | Presencial/EAD | ±23,96 (maior) |
| Pública/Privada | Bacharelado | Presencial/EAD | ±19,96 |
| Pública/Privada | Licenciatura | Presencial/EAD | ±2,31 (menor) |

## 3. Leitura

O efeito da modalidade sobre a distribuição por rede **muda conforme o grau
acadêmico** — não é um padrão único que se aplica a todos os cursos por
igual. Em Tecnológico o contraste é mais extremo: pública é majoritariamente
presencial (1.318 vs. 1.153 EAD, quase equilibrado) enquanto privada é quase
toda EAD (332.227 vs. 3.876 presencial, 98,8%). Em Bacharelado o padrão é
na mesma direção mas menos extremo. Em Licenciatura o desvio do modelo
aditivo é pequeno (resíduo 2,31, no limite do threshold de |2|) — a área
Educação (à qual Licenciatura praticamente equivale) tem um comportamento
mais parecido entre as duas redes nesse recorte específico.

## 4. Limitações/cautelas

- O teste diz que a interação **existe**, não explica **por quê** — a
  causa provável (mercantilização/EAD como estratégia de escala nas
  privadas, ver `memoria/fontes/carvalho2013mercantilizacao.md` e
  `memoria/fontes/alonso2010ead.md`) vem da literatura, não do modelo.
- Modelo saturado sempre tem deviance=0 por construção (tantos parâmetros
  quanto células) — o resultado relevante é a comparação com o modelo
  reduzido, não o ajuste do saturado em si.
- Resolve uma ambiguidade do método 2 (colinearidade área×grau), mas não a
  substitui: o log-linear não fornece odds ratio ajustado por área nem por
  região, só a estrutura de associação entre rede/grau/modalidade.

## 5. Arquivo de saída

`resultados/metodo3_log_linear.csv` (tabela de contagens + resíduos).
