---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T23:50:28.956992'
id: a0a79fd9
links: []
modified: '2026-05-09T23:50:28.956992'
project: ''
source: ''
status: active
summary: ''
tags:
- ontology
- system_sync
- map
title: Ontology_Neuron
type: ontology_map
---

# Ontology: Neuron

**Summary**: Cell structure and function

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["Cell Body (Soma)"]
    n1["initial weights"]
    n2["A biological  neuron  has three  main  parts :"]
    n3["•A neural  network's  goal is to adjust  weights  so that th"]
    n4["weights update"]
    n5["Axon"]
    n6["output"]
    n7["predicted output"]
    n8["errors"]
    n9["Neuron"]
    n10["Neural Network"]
    n11["output recalculation"]
    n12["Perceptron Model"]
    n13["Dendrite"]
    n14["final verification"]
    n15["weights"]
    n9 -->|KEYWORD_LINK| n2
    n2 -->|CONTAINS| n9
    n2 -->|CONTAINS| n13
    n2 -->|CONTAINS| n0
    n2 -->|CONTAINS| n5
    n2 -->|CONTAINS| n10
    n9 -->|CO_OCCUR| n13
    n9 -->|CO_OCCUR| n0
    n9 -->|CO_OCCUR| n5
    n9 -->|CO_OCCUR| n10
    n13 -->|CO_OCCUR| n0
    n13 -->|CO_OCCUR| n5
    n13 -->|CO_OCCUR| n10
    n0 -->|CO_OCCUR| n5
    n0 -->|CO_OCCUR| n10
    n5 -->|CO_OCCUR| n10
    n9 -->|LINKED_TO| n10
    n3 -->|CONTAINS| n10
    n15 -->|KEYWORD_LINK| n3
    n3 -->|CONTAINS| n15
    n1 -->|KEYWORD_LINK| n15
    n3 -->|CONTAINS| n1
    n3 -->|CONTAINS| n6
    n3 -->|CONTAINS| n12
    n3 -->|CONTAINS| n8
    n4 -->|KEYWORD_LINK| n15
    n3 -->|CONTAINS| n4
    n11 -->|KEYWORD_LINK| n6
    n3 -->|CONTAINS| n11
    n10 -->|CO_OCCUR| n15
    n10 -->|CO_OCCUR| n1
    n10 -->|CO_OCCUR| n6
    n10 -->|CO_OCCUR| n12
    n10 -->|CO_OCCUR| n8
    n10 -->|CO_OCCUR| n4
    n10 -->|CO_OCCUR| n11
    n15 -->|CO_OCCUR| n6
    n15 -->|CO_OCCUR| n12
    n15 -->|CO_OCCUR| n8
    n15 -->|CO_OCCUR| n11
    n1 -->|CO_OCCUR| n6
    n1 -->|CO_OCCUR| n12
    n1 -->|CO_OCCUR| n8
    n1 -->|CO_OCCUR| n4
    n1 -->|CO_OCCUR| n11
    n6 -->|CO_OCCUR| n12
    n6 -->|CO_OCCUR| n8
    n6 -->|CO_OCCUR| n4
    n12 -->|CO_OCCUR| n8
    n12 -->|CO_OCCUR| n4
```

## 🌳 Sequential Topic Tree
> Shows how topics are hierarchically and sequentially related

- [[Neural Network]]
  - *( co_occur )*
  - [[output]]
    - *( co_occur )*
    - [[Perceptron Model]]
      - *( co_occur )*
      - [[output recalculation]]
        - *( semantic_similar )*
      - *( co_occur )*
      - [[errors]]
        - *( co_occur )*
      - *( co_occur )*
      - [[weights update]]
        - *( keyword_link )*
    - *( semantic_similar )*
    - [[predicted output]]
  - *( co_occur )*
  - [[weights]]
    - *( keyword_link )*
    - [[•A neural  network's  goal is to adjust  weights  so that th]]
- [[Cell Body (Soma)]]
  - *( co_occur )*
  - [[Axon]]
- [[initial weights]]
- [[A biological  neuron  has three  main  parts :]]
  - *( contains )*
  - [[Neuron]]
    - *( co_occur )*
    - [[Dendrite]]
- [[final verification]]

## 📋 All Core Concepts
- [[Cell Body (Soma)]]
- [[initial weights]]
- [[A biological  neuron  has three  main  parts :]]
- [[•A neural  network's  goal is to adjust  weights  so that th]]
- [[weights update]]
- [[Axon]]
- [[output]]
- [[predicted output]]
- [[errors]]
- [[Neuron]]
- [[Neural Network]]
- [[output recalculation]]
- [[Perceptron Model]]
- [[Dendrite]]
- [[final verification]]
- [[weights]]
