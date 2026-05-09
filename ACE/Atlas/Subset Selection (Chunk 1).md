---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T17:36:13.065555'
id: 66b24396
links: []
modified: '2026-05-09T17:36:13.065555'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: Subset Selection (Chunk 1)
type: knowledge_chunk
---

---
chunk_id: d1dc9c13d72a
source: WINSEM2025-26_CSE3008_ETH_AP2025264000479_2026-01-24_Reference-Material-I.pdf
page: 1
title: Subset Selection (Chunk 1)
keywords: ['λ', 'Cost function', 'Ridge Regression', 'Loss', 'Lasso Regression']
created: 2026-05-09 23:06:13
tree_path: ML > Page 1 > Subset Selection
---

line) •λ= 1 •The slope of the curve= 1.4 Cost function = 0 + 1 x (1.4)2 = 1.96 For Ridge Regression, l et’s assume, Loss = 0.32 + 0.22 = 0.13 λ = 1 The slope of the curve = 0.7 Then, Cost function = 0.13 + 1 x (0.72)2 = 0.62 Ridge regression line fits the model more accurately than the linear regression line. Dr. Selva Kumar S (SCOPE) Difference between Ridge Regression and Lasso Regression •Ridge regression is mostly used to reduce the overfitting in the model and includes all the features present in the model . •It reduces the complexity of the model by shrinking the coefficients . •Lasso regression helps reduce the overfitting in the model and feature selection . Dr. Selva Kumar S (SCOPE) Lasso Regression Ridge Regression Regularization Type•Lasso adds the absolute value of the coefficients as a penalty term to the loss function •Lasso tends to shrink some coefficients to exactly zero, effectively performing feature selection•Ridge adds the squared magnitude of the coefficients as a penalty term to the loss function . •Ridge tends to shrink coefficients towards zero but usually does not set any coefficient exactly to zero. This means it keeps all features in the model . Impact on Coefficients•Can lead to sparse models where some coefficients are exactly zero, which means some features are entirely excluded from the model . •Useful when you have many features , and you expect only a few to be important•All coefficients are shrunk by the same proportion, leading to a more balanced approach where all features are retained, but their influence is reduced . •Preferred when you believe all features might contribute to the output but want to avoid overfitting . Feature Selection•Acts as a feature selector by zeroing out less important features. •Particularly useful when dealing with high - dimensional data where you expect many irrelevant features•Better when you believe all features have some impact on the response .Comparison Lasso Regression Ridge Regression Computational Efficiency•Can be computationally more expensive due to the nature of the L1 penalty, especially in very high-dimensional settings .•Generally computationally more efficient than Lasso, particularly for datasets with a large number of features . Behavior in High - Dimensional Settings•Performs well when the number of predictors 𝑝 is much larger than the number of observations 𝑛. •Tends to select a few important predictors and discard the rest•Performs well when you have many predictors that are correlated with each other . •All predictors are kept, but their coefficients are shrunk to avoid overfitting . Use Cases •When you need to identify and select a subset of features. •Ideal for models where you expect only a few predictors to be important.•When you want to retain all features but reduce their overall impact . •Useful when dealing with multicollinearity (where predictors are highly correlated) .Comparison

### Related Concepts
- [[Loss]]
- [[λ]]
- [[Lasso Regression]]
- [[Cost function]]
- [[Ridge Regression]]
