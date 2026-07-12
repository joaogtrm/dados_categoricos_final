# Método 1: qui-quadrado de independência + V de Cramér + resíduos de Pearson
# Rede de Ensino x (Área Geral CINE, Grau Acadêmico, Modalidade de Ensino)

df <- read.csv("dados/base_categorica_2024.csv", stringsAsFactors = FALSE,
                na.strings = c("", "NA")) # pandas grava NaN em coluna texto como campo vazio

df$rede <- factor(df$TP_REDE, levels = c(1, 2), labels = c("Pública", "Privada"))
df$grau <- factor(df$TP_GRAU_ACADEMICO, levels = c(1, 2, 3),
                   labels = c("Bacharelado", "Licenciatura", "Tecnológico"))
df$modalidade <- factor(df$TP_MODALIDADE_ENSINO, levels = c(1, 2),
                         labels = c("Presencial", "EAD"))
df$area_geral <- df$NO_CINE_AREA_GERAL

cramer_v <- function(tab) {
  chi2 <- suppressWarnings(chisq.test(tab)$statistic)
  n <- sum(tab)
  k <- min(dim(tab)) - 1
  sqrt(as.numeric(chi2) / (n * k))
}

testar_associacao <- function(var2, nome, dados = df) {
  tab <- table(dados$rede, dados[[var2]], dnn = c("Rede", nome))
  teste <- suppressWarnings(chisq.test(tab))
  list(
    tabela = tab,
    teste = teste,
    cramer_v = cramer_v(tab),
    residuos = round(teste$stdres, 2)
  )
}

resultados <- list(
  area_geral = testar_associacao("area_geral", "Área Geral"),
  grau       = testar_associacao("grau", "Grau Acadêmico"),
  modalidade = testar_associacao("modalidade", "Modalidade")
)

for (nome in names(resultados)) {
  r <- resultados[[nome]]
  cat("\n==== Rede x", nome, "====\n")
  cat(sprintf("qui-quadrado = %.1f, gl = %d, p-valor %s, V de Cramér = %.3f\n",
              r$teste$statistic, r$teste$parameter,
              ifelse(r$teste$p.value < 2.2e-16, "< 2.2e-16", format.pval(r$teste$p.value)),
              r$cramer_v))
  cat("Resíduos padronizados de Pearson (>|2| = célula puxa a associação):\n")
  print(r$residuos)
}

# Salva pra importar como tabela no artigo (booktabs/tabularx)
dir.create("resultados", showWarnings = FALSE)
for (nome in names(resultados)) {
  write.csv(as.data.frame.matrix(resultados[[nome]]$residuos),
            sprintf("resultados/metodo1_residuos_%s.csv", nome))
}
