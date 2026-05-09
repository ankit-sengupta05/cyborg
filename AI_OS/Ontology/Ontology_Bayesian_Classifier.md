---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T23:50:28.924650'
id: 6529761e
links: []
modified: '2026-05-09T23:50:28.924650'
project: ''
source: ''
status: active
summary: ''
tags:
- ontology
- system_sync
- map
title: Ontology_Bayesian_Classifier
type: ontology_map
---

# Ontology: Bayesian Classifier

**Summary**: A probabilistic model for classification based on Bayes' theorem with an assumption of independence between the features.

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["Gaussian Naïve Bayes"]
    n1["Naive Bayes Classifier Algorithm"]
    n2["Naive Bayes algorithm"]
    n3["Naïve Bayes with continuous variables"]
    n4["Continuous NB"]
    n5["Bayesian Classifier"]
    n6["Bayesian Classifier with Continuous Variables:  Continuous N"]
    n7["Naive Bayesian Classifier"]
    n5 -->|CONTAINS| n5
    n5 -->|CONTAINS| n1
    n5 -->|CONTAINS| n2
    n5 -->|CONTAINS| n5
    n1 -->|CO_OCCUR| n2
    n5 -->|LINKED_TO| n1
    n7 -->|KEYWORD_LINK| n5
    n5 -->|SEMANTIC_SIMILAR| n7
    n6 -->|KEYWORD_LINK| n5
    n6 -->|CONTAINS| n5
    n6 -->|CONTAINS| n4
    n6 -->|CONTAINS| n3
    n6 -->|CONTAINS| n0
    n5 -->|CO_OCCUR| n4
    n5 -->|CO_OCCUR| n3
    n5 -->|CO_OCCUR| n0
    n4 -->|CO_OCCUR| n3
    n4 -->|CO_OCCUR| n0
    n3 -->|CO_OCCUR| n0
    n5 -->|SEMANTIC_SIMILAR| n4
    n3 -->|LINKED_TO| n0
```

## 🌳 Sequential Topic Tree
> Shows how topics are hierarchically and sequentially related

- [[Bayesian Classifier]]
  - *( co_occur )*
  - [[Continuous NB]]
    - *( co_occur )*
    - [[Naïve Bayes with continuous variables]]
      - *( co_occur )*
      - [[Gaussian Naïve Bayes]]
- [[Naive Bayes Classifier Algorithm]]
  - *( co_occur )*
  - [[Naive Bayes algorithm]]
- [[Bayesian Classifier with Continuous Variables:  Continuous N]]
- [[Naive Bayesian Classifier]]

## 📋 All Core Concepts
- [[Gaussian Naïve Bayes]]
- [[Naive Bayes Classifier Algorithm]]
- [[Naive Bayes algorithm]]
- [[Naïve Bayes with continuous variables]]
- [[Continuous NB]]
- [[Bayesian Classifier]]
- [[Bayesian Classifier with Continuous Variables:  Continuous N]]
- [[Naive Bayesian Classifier]]
