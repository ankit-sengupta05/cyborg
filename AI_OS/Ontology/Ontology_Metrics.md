---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T23:56:54.463749'
id: bb8d881d
links: []
modified: '2026-05-09T23:56:54.463749'
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

**Summary**: Evaluation criteria for model performance

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["FPR"]
    n1["Recall"]
    n2["F1-score"]
    n3["Evaluation Metrics"]
    n4["Precision"]
    n5["TPR"]
    n3 -->|CONTAINS| n4
    n3 -->|CONTAINS| n1
    n3 -->|CONTAINS| n2
    n4 -->|CO_OCCUR| n1
    n4 -->|CO_OCCUR| n2
    n1 -->|CO_OCCUR| n2
    n4 -->|LINKED_TO| n5
    n1 -->|LINKED_TO| n0
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
- [[FPR]]
- [[Recall]]
- [[F1-score]]
- [[Evaluation Metrics]]
- [[Precision]]
- [[TPR]]
