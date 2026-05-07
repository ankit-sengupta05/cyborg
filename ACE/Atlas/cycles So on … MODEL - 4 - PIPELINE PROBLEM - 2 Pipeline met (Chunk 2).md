---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:34:34.252826'
id: 3037191b
links: []
modified: '2026-05-07T20:34:34.252826'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: 'cycles So on … MODEL - 4 : PIPELINE PROBLEM - 2 Pipeline met (Chunk 2)'
type: knowledge_chunk
---

---
chunk_id: 929af7deaccd
source: Pipeline-problems_1.pdf
page: 2
title: cycles So on … MODEL - 4 : PIPELINE PROBLEM - 2 Pipeline met (Chunk 2)
keywords: ['Model 4', 'Pipeline Problem', 'Pipeline method', 'Instruction structure', 'Problem 1', 'Pipeline', 'Problem 5']
created: 2026-05-08 02:04:34
tree_path: COA > Page 2 > cycles So on … MODEL - 4 : PIPELINE PROBLEM - 2 Pi
---

cycles So on … MODEL - 4 : PIPELINE PROBLEM - 2 Pipeline method F F D E E E E E E F F D E E E E E E 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 No of Clock Cycle required to execute 100 instructions is = (No of clocks required for 1st instruction)+ ((no of instruction - 1) x (difference between two instruction)) = 9 + ((100 - 1) x 6) = 9 + (99 x 6) = 9 + 594 = 603 Clock cycles No of Clock Cycle So on … I F (2) D (1) E (6) MODEL - 4 : PIPELINE PROBLEM - 2 Pipeline method F F D Ex1 Ex1 Ex1 Ex2 Ex2 Ex2 F F D Ex1 Ex1 Ex1 Ex2 Ex2 Ex2 0 1 2 3 4 5 6 7 8 9 10 11 12 No of Clock Cycle required to execute 100 instructions is = (No of clocks required for 1st instruction)+ ((no of instruction - 1) x (difference between two instruction)) = 9 + ((100 - 1) x 3) = 9 + (99 x 3) = 9 + 297 = 306 Clock cycles No of Clock Cycle So on … I F(2) D(1) Ex1 (3) Ex2 (3) Problem - 1: Find the number of clock cycles required to execute 5432 instructions with pipeline method and without pipeline method for the following instruction structure ? Improve the pipeline structure . MODEL - 4 : PIPELINE PROBLEM ASSIGNMENT - 1 I F (2) D (1) E (8) I1 I2 I3 I4 I5 I6 I7 I8 I9 I10 Fetch - 2 Clock cycle Decoding - 1 Clock cycle Execution - 8 Clock cycle MODEL - 5 PROBLEMS Problem - : Consider a pipeline having 4 phases with duration 60, 50, 90 and 80 ns. Given latch delay is 10 ns. Calculate - 1. Pipeline cycle time 2. Non - pipeline execution time 3. Speed up ratio 4. Pipeline time for 1000 instructions 5. Sequential time for 1000 instructions 6. Throughput Given - o Four stage pipeline is used o Delay of stages = 60, 50, 90 and 80 ns o Latch delay or delay due to each register = 10 ns Solution: S1 S2 S3 S4 60ns 5 0ns 90ns 80ns Non - Pipelined Architecture S1 S2 S3 S4 Latch 60ns 5 0ns 90ns 80ns 10ns Latch 10ns Latch 10ns Latch 10ns Pipelined Architecture Every stage output will be saved in the Latch or register Note: In any stage of pipeline, the output of each stage will be moved to the next state after the 100 ns (max(60,50,90,80) + 10 ns) Part - 01: Pipeline Cycle Time - Cycle time = Maximum delay due to any stage + Delay due to its register = Max { 60, 50, 90, 80 } + 10 ns = 90 ns + 10 ns = 100 ns Part - 02: Non - Pipeline Execution Time - Non - pipeline execution time for one instruction = 60 ns + 50 ns + 90 ns + 80 ns = 280 ns Part - 03: Speed Up Ratio - Speed up = Non - pipeline execution time / Pipeline execution time = 280 ns / Cycle time = 280 ns / 100 ns = 2.8 Part - 04: Pipeline Time For 1000 Instructions - Pipeline time for 1000 instructions = Time taken for 1st instruction + Time taken for remaining 999 instructions = 1 x 4 clock cycles + 999 x 1 clock cycle = 4 x cycle time + 999 x cycle time = 4 x 100 ns + 999 x 100 ns = 400 ns + 99900 ns = 100300 ns Part - 05: Sequential Time For 1000 Instructions - Non - pipeline time for 1000 tasks = 1000 x Time taken for one instruction = 1000 x 280 ns = 280000 ns Part - 06: Throughput - Throughput for pipelined execution = Number of instructions executed per unit time = 1000 instructions / 100300 ns

### Related Concepts
- [[Instruction structure]]
- [[Problem 1]]
- [[Problem 5]]
- [[Model 4]]
- [[Pipeline method]]
- [[Pipeline Problem]]
- [[Pipeline]]
