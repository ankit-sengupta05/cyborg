---
aliases: []
area: ''
backlinks: []
created: '2026-05-18T08:06:35.626655'
id: 5aaa1fa9
links: []
modified: '2026-05-18T08:06:35.626655'
project: ''
source: ''
status: active
summary: ''
tags:
- ontology
- system_sync
- map
title: Ontology_Classification_Performance
type: ontology_map
---

# Ontology: Classification Performance

**Summary**: These metrics quantify the accuracy and balance of binary classification models.

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["Evaluation Metrics"]
    n1["F1-score"]
    n2["FPR"]
    n3["Recall"]
    n4["TPR"]
    n5["Precision"]
    n0 -->|CONTAINS| n5
    n0 -->|CONTAINS| n3
    n0 -->|CONTAINS| n1
    n5 -->|CO_OCCUR| n3
    n5 -->|CO_OCCUR| n1
    n3 -->|CO_OCCUR| n1
    n5 -->|LINKED_TO| n4
    n3 -->|LINKED_TO| n2
```

## 🌳 Sequential Topic Tree
> Shows how topics are hierarchically and sequentially related

- [[Evaluation Metrics]]
  - *( contains )*
  - [[Precision]]
    - *( co_occur )*
    - [[Recall]]
      - *( co_occur )*
      - [[F1-score]]
      - *( linked_to )*
      - [[FPR]]
    - *( linked_to )*
    - [[TPR]]

## 📋 All Core Concepts
- [[Evaluation Metrics]]
- [[F1-score]]
- [[FPR]]
- [[Recall]]
- [[TPR]]
- [[Precision]]
