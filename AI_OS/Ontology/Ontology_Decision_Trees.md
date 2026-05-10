---
aliases: []
area: ''
backlinks: []
created: '2026-05-10T00:04:17.551899'
id: 57318b59
links: []
modified: '2026-05-10T00:04:17.551899'
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

**Summary**: A classification algorithm that uses tree structures to make predictions based on input features.

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["tree-structured classifier"]
    n1["Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)"]
    n2["decision node"]
    n3["Decision Trees"]
    n4["Information Gain Calculation for Outlook Cont’d"]
    n5["leaf node"]
    n6["Overcast"]
    n7["root node"]
    n8["Sunny"]
    n9["Tennis"]
    n10["Handling Missing Values in Decision Trees"]
    n11["'Insights into Decision Trees, Loss"]
    n12["Entropy when overcast = 0.0"]
    n13["Entropy among the three branches"]
    n14["Rainy"]
    n15["Loss Functions"]
    n16["Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6"]
    n17["Instability"]
    n18["Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0"]
    n19["Probability"]
    n20["Decision Trees"]
    n21["Supervised learning technique"]
    n22["Entropy"]
    n23["Rain"]
    n24["Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)"]
    n3 -->|CONTAINS| n3
    n3 -->|CONTAINS| n21
    n3 -->|CONTAINS| n0
    n3 -->|CONTAINS| n2
    n3 -->|CONTAINS| n5
    n21 -->|CO_OCCUR| n0
    n21 -->|CO_OCCUR| n2
    n21 -->|CO_OCCUR| n5
    n0 -->|CO_OCCUR| n2
    n0 -->|CO_OCCUR| n5
    n2 -->|CO_OCCUR| n5
    n3 -->|LINKED_TO| n0
    n2 -->|SEMANTIC_SIMILAR| n7
    n3 -->|CONTAINS| n19
    n3 -->|CONTAINS| n22
    n3 -->|CONTAINS| n4
    n3 -->|CONTAINS| n23
    n3 -->|CONTAINS| n9
    n3 -->|CONTAINS| n8
    n3 -->|CONTAINS| n6
    n14 -->|KEYWORD_LINK| n23
    n3 -->|CONTAINS| n14
    n19 -->|CO_OCCUR| n22
    n19 -->|CO_OCCUR| n4
    n19 -->|CO_OCCUR| n23
    n19 -->|CO_OCCUR| n9
    n19 -->|CO_OCCUR| n8
    n19 -->|CO_OCCUR| n6
    n19 -->|CO_OCCUR| n14
    n22 -->|CO_OCCUR| n4
    n22 -->|CO_OCCUR| n23
    n22 -->|CO_OCCUR| n9
    n22 -->|CO_OCCUR| n8
    n22 -->|CO_OCCUR| n6
    n22 -->|CO_OCCUR| n14
    n4 -->|CO_OCCUR| n23
    n4 -->|CO_OCCUR| n9
    n4 -->|CO_OCCUR| n8
    n4 -->|CO_OCCUR| n6
    n4 -->|CO_OCCUR| n14
    n23 -->|CO_OCCUR| n9
    n23 -->|CO_OCCUR| n8
    n23 -->|CO_OCCUR| n6
    n9 -->|CO_OCCUR| n8
    n9 -->|CO_OCCUR| n6
    n9 -->|CO_OCCUR| n14
    n8 -->|CO_OCCUR| n6
    n8 -->|CO_OCCUR| n14
    n6 -->|CO_OCCUR| n14
    n16 -->|KEYWORD_LINK| n19
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
- [[tree-structured classifier]]
  - *( co_occur )*
  - [[decision node]]
    - *( co_occur )*
    - [[leaf node]]
    - *( semantic_similar )*
    - [[root node]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[Handling Missing Values in Decision Trees]]
  - *( keyword_link )*
  - [[Decision Trees]]
  - *( co_occur )*
  - [[Instability]]
- [["Insights into Decision Trees, Loss]]
  - *( contains )*
  - [[Loss Functions]]
- [[Entropy when overcast = 0.0]]
- [[Entropy among the three branches]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [[Supervised learning technique]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]

## 📋 All Core Concepts
- [[tree-structured classifier]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[decision node]]
- [[Decision Trees]]
- [[Information Gain Calculation for Outlook Cont’d]]
- [[leaf node]]
- [[Overcast]]
- [[root node]]
- [[Sunny]]
- [[Tennis]]
- [[Handling Missing Values in Decision Trees]]
- [["Insights into Decision Trees, Loss]]
- [[Entropy when overcast = 0.0]]
- [[Entropy among the three branches]]
- [[Rainy]]
- [[Loss Functions]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Instability]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [[Probability]]
- [[Decision Trees]]
- [[Supervised learning technique]]
- [[Entropy]]
- [[Rain]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
