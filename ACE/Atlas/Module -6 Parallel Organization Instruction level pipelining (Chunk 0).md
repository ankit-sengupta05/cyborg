---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:34:04.358852'
id: 115f64ea
links: []
modified: '2026-05-07T20:34:04.358852'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: Module -6 Parallel Organization Instruction level pipelining (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: 24f900fda71f
source: Module_6.pdf
page: 0
title: Module -6 Parallel Organization Instruction level pipelining (Chunk 0)
keywords: ['Module-6', 'Superscalar processors', 'T1-T8', 'IF1-IF4', 'Pipeline', 'Multiprocessor systems', 'Single processor systems', 'Multiprocessor architecture', 'Loosely Coupled MP', 'Tightly Coupled MP']
created: 2026-05-08 02:04:04
tree_path: COA > Page 0 > Module -6 Parallel Organization Instruction level 
---

Module -6 Parallel Organization Instruction level pipelining and Superscalar processors T1 T2 T3 T4 T5 T6 T7 T8 IF1 ID1 OF1 EX1 WR1 IF2 ID2 OF2 EX2 WR2 PIPELINE STALL OF2 EX2 WR2 T1 T2 T3 T4 T5 T6 T7 T8 IF1 ID1 OF1 EX1 WR1 IF2 IF3 IF4 ID4 OF4 EX4 WR4 T1 T2 T3 T4 T5 T6 T7 T8 IF1 ID1 OF1 EX1 WR1 IF2 ID2 OF2 EX2 WR2 IF3 ID3 OF3 EX3 WR3 IF4 ID4 OF4 EX4 WR4 T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11 IF1 ID1 OF1 EX1 WR1 PIPE IF2 ID2 OF2 EX2 WR2 LINE IF3 ID3 OF3 EX3 WR3 BUBBLE IF4 ID4 OF4 EX4 WR4FLUSH THESE 3 INSTRUCTIONS Scalar to Superscalar pipeline Diversified Pipeline Multiprocessor systems Most computer systems aresingle processor systems i.ethey only have one processor .However, multiprocessor orparallel systems are increasing inimportance nowadays .These systems have multiple processors working inparallel that share thecomputer clock, memory, bus, peripheral devices etc.Animage demonstrating themultiprocessor architecture isMultiprocessor systems Loosely Coupled Multiprocessor system ⮚Itisatype ofmultiprocessing system inwhich, There isdistributed memory instead ofshared memory . ⮚Inloosely coupled multiprocessor system, data rate islower than tightly coupled multiprocessor system . ⮚Inloosely coupled multiprocessor system, modules are connected through MTS (Message transfer system )network . Loosely Coupled Multiprocessor system Loosely Coupled Multiprocessor system Channel and Arbiter Switch Tightly Coupled Multiprocessor system ⮚Itisatype ofmultiprocessing system inwhich there isshared memory . ⮚Intightly coupled multiprocessor system, data rate ishigher than loosely coupled multiprocessor system . ⮚These systems share theclock generator, buscontrol logic and entire I/Osystems between them . ⮚Intightly coupled multiprocessor system, modules are connected through PMIN, IOPIN and ISIN networks . Tightly Coupled Multiprocessor system Differences Loosely coupled Tightly coupled There is distributed memory in loosely coupled multiprocessor systemThere is shared memory, in tightly coupled multiprocessor system Has low data rate Has high data rate The cost of this system is less It is more costly Modules are connected through Message transfer system networkWhile there is PMIN, IOPIN and ISIN networks Memory conflicts don’t take place This system have memory conflicts It has low degree of interaction between tasks It has high degree of interaction between tasks there is direct connection between processor and I/O devicesIOPIN helps connection between processor and I/O devices Applications of loosely coupled multiprocessor are in distributed computing systemsApplications of tightly coupled multiprocessor are in parallel processing systems Symmetric Multiprocessor system ⮚SMP systems have centralized shared memory called main memory (MM) operating under a single operating system with two ormore homogeneous processors . ⮚Usually each processor has anassociated private high -speed memory known ascache memory (orcache) tospeed upthemain memory data access and toreduce thesystem bus traffic . ⮚Processors may beinterconnected using buses, crossbar switches oron-chip mesh networks . ⮚The bottleneck inthescalability ofSMP using buses orcrossbar switches isthebandwidth and power consumption ofthe interconnect among the various processors, the memory, and thedisk arrays . ⮚Mesh architectures avoid these bottlenecks ,and provide nearly linear scalability tomuch higher processor counts atthesacrifice ofprogrammability Symmetric Multiprocessor system ⮚SMP systems allow any processor to work onany task nomatter where the data forthat task islocated in memory, provided that each task in the system isnot inexecution on two ormore processors atthesame time . ⮚With proper operating system support, SMP systems can easily move tasks between processors tobalance the workload efficiently . UMA ⮚UMA stands forUniform Memory Access ;itisashared memory architecture forthemultiprocessors . ⮚Single memory controller isused and accessed byalltheprocessors with thehelp oftheinterconnection network . ⮚Each processor has equal memory accessing time (latency) and access speed . ⮚Itcan employ either ofthe single bus, multiple bus orcrossbar switch . ⮚Asitprovides balanced shared memory access, itisalso known asSMP (Symmetric multiprocessor) systems . ⮚Uniform Memory Access isslower than non-uniform Memory Access . ⮚Uniform Memory Access haslimited bandwidth . ⮚Uniform Memory Access isapplicable for general purpose applications and time -sharing applications . ⮚Inuniform Memory Access, memory access time isbalanced orequal . NUMA ⮚NUMA stands forNon -Uniform Memory Access ;itisamultiprocessor model in which each processor isconnected with adedicated memory . ⮚However, these small parts ofthe memory combine tomake asingle address space . ⮚Unlike UMA, the access time ofthe memory relies onthe distance where the processor isplaced🡪which means varying memory access time . ⮚Itallows access toany ofthememory location byusing thephysical address . ⮚NUMA isintended toincrease the available bandwidth tothe memory and for which ituses multiple memory controllers . ⮚Itcombines numerous machine cores into “nodes ”where each core hasamemory controller . ⮚Toaccess the local memory inaNUMA machine the core retrieves the memory managed bythememory controller byitsnode . ⮚While toaccess the remote memory which ishandled bythe other memory controller, thecore sends thememory request through theinterconnection links .

### Related Concepts
- [[Multiprocessor systems]]
- [[T1-T8]]
- [[Loosely Coupled MP]]
- [[Tightly Coupled MP]]
- [[Multiprocessor architecture]]
- [[Single processor systems]]
- [[Module-6]]
- [[Pipeline]]
- [[Superscalar processors]]
- [[IF1-IF4]]
