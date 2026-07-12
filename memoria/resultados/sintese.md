# Síntese dos resultados — Métodos 1, 2 e 3

## Pergunta de pesquisa

É possível identificar uma distinção clara entre as áreas dos cursos de
graduação ofertados por instituições privadas e públicas no Brasil?

## Resposta consolidada

**Sim, e o eixo mais forte dessa distinção não é a área do curso em si —
é a modalidade de ensino, condicionada ao grau acadêmico.**

1. **Método 1** estabeleceu que existem três associações significativas
   (Rede×Área V=0,128; Rede×Grau V=0,132; Rede×Modalidade V=0,395) — e já
   apontou que Modalidade é, isoladamente, a mais forte das três.
2. **Método 2** confirmou isso controlando as variáveis simultaneamente:
   `modalidadeEAD` teve o odds ratio mais extremo do modelo (0,033), maior
   que qualquer área isolada. Mas revelou um problema — `grauLicenciatura`
   saiu instável (OR=52, IC enorme) — que só foi possível diagnosticar
   corretamente (colinearidade quase determinística com área Educação, não
   um erro de modelo) comparando com o resultado do método 1 (onde Educação
   já tinha o maior resíduo, +83,57).
3. **Método 3** explicou o resíduo problemático de outro ângulo: a relação
   entre Rede e Modalidade **não é a mesma em todo Grau Acadêmico** —
   interação tripla significativa (p<2,2e-16), mais extrema em Tecnológico
   (pública quase 50/50 presencial/EAD; privada 98,8% EAD) e mais suave em
   Licenciatura. Isso é o motivo estrutural por trás da instabilidade que o
   método 2 mostrou meramente como sintoma (IC largo).

## Narrativa pra Discussão

A rede privada não se diferencia da pública por "que áreas oferece" de
forma simples — ela se diferencia por **como** oferece, especialmente via
EAD, e esse "como" interage com **o quê** (grau acadêmico): a modalidade EAD
é usada de forma mais agressiva exatamente nos cursos de menor custo/maior
escalabilidade (Tecnólogo), enquanto em Licenciatura (quase= Educação) o
padrão das duas redes se aproxima mais. Isso é consistente com a leitura da
literatura de mercantilização (`memoria/fontes/carvalho2013mercantilizacao.md`)
e da expansão histórica da EaD privada (`memoria/fontes/alonso2010ead.md`,
`memoria/fontes/segenreichcastanheira2009expansao.md`): a rede privada
segue lógica de mercado/escala, não de formação básica, e usa a combinação
grau+modalidade como principal alavanca dessa lógica — mais do que a
escolha de área de conhecimento propriamente dita.

## Limitação metodológica geral

Os três métodos usam a mesma base censitária (INEP 2024, N≈706-720 mil),
então nenhum resultado é "independente" dos outros no sentido estatístico
clássico — são três lentes sobre os mesmos dados, não três replicações. A
convergência entre eles (mesma direção de efeito, mesma variável
apontada como mais distintiva) é o que dá robustez à conclusão, não a
independência das fontes de evidência.

## Fontes relacionadas

- [[metodo1_qui_quadrado]] — associações marginais + V de Cramér
- [[metodo2_regressao_logistica]] — OR ajustado, achado da colinearidade Educação/Licenciatura
- [[metodo3_log_linear]] — interação tripla, resolve a colinearidade do método 2
- [[carvalho2013mercantilizacao]], [[alonso2010ead]], [[segenreichcastanheira2009expansao]] — explicação qualitativa do padrão
