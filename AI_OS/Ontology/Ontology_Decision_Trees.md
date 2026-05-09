---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T17:32:25.207794'
id: 61075d56
links: []
modified: '2026-05-09T17:32:25.207794'
project: ''
source: ''
status: active
summary: ''
tags:
- ontology
- system_sync
- map
title: Ontology_Decision_Trees
type: ontology_map
---

# Ontology: Decision Trees

**Summary**: A classification and regression technique used in machine learning.

## 🗺️ Visual Concept Map
```mermaid
graph TD
    n0["Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)"]
    n1["Information Gain Calculation for Outlook Cont’d"]
    n2["Rain"]
    n3["Instability"]
    n4["Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4) = 0.97 Entropy among the three branches Entropy among three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy)) = ((5/14) * 0.97) + ((4/14) * 0) + ((5/14) * 0.97) = 0.69 Information Gain = H(S) - H(S|X) Reduction in randomness = entropy source – entropy of branches = 0.940 – 0.69 = 0.246 Example Cont’d The next step calculates the Information Gain for each feature."]
    n5["Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6) = 0.97 Overcast: In the given data, 4 days were overcast and tennis was played on all four days."]
    n6["Supervised learning technique"]
    n7["Rainy"]
    n8["Overcast"]
    n9["Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0"]
    n10["Decision Trees"]
    n11["Tennis"]
    n12["Loss Functions"]
    n13["tree-structured classifier"]
    n14["Probability"]
    n15["decision node"]
    n16["Classification problems"]
    n17["leaf node"]
    n18["Handling Missing Values in Decision Trees"]
    n19["Entropy"]
    n20["Sunny"]
    n21["Entropy among the three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy))"]
    n22["Decision Trees"]
    n23["'Insights into Decision Trees, Loss"]
    n24["Regression problems"]
    n10 -->|CONTAINS| n10
    n10 -->|CONTAINS| n6
    n10 -->|CONTAINS| n13
    n10 -->|CONTAINS| n15
    n10 -->|CONTAINS| n17
    n6 -->|CO_OCCUR| n13
    n6 -->|CO_OCCUR| n15
    n6 -->|CO_OCCUR| n17
    n13 -->|CO_OCCUR| n15
    n13 -->|CO_OCCUR| n17
    n15 -->|CO_OCCUR| n17
    n10 -->|CONTAINS| n14
    n10 -->|CONTAINS| n19
    n10 -->|CONTAINS| n1
    n10 -->|CONTAINS| n2
    n10 -->|CONTAINS| n11
    n10 -->|CONTAINS| n20
    n10 -->|CONTAINS| n8
    n7 -->|KEYWORD_LINK| n2
    n10 -->|CONTAINS| n7
    n14 -->|CO_OCCUR| n19
    n14 -->|CO_OCCUR| n1
    n14 -->|CO_OCCUR| n2
    n14 -->|CO_OCCUR| n11
    n14 -->|CO_OCCUR| n20
    n14 -->|CO_OCCUR| n8
    n14 -->|CO_OCCUR| n7
    n19 -->|CO_OCCUR| n1
    n19 -->|CO_OCCUR| n2
    n19 -->|CO_OCCUR| n11
    n19 -->|CO_OCCUR| n20
    n19 -->|CO_OCCUR| n8
    n19 -->|CO_OCCUR| n7
    n1 -->|CO_OCCUR| n2
    n1 -->|CO_OCCUR| n11
    n1 -->|CO_OCCUR| n20
    n1 -->|CO_OCCUR| n8
    n1 -->|CO_OCCUR| n7
    n2 -->|CO_OCCUR| n11
    n2 -->|CO_OCCUR| n20
    n2 -->|CO_OCCUR| n8
    n11 -->|CO_OCCUR| n20
    n11 -->|CO_OCCUR| n8
    n11 -->|CO_OCCUR| n7
    n20 -->|CO_OCCUR| n8
    n20 -->|CO_OCCUR| n7
    n8 -->|CO_OCCUR| n7
    n0 -->|KEYWORD_LINK| n19
    n0 -->|KEYWORD_LINK| n2
    n0 -->|KEYWORD_LINK| n7
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
  - *( contains )*
  - [[Probability]]
- [[Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[Information Gain Calculation for Outlook Cont’d]]
- [[Instability]]
  - *( semantic_similar )*
  - [[Decision Trees]]
- [[Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4) = 0.97 Entropy among the three branches Entropy among three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy)) = ((5/14) * 0.97) + ((4/14) * 0) + ((5/14) * 0.97) = 0.69 Information Gain = H(S) - H(S|X) Reduction in randomness = entropy source – entropy of branches = 0.940 – 0.69 = 0.246 Example Cont’d The next step calculates the Information Gain for each feature.]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6) = 0.97 Overcast: In the given data, 4 days were overcast and tennis was played on all four days.]]
  - *( keyword_link )*
  - [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Supervised learning technique]]
  - *( co_occur )*
  - [[tree-structured classifier]]
    - *( co_occur )*
    - [[decision node]]
      - *( co_occur )*
      - [[leaf node]]
  - *( co_occur )*
  - [[Classification problems]]
    - *( co_occur )*
    - [[Regression problems]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
  - *( keyword_link )*
  - [[Probability of playing tennis = 4/4 = 1]]
  - *( keyword_link )*
  - [[Probability of not playing tennis = 0/4 = 0]]
- [[Loss Functions]]
  - *( co_occur )*
  - [[Handling Missing Values in Decision Trees]]
- [[Entropy among the three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy))]]
- [["Insights into Decision Trees, Loss]]

## 📋 All Core Concepts
- [[Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[Information Gain Calculation for Outlook Cont’d]]
- [[Rain]]
- [[Instability]]
- [[Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4) = 0.97 Entropy among the three branches Entropy among three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy)) = ((5/14) * 0.97) + ((4/14) * 0) + ((5/14) * 0.97) = 0.69 Information Gain = H(S) - H(S|X) Reduction in randomness = entropy source – entropy of branches = 0.940 – 0.69 = 0.246 Example Cont’d The next step calculates the Information Gain for each feature.]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6) = 0.97 Overcast: In the given data, 4 days were overcast and tennis was played on all four days.]]
- [[Supervised learning technique]]
- [[Rainy]]
- [[Overcast]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [[Decision Trees]]
- [[Tennis]]
- [[Loss Functions]]
- [[tree-structured classifier]]
- [[Probability]]
- [[decision node]]
- [[Classification problems]]
- [[leaf node]]
- [[Handling Missing Values in Decision Trees]]
- [[Entropy]]
- [[Sunny]]
- [[Entropy among the three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy))]]
- [[Decision Trees]]
- [["Insights into Decision Trees, Loss]]
- [[Regression problems]]
