# Método 3: modelo log-linear (tabela 3 vias Rede x Grau Acadêmico x Modalidade de Ensino)
#
# Investiga o que a colinearidade do método 2 deixou em aberto: o efeito da Modalidade
# sobre a distribuição por Rede é o mesmo em todo Grau Acadêmico, ou os três fatores
# interagem? Testa isso via razão de verossimilhança comparando o modelo saturado
# (log-linear via glm poisson) com o modelo sem o termo de interação tripla.

df <- read.csv("dados/base_categorica_2024.csv", stringsAsFactors = FALSE,
                na.strings = c("", "NA"))

cols_modelo <- c("TP_REDE", "TP_GRAU_ACADEMICO", "TP_MODALIDADE_ENSINO")
completos <- complete.cases(df[cols_modelo])
df_modelo <- droplevels(df[completos, ])

df_modelo$rede <- factor(df_modelo$TP_REDE, levels = c(1, 2),
                          labels = c("Pública", "Privada"))
df_modelo$grau <- factor(df_modelo$TP_GRAU_ACADEMICO, levels = c(1, 2, 3),
                          labels = c("Bacharelado", "Licenciatura", "Tecnológico"))
df_modelo$modalidade <- factor(df_modelo$TP_MODALIDADE_ENSINO, levels = c(1, 2),
                                labels = c("Presencial", "EAD"))

tabela <- as.data.frame(table(rede = df_modelo$rede, grau = df_modelo$grau,
                               modalidade = df_modelo$modalidade))

modelo_saturado <- glm(Freq ~ rede * grau * modalidade, data = tabela, family = poisson)
modelo_sem_3via <- glm(Freq ~ (rede + grau + modalidade)^2, data = tabela, family = poisson)

teste_3via <- anova(modelo_sem_3via, modelo_saturado, test = "Chisq")

cat("\n==== Modelo log-linear: Rede x Grau Acadêmico x Modalidade de Ensino ====\n")
cat(sprintf("N = %d (casos completos: %d, descartados por NA: %d)\n",
            nrow(df), nrow(df_modelo), sum(!completos)))
cat("\nTabela de contagens observadas:\n")
print(xtabs(Freq ~ rede + grau + modalidade, data = tabela))

cat("\nTeste da interação tripla Rede:Grau:Modalidade (modelo sem ela vs. saturado):\n")
print(teste_3via)

p_3via <- teste_3via[["Pr(>Chi)"]][2]
if (p_3via < 0.05) {
  cat(sprintf(
    "\np-valor = %s < 0.05: a interação tripla é significativa -- o efeito da\n",
    ifelse(p_3via < 2.2e-16, "< 2.2e-16", format.pval(p_3via))))
  cat("modalidade sobre a distribuição por rede muda conforme o grau acadêmico.\n")
} else {
  cat(sprintf("\np-valor = %s >= 0.05: interação tripla não é necessária -- o efeito\n",
              format.pval(p_3via)))
  cat("da modalidade sobre rede é consistente entre os graus acadêmicos.\n")
}

# resíduos padronizados de Pearson do modelo sem interação tripla:
# células onde esse modelo mais erra são as que "puxam" a necessidade da interação
tabela$resid_sem_3via <- round(rstandard(modelo_sem_3via, type = "pearson"), 2)
cat("\nResíduos padronizados (modelo sem interação tripla) por célula:\n")
print(tabela[order(-abs(tabela$resid_sem_3via)), c("rede", "grau", "modalidade", "Freq", "resid_sem_3via")],
      row.names = FALSE)

dir.create("resultados", showWarnings = FALSE)
write.csv(tabela, "resultados/metodo3_log_linear.csv", row.names = FALSE)
