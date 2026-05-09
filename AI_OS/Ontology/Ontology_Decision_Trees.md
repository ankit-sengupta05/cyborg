---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T23:56:54.439110'
id: bb218ef9
links: []
modified: '2026-05-09T23:56:54.439110'
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
    n0["Tennis"]
    n1["Handling Missing Values in Decision Trees"]
    n2["root node"]
    n3["Loss Functions"]
    n4["Decision Trees"]
    n5["Instability"]
    n6["Overcast"]
    n7["Information Gain Calculation for Outlook Cont’d"]
    n8["Supervised learning technique"]
    n9["tree-structured classifier"]
    n10["Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)"]
    n11["Decision Trees"]
    n12["leaf node"]
    n13["'Insights into Decision Trees, Loss"]
    n14["Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)"]
    n15["Rainy"]
    n16["Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0"]
    n17["decision node"]
    n18["Probability"]
    n19["Entropy"]
    n20["Entropy among the three branches"]
    n21["Entropy when overcast = 0.0"]
    n22["Rain"]
    n23["Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6"]
    n24["Sunny"]
    n11 -->|CONTAINS| n11
    n11 -->|CONTAINS| n8
    n11 -->|CONTAINS| n9
    n11 -->|CONTAINS| n17
    n11 -->|CONTAINS| n12
    n8 -->|CO_OCCUR| n9
    n8 -->|CO_OCCUR| n17
    n8 -->|CO_OCCUR| n12
    n9 -->|CO_OCCUR| n17
    n9 -->|CO_OCCUR| n12
    n17 -->|CO_OCCUR| n12
    n11 -->|LINKED_TO| n9
    n17 -->|SEMANTIC_SIMILAR| n2
    n11 -->|CONTAINS| n18
    n11 -->|CONTAINS| n19
    n11 -->|CONTAINS| n7
    n11 -->|CONTAINS| n22
    n11 -->|CONTAINS| n0
    n11 -->|CONTAINS| n24
    n11 -->|CONTAINS| n6
    n15 -->|KEYWORD_LINK| n22
    n11 -->|CONTAINS| n15
    n18 -->|CO_OCCUR| n19
    n18 -->|CO_OCCUR| n7
    n18 -->|CO_OCCUR| n22
    n18 -->|CO_OCCUR| n0
    n18 -->|CO_OCCUR| n24
    n18 -->|CO_OCCUR| n6
    n18 -->|CO_OCCUR| n15
    n19 -->|CO_OCCUR| n7
    n19 -->|CO_OCCUR| n22
    n19 -->|CO_OCCUR| n0
    n19 -->|CO_OCCUR| n24
    n19 -->|CO_OCCUR| n6
    n19 -->|CO_OCCUR| n15
    n7 -->|CO_OCCUR| n22
    n7 -->|CO_OCCUR| n0
    n7 -->|CO_OCCUR| n24
    n7 -->|CO_OCCUR| n6
    n7 -->|CO_OCCUR| n15
    n22 -->|CO_OCCUR| n0
    n22 -->|CO_OCCUR| n24
    n22 -->|CO_OCCUR| n6
    n0 -->|CO_OCCUR| n24
    n0 -->|CO_OCCUR| n6
    n0 -->|CO_OCCUR| n15
    n24 -->|CO_OCCUR| n6
    n24 -->|CO_OCCUR| n15
    n6 -->|CO_OCCUR| n15
    n23 -->|KEYWORD_LINK| n18
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
- [[Handling Missing Values in Decision Trees]]
  - *( keyword_link )*
  - [[Decision Trees]]
  - *( co_occur )*
  - [[Instability]]
- [[root node]]
- [[Loss Functions]]
- [[Supervised learning technique]]
  - *( co_occur )*
  - [[decision node]]
    - *( co_occur )*
    - [[leaf node]]
  - *( co_occur )*
  - [[tree-structured classifier]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [["Insights into Decision Trees, Loss]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
  - *( linked_to )*
  - [[Entropy when overcast = 0.0]]
- [[Entropy among the three branches]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]

## 📋 All Core Concepts
- [[Tennis]]
- [[Handling Missing Values in Decision Trees]]
- [[root node]]
- [[Loss Functions]]
- [[Decision Trees]]
- [[Instability]]
- [[Overcast]]
- [[Information Gain Calculation for Outlook Cont’d]]
- [[Supervised learning technique]]
- [[tree-structured classifier]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[Decision Trees]]
- [[leaf node]]
- [["Insights into Decision Trees, Loss]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Rainy]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [[decision node]]
- [[Probability]]
- [[Entropy]]
- [[Entropy among the three branches]]
- [[Entropy when overcast = 0.0]]
- [[Rain]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Sunny]]
