---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:42:54.489513'
id: 45a46fb5
links: []
modified: '2026-05-07T20:42:54.489513'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: '{A3}, {A4}, {A5}, {A6}, {A7}, {A8} 2 5 {A4, A8}, {A1}, {A3,  (Chunk 1)'
type: knowledge_chunk
---

---
chunk_id: cfd5eece0915
source: WINSEM2025-26_CSE3008_ETH_AP2025264000489_2026-04-17_Reference-Material-I.pdf
page: 1
title: {A3}, {A4}, {A5}, {A6}, {A7}, {A8} 2 5 {A4, A8}, {A1}, {A3,  (Chunk 1)
keywords: ['Exercise 5', 'DBScan', 'Epsilon', 'minpoint', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'C1', 'C2', 'C3']
created: 2026-05-08 02:12:54
tree_path: ML > Page 1 > {A3}, {A4}, {A5}, {A6}, {A7}, {A8} 2 5 {A4, A8}, {
---

{A3}, {A4}, {A5}, {A6}, {A7}, {A8} 2 5 {A4, A8}, {A1}, {A3, A5, A6}, {A2}, {A7} 3 4 {A4, A8, A1}, {A3, A5, A6}, {A2}, {A7} 4 2 {A1, A3, A4, A5, A6, A8}, {A2, A7} 5 1 {A1, A3, A4, A5, A6, A8, A2, A7} Exercise 5: DBScan If Epsilon is 2 and minpoint is 2, what are the clusters that DBScan would discover with the following 8 examples: A1=(2,10), A2=(2,5), A3=(8,4), A4=(5, 8), A5=(7,5), A6=(6,4), A7=(1,2), A8=(4,9). The distance matrix is the same as the one in Exercise 1. Draw the 10 by 10 space and illustrate the discovered clusters. What if Epsilon is increased to 10? Solution: What is the Epsilon neighborhood of each point? N2(A1)={}; N 2(A2)={}; N 2(A3)={A5, A6}; N 2(A4)={A8}; N 2(A5)={A3, A6}; N2(A6)={A3, A5}; N 2(A7)={}; N 2(A8)={A4} So A1, A2, and A7 are outliers, while we have two clusters C1={A4, A8} and C2={A3, A5, A6} If Epsilon is 10 then the neighborhood of some points will increase: A1 would join the cluster C1 and A2 would joint with A7 to form cluster C3={A2, A7}. A4 A8 A1 A3 A5 A6 A2 A7 0 1 23 4 5A4 A8 A1 A3 A5 A6 A2 A7 0 1 2 3 4 5 6A4 A8 A1 A3 A5 A6 A2 A7 0 1 2 3 4 5 6 Epsilon = 2 Epsilon = 10 0 0 1 2 3 4 5 6 7 8 9 11 2 3 4 5 6 7 8 9 10 A1 A2 A3 A4 A5 A6 A7 A8 0 0 1 2 3 4 5 6 7 8 9 11 2 3 4 5 6 7 8 9 10 A1 A2 A3 A4 A5 A6 A7 A8

### Related Concepts
- [[A4]]
- [[C1]]
- [[DBScan]]
- [[minpoint]]
- [[A2]]
- [[Exercise 5]]
- [[Epsilon]]
- [[A1]]
- [[A7]]
- [[A5]]
- [[C3]]
- [[A8]]
- [[A3]]
- [[C2]]
- [[A6]]
