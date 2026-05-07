---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:33:28.918043'
id: 5f1d2877
links: []
modified: '2026-05-07T20:33:28.918043'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: (AX) If DF = 0, then (DI)  (DI) + 2 If DF = 1, then (DI)   (Chunk 2)
type: knowledge_chunk
---

---
chunk_id: b56d94081077
source: Module_3_Part_1.pdf
page: 2
title: (AX) If DF = 0, then (DI)  (DI) + 2 If DF = 1, then (DI)   (Chunk 2)
keywords: ['AX', 'DI', 'DF', 'AL', 'STC', 'CF', 'CLC', 'CMC', 'STD', 'DF', 'CLI', 'IF', 'NOP', 'HLT', 'Processor Control Instructions', 'Instruction Set 40', '8086 Microprocessor', 'Control Transfer Instructions', 'Instruction Set 41', 'Instruction Set 42', 'Instruction Set 43', 'Instruction Set 44']
created: 2026-05-08 02:03:28
tree_path: COA > Page 2 > (AX) If DF = 0, then (DI)  (DI) + 2 If DF = 1, th
---

(AX) If DF = 0, then (DI)  (DI) + 2 If DF = 1, then (DI)  (DI) – 2 Store byte from AL or word from AX in to string Mnemonics Explanation STC Set CF  1 CLC Clear CF  0 CMC Complement carry CF  CF / STD Set direction flag DF  1 CLD Clear direction flag DF  0 STI Set interrupt enable flag IF  1 CLI Clear interrupt enable flag IF  0 NOP No operation HLT Halt after interrupt is set 5. Processor Control Instructions Instruction Set 40 8086 Microprocessor 6. Control Transfer Instructions Instruction Set 41 8086 Microprocessor Transfer the control to a specific destination or target instruction Do not affect flags Mnemonics Explanation CALL reg / mem / disp16 Call subroutine RET Return from subroutine JMP reg / mem / disp8/ disp16 Unconditional jump  8086 Unconditional transfers 6. Control Transfer Instructions Instruction Set 42 8086 Microprocessor Checks flags If conditions are true, the program control is transferred to the new memory location in the same segment by modifying the content of IP 6. Control Transfer Instructions Instruction Set 43 8086 Microprocessor Name Alternate name JE disp8 Jump if equal JZ disp8 Jump if result is 0 JNE disp8 Jump if not equal JNZ disp8 Jump if not zero JG disp8 Jump if greater JNLE disp8 Jump if not less or equal JGE disp8 Jump if greater than or equal JNL disp8 Jump if not less JL disp8 Jump if less than JNGE disp8 Jump if not greater than or equal JLE disp8 Jump if less than or equal JNG disp8 Jump if not greater Name Alternate name JE disp8 Jump if equal JZ disp8 Jump if result is 0 JNE disp8 Jump if not equal JNZ disp8 Jump if not zero JA disp8 Jump if above JNBE disp8 Jump if not below or equal JAE disp8 Jump if above or equal JNB disp8 Jump if not below JB disp8 Jump if below JNAE disp8 Jump if not above or equal JBE disp8 Jump if below or equal JNA disp8 Jump if not above 6. Control Transfer Instructions Instruction Set 44 8086 Microprocessor Mnemonics Explanation JC disp8 Jump if CF = 1 JNC disp8 Jump if CF = 0 JP disp8 Jump if PF = 1 JNP disp8 Jump if PF = 0 JO disp8 Jump if OF = 1 JNO disp8 Jump if OF = 0 JS disp8 Jump if SF = 1 JNS disp8 Jump if SF = 0 JZ disp8 Jump if result is zero, i.e , Z = 1 JNZ disp8 Jump if result is not zero, i.e , Z = 1  8086 conditional branch instructions affecting individual flags Branch Instruction Nested Procedure Calls Addressing Modes of 8086 Why study addressing modes? Addressing modes help us to understand the types of operands and the way they are accessed while executing an instruction . What are we going to study? Addressing modes  We will see the types of addressing modes present in 8086.  We will study each addressing mode with example. Types of addressing mode in 8086 1. Immediate addressing mode 2. Direct addressing mode 3. Register addressing mode 4. Register Indirect addressing mode 5. Indexed addressing mode 6. Register relative addressing mode 7. Base plus index addressing mode 8. Base relative plus index addressing mode 1: Immediate addressing mode  In this type of mode, immediate data is part of instruction and appears in the form of successive byte or bytes MOV AX,10AB H AX 10 AB H 2: Direct addressing mode  In this type of addressing mode a 16 - bit memory address is directly specified in the instruction as a part of it. MOV AX,[5000 H ] AX Memory 5000 5001 5002 22 33 22 33 3: Register addressing mode  In this type of addressing mode, the data is stored in the register and it can be a 8 - bit or 16 - bit register. All the registers, except IP, may be used in this mode. MOV AL,BL H MOV AX,BX H AH AL AX FF 33 BX 10 AB BH BL 10 AB 4: Register Indirect addressing mode  The address of the memory location which contains data or operand is determined in a indirect way, using the offset register . MOV AX,[BX] Memory 5000 5001 5002 22 50 00 AX BX 33 22 33 Reflection Spot Q) Which addressing does instruction above belong, and why? MOV [7000H],CX Reflection Spot Q) Which addressing does instruction above belonging and why? MOV [7000H],CX Memory 7000 7001 7002 22 CX 33 Ans ) Direct addressing mode 43 56 43 56 5: Indexed addressing mode  In this addressing mode, offset of the operand is stored in one of the index registers . DS is the default segment for index register SI and DI . MOV AX,[SI] Memory 5000 5001 5002 22 50 00 AX SI 33 22 33 6: Register relative addressing mode  In this mode, the data is available at an effective address formed by adding an 8 - bit or 16 - bit displacement with the content of any one of the registers BX, BP, SI and DI in the default (either DS or ES) segment . MOV AX, 50H[BX] Memory 505 0 505 1 505 2 44 50 00 AX BX33 Offset+ 50H = 5050H Final Index Address 44 33 7: Base plus index addressing mode  In this mode the effective address is formed by adding content of a base register (any one of BX or BP) to the content of an index register (SI or DI) . Default segment register DS . MOV AX, [BX] [SI] 3000 3001 3002 10 00 AX BX = 3000H Final Index Address 20 00 SI + 12 34 12 34 8: Base relative plus index addressing mode  In the effective address is formed by adding an 8 or 16 - bit displacement with sum of contents of any one of the base registers (BX or BP) and any one of the index registers, in a default segment . MOV AX,50H[BX][SI] 3050 3051 3052 10 00 AX BX = 3050H Final Index Address 20 00 SI 12 50H + 34 12 34 What we have learnt  Different types of addressing modes present in 8086.  Location of operands with respect to different addressing modes. Summery

### Related Concepts
- [[CMC]]
- [[NOP]]
- [[IF]]
- [[Instruction Set 44]]
- [[Instruction Set 43]]
- [[Instruction Set 40]]
- [[Instruction Set 42]]
- [[Control Transfer Instructions]]
- [[Processor Control Instructions]]
- [[CLI]]
- [[8086 Microprocessor]]
- [[AX]]
- [[STC]]
- [[DI]]
- [[DF]]
- [[CF]]
- [[CLC]]
- [[AL]]
- [[HLT]]
- [[STD]]
- [[Instruction Set 41]]
