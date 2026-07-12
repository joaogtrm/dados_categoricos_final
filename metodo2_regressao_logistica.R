# Método 2: regressão logística binária
# Rede de Ensino (1 = Pública) ~ Área Geral CINE + Grau Acadêmico + Modalidade + Região
#
# TP_CATEGORIA_ADMINISTRATIVA fica de fora de propósito: é subtipo determinístico
# de rede (Federal/Estadual/Municipal -> pública; c/ ou s/ fins lucrativos -> privada),
# não é confundidor, entraria como vazamento de dado (separação perfeita).

df <- read.csv("dados/base_categorica_2024.csv", stringsAsFactors = FALSE,
                na.strings = c("", "NA")) # pandas grava NaN em coluna texto como campo vazio

cols_modelo <- c("TP_REDE", "NO_CINE_AREA_GERAL", "TP_GRAU_ACADEMICO",
                  "TP_MODALIDADE_ENSINO", "NO_REGIAO")
completos <- complete.cases(df[cols_modelo])
n_incompletos <- sum(!completos)
# "Programas básicos" tem 100% de Grau Acadêmico ausente -> some inteiro do caso completo;
# filtra antes de criar os fatores pra não deixar nível vazio (senão o glm aliasa o
# coeficiente e ele some da tabela sem aviso).
df_modelo <- droplevels(df[completos, ])

df_modelo$rede_bin   <- ifelse(df_modelo$TP_REDE == 1, 1, 0) # 1 = Pública (evento de interesse)
df_modelo$area_geral <- relevel(factor(df_modelo$NO_CINE_AREA_GERAL),
                                 ref = "Negócios, administração e direito")
df_modelo$grau       <- relevel(factor(df_modelo$TP_GRAU_ACADEMICO, levels = c(1, 2, 3),
                                        labels = c("Bacharelado", "Licenciatura", "Tecnológico")),
                                 ref = "Bacharelado")
df_modelo$modalidade <- relevel(factor(df_modelo$TP_MODALIDADE_ENSINO, levels = c(1, 2),
                                        labels = c("Presencial", "EAD")),
                                 ref = "Presencial")
df_modelo$regiao     <- relevel(factor(df_modelo$NO_REGIAO), ref = "Sudeste")

# grau*modalidade (não só grau+modalidade): o método 3 (log-linear) já provou que a
# interação tripla Rede:Grau:Modalidade é significativa (p<2,2e-16) -- um modelo aditivo
# aqui assumiria implicitamente que o efeito de Modalidade sobre Rede é igual em todo
# Grau, premissa que o método 3 refuta. Testado: LRT confirma a interação também na
# escala logística (deviance=495,43, 2 gl, p<2,2e-16; AIC cai de 119578,8 pra 119087,4).
modelo <- glm(rede_bin ~ area_geral + grau * modalidade + regiao,
              data = df_modelo, family = binomial)

if (!is.null(modelo$fitted.values) &&
    any(modelo$fitted.values < 1e-8 | modelo$fitted.values > 1 - 1e-8)) {
  warning("Probabilidades ajustadas perto de 0/1 -- checar separação quase perfeita.")
}

coefs   <- coef(summary(modelo))
ic_wald <- confint.default(modelo) # Wald, rápido para N grande; profile seria caro aqui

tabela_or <- data.frame(
  termo      = rownames(coefs),
  odds_ratio = exp(coefs[, "Estimate"]),
  ic_2.5     = exp(ic_wald[, 1]),
  ic_97.5    = exp(ic_wald[, 2]),
  p_valor    = coefs[, "Pr(>|z|)"]
)
row.names(tabela_or) <- NULL

# pseudo-R² de McFadden + teste da razão de verossimilhança (modelo x nulo)
pseudo_r2 <- 1 - modelo$deviance / modelo$null.deviance
lr_stat   <- modelo$null.deviance - modelo$deviance
lr_gl     <- modelo$df.null - modelo$df.residual
lr_p      <- pchisq(lr_stat, lr_gl, lower.tail = FALSE)

cat("\n==== Regressão logística: Rede (Pública=1) ~ Área + Grau + Modalidade + Região ====\n")
cat(sprintf("N = %d (casos completos usados: %d, descartados por NA: %d)\n",
            nrow(df), nrow(df_modelo), n_incompletos))
cat("Área \"Programas básicos\" (2.042 cursos) sai do modelo: 100% sem Grau Acadêmico informado.\n")
cat(sprintf("Pseudo-R² de McFadden = %.3f\n", pseudo_r2))
cat(sprintf("Razão de verossimilhança: qui-quadrado = %.1f, gl = %d, p-valor %s\n",
            lr_stat, lr_gl, ifelse(lr_p < 2.2e-16, "< 2.2e-16", format.pval(lr_p))))
cat("\nOdds ratios (IC 95% Wald):\n")
print(tabela_or, digits = 3, row.names = FALSE)

# quantifica a colinearidade estrutural Área=Educação x Grau=Licenciatura (não é só
# "correlação forte": é quase determinística pela própria taxonomia CINE)
pct_lic_em_edu <- 100 * mean(df_modelo$area_geral[df_modelo$grau == "Licenciatura"] == "Educação")
pct_edu_e_lic  <- 100 * mean(df_modelo$grau[df_modelo$area_geral == "Educação"] == "Licenciatura")
cat(sprintf(
  "\nAviso: grauLicenciatura sai com magnitude extrema e IC largo. Causa quantificada:\n%.1f%% dos cursos de Licenciatura estão na área Educação, e %.1f%% da área Educação\né Licenciatura -- quase colinearidade determinística pela taxonomia CINE (não é\napenas correlação forte). O OR de grauLicenciatura não deve ser lido como efeito\nparcial \"controlando por área\", porque quase não há variação de grau dentro/fora\nde Educação pra separar os dois efeitos. Sinal (direção) é confiável; magnitude não.\n",
  pct_lic_em_edu, pct_edu_e_lic))

dir.create("resultados", showWarnings = FALSE)
write.csv(tabela_or, "resultados/metodo2_odds_ratios.csv", row.names = FALSE)
