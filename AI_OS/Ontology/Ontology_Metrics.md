---
aliases: []
area: ''
backlinks: []
created: '2026-05-10T00:04:17.590874'
id: 3bbf296b
links: []
modified: '2026-05-10T00:04:17.590874'
project: ''
source: ''
status: active
summary: ''
tags:
- ontology
- system_sync
- map
title: Ontology_Metrics
type: ontology_map
---

# Ontology: Metrics

**Summary**: Evaluation criteria for classification tasks

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["Precision"]
    n1["TPR"]
    n2["F1-score"]
    n3["Evaluation Metrics"]
    n4["FPR"]
    n5["Recall"]
    n3 -->|CONTAINS| n0
    n3 -->|CONTAINS| n5
    n3 -->|CONTAINS| n2
    n0 -->|CO_OCCUR| n5
    n0 -->|CO_OCCUR| n2
    n5 -->|CO_OCCUR| n2
    n0 -->|LINKED_TO| n1
    n5 -->|LINKED_TO| n4
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
- [[Precision]]
- [[TPR]]
- [[F1-score]]
- [[Evaluation Metrics]]
- [[FPR]]
- [[Recall]]
