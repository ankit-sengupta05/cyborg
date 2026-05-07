---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:34:15.241543'
id: 6ef4ad6b
links: []
modified: '2026-05-07T20:34:15.241543'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: PRA C TICE PROBLEMS BASED ON SE T ASSOCI A TIVE M APPING- Pr (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: 263c929370be
source: numerical.pdf
page: 0
title: PRA C TICE PROBLEMS BASED ON SE T ASSOCI A TIVE M APPING- Pr (Chunk 0)
keywords: ['Problem 01', 'Cache size', 'Block size', 'Main memory size', 'Physical address', 'Tag directory size', 'Problem 02']
created: 2026-05-08 02:04:15
tree_path: COA > Page 0 > PRA C TICE PROBLEMS BASED ON SE T ASSOCI A TIVE M 
---

PRA C TICE PROBLEMS BASED ON SE T ASSOCI A TIVE M APPING- Pr oblem-01: Consider a 2-way set associative mapped cache of size 16 KB with block size 256 bytes. The size of main memory is 128 KB. Find- 1. Number of bits in tag 2. T ag directory size Solution- Given- Set size = 2 Cache memory size = 16 KB Block size = Frame size = Line size = 256 bytes Main memory size = 128 KB W e consider that the memory is byte addressable. Number of Bits in Physical Addr ess- W e have, Size of main memory = 128 KB = 2 17 bytes Thus, Number of bits in physical address = 17 bits Number of Bits in Block Offset- W e have, Block size = 256 bytes = 2 8 bytes Thus, Number of bits in block of fset = 8 bits Number of Lines in Cache- T otal number of lines in cache = Cache size / Line size = 16 KB / 256 bytes = 2 14 bytes / 2 8 bytes = 64 lines Thus, Number of lines in cache = 64 lines Number of Sets in Cache- T otal number of sets in cache = T otal number of lines in cache / Set size = 64 / 2 = 32 sets = 2 5 sets Thus, Number of bits in set number = 5 bits Number of Bits in T ag- Number of bits in tag = Number of bits in physical address – (Number of bits in set number + Number of bits in block of fset) = 17 bits – (5 bits + 8 bits) = 17 bits – 13 bits = 4 bits Thus, Number of bits in tag = 4 bits T ag Dir ect or y Siz e- T ag directory size = Number of tags x T ag size = Number of lines in cache x Number of bits in tag = 64 x 4 bits = 256 bits = 32 bytes Thus, size of tag directory = 32 bytes Pr oblem-02: Consider a 8-way set associative mapped cache of size 512 KB with block size 1 KB. There are 7 bits in the tag. Find- 1. Size of main memory 2. T ag directory size Solution- Given- Set size = 8 Cache memory size = 512 KB Block size = Frame size = Line size = 1 KB Number of bits in tag = 7 bits W e consider that the memory is byte addressable. Number of Bits in Block Offset- W e have, Block size = 1 KB = 2 10 bytes Thus, Number of bits in block of fset = 10 bits Number of Lines in Cache- T otal number of lines in cache = Cache size / Line size = 512 KB / 1 KB = 512 lines Thus, Number of lines in cache = 512 lines Number of Sets in Cache- T otal number of sets in cache = T otal number of lines in cache / Set size = 512 / 8 = 64 sets = 2 6 sets Thus, Number of bits in set number = 6 bits Number of Bits in Physical Addr ess- Number of bits in physical address = Number of bits in tag + Number of bits in set number + Number of bits in block of fset = 7 bits + 6 bits + 10 bits = 23 bits Thus, Number of bits in physical address = 23 bits Siz e of Main Memor y- W e have, Number of bits in physical address = 23 bits Thus, Size of main memory = 2 23 bytes = 8 MB T ag Dir ect or y Siz e- T ag directory size = Number of tags x T ag size = Number of lines in cache x Number of bits in tag = 512 x 7 bits = 3584 bits = 448 bytes Thus, size of tag directory = 448 bytes Pr oblem-03: Consider a 4-way set associative mapped cache with block size 4 KB. The size of main memory is 16 GB and there are 10 bits in the tag. Find- 1. Size of cache memory 2. T ag directory size Solution- Given- Set size = 4 Block size = Frame size = Line size = 4 KB Main memory size = 16 GB Number of bits in tag = 10 bits W e consider that the memory is byte addressable. Number of Bits in Physical Addr ess- W e have, Size of main memory = 16 GB = 2 34 bytes Thus, Number of bits in physical address = 34 bits Number of Bits in Block Offset- W e have, Block size = 4 KB = 2 12 bytes Thus, Number of bits in block of fset = 12 bits Number of Bits in Set Number- Number of bits in set number = Number of bits in physical address – (Number of bits in tag + Number of bits in block of fset) = 34 bits – (10 bits + 12 bits) = 34 bits – 22 bits = 12 bits Thus, Number of bits in set number = 12 bits Number of Sets in Cache- W e have- Number of bits in set number = 12 bits Thus, T otal number of sets in cache = 2 12 sets Number of Lines in Cache- W e have- T otal number of sets in cache = 2 12 sets Each set contains 4 lines Thus, T otal number of lines in cache = T otal number of sets in cache x Number of lines in each set = 2 12 x 4 lines = 2 14 lines Siz e of Cache Memor y- Size of cache memory = T otal number of lines in cache x Line size = 2 14 x 4 KB = 2 16 KB = 64 MB Thus, Size of cache memory = 64 MB T ag Dir ect or y Siz e- T ag directory size = Number of tags x T ag size = Number of lines in cache x Number of bits in tag = 2 14 x 10 bits = 163840 bits = 20480 bytes = 20 KB Thus, size of tag directory = 20 KB Pr oblem-04: Consider a 8-way set associative mapped cache. The size of cache memory is 512 KB and there are 10 bits in the tag. Find the size of main memory . Solution- Given- Set size = 8 Cache memory size = 512 KB Number of bits in tag = 10 bits W e consider that the memory is byte addressable. Let- Number of bits in set number field = x bits Number of bits in block of fset field = y bits Sum of Number Of Bits Of Set Number Field A nd Block Offset Field- W e have, Cache memory size = Number of sets in cache x Number of lines in one set x Line size Now , substituting the values, we get- 512 KB = 2 x x 8 x 2 y bytes 2 19 bytes = 2 3+x+y bytes 19 = 3 +x + y x + y = 19 – 3 x + y = 16 Number of Bits in Physical Addr ess- Number of bits in physical address = Number of bits in tag + Number of bits in set number + Number of bits in block of fset = 10 bits + x bits + y bits = 10 bits + (x + y) bits = 10 bits + 16 bits = 26 bits Thus, Number of bits in physical address = 26 bits Siz e of Main Memor y- W e have, Number of bits in physical address = 26 bits Thus, Size of main memory = 2 26 bytes = 64 MB Thus, size of main memory = 64 MB Pr oblem-05: Consider a 4-way set associative mapped cache. The size of main memory is 64 MB and there are 10 bits in the tag. Find the size of cache memory . Solution- Given- Set size = 4 Main memory size = 64 MB Number of bits in tag = 10 bits W e consider that the memory is byte addressable. Number of Bits in Physical Addr ess- W e have, Size of main memory = 64 MB = 2 26 bytes Thus, Number of bits in physical address = 26 bits Sum Of Number Of Bits Of Set Number Field A nd Block Offset Field- Let- Number of bits in set number field = x bits Number of bits in block of fset field = y bits Then, Number of bits in physical address = Number of bits in tag + Number of bits in set number + Number of bits in block of fset So, we have- 26 bits = 10 bits + x bits + y bits 26 = 10 + (x + y) x + y = 26 – 10 x + y = 16 Thus, Sum of number of bits of set number field and block of fset field = 16 bits Siz e of Cache Memor y- Cache memory size = Number of sets in cache x Number of lines in one set x Line size = 2 x x 4 x 2 y bytes = 2 2+x+y bytes = 2 2+16 bytes = 2 18 bytes = 256 KB Thus, size of cache memory = 256 KB

### Related Concepts
- [[Tag directory size]]
- [[Physical address]]
- [[Problem 02]]
- [[Block size]]
- [[Main memory size]]
- [[Cache size]]
- [[Problem 01]]
