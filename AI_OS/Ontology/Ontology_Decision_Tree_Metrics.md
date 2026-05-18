---
aliases: []
area: ''
backlinks: []
created: '2026-05-18T08:21:52.197525'
id: 06bfd073
links: []
modified: '2026-05-18T08:21:52.197525'
project: ''
source: ''
status: active
summary: ''
tags:
- ontology
- system_sync
- map
title: Ontology_Decision_Tree_Metrics
type: ontology_map
---

# Ontology: Decision Tree Metrics

**Summary**: This set of entities details the mathematical foundations and structural components used to build and evaluate decision trees.

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["Entropy among the three branches"]
    n1["Supervised learning technique"]
    n2["Decision Trees"]
    n3["Instability"]
    n4["Sunny"]
    n5["Rainy"]
    n6["Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6"]
    n7["Loss Functions"]
    n8["Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)"]
    n9["Information Gain Calculation for Outlook Cont’d"]
    n10["Probability"]
    n11["Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)"]
    n12["Entropy"]
    n13["Tennis"]
    n14["Decision Trees"]
    n15["root node"]
    n16["Handling Missing Values in Decision Trees"]
    n17["Entropy when overcast = 0.0"]
    n18["decision node"]
    n19["Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0"]
    n20["'Insights into Decision Trees, Loss"]
    n21["Overcast"]
    n22["tree-structured classifier"]
    n23["leaf node"]
    n24["Rain"]
    n2 -->|CONTAINS| n2
    n2 -->|CONTAINS| n1
    n2 -->|CONTAINS| n22
    n2 -->|CONTAINS| n18
    n2 -->|CONTAINS| n23
    n1 -->|CO_OCCUR| n22
    n1 -->|CO_OCCUR| n18
    n1 -->|CO_OCCUR| n23
    n22 -->|CO_OCCUR| n18
    n22 -->|CO_OCCUR| n23
    n18 -->|CO_OCCUR| n23
    n2 -->|LINKED_TO| n22
    n18 -->|SEMANTIC_SIMILAR| n15
    n2 -->|CONTAINS| n10
    n2 -->|CONTAINS| n12
    n2 -->|CONTAINS| n9
    n2 -->|CONTAINS| n24
    n2 -->|CONTAINS| n13
    n2 -->|CONTAINS| n4
    n2 -->|CONTAINS| n21
    n5 -->|KEYWORD_LINK| n24
    n2 -->|CONTAINS| n5
    n10 -->|CO_OCCUR| n12
    n10 -->|CO_OCCUR| n9
    n10 -->|CO_OCCUR| n24
    n10 -->|CO_OCCUR| n13
    n10 -->|CO_OCCUR| n4
    n10 -->|CO_OCCUR| n21
    n10 -->|CO_OCCUR| n5
    n12 -->|CO_OCCUR| n9
    n12 -->|CO_OCCUR| n24
    n12 -->|CO_OCCUR| n13
    n12 -->|CO_OCCUR| n4
    n12 -->|CO_OCCUR| n21
    n12 -->|CO_OCCUR| n5
    n9 -->|CO_OCCUR| n24
    n9 -->|CO_OCCUR| n13
    n9 -->|CO_OCCUR| n4
    n9 -->|CO_OCCUR| n21
    n9 -->|CO_OCCUR| n5
    n24 -->|CO_OCCUR| n13
    n24 -->|CO_OCCUR| n4
    n24 -->|CO_OCCUR| n21
    n13 -->|CO_OCCUR| n4
    n13 -->|CO_OCCUR| n21
    n13 -->|CO_OCCUR| n5
    n4 -->|CO_OCCUR| n21
    n4 -->|CO_OCCUR| n5
    n21 -->|CO_OCCUR| n5
    n6 -->|KEYWORD_LINK| n10
```

## 🌳 Sequential Topic Tree
> Shows how topics are hierarchically and sequentially related

- [[Decision Trees]]
  - *( contains )*
  - [[Entropy]]
    - *( co_occur )*
    - [[Tennis]]
      - *( co_occur )*
      - [[Sunny]]
        - *( co_occur )*
        - *( co_occur )*
      - *( co_occur )*
      - [[Overcast]]
        - *( co_occur )*
      - *( co_occur )*
      - [[Rainy]]
        - *( keyword_link )*
    - *( co_occur )*
    - [[Rain]]
    - *( co_occur )*
    - [[Information Gain Calculation for Outlook Cont’d]]
  - *( contains )*
  - [[Probability]]
- [[Entropy among the three branches]]
- [[Supervised learning technique]]
  - *( co_occur )*
  - [[decision node]]
    - *( co_occur )*
    - [[leaf node]]
    - *( semantic_similar )*
    - [[root node]]
  - *( co_occur )*
  - [[tree-structured classifier]]
- [[Instability]]
  - *( semantic_similar )*
  - [[Decision Trees]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Loss Functions]]
  - *( co_occur )*
  - [[Handling Missing Values in Decision Trees]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Entropy when overcast = 0.0]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [["Insights into Decision Trees, Loss]]

## 📋 All Core Concepts
- [[Entropy among the three branches]]
- [[Supervised learning technique]]
- [[Decision Trees]]
- [[Instability]]
- [[Sunny]]
- [[Rainy]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Loss Functions]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[Information Gain Calculation for Outlook Cont’d]]
- [[Probability]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Entropy]]
- [[Tennis]]
- [[Decision Trees]]
- [[root node]]
- [[Handling Missing Values in Decision Trees]]
- [[Entropy when overcast = 0.0]]
- [[decision node]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [["Insights into Decision Trees, Loss]]
- [[Overcast]]
- [[tree-structured classifier]]
- [[leaf node]]
- [[Rain]]
