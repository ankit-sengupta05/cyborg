---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:36:30.478375'
id: 32cc3d7a
links: []
modified: '2026-05-07T20:36:30.478375'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: 'Animated demo: http:// ats.oka.nu/b -tree/b -tree.html https (Chunk 0)'
type: knowledge_chunk
---

---
chunk_id: 526431861392
source: WINSEM2025-26_CSE2007_ETH_AP2025264000241_2026-04-22_Reference-Material-I.pdf
page: 0
title: Animated demo: http:// ats.oka.nu/b -tree/b -tree.html https (Chunk 0)
keywords: ['B-tree', 'Yael Moses', 'IDC Herzliya', 'Shweta Agrawal', 'Amit Kumar']
created: 2026-05-08 02:06:30
tree_path: DBMS > Page 0 > Animated demo: http:// ats.oka.nu/b -tree/b -tree.
---

Animated demo: http:// ats.oka.nu/b -tree/b -tree.html https://www.youtube.com/watch?v=coRJrcIYbF 4B-Trees Slide Credit : Yael Moses, IDC HerzliyaCOL 106 Shweta Agrawal, Amit Kumar Motivation •Large differences between time access to disk, cash memory and core memory •Minimize expensive access (e.g., disk access) •B-tree: Dynamic sets that is optimized for disks AB-treeis an M-way search tree with two properties : 1.It is perfectly balanced: every leaf node is at the same depth 2.Every internal node other than the root, is at least half - full, i.e. M/2-1 ≤ #keys ≤ M-1 3.Every internal node with k keys has k+1non-null children For simplicity we consider Meven and we use t=M/ 2: 2.* Every internal node other than the root is at least half - full, i.e. t-1≤ #keys ≤2t-1, t≤ #children ≤2tB-Trees Example: a 4-way B -tree B-tree 4-way tree B-tree 1. It is perfectly balanced: every leaf node is at the same depth. 2. Every node, except maybe the root, is at least half-full t-1≤ #keys ≤2t-1 3. Every internal node with k keys has k+1non-null children20 40 0 5 10 25 35 45 5520 40 0 5 25 35 45 55 10 B-tree Height Claim: any B -tree with nkeys, height hand minimum degree t satisfies: Proof : •The minimum number of KEYS for a tree with height his obtained when: –The root contains one key –All other nodes contain t-1 keys 21lognht B-Tree: Insert X 1. As in M-way tree find the leaf node to which Xshould be added 2. Add Xto this node in the appropriate place among the values already there (there are no subtrees to worry about) 3. Number of values in the node after adding the key: – Fewer than 2t-1: done – Equal to 2t: overflowed 4. Fix overflowed node Fix an Overflowed 1. Split the node into three parts, M=2t: – Left: the first t values, become a left child node – Middle : the middle value at position t, goes up to parent – Right : the last t-1 values, become a right child node 2. Continue with the parent: 1. Until no overflow occurs in the parent 2. If the root overflows, split it too, and create a new root node y…56 98 …. 60 65 68 83 86 90…56 68 98 …. 60 65 83 86 90splitJ x x y z Insert example 20 40 60 80 0 5 10 15 25 35 45 55 87 98 Insert 3: 20 40 60 80 0 3 5 10 15 25 35 45 55 3;6t M62 66 70 74 78 62 66 70 74 78 87 98 6162 66 7074 7820 40 60 80 0 3 5 10 15 25 35 45 55 Insert 61: 3;6t M62 66 70 74 78 87 98 20 40 60 80 0 3 5 10 15 25 35 45 55 87 98 74 78 61 62 66OVERFLOW 20 40 60 70 80 0 3 5 10 15 25 35 45 55 87 98SPLIT IT Insert 38: 74 78 61 626620 40 60 70 80 0 3 5 1015 25 35 45 55 87 98 74 78 6162 6620 40 60 70 80 0 3 5 10 15 25 35 38 45 55 87 98 3;6t M 5 20 40 60 7080Insert 4: 0 3 4 2535 38 45 55 616266 87 98 74 78 10 1574 78 61626620 40 60 70 80 0 3 4 5 101525 35 38 45 55 87 98 74 78 61 626620 40 60 70 80 25 35 38 45 55 87 98 OVERFLOW0 3 5 10 15 SPLIT ITOVERFLOW SPLIT IT 3;6t M 0 3 4 25 35 38 45 55 6162 66 87 98 74 7860 5 20 40 70 80 10155 20 40 60 70 80 0 3 4 2535 38 45 55 6162 66 87 98 74 78 10 15OVERFLOW SPLIT IT 3;6t M Complexity Insert •Inserting a key into a B -tree of height h is done in a single pass down the tree and a single pass up the tree Complexity : ) (log )( n OhOt B-Tree: Delete X •Delete as in M -way tree •A problem: –might cause underflow : the number of keys remain in a node < t-1 Recall: The root should have at least 1value in it, and all other nodes should have at least t-1values in them 0 3 4 25 3538 45 55 61 62 66 87 98 74 7860 5 20 40 70 80 10 15 3;6t MUnderflow Example Delete 87: 0 3 4 2535 38 45 55 616266 98 74 7860 5 20 40 70 80 10 15B-tree UNDERFLOW B-Tree: Delete X,k •Delete as in M -way tree •A problem: –might cause underflow : the number of keys remain in a node < t-1 •Solution: –make sure a node that is visited has at least t instead of t-1 keys. –If it doesn ’t have k •(1) either take from sibling via a rotate, or •(2) merge with the parent –If it does have k •See next slides Recall: The root should have at least 1value in it, and all other nodes should have at least t-1 (at most 2t -1)values in them 62 66 70 74 62 70 74B-Tree -Delete( x,k) 1st case: kis in xand xis aleaf delete k How many keys are left?k=66 Example t= 3x x 30 50 70 90 35 40 4530 45 70 90 35 40 455 6 7 5 6 7 Example t= 3k=50 x x yy 35 40 55 60 35 40 50 55 652nd case cont .: c.Both aand bare not satisfied: y and zhave t-1 keys –Merge the two children, y and z –Recursively delete kfrom the merged cell 30 50 70 9030 70 90 1 2 3 5 4 6 1 2 3 5 4 6 Example t= 3x y zx y Questions •When does the height of the tree shrink? •Why do we need the number of keys to be at least t and not t-1when we proceed down in the tree? Copyright © The McGraw -Hill Companies, Inc. Permission required for reproduction or display. Delete Complexity •Basically downward pass: –Most of the keys are in the leaves –one downward pass –When deleting a key in internal node –may have to go one step up to replace the key with its predecessor or successor Complexity ) (log )( n OhOt Run Time Analysis of B-Tree Operations •For a B -Tree of order M=2t –#keys in internal node: M-1 –#children of internal node: between M/2and M –Depth of B-Tree storing nitems is O(logM/2N) •Find run time is: –O(log M) to binary search which branch to take at each node, since M is constant it is O(1). –Total time to find an item is O(h*log M) = O(log n ) •Insert & Delete –Similar to find but update a node may take : O(M )=O( 1) Note: if M is > 32 it worth using binary search at each node Copyright © The McGraw -Hill Companies, Inc. Permission required for reproduction or display. A typical B -Tree Why B -Tree? •B-trees is an implementation of dynamic sets that is optimized for disks –The memory has an hierarchy and there is a tradeoff between size of units/blocks and access time –The goal is to optimize the number of times needed to access an “expensive access time memory ” –The size of a node is determined by characteristics of the disk –block size –page size –The number of access is proportional to the tree depth

### Related Concepts
- [[Amit Kumar]]
- [[Shweta Agrawal]]
- [[B-tree]]
- [[IDC Herzliya]]
- [[Yael Moses]]
