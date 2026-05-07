---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:35:24.691285'
id: 062a0aeb
links: []
modified: '2026-05-07T20:35:24.691285'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: number, except the one corresponding to the number zero, can (Chunk 1)
type: knowledge_chunk
---

---
chunk_id: 5fa07b32aea9
source: WINSEM2025-26_ECE2002_TH_AP2025264001004_2025-12-10_Reference-Material-I.pdf
page: 1
title: number, except the one corresponding to the number zero, can (Chunk 1)
keywords: ['Number', 'IEEE FP']
created: 2026-05-08 02:05:24
tree_path: COA > Page 1 > number, except the one corresponding to the number
---

number, except the one corresponding to the number zero, can be normalized by choosing the exponent so that the radix point falls to the right of the leftmost 1 bit . 37.2510= 100101.012= 1.0010101 x 25=> Biased exponent = 132 7.62510= 111.1012= 1.11101 x 22 => Biased exponent = 129 0.312510= 0.01012 = 1.01x 2-2 => Biased exponent = 125 IEEE Floating Point Representation •Suppose number is using 32 -bit format: the 1 bit sign bit, 8 bits for signed exponent, and 23 bits for the fractional part. •Floating point numbers can be stored into 32- bits, by dividing the bits into three parts: the sign, the biased exponent , and the mantissa. Example: 37.2510= 100101.012= 1.0010101 x 25 Biased exponent= 127+5=132= 10000100 Mantissa= 0010101 SB Exponent (8-bits) Mantissa (23 bits) 0 1000010000101010000000000000000 Example: Find the IEEE FP representation of –24.75 Step 1. Compute the binary equivalent of the whole part and the fractional part. 2410=> 110002, .7510 =>.112 So : - 24.75 10 = - 11000.11 2 Step 2.Normalize thenumber bymoving thedecimal point totheright oftheleftmost one. -11000.11 = -1.100011 x 24 So, Mantissa = 100011, True Exponent = 4 Example: Find the IEEE FP representation of –24.75 Step 3. Convert the exponent to a biased exponent 127+4=131 ==> 13110=100000112 Step 4.Store theresults from steps 1-3 SB Exponent (8-bits) Mantissa (23 bits) 1 1000001110001100000000000000000 IEEE standard to Decimal Floating Point Conversion SB Exponent (8-bits) Mantissa (23 bits) 1 0111110101000000000000000000000Ex 1:Convert the following 32- bit binary number to its decimal floating point equivalent: Step 1: Extract the biased exponent and unbias it Biased exponent = 011111012= 12510 True exponent (or) Unbiased Exponent: 125 –127 = - 2 Step 3: Denormalize the binary number from step 2 (i.e. move the decimal and get rid of (x 2n) part): -0.01012(negative exponent –move left) Step 4: Convert binary number to the FP equivalent (i.e. Add all column values with 1s in them) -0.01012= -( 0.25 + 0.0625) = -0.312510 Ex 2: Convert the following 32 bit binary number to its decimal floating point equivalent: Sign Exponent Mantissa 0 10000011 10011000..0 Step 1:Extract thebiased exponent andunbias it Biased exponent =10000112=13110 Unbiased Exponent :131–127=4 Step 4: Convert binary number to the FP equivalent (i.e. Add all column values with 1s in them) 11001. 1=16+8+1+.5 =25.510Step 3: Denormalize the binary number from step 2 (i.e. move the decimal and get rid of (x 2n) part: 11001.12 (positive exponent –move right)

### Related Concepts
- [[Number]]
- [[IEEE FP]]
