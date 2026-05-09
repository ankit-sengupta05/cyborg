---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T17:19:26.771536'
id: 1c44b3b7
links: []
modified: '2026-05-09T17:19:26.771536'
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
    n0["Overcast"]
    n1["Entropy among the three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy))"]
    n2["Decision Trees"]
    n3["Supervised learning technique"]
    n4["Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)"]
    n5["leaf node"]
    n6["Rain"]
    n7["Probability"]
    n8["Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6) = 0.97 Overcast: In the given data, 4 days were overcast and tennis was played on all four days."]
    n9["Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4) = 0.97 Entropy among the three branches Entropy among three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy)) = ((5/14) * 0.97) + ((4/14) * 0) + ((5/14) * 0.97) = 0.69 Information Gain = H(S) - H(S|X) Reduction in randomness = entropy source – entropy of branches = 0.940 – 0.69 = 0.246 Example Cont’d The next step calculates the Information Gain for each feature."]
    n10["Sunny"]
    n11["Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0"]
    n12["Rainy"]
    n13["Tennis"]
    n14["Regression problems"]
    n15["'Insights into Decision Trees, Loss"]
    n16["Entropy"]
    n17["Handling Missing Values in Decision Trees"]
    n18["decision node"]
    n19["Decision Tree"]
    n20["tree-structured classifier"]
    n21["Decision Trees"]
    n22["Loss Functions"]
    n23["Information Gain Calculation for Outlook Cont’d"]
    n24["Classification problems"]
    n21 -->|CONTAINS| n21
    n21 -->|CONTAINS| n3
    n21 -->|CONTAINS| n20
    n21 -->|CONTAINS| n18
    n21 -->|CONTAINS| n5
    n3 -->|CO_OCCUR| n20
    n3 -->|CO_OCCUR| n18
    n3 -->|CO_OCCUR| n5
    n20 -->|CO_OCCUR| n18
    n20 -->|CO_OCCUR| n5
    n18 -->|CO_OCCUR| n5
    n21 -->|CONTAINS| n7
    n21 -->|CONTAINS| n16
    n21 -->|CONTAINS| n23
    n21 -->|CONTAINS| n6
    n21 -->|CONTAINS| n13
    n21 -->|CONTAINS| n10
    n21 -->|CONTAINS| n0
    n12 -->|KEYWORD_LINK| n6
    n21 -->|CONTAINS| n12
    n7 -->|CO_OCCUR| n16
    n7 -->|CO_OCCUR| n23
    n7 -->|CO_OCCUR| n6
    n7 -->|CO_OCCUR| n13
    n7 -->|CO_OCCUR| n10
    n7 -->|CO_OCCUR| n0
    n7 -->|CO_OCCUR| n12
    n16 -->|CO_OCCUR| n23
    n16 -->|CO_OCCUR| n6
    n16 -->|CO_OCCUR| n13
    n16 -->|CO_OCCUR| n10
    n16 -->|CO_OCCUR| n0
    n16 -->|CO_OCCUR| n12
    n23 -->|CO_OCCUR| n6
    n23 -->|CO_OCCUR| n13
    n23 -->|CO_OCCUR| n10
    n23 -->|CO_OCCUR| n0
    n23 -->|CO_OCCUR| n12
    n6 -->|CO_OCCUR| n13
    n6 -->|CO_OCCUR| n10
    n6 -->|CO_OCCUR| n0
    n13 -->|CO_OCCUR| n10
    n13 -->|CO_OCCUR| n0
    n13 -->|CO_OCCUR| n12
    n10 -->|CO_OCCUR| n0
    n10 -->|CO_OCCUR| n12
    n0 -->|CO_OCCUR| n12
    n4 -->|KEYWORD_LINK| n16
    n4 -->|KEYWORD_LINK| n6
    n4 -->|KEYWORD_LINK| n12
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
- [[Entropy among the three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy))]]
- [[Decision Trees]]
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
- [[Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6) = 0.97 Overcast: In the given data, 4 days were overcast and tennis was played on all four days.]]
  - *( keyword_link )*
  - [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6)]]
- [[Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4) = 0.97 Entropy among the three branches Entropy among three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy)) = ((5/14) * 0.97) + ((4/14) * 0) + ((5/14) * 0.97) = 0.69 Information Gain = H(S) - H(S|X) Reduction in randomness = entropy source – entropy of branches = 0.940 – 0.69 = 0.246 Example Cont’d The next step calculates the Information Gain for each feature.]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
  - *( keyword_link )*
  - [[Probability of playing tennis = 4/4 = 1]]
  - *( keyword_link )*
  - [[Probability of not playing tennis = 0/4 = 0]]
- [["Insights into Decision Trees, Loss]]
  - *( keyword_link )*
  - [[Decision Tree]]
    - *( linked_to )*
    - [[Classification tree]]
      - *( keyword_link )*
      - [[Classification trees]]
    - *( linked_to )*
    - [[Regression tree]]
      - *( keyword_link )*
      - [[Regression trees]]
  - *( contains )*
  - [[Loss Functions]]
    - *( co_occur )*
    - [[Handling Missing Values in Decision Trees]]
      - *( co_occur )*
      - [[Instability]]
- [[Information Gain Calculation for Outlook Cont’d]]

## 📋 All Core Concepts
- [[Overcast]]
- [[Entropy among the three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy))]]
- [[Decision Trees]]
- [[Supervised learning technique]]
- [[Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4)]]
- [[leaf node]]
- [[Rain]]
- [[Probability]]
- [[Entropy when sunny = -0.4 * log2(0.4) – 0.6 * log2(0.6) = 0.97 Overcast: In the given data, 4 days were overcast and tennis was played on all four days.]]
- [[Entropy when rainy = -0.6 * log2(0.6) – 0.4 * log2(0.4) = 0.97 Entropy among the three branches Entropy among three branches = ((number of sunny days)/(total days) * (entropy when sunny)) + ((number of overcast days)/(total days) * (entropy when overcast)) + ((number of rainy days)/(total days) * (entropy when rainy)) = ((5/14) * 0.97) + ((4/14) * 0) + ((5/14) * 0.97) = 0.69 Information Gain = H(S) - H(S|X) Reduction in randomness = entropy source – entropy of branches = 0.940 – 0.69 = 0.246 Example Cont’d The next step calculates the Information Gain for each feature.]]
- [[Sunny]]
- [[Probability of playing tennis = 4/4 = 1 Probability of not playing tennis = 0/4 = 0]]
- [[Rainy]]
- [[Tennis]]
- [[Regression problems]]
- [["Insights into Decision Trees, Loss]]
- [[Entropy]]
- [[Handling Missing Values in Decision Trees]]
- [[decision node]]
- [[Decision Tree]]
- [[tree-structured classifier]]
- [[Decision Trees]]
- [[Loss Functions]]
- [[Information Gain Calculation for Outlook Cont’d]]
- [[Classification problems]]
