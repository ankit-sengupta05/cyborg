---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:38:05.536620'
id: 6878f5ff
links: []
modified: '2026-05-07T20:38:05.536620'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: 'Translating from Nested Quantifiers into English Example 1:  (Chunk 0)'
type: knowledge_chunk
---

---
chunk_id: 52e5719e0e97
source: FALL2025-26_MAT1003_TH_AP2025262000358_2025-08-05_Reference-Material-I.pdf
page: 0
title: Translating from Nested Quantifiers into English Example 1:  (Chunk 0)
keywords: ['Example 1', 'C(x)', 'F(x, y)', 'Student', 'Example 2', 'Positive integers', 'Example 3', 'Person', 'F(x)']
created: 2026-05-08 02:08:05
tree_path: Maths > Page 0 > Translating from Nested Quantifiers into English E
---

Translating from Nested Quantifiers into English Example 1: Translate the statement x( C(x ) ∨y (C(y ) ∧F(x, y )) )into English, where C(x) is “ xhas a computer,” and F( x,y) is “xand yare friends,” and the domain for both xand yconsists of all students in your school. Solution : The statement says: For every student x in your school, x has a computer orthere is a student y such that y has a computer and x and y are friends. In more simple way, Every student in your school has a computer or has a friend who has a computer. Translating Mathematical Statements into Predicate Logic Example :Translate “ The sum of two positive integers is always positive ” into a logical expression. Solution : 1.Rewrite the statement to make the implied quantifiers and domains explicit: “For every two integers, if these integers are both positive, then the sum of these integers is positive.” 2.Introduce the variables xand y, and specify the domain, to obtain: “For all positive integers xand y, x+ yis positive .” 3.The result is: xy( (x> 0)∧ ( y> 0) → (x+ y > 0) ) where the domain of both variables consists of all integers. Translating English into Logical Expressions Example : Express the statement “ If a person is female and is a parent, then this person is someone’s mother ” as a logical expression involving predicates, quantifiers with domain consisting of all people, and logical connectives. Solution: We have the predicates as: F(x): x is female P(x): x is a parent M(x, y): x is mother of y Now, we can rewrite the above sentence in the question as: “For every person x, if person x is female and person x is a parent, then there exists a person y such that person x is the mother of person y ”. In terms of logical expression: x( (F(x) ∧P(x)) → y M(x, y) ). xy ( (F(x) ∧P(x)) → M(x, y) ).  Examples for Translating English into Logical Expressions If B(x, y), S(x, y) and L(x, y) denotes “ x and y are brothers ”, “x and y are siblings ” and “ x loves y ”, respectively. Choose the obvious predicates and express in predicate logic. Example 1: “Brothers are siblings.” Solution : xy (B(x, y) → S(x, y)) Example 2: “Siblinghood is symmetric.” Solution : xy (S(x,y) → S(y , x)) Example 3: “Everybody loves somebody.” Solution : xy L(x,y) Example 4: “There is someone who is loved by everyone.” Solution : y xL(x,y) Example 5: “There is someone who loves someone.” Solution : x y L(x,y) Example 6: “Everyone loves himself” Solution : x L(x,x) Negating Nested Quantifiers Example : Express the negation of the statement xy( xy= 1) so that no negation precedes a quantifier. Solution: By successively applying De Morgan’s Laws for Quantifiers, we can move the negation in¬xy( xy= 1) inside all the quantifiers. ¬xy( xy= 1) is equivalent to x¬y( xy= 1), which is equivalent to xy¬( xy= 1). But ¬( xy= 1) simply means xy 1. Finally, our negated statement is expressed as: xy(xy 1).  Answers QUESTIONS FOR PRACTICE QUESTIONS FOR PRACTICE

### Related Concepts
- [[F(x)]]
- [[Example 3]]
- [[Positive integers]]
- [[Student]]
- [[C(x)]]
- [[Person]]
- [[Example 2]]
- [[Example 1]]
- [[F(x, y)]]
