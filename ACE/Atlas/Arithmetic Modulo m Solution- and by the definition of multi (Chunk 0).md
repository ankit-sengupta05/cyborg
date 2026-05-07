---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:38:55.976109'
id: f0090f63
links: []
modified: '2026-05-07T20:38:55.976109'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: 'Arithmetic Modulo m Solution: and by the definition of multi (Chunk 0)'
type: knowledge_chunk
---

---
chunk_id: ea7175f12fa8
source: FALL2025-26_MAT1003_TH_AP2025262000358_2025-08-13_Reference-Material-II.pdf
page: 0
title: Arithmetic Modulo m Solution: and by the definition of multi (Chunk 0)
keywords: ['Modulo m', 'Base 10', 'Base 2', 'Base 8', 'Base 16', 'Mayans', 'Babylonians']
created: 2026-05-08 02:08:55
tree_path: Maths > Page 0 > Arithmetic Modulo m Solution: and by the definitio
---

Arithmetic Modulo m Solution: and by the definition of multiplication modulo 11, we have: Integer Representations and Algorithms Section Summary Integer Representations Base bExpansions Binary Expansions Octal Expansions Hexadecimal Expansions Base Conversion Algorithm Algorithms for Integer Operations Representations of Integers In the modern world, we use decimal, or base 10,notation to represent integers. For example when we write 965, we mean 9∙102 + 6∙101 + 5∙100 . We can represent numbers using any base b, where bis a positive integer greater than 1. The bases b= 2 (binary ), b= 8 (octal ) , and b= 16 (hexadecimal ) are important for computing and communications The ancient Mayans used base 20and the ancient Babylonians used base 60. Base bRepresentations We can use positive integer bgreater than 1as a base, because of this theorem: Theorem 1: Let bbe a positive integer greater than 1. Then if nis a positive integer, it can be expressed uniquely in the form: n= akbk+ ak-1bk-1+ …. + a1b+ a0 where kis a nonnegative integer, a0,a1,…. akare nonnegative integers less than b, and ak≠ 0. The aj, j= 0,…,kare called the base - bdigits of the representation. The representation of n given in Theorem 1is called the base b expansion of n and is denoted by (akak-1….a1a0)b. We usually omit the subscript 10for base 10expansions. Binary Expansions Most computers represent integers and do arithmetic with binary ( base 2) expansions of integers. In these expansions, the only digits used are 0 and 1 . Example : What is the decimal expansion of the integer that has ( 1 0101 1111 )2 as its binary expansion? Solution : (1 0101 1111 )2 = 1∙28 + 0∙27 + 1∙26 + 0∙25 + 1∙24 + 1∙23 + 1∙22 + 1∙21 + 1∙20 =351. Example : What is the decimal expansion of the integer that has ( 11011 )2as its binary expansion? Solution : (11011 )2 = 1 ∙24 + 1∙23 + 0∙22 + 1∙21 + 1∙20 =27. Octal Expansions The octal expansion ( base 8 ) uses the digits { 0,1,2,3,4,5,6,7 }. Example : What is the decimal expansion of the number with octal expansion ( 7016 )8? Solution : 7∙83 + 0∙82 + 1∙81 + 6∙80 =3598 Example : What is the decimal expansion of the number with octal expansion ( 111)8 ? Solution : 1∙82 + 1∙81 + 1∙80 = 64 + 8 + 1 = 73 Hexadecimal Expansions The hexadecimal expansion needs 16digits , but our decimal system provides only 10. So letters are used for the additional symbols . The hexadecimal system uses the digits { 0,1,2,3,4,5,6,7,8,9 ,A,B,C,D,E,F }. The letters A through Frepresent the decimal numbers 10through 15. Here, base is 16 . Example : What is the decimal expansion of the number with hexadecimal expansion ( 2AE0B )16? Solution : 2∙164 + 10∙163 + 14∙162 + 0∙161 + 11∙160 =175627 Example : What is the decimal expansion of the number with hexadecimal expansion (E 5)16? Solution :14∙161 + 5∙160 = 224 + 5 = 229 Base Conversion To construct the base bexpansion of an integer n: Divide nby bto obtain a quotient and remainder . n= bq0+ a00≤a0 ≤b The remainder, a0, is the rightmost digit in the base bexpansion of n. Next, divide q0by b. q0= bq1+ a10≤a1 ≤b The remainder, a1, is the second digit from the right in the base b expansion of n. Continue by successively dividing the quotients by b, obtaining the additional base bdigits as the remainder. The process terminates when the quotient is 0. continued → Algorithm: Constructing Base bExpansions q represents the quotient obtained by successive divisions by b, starting with q = n. The digits in the base b expansion are the remainders of the division given by q mod b. The algorithm terminates when q = 0is reached .procedure base b expansion (n, b: positive integers with b> 1) q:= n k := 0 while (q≠ 0) ak:= qmod b q:= qdivb k:= k+ 1 return (ak-1,…, a1,a0){(ak-1… a1a0)bis base b expansion of n} Base Conversion Example : Find the octal expansion of (12345 )10 Solution : Successively dividing by 8 gives:  12345 = 8 ∙ 1543 + 1  1543 = 8 ∙ 192+ 7  192= 8 ∙ 24+ 0  24= 8 ∙ 3+ 0  3= 8∙ 0+ 3 The remainders are the digits from right to left yielding ( 30071)8. Comparison of Hexadecimal, Octal, and Binary Representations Each octal digit corresponds to a block of 3binary digits. Each hexadecimal digit corresponds to a block of 4binary digits. So, conversion between binary, octal, and hexadecimal is easy.Initial 0s are not shown. Conversion Between Binary, Octal, and Hexadecimal Expansions Example : Find the octal and hexadecimal expansions of ( 11 1110 1011 1100 )2. Solution : To convert to octal , we group the digits into blocks of three (011 111 010 111 100)2, adding initial 0s as needed. The blocks from left to right correspond to the digits 3,7,2,7, and 4. Hence, the solution is ( 37274 )8. To convert to hexadecimal , we group the digits into blocks of four (0011 1110 1011 1100 )2, adding initial 0s as needed. The blocks from left to right correspond to the digits 3,E,B,and C. Hence, the solution is ( 3EBC )16.

### Related Concepts
- [[Base 10]]
- [[Mayans]]
- [[Modulo m]]
- [[Babylonians]]
- [[Base 2]]
- [[Base 8]]
- [[Base 16]]
