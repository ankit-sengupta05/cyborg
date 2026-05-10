---
aliases: []
area: ''
backlinks: []
created: '2026-05-10T00:04:17.499640'
id: d5f21c74
links: []
modified: '2026-05-10T00:04:17.499640'
project: ''
source: ''
status: active
summary: ''
tags:
- ontology
- system_sync
- map
title: Ontology_Statistical_Analysis
type: ontology_map
---

# Ontology: Statistical Analysis

**Summary**: Exploring relationships between variables using statistical methods.

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["Lasso Regression"]
    n1["Locating Important Characteristics"]
    n2["λ= 1"]
    n3["Loss = 0.32 + 0.22"]
    n4["Loss"]
    n5["The slope of the curve = 0.7"]
    n6["Discovering Linear Combinations of Varying Sequences"]
    n7["PCA Why Do We Need PCA in Machine Learning?"]
    n8["λ"]
    n9["The slope of the curve= 1.4"]
    n10["Overfitting Issues"]
    n11["Ridge Regression"]
    n12["λ = 1"]
    n13["Interpretability and Minimizing Information Loss"]
    n8 -->|CO_OCCUR| n11
    n8 -->|CO_OCCUR| n4
    n8 -->|CO_OCCUR| n0
    n11 -->|CO_OCCUR| n4
    n11 -->|CO_OCCUR| n0
    n4 -->|CO_OCCUR| n0
    n2 -->|KEYWORD_LINK| n8
    n2 -->|LINKED_TO| n11
    n12 -->|KEYWORD_LINK| n8
    n12 -->|LINKED_TO| n0
    n9 -->|INFERRED| n11
    n5 -->|INFERRED| n0
    n3 -->|KEYWORD_LINK| n4
    n3 -->|INFERRED| n0
    n7 -->|LINKED_TO| n10
    n13 -->|KEYWORD_LINK| n4
    n7 -->|LINKED_TO| n13
    n7 -->|LINKED_TO| n1
    n7 -->|LINKED_TO| n6
```

## 🌳 Sequential Topic Tree
> Shows how topics are hierarchically and sequentially related

- [[Loss]]
  - *( co_occur )*
  - [[Lasso Regression]]
- [[Locating Important Characteristics]]
- [[λ= 1]]
  - *( linked_to )*
  - [[Ridge Regression]]
  - *( keyword_link )*
  - [[λ]]
- [[Loss = 0.32 + 0.22]]
- [[The slope of the curve = 0.7]]
- [[Discovering Linear Combinations of Varying Sequences]]
- [[PCA Why Do We Need PCA in Machine Learning?]]
  - *( linked_to )*
  - [[Interpretability and Minimizing Information Loss]]
  - *( linked_to )*
  - [[Overfitting Issues]]
- [[The slope of the curve= 1.4]]
- [[λ = 1]]

## 📋 All Core Concepts
- [[Lasso Regression]]
- [[Locating Important Characteristics]]
- [[λ= 1]]
- [[Loss = 0.32 + 0.22]]
- [[Loss]]
- [[The slope of the curve = 0.7]]
- [[Discovering Linear Combinations of Varying Sequences]]
- [[PCA Why Do We Need PCA in Machine Learning?]]
- [[λ]]
- [[The slope of the curve= 1.4]]
- [[Overfitting Issues]]
- [[Ridge Regression]]
- [[λ = 1]]
- [[Interpretability and Minimizing Information Loss]]
