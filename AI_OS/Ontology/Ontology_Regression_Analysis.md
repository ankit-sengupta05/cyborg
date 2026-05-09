---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T17:36:38.534029'
id: a617ee1f
links: []
modified: '2026-05-09T17:36:38.534029'
project: ''
source: ''
status: active
summary: ''
tags:
- ontology
- system_sync
- map
title: Ontology_Regression_Analysis
type: ontology_map
---

# Ontology: Regression Analysis

**Summary**: Exploring Ridge Regression's parameters and cost function.

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["root node"]
    n1["tree-structured classifier"]
    n2["Probability"]
    n3["Information Gain Calculation for Outlook Cont’d"]
    n4["Rain"]
    n5["decision node"]
    n6["Overcast"]
    n7["Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6"]
    n8["Entropy"]
    n9["Sunny"]
    n10["Supervised learning technique"]
    n11["Decision Trees"]
    n12["leaf node"]
    n13["Tennis"]
    n14["Rainy"]
    n11 -->|CONTAINS| n11
    n11 -->|CONTAINS| n10
    n11 -->|CONTAINS| n1
    n11 -->|CONTAINS| n5
    n11 -->|CONTAINS| n12
    n10 -->|CO_OCCUR| n1
    n10 -->|CO_OCCUR| n5
    n10 -->|CO_OCCUR| n12
    n1 -->|CO_OCCUR| n5
    n1 -->|CO_OCCUR| n12
    n5 -->|CO_OCCUR| n12
    n11 -->|LINKED_TO| n1
    n5 -->|SEMANTIC_SIMILAR| n0
    n11 -->|CONTAINS| n2
    n11 -->|CONTAINS| n8
    n11 -->|CONTAINS| n3
    n11 -->|CONTAINS| n4
    n11 -->|CONTAINS| n13
    n11 -->|CONTAINS| n9
    n11 -->|CONTAINS| n6
    n14 -->|KEYWORD_LINK| n4
    n11 -->|CONTAINS| n14
    n2 -->|CO_OCCUR| n8
    n2 -->|CO_OCCUR| n3
    n2 -->|CO_OCCUR| n4
    n2 -->|CO_OCCUR| n13
    n2 -->|CO_OCCUR| n9
    n2 -->|CO_OCCUR| n6
    n2 -->|CO_OCCUR| n14
    n8 -->|CO_OCCUR| n3
    n8 -->|CO_OCCUR| n4
    n8 -->|CO_OCCUR| n13
    n8 -->|CO_OCCUR| n9
    n8 -->|CO_OCCUR| n6
    n8 -->|CO_OCCUR| n14
    n3 -->|CO_OCCUR| n4
    n3 -->|CO_OCCUR| n13
    n3 -->|CO_OCCUR| n9
    n3 -->|CO_OCCUR| n6
    n3 -->|CO_OCCUR| n14
    n4 -->|CO_OCCUR| n13
    n4 -->|CO_OCCUR| n9
    n4 -->|CO_OCCUR| n6
    n13 -->|CO_OCCUR| n9
    n13 -->|CO_OCCUR| n6
    n13 -->|CO_OCCUR| n14
    n9 -->|CO_OCCUR| n6
    n9 -->|CO_OCCUR| n14
    n6 -->|CO_OCCUR| n14
    n7 -->|KEYWORD_LINK| n2
```

## 🌳 Sequential Topic Tree
> Shows how topics are hierarchically and sequentially related

- [[Decision Trees]]
  - *( contains )*
  - [[Probability]]
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
    - [[Entropy]]
      - *( co_occur )*
      - [[Information Gain Calculation for Outlook Cont’d]]
        - *( co_occur )*
      - *( co_occur )*
      - [[Rain]]
- [[root node]]
- [[tree-structured classifier]]
  - *( co_occur )*
  - [[decision node]]
    - *( co_occur )*
    - [[leaf node]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Supervised learning technique]]

## 📋 All Core Concepts
- [[root node]]
- [[tree-structured classifier]]
- [[Probability]]
- [[Information Gain Calculation for Outlook Cont’d]]
- [[Rain]]
- [[decision node]]
- [[Overcast]]
- [[Probability of playing tennis = 2/5 = 0.4 Probability of not playing tennis = 3/5 = 0.6]]
- [[Entropy]]
- [[Sunny]]
- [[Supervised learning technique]]
- [[Decision Trees]]
- [[leaf node]]
- [[Tennis]]
- [[Rainy]]
