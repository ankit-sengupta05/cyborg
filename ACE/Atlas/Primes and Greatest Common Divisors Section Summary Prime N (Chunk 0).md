---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:39:02.234379'
id: 699bae85
links: []
modified: '2026-05-07T20:39:02.234379'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: Primes and Greatest Common Divisors Section Summary Prime N (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: 41cd99225cd2
source: FALL2025-26_MAT1003_TH_AP2025262000358_2025-08-16_Reference-Material-I.pdf
page: 0
title: Primes and Greatest Common Divisors Section Summary Prime N (Chunk 0)
keywords: []
created: 2026-05-08 02:09:02
tree_path: Maths > Page 0 > Primes and Greatest Common Divisors Section Summar
---

Primes and Greatest Common Divisors Section Summary Prime Numbers and their Properties Greatest Common Divisors and Least Common Multiples The Euclidian Algorithm gcds as Linear Combinations Primes Definition : A positive integer pgreater than 1is called prime if the only positive factors of pare 1and p. A positive integer that is greater than 1and is not prime is called composite . Example : The integer 7is prime because its only positive factors are 1and 7, but 9is composite because it is divisible by 3. The Fundamental Theorem of Arithmetic Theorem 1 : Every positive integer greater than 1can be written uniquely as a prime or as the product of two or more primes where the prime factors are written in order of non-decreasing size. 1024 = 2 ∙ 2 ∙ 2 ∙ 2 ∙ 2 ∙ 2 ∙ 2 ∙ 2 ∙ 2 ∙ 2 = 210Examples : 100 = 2 ∙ 2 ∙ 5 ∙ 5 = 22∙ 52 641 = 641 999 = 3 ∙ 3 ∙ 3 ∙ 37 = 33∙ 37 Greatest Common Divisor Example 1: Example 2: Greatest Common Divisor Example: The integers 17 and 22 are relatively prime, because gcd(17,22)=1. Example: Finding the Greatest Common Divisor Using Prime Factorizations Suppose the prime factorizations of aand bare: where each exponent is a nonnegative integer, and where all primes occurring in either prime factorization are included in both. Then: This formula is valid since the integer on the right (of the equals sign) divides both aand b. No larger integer can divide both aand b. Example : 120= 23∙3 ∙5 500= 22∙53 gcd( 120,500) = 2min(3,2) ∙3min(1,0) ∙5min(1,3) =22∙30∙51= 20 Finding the gcd of two positive integers using their prime factorizations is not efficient because there is no efficient algorithm for finding the prime factorization of a positive integer. Least Common Multiple Least Common Multiple Definition : The least common multiple of the positive integers aand b is the smallest positive integer that is divisible by both aand b. It is denoted by lcm( a,b). The least common multiple can also be computed from the prime factorizations. This number is divided by both aand band no smaller number is divided by aand b. Example: lcm( 233572,2433) = 2max(3,4)3max(5,3)7max(2,0)=243572 The greatest common divisor and the least common multiple of two integers are related by: Theorem 5: Let a and b be positive integers. Then ab= gcd(a,b)∙ lcm(a,b) Euclidean Algorithm (Efficient way to find gcd) Stopping conditionDivide 287by 91 continued →The Euclidian algorithm is an efficient method for computing the greatest common divisor of two integers. It is based on the idea that gcd(a,b) is equal to gcd(b,r) when a>band ris the remainder when a is divided by b. Example : Find gcd(91, 287): 287 = 91 ∙ 3 + 14 91 = 14 ∙ 6 + 7 Divide 91by 14 14 = 7 ∙ 2 + 0 Divide 14by 7 gcd(287, 91) = gcd(91, 14) = gcd(14, 7) = 7 gcds as Linear Combinations Bézout’s Theorem : If aand bare positive integers, then there exist integers sand tsuch that gcd(a,b) = sa+ tb. Definition : If aand bare positive integers, then integers sand t such that gcd(a,b) = sa+ tbare called Bézout coefficients of aand b. The equation gcd(a,b) = sa+ tbis called Bézout’s identity. By Bézout’s Theorem, the gcd of integers aand bcan be expressed in the form sa+ tbwhere sand tare integers. This is a linear combination with integer coefficients of aand b. gcd(6,14) = 2 = ( −2)∙6 + 1∙14 Étienne Bézout (1730 -1783 ) Example of Bezout’s Theorem : Consequences of Bézout’s Theorem PRACTICE QUESTIONS

