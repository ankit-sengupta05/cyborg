---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T23:50:28.894402'
id: 02d27428
links: []
modified: '2026-05-09T23:50:28.894402'
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
    n1["Entropy when overcast = 0.0"]
    n2["Decision Trees"]
    n3["Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0"]
    n4["decision node"]
    n5["Overcast"]
    n6["Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)"]
    n7["Information Gain Calculation for Outlook Cont’d"]
    n8["Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6"]
    n9["Sunny"]
    n10["Decision Trees"]
    n11["Instability"]
    n12["root node"]
    n13["Handling Missing Values in Decision Trees"]
    n14["Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)"]
    n15["tree-structured classifier"]
    n16["Supervised learning technique"]
    n17["Loss Functions"]
    n18["Entropy among the three branches"]
    n19["leaf node"]
    n20["Rain"]
    n21["Probability"]
    n22["'Insights into Decision Trees, Loss"]
    n23["Rainy"]
    n24["Entropy"]
    n10 -->|CONTAINS| n10
    n10 -->|CONTAINS| n16
    n10 -->|CONTAINS| n15
    n10 -->|CONTAINS| n4
    n10 -->|CONTAINS| n19
    n16 -->|CO_OCCUR| n15
    n16 -->|CO_OCCUR| n4
    n16 -->|CO_OCCUR| n19
    n15 -->|CO_OCCUR| n4
    n15 -->|CO_OCCUR| n19
    n4 -->|CO_OCCUR| n19
    n10 -->|LINKED_TO| n15
    n4 -->|SEMANTIC_SIMILAR| n12
    n10 -->|CONTAINS| n21
    n10 -->|CONTAINS| n24
    n10 -->|CONTAINS| n7
    n10 -->|CONTAINS| n20
    n10 -->|CONTAINS| n0
    n10 -->|CONTAINS| n9
    n10 -->|CONTAINS| n5
    n23 -->|KEYWORD_LINK| n20
    n10 -->|CONTAINS| n23
    n21 -->|CO_OCCUR| n24
    n21 -->|CO_OCCUR| n7
    n21 -->|CO_OCCUR| n20
    n21 -->|CO_OCCUR| n0
    n21 -->|CO_OCCUR| n9
    n21 -->|CO_OCCUR| n5
    n21 -->|CO_OCCUR| n23
    n24 -->|CO_OCCUR| n7
    n24 -->|CO_OCCUR| n20
    n24 -->|CO_OCCUR| n0
    n24 -->|CO_OCCUR| n9
    n24 -->|CO_OCCUR| n5
    n24 -->|CO_OCCUR| n23
    n7 -->|CO_OCCUR| n20
    n7 -->|CO_OCCUR| n0
    n7 -->|CO_OCCUR| n9
    n7 -->|CO_OCCUR| n5
    n7 -->|CO_OCCUR| n23
    n20 -->|CO_OCCUR| n0
    n20 -->|CO_OCCUR| n9
    n20 -->|CO_OCCUR| n5
    n0 -->|CO_OCCUR| n9
    n0 -->|CO_OCCUR| n5
    n0 -->|CO_OCCUR| n23
    n9 -->|CO_OCCUR| n5
    n9 -->|CO_OCCUR| n23
    n5 -->|CO_OCCUR| n23
    n8 -->|KEYWORD_LINK| n21
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
- [[Entropy when overcast = 0.0]]
- [[Decision Trees]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [[decision node]]
  - *( co_occur )*
  - [[leaf node]]
  - *( semantic_similar )*
  - [[root node]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Instability]]
- [[Handling Missing Values in Decision Trees]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[tree-structured classifier]]
- [[Supervised learning technique]]
- [[Loss Functions]]
- [[Entropy among the three branches]]
- [["Insights into Decision Trees, Loss]]

## 📋 All Core Concepts
- [[Tennis]]
- [[Entropy when overcast = 0.0]]
- [[Decision Trees]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [[decision node]]
- [[Overcast]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Information Gain Calculation for Outlook Cont’d]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Sunny]]
- [[Decision Trees]]
- [[Instability]]
- [[root node]]
- [[Handling Missing Values in Decision Trees]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[tree-structured classifier]]
- [[Supervised learning technique]]
- [[Loss Functions]]
- [[Entropy among the three branches]]
- [[leaf node]]
- [[Rain]]
- [[Probability]]
- [["Insights into Decision Trees, Loss]]
- [[Rainy]]
- [[Entropy]]
