---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:32:39.193291'
id: 116d4ccf
links: []
modified: '2026-05-07T20:32:39.193291'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: erased and reprogrammed about ten thousand times . Both era (Chunk 1)
type: knowledge_chunk
---

---
chunk_id: b14b06698664
source: Moduel_5.pdf
page: 1
title: erased and reprogrammed about ten thousand times . Both era (Chunk 1)
keywords: ['EEPROMs', 'FLASH ROM', 'Android devices', 'Custom ROM', 'Cache Memory', 'CPU']
created: 2026-05-08 02:02:39
tree_path: COA > Page 1 > erased and reprogrammed about ten thousand times .
---

erased and reprogrammed about ten thousand times . Both erasing and programming take about 4 to 10 ms(millisecond). EEPROMs can be erased one byte at a time, rather than erasing the entire chip. Hence, the process of reprogramming is flexible but slow . The method of erasure is electrical and immediate. FLASH ROM FLASH ROM are used for android devices . There is also something called as custom rom . It will provide you better functionality, user interface, features and more . Many android users are going for custom roms, as they help them change the look and feel however they want. CACHE MEMORY 1 What is Cache Memory?  Cache memory is a small, high-speed RAM buffer located between the CPU and main memory.  Cache memory holds a copy of the instructions (instruction cache) or data (operand or data cache) currently being used by the CPU.  The main purpose of a cache is to accelerate your computer while keeping the price of the computer low. 2 Placement of Cache in computer 3 Hit Ratio  The ratio of the total number of hits divided by the total CPU accesses to memory (i.e. hits plus misses) is called Hit Ratio.  Hit Ratio = Total Number of Hits / (Total Number of Hits + Total Number of Miss) 4 Example 5 A system with 512 x 12 cache and 32 K x 12 of main memory. Types of Cache Mapping 1. Direct Mapping 2. Associative Mapping 3. Set Associative Mapping 6 1. Direct Mapping  The direct mapping technique is simple and inexpensive to implement.  When the CPU wants to access data from memory, it places a address. The index field of CPU address is used to access address.  The tag field of CPU address is compared with the associated tag in the word read from the cache.  If the tag-bits of CPU address is matched with the tag-bits of cache, then there is a hit and the required data word is read from cache.  If there is no match, then there is a miss and the required data word is stored in main memory. It is then transferred from main memory to cache memory with the new tag. 7 1. Direct Mapping 8 1. Direct Mapping 9 2. Associative Mapping  An associative mapping uses an associative memory.  This memory is being accessed using its contents.  Each line of cache memory will accommodate the address (main memory) and the contents of that address from the main memory.  That is why this memory is also called Content Addressable Memory (CAM). It allows each block of main memory to be stored in the cache. 10 2. Associative Mapping 11 3. Set Associative Mapping  That is the easy control of the direct mapping cache and the more flexible mapping of the fully associative cache.  In set associative mapping, each cache location can have more than one pair of tag + data items.  That is more than one pair of tag and data are residing at the same location of cache memory. If one cache location is holding two pair of tag + data items, that is called 2-way set associative mapping . 12 3. Two-Way Set Associative Mapping 13 Replacement Algorithms of Cache Memory  Replacement algorithms are used when there are no available space in a cache in which to place a data. Four of the most common cache replacement algorithms are described below:  Least Recently Used (LRU):  The LRU algorithm selects for replacement the item that has been least recently used by the CPU.  First-In-First-Out (FIFO):  The FIFO algorithm selects for replacement the item that has been in the cache from the longest time.  Least Frequently Used (LRU):  The LRU algorithm selects for replacement the item that has been least frequently used by the CPU.  Random:  The random algorithm selects for replacement the item randomly. 14 Writing into Cache  When memory write operations are performed, CPU first writes into the cache memory. These modifications made by CPU during a write operations, on the data saved in cache, need to be written back to main memory or to auxiliary memory.  These two popular cache write policies (schemes) are:  Write-Through  Write-Back 15 Write-Through  In a write through cache, the main memory is updated each time the CPU writes into cache.  The advantage of the write-through cache is that the main memory always contains the same data as the cache contains.  This characteristic is desirable in a system which uses direct memory access scheme of data transfer. The I/O devices communicating through DMA receive the most recent data. 16 Write-Back  In a write back scheme, only the cache memory is updated during a write operation.  The updated locations in the cache memory are marked by a flag so that later on, when the word is removed from the cache, it is copied into the main memory.  The words are removed from the cache time to time to make room for a new block of words. 17

### Related Concepts
- [[CPU]]
- [[EEPROMs]]
- [[Android devices]]
- [[Custom ROM]]
- [[Cache Memory]]
- [[FLASH ROM]]
