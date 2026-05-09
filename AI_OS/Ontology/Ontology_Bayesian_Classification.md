---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T17:19:26.798758'
id: 76589a82
links: []
modified: '2026-05-09T17:19:26.798758'
project: ''
source: ''
status: active
summary: ''
tags:
- ontology
- system_sync
- map
title: Ontology_Bayesian_Classification
type: ontology_map
---

# Ontology: Bayesian Classification

**Summary**: A family of probabilistic models for classification tasks.

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["Naive Bayes Classifier Algorithm"]
    n1["Bayesian Classifier with Continuous Variables:  Continuous N"]
    n2["Naive Bayesian Classifier"]
    n3["Gaussian Naïve Bayes"]
    n4["Naïve Bayes with continuous variables"]
    n5["Naive Bayes algorithm"]
    n6["Bayesian Classifier"]
    n7["Naïve Bayes"]
    n8["Continuous NB"]
    n6 -->|CONTAINS| n6
    n6 -->|CONTAINS| n0
    n6 -->|CONTAINS| n5
    n6 -->|CONTAINS| n6
    n0 -->|CO_OCCUR| n5
    n6 -->|LINKED_TO| n0
    n2 -->|KEYWORD_LINK| n6
    n2 -->|SEMANTIC_SIMILAR| n6
    n1 -->|KEYWORD_LINK| n6
    n1 -->|CONTAINS| n6
    n1 -->|CONTAINS| n8
    n1 -->|CONTAINS| n7
    n3 -->|KEYWORD_LINK| n7
    n1 -->|CONTAINS| n3
    n6 -->|CO_OCCUR| n8
    n6 -->|CO_OCCUR| n7
    n6 -->|CO_OCCUR| n3
    n8 -->|CO_OCCUR| n7
    n8 -->|CO_OCCUR| n3
    n6 -->|SEMANTIC_SIMILAR| n8
    n4 -->|KEYWORD_LINK| n7
    n3 -->|LINKED_TO| n4
```

## 🌳 Sequential Topic Tree
> Shows how topics are hierarchically and sequentially related

- [[Bayesian Classifier]]
  - *( co_occur )*
  - [[Naïve Bayes]]
  - *( co_occur )*
  - [[Gaussian Naïve Bayes]]
    - *( linked_to )*
    - [[Naïve Bayes with continuous variables]]
  - *( co_occur )*
  - [[Continuous NB]]
- [[Naive Bayes Classifier Algorithm]]
  - *( co_occur )*
  - [[Naive Bayes algorithm]]
- [[Bayesian Classifier with Continuous Variables:  Continuous N]]
- [[Naive Bayesian Classifier]]

## 📋 All Core Concepts
- [[Naive Bayes Classifier Algorithm]]
- [[Bayesian Classifier with Continuous Variables:  Continuous N]]
- [[Naive Bayesian Classifier]]
- [[Gaussian Naïve Bayes]]
- [[Naïve Bayes with continuous variables]]
- [[Naive Bayes algorithm]]
- [[Bayesian Classifier]]
- [[Naïve Bayes]]
- [[Continuous NB]]
