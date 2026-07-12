# Achados para a Discussão do artigo

Cruzamento entre os resultados estatísticos (`resultados/metodo1-3_*.md`) e a
literatura temática (`fontes/*.md`). Cada achado abaixo já vem com estatística
+ referência + trecho citável, pronto pra virar parágrafo de Discussão.
Ordenados por força/originalidade do argumento.

---

## 1. Inversão histórica da EAD: de majoritariamente pública (2002) a quase exclusivamente privada (2024)

**Estatística**: `modalidadeEAD` é o termo mais extremo do método 2 (OR=0,033);
V de Cramér de Rede×Modalidade (0,395) é a maior associação isolada do
método 1; EAD privada = 96,6% da oferta privada.

**Literatura**: Pinto (2004) mostra que em **2002** a EAD ainda era
majoritariamente **pública**: 55% das matrículas EAD em estaduais, 29% em
federais, só **16% em privadas** — "atípico e sujeito a forte pressão
expansionista do setor privado". Mota e Anjos (2012) confirmam esse quadro
em nível de área específica: em 2010/2011, dos 13 cursos de Turismo
ofertados pelos Institutos Federais no Nordeste, só 1 era EAD. Segenreich e
Castanheira (2009) capturam a virada em andamento: entre 2001 e 2006 as IES
credenciadas para EAD privada cresceram **4.700%** contra 200% na pública,
invertendo a proporção (90% pública em 2001 → 64% privada em 2006).

**Uso na Discussão**: dá pra montar uma trajetória quantificada e citável —
**2002: ~84% da EAD é pública → 2006: ~64% da EAD é privada → 2024: 96,6%
da oferta privada é EAD** (método 1). É o achado mais forte e mais
"contraintuitivo" disponível: quem lê o dado de 2024 isolado pensaria que a
EAD sempre foi terreno do setor privado; a literatura mostra que é uma
inversão completa em duas décadas, não uma característica estrutural
antiga.

---

## 2. Interação tripla (método 3) explicada pelo timing diferencial de adesão ao Tecnólogo+EAD

**Estatística**: método 3 — interação Rede×Grau×Modalidade significativa
(deviance=654,13, p<2,2e-16), mais extrema em Tecnólogo (pública quase
50/50 presencial/EAD; privada 98,8% EAD).

**Literatura**: Segenreich e Castanheira (2009) documentam que os Centros de
Educação Tecnológica foram **criação pública** (100% em 1999), mas a rede
privada inverteu essa predominância entre 2001-2006 (23,5% → 68,3% de
participação privada, crescimento de 1.675% vs. 153,8% na pública) — e
isso aconteceu **no mesmo período e pelas mesmas instituições** que
capturaram a EAD. Carvalho (2013) fecha o mecanismo: cursos "orientados
para os negócios", de ciclo curto, sem exigência de pesquisa — perfil que
maximiza escala e minimiza custo por aluno, exatamente a lógica de
maximização de valor ao acionista das IES lucrativas.

**Uso na Discussão**: a interação tripla não é um artefato estatístico —
tem explicação causal na literatura: Tecnólogo e EAD são o **mesmo pacote
estratégico comercial**, adotado pelas mesmas instituições privadas no
mesmo período (2001-2006), o que explica por que o efeito de Modalidade
sobre Rede se concentra tão fortemente nesse grau específico.

---

## 3. Colinearidade Educação≈Licenciatura (100%/93,3%) tem explicação estrutural, não é erro de especificação

**Estatística**: método 2 — `grauLicenciatura` instável (OR=52, IC
[26;105]); método 1 — maior resíduo do trabalho é Pública×Educação (+83,57).

**Literatura**: Durham (2003) mostra que a obrigatoriedade da Faculdade de
Filosofia, Ciências e Letras (embrião da formação de professores) integrar
toda universidade pública remonta à Era Vargas — vínculo histórico entre
setor público e formação docente. Pinto (2004) quantifica o desincentivo
econômico do lado privado: Licenciaturas já eram 52% das vagas públicas em
2002, mas tinham 61% de vagas não preenchidas por baixa remuneração da
carreira — ou seja, é uma área estruturalmente pouco atrativa para
investimento privado voltado a retorno financeiro.

**Uso na Discussão**: a instabilidade do coeficiente não deve ser tratada
como limitação a esconder — é evidência estatística de um fato
sociológico real e bem documentado: Educação/Licenciatura é uma área que o
setor privado historicamente evita por baixo retorno, então a variável
"grau" e "área" carregam quase a mesma informação porque, na prática, quase
não existe Licenciatura fora do nicho de formação docente vinculado à
função pública.

---

## 4. Achado potencialmente contraditório: Pedagogia era área forte na rede PRIVADA em 2007, hoje é a rede PÚBLICA que concentra Educação

**Estatística**: método 1 — resíduo Pública×Educação = +83,57 (maior do
trabalho); área Educação, hoje, puxa fortemente pra pública.

**Literatura**: Alonso (2010), citando INEP 2007: ~52% das matrículas
privadas se concentravam em **Administração, Direito e Pedagogia** — ou
seja, Pedagogia aparecia como área forte na rede **privada** há menos de
20 anos. Durham (2003) documenta que a expansão privada dos anos 1970 já
incluía "formação de professores" como um dos três pilares de baixo custo
do setor (ao lado de administração e economia).

**Uso na Discussão**: esse é um ponto que precisa ser tratado com cuidado
(é uma tensão real, não um erro) — vale citar como limitação temporal da
comparação e como uma pergunta em aberto pra pesquisas futuras: o que
mudou entre 2007 e 2024 pra recompor esse mercado? Hipóteses a mencionar
sem afirmar como causa provada: política de expansão de Licenciaturas via
Institutos Federais/UAB, mudanças em PROUNI/FIES, ou mera mudança na forma
de classificação CINE (Pedagogia vs. "Educação" como área CINE pode não
ser 1:1 comparável à antiga classificação do INEP usada por Alonso).

---

## 5. Contraponto qualitativo: quando modalidade é controlada, a distinção público/privado quase desaparece

**Estatística**: método 3 mostra que o padrão Rede×Modalidade é fortemente
condicional ao Grau — mais extremo em Tecnólogo.

**Literatura**: Schonarth e Moraes (2016) comparam 5 Cursos Superiores de
Tecnologia em Gestão da Qualidade presenciais em Curitiba (1 pública — UFPR
—, 4 privadas) e encontram **convergência curricular**: as mesmas três
categorias de disciplina dominam ~75-80% da carga horária em pública e
privadas por igual.

**Uso na Discussão**: acrescenta nuance importante — a distinção
estatística encontrada nos métodos 1-3 é sobre **estratégia de oferta**
(que modalidade, que grau), não necessariamente sobre **conteúdo
pedagógico**. Quando modalidade e área são fixadas, pública e privada se
parecem. Isso sustenta a leitura de que EAD é uma escolha de modelo de
negócio (escala/custo) da rede privada, não uma diferença de "qualidade"
ou "proposta pedagógica" do curso em si — argumento que evita uma leitura
moralizante do achado.

---

## 6. Trajetória histórica que contextualiza os 97,2% de cursos privados em 2024

**Estatística**: 700.198 de 720.349 cursos (97,2%) são da rede privada.

**Literatura**: cadeia de citações com números comparáveis ao longo do
tempo — Martins/Sampaio (2002): 43% das matrículas privadas em 1965 → 63%
em 1980; Pinto (2004): 44% em 1960 → 70% em 2002; Segenreich e Castanheira
(2009): participação pública em cursos presenciais cai de 44,8% (1996) para
29,6% (2006).

**Uso na Discussão**: permite montar uma frase de trajetória de quatro
pontos no tempo (1960 → 1980 → 2002 → 2024) mostrando que 97,2% não é
ruptura recente, é o ponto de chegada de uma tendência contínua de mais de
60 anos — reforça que a "distinção clara" que a pergunta de pesquisa busca
não é só estatisticamente significativa, é historicamente esperada.

---

## 7. Limitação a declarar: "Rede Privada" é heterogênea (lucrativa x não lucrativa) e o INEP parou de discriminar isso

**Estatística**: a variável `TP_REDE` usada nos 3 métodos só distingue
Pública/Privada, sem subdividir a rede privada.

**Literatura**: Carvalho (2013) registra que "o INEP deixou de divulgar as
informações discriminadas relativas às instituições lucrativas e não
lucrativas no censo da educação superior de 2010, o que impossibilita a
análise quantitativa sobre o segmento empresarial" (p. 774) — e mostra que,
já em 2008-09, o crescimento em EAD e cursos de negócios era
desproporcionalmente puxado pelo segmento **lucrativo** especificamente
(79-81% das matrículas EAD privadas), não pela rede privada como um todo
(que inclui comunitárias/confessionais/filantrópicas, mais parecidas com a
lógica pública).

**Uso na Discussão**: limitação importante e honesta — o padrão
encontrado (concentração em Negócios/Tecnólogo/EAD) provavelmente é ainda
mais extremo dentro do subconjunto lucrativo da rede privada do que a
média geral sugere, mas a base do Censo 2024 usada no trabalho não permite
testar isso diretamente.

---

## 8. Achado que qualifica a interpretação de "Grau": tecnólogo já é perfil aplicado mesmo dentro da rede pública

**Estatística**: método 2/3 atribuem parte do padrão a Grau Acadêmico
(Tecnólogo especialmente ligado à privada/EAD).

**Literatura**: Mota e Anjos (2012) mostram que os cursos tecnológicos
ofertados pelos próprios Institutos Federais (rede pública) já têm perfil
"aplicado, prático-operacional", sem nenhum coordenador apontando pesquisa
como objetivo do curso — o mesmo perfil atribuído à rede privada por
Carvalho (2013).

**Uso na Discussão**: ressalva metodológica útil — parte do "efeito de
Rede" capturado nos métodos 1-3 pode na verdade ser efeito do próprio
Grau Acadêmico (Tecnólogo é definido, por natureza, como formação aplicada
de ciclo curto, em qualquer rede), e não um traço exclusivo da lógica
comercial privada. Reforça por que separar Grau de Rede (como os métodos 2
e 3 fazem) era necessário, e por que a leitura dos coeficientes precisa ser
cautelosa.

---

## Como usar esta página

Cada achado acima pode virar 1 parágrafo da Discussão: abrir com o número
do método, citar a literatura com o trecho já pronto (ver `fontes/*.md`
pra citação completa/página), fechar com a implicação. Achados 1 e 6 são
os mais fortes pra abrir a Discussão (dão uma narrativa histórica clara);
achados 3, 4, 7 e 8 são as ressalvas/limitações que dão sofisticação
metodológica ao texto; achado 5 é o contraponto que evita uma leitura
simplista demais do resultado principal.
