---
aliases: []
area: ''
backlinks: []
created: '2026-05-18T08:06:35.561815'
id: 55f626ed
links: []
modified: '2026-05-18T08:06:35.561815'
project: ''
source: ''
status: active
summary: ''
tags:
- ontology
- system_sync
- map
title: Ontology_Decision_Tree_Analysis
type: ontology_map
---

# Ontology: Decision Tree Analysis

**Summary**: This knowledge graph details the mathematical foundations and structural components of decision tree algorithms.

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["Entropy among the three branches"]
    n1["Tennis"]
    n2["Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)"]
    n3["Rainy"]
    n4["Handling Missing Values in Decision Trees"]
    n5["Overcast"]
    n6["decision node"]
    n7["Decision Trees"]
    n8["Entropy when overcast = 0.0"]
    n9["Probability"]
    n10["Decision Trees"]
    n11["Loss Functions"]
    n12["Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0"]
    n13["Loss"]
    n14["Sunny"]
    n15["'Insights into Decision Trees, Loss"]
    n16["Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6"]
    n17["Information Gain Calculation for Outlook Cont’d"]
    n18["tree-structured classifier"]
    n19["Supervised learning technique"]
    n20["Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)"]
    n21["Rain"]
    n22["Entropy"]
    n23["leaf node"]
    n24["Instability"]
    n10 -->|CONTAINS| n10
    n10 -->|CONTAINS| n19
    n10 -->|CONTAINS| n18
    n10 -->|CONTAINS| n6
    n10 -->|CONTAINS| n23
    n19 -->|CO_OCCUR| n18
    n19 -->|CO_OCCUR| n6
    n19 -->|CO_OCCUR| n23
    n18 -->|CO_OCCUR| n6
    n18 -->|CO_OCCUR| n23
    n6 -->|CO_OCCUR| n23
    n10 -->|LINKED_TO| n18
    n10 -->|CONTAINS| n9
    n10 -->|CONTAINS| n22
    n10 -->|CONTAINS| n17
    n10 -->|CONTAINS| n21
    n10 -->|CONTAINS| n1
    n10 -->|CONTAINS| n14
    n10 -->|CONTAINS| n5
    n3 -->|KEYWORD_LINK| n21
    n10 -->|CONTAINS| n3
    n9 -->|CO_OCCUR| n22
    n9 -->|CO_OCCUR| n17
    n9 -->|CO_OCCUR| n21
    n9 -->|CO_OCCUR| n1
    n9 -->|CO_OCCUR| n14
    n9 -->|CO_OCCUR| n5
    n9 -->|CO_OCCUR| n3
    n22 -->|CO_OCCUR| n17
    n22 -->|CO_OCCUR| n21
    n22 -->|CO_OCCUR| n1
    n22 -->|CO_OCCUR| n14
    n22 -->|CO_OCCUR| n5
    n22 -->|CO_OCCUR| n3
    n17 -->|CO_OCCUR| n21
    n17 -->|CO_OCCUR| n1
    n17 -->|CO_OCCUR| n14
    n17 -->|CO_OCCUR| n5
    n17 -->|CO_OCCUR| n3
    n21 -->|CO_OCCUR| n1
    n21 -->|CO_OCCUR| n14
    n21 -->|CO_OCCUR| n5
    n1 -->|CO_OCCUR| n14
    n1 -->|CO_OCCUR| n5
    n1 -->|CO_OCCUR| n3
    n14 -->|CO_OCCUR| n5
    n14 -->|CO_OCCUR| n3
    n5 -->|CO_OCCUR| n3
    n16 -->|KEYWORD_LINK| n9
    n16 -->|KEYWORD_LINK| n1
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
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Handling Missing Values in Decision Trees]]
  - *( keyword_link )*
  - [[Decision Trees]]
  - *( co_occur )*
  - [[Instability]]
- [[decision node]]
  - *( co_occur )*
  - [[leaf node]]
  - *( semantic_similar )*
  - [[root node]]
- [[Entropy when overcast = 0.0]]
- [[Loss Functions]]
  - *( keyword_link )*
  - [[Loss]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [["Insights into Decision Trees, Loss]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[tree-structured classifier]]
- [[Supervised learning technique]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]

## 📋 All Core Concepts
- [[Entropy among the three branches]]
- [[Tennis]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Rainy]]
- [[Handling Missing Values in Decision Trees]]
- [[Overcast]]
- [[decision node]]
- [[Decision Trees]]
- [[Entropy when overcast = 0.0]]
- [[Probability]]
- [[Decision Trees]]
- [[Loss Functions]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [[Loss]]
- [[Sunny]]
- [["Insights into Decision Trees, Loss]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Information Gain Calculation for Outlook Cont’d]]
- [[tree-structured classifier]]
- [[Supervised learning technique]]
- [[Probability of not playing tennis = 2/5 = 0.4 Probability of playing tennis = 3/5 = 0.6 Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[Rain]]
- [[Entropy]]
- [[leaf node]]
- [[Instability]]
