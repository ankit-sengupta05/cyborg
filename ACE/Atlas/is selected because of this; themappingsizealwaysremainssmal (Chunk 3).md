---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:37:01.708777'
id: 694edf9a
links: []
modified: '2026-05-07T20:37:01.708777'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: is selected because of this; themappingsizealwaysremainssmal (Chunk 3)
type: knowledge_chunk
---

---
chunk_id: 41030692a11b
source: WINSEM2025-26_CSE2007_ETH_AP2025264000241_2026-04-28_Reference-Material-I.pdf
page: 3
title: is selected because of this; themappingsizealwaysremainssmal (Chunk 3)
keywords: ['Clustering Index', 'Clustering Index Key', 'Index Records', 'Multilevel Index', 'B-Tree']
created: 2026-05-08 02:07:01
tree_path: DBMS > Page 3 > is selected because of this; themappingsizealwaysr
---

is selected because of this; themappingsizealwaysremainssmall . 91 92 Clustering indexing is a database indexing technique that is used to physically arrange the data in a table based on the values of the clustered indexkey. This means that the rows in the table are stored on disk in the same order astheclusteredindexkey. 93 Indexrecordscomprisesearch-keyvaluesanddatapointers. Multilevel index is stored on the disk along with the actual database files. As the size of the database grows, so does the size of the indices. There is an immense need to keeptheindexrecordsin themainmemoryso as to speedup thesearchoperations. If single-level index is used, then a large size index cannot be kept in memory which leads to multipledisk accesses. 94 Therearetwomaintypesofmultilevelindexingare: B-Tree B+ tree 95 B-treein DBMS isanm-waytreethatbalancesitself. Due to their balanced structure ,such trees are frequently used to manage and organizeenormousdatabasesand facilitatesearches. Ina B-tree,eachnodecanhavea maximumofnchildnodes. InDBMS,B-treeis an exampleof multilevelindexing . Leafnodesandinternalnodeswillbothhaverecordreferences. B-Tree is called a Balanced stored tree as all the leaf nodes are at the same levels. ThusB-treesimprove thedatabases' performance .96 97 A non-leaf node's number of keys is one less than the number of its children. Thenumberofkeysin therootrangesfromoneto(m-1) maximum. Therefore,theroothasaminimumoftwoandamaximum ofmchildren. The keys range from min([m/2]-1) to max(m-1) for all nodes (non-leaf nodes)besidestheroot.Thus,theycanhavebetweenmand[m/2] children. Thelevelofeachleafnodeis thesame. 98 Thefollowingaretheoperationsin B-Tree: Searching Insertion Deletion 99 100 Insertions are done at the leaf node level.The following algorithm needs tobefollowedin ordertoinsertanitem intoBTree. Traverse the B Tree in order to find the appropriate leaf node at which thenodecanbeinserted. If the leaf node contain less than m-1 keys then insert the element in the increasingorder. Else,iftheleafnodecontainsm-1keys,thenfollow thefollowingsteps. Insertthenewelementinthe increasingorderofelements. Splitthenodeintothetwonodesatthemedian. Pushthemedianelementuptoits parentnode. If the parent node also contain m-1 number of keys,then split it too by followingthesamesteps. 101 102 Deletion is also performed at the leaf nodes.The node which is to be deleted can either be a leafnodeor aninternal node. Following needs to befollowedinorderto deletea nodefrom a B tree. i.Locate the leaf node. ii.If thereare morethanm/2 keysintheleafnodethen deletethedesired keyfrom thenode. iii. If the leaf node doesn't contain m/2 keys then complete the keys by taking the element from eightorleftsibling. If the left sibling contains more than m/2 elements then push its largest element up to its parent and movethe intervening elementdownto the nodewherethe keyisdeleted. If the right sibling contains more than m/2 elements then push its smallest element up to theparentand moveintervening elementdownto the nodewherethe keyisdeleted. iv. If neither of the sibling contain more than m/2 elements then create a new leaf node by joiningtwo leafnodesand the interveningelementoftheparentnode. v.Ifparentis left with less than m/2nodesthen,apply the above process onthe parenttoo. 103 Delete the node 53 from the B Tree of order 5 shown in the following figure. 53 is present in the right child of element 49. Delete it. 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 ADVANTAGES DIS-ADVANTAGES •B-Trees have a guaranteed time complexity of O(log n) for basic operations like insertion, deletion, and searching, which makes them suitable for large data sets and real- timeapplications. •B-Treesareself-balancing. •High-concurrency and high- throughput. •Efficientstorageutilization.•B-Trees are based on disk-based data structures and can have a high disk usage. •Notthebestfor allcases. •For small datasets, the search time in a B-Tree might be slower compared to a binary search tree, as each node maycontainmultiplekeys. 119 TheB+treeis a balancedbinarysearchtree. It followsa multi-levelindexformat. In the B+ tree,leaf nodes denote actual data pointers.B+ tree ensures that allleafnodesremainatthesameheight. IntheB+tree,theleafnodesarelinkedusinga link list. Therefore, a B+ tree can support random access as well as sequential access. 120 IntheB+tree,everyleafnodeis atequaldistancefromtherootnode. TheB+treeis oftheordernwherenis fixedforeveryB+tree. It containsaninternalnodeandleafnode. 121 i) Internalnode An internal node of the B+ tree can contain at least n/2 record pointers excepttherootnode. Atmost,aninternalnodeofthetreecontainsnpointers. ii) Leafnode The leaf node of the B+ tree can contain at least n/2 record pointers and n/2keyvalues. Atmost,aleafnodecontainsnrecordpointerandn keyvalues. Every leaf node of the B+ treecontains one block pointer P to pointtonext leafnode. 122 Thefollowingaretheoperationsin B+Tree: Searching Insertion Deletion 123 Suppose we have to search 55 in the below B+ tree structure. First, we will fetch for theintermediarynodewhichwilldirect totheleafnodethat cancontaina recordfor55. So, in the intermediary node, we will find a branch between 50 and 75 nodes.Thenattheend,wewillberedirectedtothethirdleafnode. HereDBMS willperforma sequentialsearchto find55. 124 Suppose 60 needs to be inserted in the below structure.It will go to the 3rd leafnodeafter55. It is a balanced tree,and a leafnodeofthis treeis already full,sowe cannot insert60there. In this case, we have to split the leaf node, so that it can be inserted into treewithoutaffectingthefill factor,balanceandorder. 125 Suppose60needstobedeletedfromthebelowstructure. In this case,60 can be removed from the intermediatenode as well as from the4thleafnodetoo. If it is removed from the intermediate node, then the tree will not satisfy the rule of the B+ tree. So it needs to be modified to make it a balanced tree. 126 127 128 129 130 EXAMPLE Order:4 131 132 DELETION 133 INSERTION 134 Delete 65 from the above B+ tree Delete 70 from the above B+ treeDELETION Height of the B+ tree is always balanced and is comparatively lesser than Btree. It takesequalnumberofdiskaccessesto fetchrecords. Keysareusedfor indexing. Because the data is only stored on the leaf nodes, search queries are faster. Data storedina B+treecanbeaccessedbothsequentiallyanddirectly. 135 136

### Related Concepts
- [[Index Records]]
- [[Clustering Index Key]]
- [[Clustering Index]]
- [[B-Tree]]
- [[Multilevel Index]]
