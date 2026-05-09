---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T17:36:28.657130'
id: 35ead421
links: []
modified: '2026-05-09T17:36:28.657130'
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
    n0["λ= 1"]
    n1["Cost function = 0 + 1 x (1.4)2"]
    n2["Loss = 0.32 + 0.22"]
    n3["λ"]
    n4["λ = 1"]
    n5["Loss"]
    n6["Ridge Regression"]
    n7["The slope of the curve = 0.7"]
    n8["The slope of the curve= 1.4"]
    n9["Lasso Regression"]
    n3 -->|CO_OCCUR| n6
    n3 -->|CO_OCCUR| n5
    n3 -->|CO_OCCUR| n9
    n6 -->|CO_OCCUR| n5
    n6 -->|CO_OCCUR| n9
    n5 -->|CO_OCCUR| n9
    n0 -->|KEYWORD_LINK| n3
    n0 -->|LINKED_TO| n6
    n4 -->|KEYWORD_LINK| n3
    n4 -->|LINKED_TO| n9
    n8 -->|INFERRED| n6
    n7 -->|INFERRED| n9
    n1 -->|LINKED_TO| n6
    n2 -->|KEYWORD_LINK| n5
    n2 -->|INFERRED| n9
```

## 🌳 Sequential Topic Tree
> Shows how topics are hierarchically and sequentially related

- [[Ridge Regression]]
  - *( co_occur )*
  - [[Lasso Regression]]
  - *( co_occur )*
  - [[Loss]]
- [[λ= 1]]
  - *( keyword_link )*
  - [[λ]]
- [[Cost function = 0 + 1 x (1.4)2]]
- [[Loss = 0.32 + 0.22]]
- [[λ = 1]]
- [[The slope of the curve = 0.7]]
- [[The slope of the curve= 1.4]]

## 📋 All Core Concepts
- [[λ= 1]]
- [[Cost function = 0 + 1 x (1.4)2]]
- [[Loss = 0.32 + 0.22]]
- [[λ]]
- [[λ = 1]]
- [[Loss]]
- [[Ridge Regression]]
- [[The slope of the curve = 0.7]]
- [[The slope of the curve= 1.4]]
- [[Lasso Regression]]
