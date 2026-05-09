---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T23:43:52.209489'
id: 5ab1fcdf
links: []
modified: '2026-05-09T23:43:52.209489'
project: ''
source: ''
status: active
summary: ''
tags:
- ontology
- system_sync
- map
title: Ontology_Decision_Trees
type: ontology_map
---

# Ontology: Decision Trees

**Summary**: Classification algorithm for supervised learning, decision-making process based on probability and entropy.

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["Entropy among the three branches"]
    n1["Tennis"]
    n2["decision node"]
    n3["'Insights into Decision Trees, Loss"]
    n4["Rainy"]
    n5["tree-structured classifier"]
    n6["root node"]
    n7["Decision Trees"]
    n8["Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)"]
    n9["Entropy when overcast = 0.0"]
    n10["Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6"]
    n11["Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0"]
    n12["Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)"]
    n13["Supervised learning technique"]
    n14["Information Gain Calculation for Outlook Cont’d"]
    n15["Decision Trees"]
    n16["leaf node"]
    n17["Instability"]
    n18["Sunny"]
    n19["Handling Missing Values in Decision Trees"]
    n20["Loss Functions"]
    n21["Overcast"]
    n22["Entropy"]
    n23["Probability"]
    n24["Rain"]
    n7 -->|CONTAINS| n7
    n7 -->|CONTAINS| n13
    n7 -->|CONTAINS| n5
    n7 -->|CONTAINS| n2
    n7 -->|CONTAINS| n16
    n13 -->|CO_OCCUR| n5
    n13 -->|CO_OCCUR| n2
    n13 -->|CO_OCCUR| n16
    n5 -->|CO_OCCUR| n2
    n5 -->|CO_OCCUR| n16
    n2 -->|CO_OCCUR| n16
    n7 -->|LINKED_TO| n5
    n2 -->|SEMANTIC_SIMILAR| n6
    n7 -->|CONTAINS| n23
    n7 -->|CONTAINS| n22
    n7 -->|CONTAINS| n14
    n7 -->|CONTAINS| n24
    n7 -->|CONTAINS| n1
    n7 -->|CONTAINS| n18
    n7 -->|CONTAINS| n21
    n4 -->|KEYWORD_LINK| n24
    n7 -->|CONTAINS| n4
    n23 -->|CO_OCCUR| n22
    n23 -->|CO_OCCUR| n14
    n23 -->|CO_OCCUR| n24
    n23 -->|CO_OCCUR| n1
    n23 -->|CO_OCCUR| n18
    n23 -->|CO_OCCUR| n21
    n23 -->|CO_OCCUR| n4
    n22 -->|CO_OCCUR| n14
    n22 -->|CO_OCCUR| n24
    n22 -->|CO_OCCUR| n1
    n22 -->|CO_OCCUR| n18
    n22 -->|CO_OCCUR| n21
    n22 -->|CO_OCCUR| n4
    n14 -->|CO_OCCUR| n24
    n14 -->|CO_OCCUR| n1
    n14 -->|CO_OCCUR| n18
    n14 -->|CO_OCCUR| n21
    n14 -->|CO_OCCUR| n4
    n24 -->|CO_OCCUR| n1
    n24 -->|CO_OCCUR| n18
    n24 -->|CO_OCCUR| n21
    n1 -->|CO_OCCUR| n18
    n1 -->|CO_OCCUR| n21
    n1 -->|CO_OCCUR| n4
    n18 -->|CO_OCCUR| n21
    n18 -->|CO_OCCUR| n4
    n21 -->|CO_OCCUR| n4
    n10 -->|KEYWORD_LINK| n23
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
- [[decision node]]
  - *( co_occur )*
  - [[leaf node]]
  - *( semantic_similar )*
  - [[root node]]
- [["Insights into Decision Trees, Loss]]
  - *( keyword_link )*
  - [[Decision Trees]]
  - *( contains )*
  - [[Loss Functions]]
    - *( co_occur )*
    - [[Handling Missing Values in Decision Trees]]
      - *( co_occur )*
      - [[Instability]]
- [[tree-structured classifier]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[Entropy when overcast = 0.0]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Supervised learning technique]]

## 📋 All Core Concepts
- [[Entropy among the three branches]]
- [[Tennis]]
- [[decision node]]
- [["Insights into Decision Trees, Loss]]
- [[Rainy]]
- [[tree-structured classifier]]
- [[root node]]
- [[Decision Trees]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[Entropy when overcast = 0.0]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Supervised learning technique]]
- [[Information Gain Calculation for Outlook Cont’d]]
- [[Decision Trees]]
- [[leaf node]]
- [[Instability]]
- [[Sunny]]
- [[Handling Missing Values in Decision Trees]]
- [[Loss Functions]]
- [[Overcast]]
- [[Entropy]]
- [[Probability]]
- [[Rain]]
