---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T17:32:25.227520'
id: 22edfd5f
links: []
modified: '2026-05-09T17:32:25.227520'
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
    n0["Naïve Bayes"]
    n1["Naive Bayes Classifier Algorithm"]
    n2["Naive Bayes algorithm"]
    n3["Gaussian Naïve Bayes"]
    n4["Naïve Bayes with continuous variables"]
    n5["Bayesian Classifier with Continuous Variables:  Continuous N"]
    n6["Naive Bayesian Classifier"]
    n7["Bayesian Classifier"]
    n8["Continuous NB"]
    n7 -->|CONTAINS| n7
    n7 -->|CONTAINS| n1
    n7 -->|CONTAINS| n2
    n7 -->|CONTAINS| n7
    n1 -->|CO_OCCUR| n2
    n7 -->|LINKED_TO| n1
    n6 -->|KEYWORD_LINK| n7
    n6 -->|SEMANTIC_SIMILAR| n7
    n5 -->|KEYWORD_LINK| n7
    n5 -->|CONTAINS| n7
    n5 -->|CONTAINS| n8
    n5 -->|CONTAINS| n0
    n3 -->|KEYWORD_LINK| n0
    n5 -->|CONTAINS| n3
    n7 -->|CO_OCCUR| n8
    n7 -->|CO_OCCUR| n0
    n7 -->|CO_OCCUR| n3
    n8 -->|CO_OCCUR| n0
    n8 -->|CO_OCCUR| n3
    n7 -->|SEMANTIC_SIMILAR| n8
    n4 -->|KEYWORD_LINK| n0
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
- [[Naïve Bayes]]
- [[Naive Bayes Classifier Algorithm]]
- [[Naive Bayes algorithm]]
- [[Gaussian Naïve Bayes]]
- [[Naïve Bayes with continuous variables]]
- [[Bayesian Classifier with Continuous Variables:  Continuous N]]
- [[Naive Bayesian Classifier]]
- [[Bayesian Classifier]]
- [[Continuous NB]]
