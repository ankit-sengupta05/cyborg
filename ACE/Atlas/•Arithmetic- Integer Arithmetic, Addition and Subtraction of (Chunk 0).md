---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:35:30.953522'
id: 4557a785
links: []
modified: '2026-05-07T20:35:30.953522'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: '•Arithmetic: Integer Arithmetic, Addition and Subtraction of (Chunk 0)'
type: knowledge_chunk
---

---
chunk_id: e3c98c098964
source: WINSEM2025-26_ECE2002_TH_AP2025264001004_2025-12-11_Reference-Material-I.pdf
page: 0
title: •Arithmetic: Integer Arithmetic, Addition and Subtraction of (Chunk 0)
keywords: ['Arithmetic', 'Integer Arithmetic', 'ALU', 'Signed numbers', 'Sign -Magnitude', "2's Complement"]
created: 2026-05-08 02:05:30
tree_path: COA > Page 0 > •Arithmetic: Integer Arithmetic, Addition and Subt
---

•Arithmetic: Integer Arithmetic, Addition and Subtraction of signed and unsigned numbers, Multiplication of signed and unsigned numbers, 2’s Complement method for multiplication, •Booths Algorithm, Hardware Implementation, •Array Multiplier, Integer Division, •Restoring and Non Restoring algorithms, •Floating point operations. 22-01-20251Module No. 2 ALU ALU : Arithmetic Logic Unit The Arithmetic Logic Unit (ALU) is a critical component of a computer's processor, designed to perform arithmetic and logical operations. 22-01-20252 Integer Arithmetic Addition and Subtraction Multiplication 22-01-20253 Integer Arithmetic Signed numbers can represent both positive and negative values. Two common representations for signed numbers are, Sign -Magnitude and 2’s Complement . 22-01-20254 Integer Arithmetic Sign - Magnitude Representation: The most significant bit (MSB) represents the sign: 0 indicates a positive number, and 1 indicates a negative number. The remaining bits represent the magnitude of the number. Eg: +18 = 00010010, -18 = 10010010 Need to consider both sign and magnitude in arithmetic Two representations of zero (+0 and -0) 22-01-20255 Integer Arithmetic 2’s Complement Representation: Itiswidely used indigital systems torepresent signed integers because it simplifies arithmetic operations (e.g.,addition and subtraction) and avoids issues like dual representations ofzero . In a 2's complement system: Positive numbers are represented in standard binary form. Negative numbers are represented by taking the 2's complement of the corresponding positive number: Invert all bits of the positive number (take the 1's complement). Add 1 to the result. 22-01-20256 Integer Arithmetic Key Properties of 2's Complement Representation: Single Representation for Zero: zero is always represented as 000000000000000, regardless of sign. Arithmetic Simplification: Addition and subtraction can be performed using the same circuitry, as subtraction isjust addition ofthe2'scomplement . Range for n -bit numbers: Minimum value: −2𝑛𝑛−1 Maximum value: 2𝑛𝑛−1-1 22-01-20257 Integer Arithmetic Example : 4-bit Representation of +18 and −18. Note: Since 18>24−1−1=7, we need at least 6 bits to represent these numbers +18 binary representation: 𝟏𝟏𝟏𝟏 𝟏𝟏𝟏𝟏 = 𝟏𝟏𝟏𝟏𝟏𝟏𝟏𝟏𝟏𝟏 𝟐𝟐 In 6 - bit binary: +18=010010 (the leading bit, 0, indicates it is positive). - 18 representation: binary representation of + 𝟏𝟏𝟏𝟏 𝟏𝟏𝟏𝟏 = 𝟏𝟏𝟏𝟏𝟏𝟏𝟏𝟏𝟏𝟏 𝟐𝟐 Take the 1's complement (invert all bits): 1 𝑠𝑠 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑛𝑛 𝑐𝑐 𝑐𝑐𝑜𝑜 010010 = 101101 Add 1 to the result: 101101 +1 = 101110 22-01-20258 Ifann-bitinteger isrequired tobestored inmbits, insign-magnitude notation, this iseasily accomplished: simply move thesign bittothenew leftmost position andfillinwithzeros .Conversion Between Lengths Instead, the rule for twos complement integers is to move the sign bit to the new leftmost position and fill in with copies of the sign bit . Problem: 1.Represent the following decimal numbers in both binary sign magnitude form and twos complement form using 16 bits: +512, - 29. Problem: 1.Represent the following decimal numbers in both binary sign magnitude form and twos complement form using 16 bits: +512, - 29. Problem: Represent the following twos complement values in decimal: 1101011; 0101101. Ans: -21 and 45 Addition and Subtraction: Addition (M+N): Normal binary addition Monitor sign bit for overflow Subtraction (M–N): 1. Add theminuend Mtothe2’scompleme ntofthesubtrahend N. 2. IfM≥N,thesum will produce anend carry,which canbediscarded; whatisleftisthe result M-N. 3. IfM<N,thesum does notproduce anend carryand it isthe 2 ’scompleme ntof(N-M).To obtaintheanswerinafamiliar form, takethe2’scompleme ntofthesum and place a negativesign infront. Addition and Subtraction: Problem: Assume numbers are represented in 8- bit twos complement representation. Show the calculation of the following: a. 6+13 b. -6+13 c. 6-13 d. -6-13 Multiplication: Unsigned Numbers The multiplication of two unsigned binary numbers is performed using the traditional multiplication algorithm, similar to decimal multiplication. Example: 7 x 5 Multiplication: Signed Numbers or 2s Complement Multiplication Convert numbers to two's complement: If one or both numbers are negative, convert them to their two's complement representation. Perform unsigned multiplication: Treat the two's complement numbers as unsigned numbers and multiply them. Adjust the result: If the result was expected to be negative, apply the two's complement to the product. Multiplication: Signed Numbers or 2s Complement Multiplication Example: Multiplication: Signed Numbers or 2s Complement Multiplication Example: Multiplication: Signed Numbers or 2s Complement Multiplication Example: Booth's algorithm Booth's algorithm is a method used for multiplying binary numbers, especially signed numbers in two's complement representation. It is an efficient algorithm that reduces the number of operations required for binary multiplication. Booth's algorithm Step 1: Initialization: The algorithm uses three registers: one for the multiplicand (M), one for the multiplier (Q), and an accumulator (A),initially set to zero. Initialise number of bits to ‘count’ variable. Step 2: Examine each bit pair of the multiplier (Q 0Q-1) and determine the appropriate operation:00 or 11: Do nothing (no operation). 01: Add the multiplicand (M) to the accumulator. 10: Subtract the multiplicand (M) from the accumulator. Step 3: Shift: After each step, the content of the registers is shifted right by one bit. Step 4: Repeat: This process is repeated for the number of bits in the multiplier. Booth's algorithm Booth's algorithm Thank You

### Related Concepts
- [[Arithmetic]]
- [[Sign -Magnitude]]
- [[ALU]]
- [[2's Complement]]
- [[Signed numbers]]
- [[Integer Arithmetic]]
