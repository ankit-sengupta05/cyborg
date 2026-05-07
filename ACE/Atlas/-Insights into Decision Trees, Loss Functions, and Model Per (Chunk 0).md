---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:41:19.147801'
id: a9569c3e
links: []
modified: '2026-05-07T20:41:19.147801'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: '"Insights into Decision Trees, Loss Functions, and Model Per (Chunk 0)'
type: knowledge_chunk
---

---
chunk_id: 5b3b6da4ad16
source: WINSEM2025-26_CSE3008_ETH_AP2025264000479_2026-02-28_Reference-Material-I.pdf
page: 0
title: "Insights into Decision Trees, Loss Functions, and Model Per (Chunk 0)
keywords: ['Decision Trees', 'Loss Functions', 'Missing Values', 'Instability', 'Class Evaluation', 'Confusion Matrix', 'Cross-Validation']
created: 2026-05-08 02:11:19
tree_path: ML > Page 0 > "Insights into Decision Trees, Loss Functions, and
---

"Insights into Decision Trees, Loss Functions, and Model Performance" 1. Loss Functions Loss functions are mathematical functions used to measure how well a machine learning model predicts an outcome. In decision trees, loss functions are used to determine the best split by evaluating impurity or error 2. Decision Trees Multiway Splits: 3. Handling Missing Values in Decision Trees Handling missing values is an important part of building robust decision trees . In real-world datasets, it is common for some features or attributes to have missing values . For instance, a person’s age might be missing in a dataset, or some records might have incomplete information for certain attributes . In decision trees, missing values must be handled carefully because they can affect the purity of splits, leading to biased results or even errors in prediction . There are several methods to handle missing values in decision trees, and each method has its advantages and trade -offs. 4. Decision Trees – Instability Decision trees are powerful tools for classification and regression tasks, but one of their main drawbacks is instability . Instability refers to the sensitivity of decision trees to small changes in the data . Even minor variations or noise in the training data can lead to very different decision tree structures, which may negatively affect the model's robustness and generalizability . Class Evaluation Measures: Class evaluation measures are essential for assessing the performance of classification models . These metrics help to determine how well the model performs in classifying data points into the correct classes . Confusion Matrix Confusion Matrix For binary classification Evaluation Measures Classification Metrics Regression Metrics Cross -Validation Cross -validation is a technique that involves partitioning the data into subsets, training the model on some subsets, and validating it on the remaining subsets. The process is repeated multiple times, and the results are averaged to produce a more robust estimate of model performance. Bootstrapping Bootstrapping is a statistical technique where you randomly sample the data with replacement (i.e., a data point can appear more than once in the new sample) . This method is used to estimate the accuracy of a model and create multiple datasets for training models, often in ensemble methods like Random Forests . AUC ROC Curve in Machine Learning Minimum Description Length (MDL) Principle

### Related Concepts
- [[Decision Trees]]
- [[Instability]]
- [[Missing Values]]
- [[Cross-Validation]]
- [[Loss Functions]]
- [[Class Evaluation]]
- [[Confusion Matrix]]
