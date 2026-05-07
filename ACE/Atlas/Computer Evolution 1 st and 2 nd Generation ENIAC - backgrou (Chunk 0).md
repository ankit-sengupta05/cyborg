---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:32:25.436928'
id: 40dc839a
links: []
modified: '2026-05-07T20:32:25.436928'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: Computer Evolution 1 st and 2 nd Generation ENIAC - backgrou (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: b12c8ab93e7c
source: Ias machine.pdf
page: 0
title: Computer Evolution 1 st and 2 nd Generation ENIAC - backgrou (Chunk 0)
keywords: ['ENIAC', 'John Mauchly', 'J. Presper Eckert', 'University of Pennsylvania', 'Ballistic Research Laboratory', 'Princeton IAS', 'Von Neumann', 'IAS', 'CA', 'CC']
created: 2026-05-08 02:02:25
tree_path: COA > Page 0 > Computer Evolution 1 st and 2 nd Generation ENIAC 
---

Computer Evolution 1 st and 2 nd Generation ENIAC - background • Electronic Numerical Integrator And Computer (ENIAC) • John Mauchly and J. Presper Eckert • University of Pennsylvania • Ballistic Research Laboratory • calculate artillery firing tables of US Army • Started 1943 • Finished 1946 • Too late for war effort • Used until 1955 ENIAC - details • Decimal (not binary) • 20 accumulators of 10 digits • Programmed manually by switches • 30 tons • 15,000 square feet • 140 kW power consumption • 5,000 additions per second V on Neumann/Turing • Stored Program concept • Main memory storing programs and data • ALU operating on binary data • Control unit interpreting instructions from memory and executing • Input and output equipment operated by control unit • Princeton Institute for Advanced Studies ( IAS ) • Completed 1952 Structure of von Neumann machine CA: Central Arithmetic CC: Central Control IAS – Memory format • 4096 x 40 bit words • Binary number Main memory • 2 x 20 bit instructions Institute for Advanced Study Structure of IAS – detail • Set of registers (storage in CPU) • Memory Buffer Register • Memory Address Register • Instruction Register • Instruction Buffer Register • Program Counter • Accumulator • Multiplier Quotient • Memory buffer register (MBR) : Contains a word to be stored in memory or sent to the I/O unit, or is used to receive a word from memory or from the I/O unit . • Memory address register (MAR) : Specifies the address in memory of the word to be written from or read into the MBR . • Instruction register (IR) : Contains the 8 - bit opcode instruction being executed . • Instruction buffer register (IBR) : Employed to hold temporarily the right hand instruction from a word in memory . • Program counter (PC) : Contains the address of the next instruction - pair to be fetched from memory . • Accumulator (AC) and multiplier quotient (MQ) : Employed to hold temporarily operands and results of ALU operations . For example, the result of multiplying two 40 - bit numbers is an 80 - bit number ; the most significant 40 bits are stored in the AC and the least significant in the MQ . Instruction cycle Explanation of instruction cycle • The IAS operates by repetitively performing an instruction cycle, as shown in l ast Figure. Each instruction cycle consists of two subcycles . • During the fetch cycle, the opcode of the next instruction is loaded into the IR and the address portion is loaded into the MAR . This instruction may be taken from the IBR, or it can be obtained from memory by loading a word into the MBR, and then down to the IBR, IR , and MAR . • Once the opcode is in the IR, the execute cycle is performed . • Control circuitry interprets the opcode and executes the instruction by sending out the appropriate control signals to cause data to be moved or an operation to be performed by the ALU . IAS Instruction set (21 instructions) The IAS computer had a total of 21 instructions, which are listed in Table. These can be grouped as follows: • Data transfer : Move data between memory and ALU registers or between two ALU registers . • Unconditional branch : Normally , the control unit executes instructions in sequence from memory . This sequence can be changed by a branch instruction, which facilitates repetitive operations . • Conditional branch : The branch can be made dependent on a condition, thus allowing decision points . • Arithmetic : Operations performed by the ALU . • Address modify : Permits addresses to be computed in the ALU and then inserted into instructions stored in memory . This allows a program considerable addressing flexibility . Example of addition 1. LOAD M(X) 500, ADD M(X) 501 (PC=1) • MAR<PC • MBR<M[MAR] • IBR<MBR[20:39] • IR<MBR[0:7] • MAR<MBR[8:19] • MBR<M[MAR] • AC<MBR • IR<IBR[0:7] • MAR<IBR[8:19] • PC<PC+1 • MBR<M[MAR] • AC<AC+MBR 2. STOR M(X) 500, Other instruction (PC=2) • MAR<PC • MBR<M[MAR] • IBR<MBR[20:39] • IR<MBR[0:7] • MAR<MBR[8:19] • MBR<AC • M[MAR]<MBR P1 P2 P3 P1 P2 P3 Answer P1 This program will store the absolute value of content at memory location 0FA into memory location 0FB. P2 First, the CPUmust make access memory tofetch the instruction .The instruction contains the address ofthe data wewant toload .During the execute phase accesses memory toload thedata value located atthat address foratotal oftwo trips tomemory . OPCODE OPERAND 00000001 000000000010 Answer P3 The vectors A,B,and Careeach stored in 1,000 continuous locations inmemory, beginning atlocations 1001 ,2001 ,and 3001 ,respectively .The program begins with the left half of location 3.Acounting variable N isset to999 and decremented after each step until itreaches -1. Thus, the vectors are processed from high location to low location . Example 3 main () { inta=15, b=5, c; if (a >= b) c = a –b; else c = a + b; }0 15 a 1 5 b 2 c 3 begin 4 . If (a >=b) 4 load M(0) 5 sub M(1) 6 jump+ M(8) 7 jump M(12) 8 .true, c=a -b 8 load M(0) 9 sub M(1) 10 stor M(2) 11 jump M(15) 12 .false c = a+b 12 load M(0) 13 add M(1) 14 stor M(2) 15 halt Example 3 (continued) •Optimized0 15 a 1 5 b 2 c 3 begin 4 load M(0) 5 sub M(1) 6 jump+ M(9) 7 load M(0) 8 add M(1) 9 stor M(2) 10 haltmain () { int a=15, b=5, c; if (a >= b) c = a –b; else c = a + b; } Example3 ( with a > b) main () { inta=15, b=5, c; if (a > b) c = a –b; else c = a + b; }0 15 a 1 5 b 2 c 3 1 4 begin 5 . a > b 5 load M(0) 6 sub M(1) 7 sub M(3) 8 jump+ M(10) 9 jump M(14) 10 . True, c = a -b 10 load M(0) 11 sub M(1) 12 stor M(2) 13 jump M(17) 14 . False, c = a + b 14 load M(0) 15 add M(1) 16 stor M(2) 17 halt Example 6 main () { inta=2, b=2, I; I = 1; while (I < 10) { a = a +b; I = I +1; } }Give it a try. Example 6 (continued) main () { int a=2, b=2, I; I = 1; while (I < 10) { a = a +b; I = I +1; } }0 1 1 10 2 2 a 3 2 b 4 i 5 begin 6 . I =1 7 load M(0) 8 storM(4) 9 . while (I < 10) 10 load M(4) 11 sub M(1) 12 jump+ M(22) 13 . a = a +b 14 load M(2) 15 add M(3) 16 storM(2) 17 . I=I+1 18 load M(4) 19 add M(0) 20 storM(4) 21 jump M(10) 22 halt

### Related Concepts
- [[Ballistic Research Laboratory]]
- [[IAS]]
- [[John Mauchly]]
- [[University of Pennsylvania]]
- [[CC]]
- [[CA]]
- [[Von Neumann]]
- [[ENIAC]]
- [[Princeton IAS]]
- [[J. Presper Eckert]]
