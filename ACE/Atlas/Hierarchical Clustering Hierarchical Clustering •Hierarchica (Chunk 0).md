---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:42:17.776449'
id: 6f851beb
links: []
modified: '2026-05-07T20:42:17.776449'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: Hierarchical Clustering Hierarchical Clustering •Hierarchica (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: 1faed5306e64
source: WINSEM2025-26_CSE3008_ETH_AP2025264000479_2026-04-25_Reference-Material-I.pdf
page: 0
title: Hierarchical Clustering Hierarchical Clustering •Hierarchica (Chunk 0)
keywords: ['Hierarchical Clustering', 'Dendrogram', 'Agglomerative', 'Divisive', 'Clustering Ensemble', 'AGNES', 'DIANA']
created: 2026-05-08 02:12:17
tree_path: ML > Page 0 > Hierarchical Clustering Hierarchical Clustering •H
---

Hierarchical Clustering Hierarchical Clustering •Hierarchical clustering is another unsupervised machine learning algorithm. •The hierarchy of clusters in the form of a tree , and this tree -shaped structure is known as the dendrogram . •There is no requirement to predetermine the number of clusters. Introduction Hierarchical Clustering Approach Types •Agglomerative :Agglomerative isabottom -upapproach, inwhich the algorithm starts bytaking alldata points assingle clusters andmerging them until onecluster isleft. •Divisive: Divisive algorithm is the reverse of the agglomerative algorithm as it is a top -down approach. Introduction •Agglomerative vs. Divisive –Agglomerative: a bottom -up strategy ▪Initially each data object is in its own (atomic) cluster ▪Then merge these atomic clusters intolarger andlarger clusters –Divisive: a top -down strategy ▪Initially all objects are in one single cluster ▪Then the cluster is subdivided into smaller and smaller clusters •Clustering Ensemble –Using multiple clustering results for robustness and overcoming weaknesses of single clustering algorithms. Introduction: Illustration •Illustrative Example: Agglomerative ( AGNES ) vs. Divisive ( DIANA ) Agglomerative and divisive clustering on the data set {a, b, c, d ,e } ▪ Cluster distance ▪ Termination conditionStep 0 Step 1 Step 2 Step 3 Step 4 b dc eaa b d ec d ea b c d e Step 4 Step 3 Step 2 Step 1 Step 0Agglomerative Divisive Agglomerative Algorithm •The Agglomerative algorithm is carried out in three steps: 1)Convert all object features into a distance matrix 2)Set each object as a cluster (thus if we have N objects, we will have N clusters at the beginning) 3)Repeat until number of cluster is one (or known # of clusters) ▪Merge two closest clusters ▪Update “distance matrix” Agglomerative Algorithm •Step-1: Create each data point as a single cluster . Let's say there are N data points, so the number of clusters will also be N. Agglomerative Algorithm •Step-2: Take two closest data points or clusters and merge them to form one cluster. So, there will now be N -1 clusters . Agglomerative Algorithm •Step -3: Again, take the two closest clusters and merge them together to form one cluster. There will be N -2 clusters . Agglomerative Algorithm Step -4:Repeat Step 3 until only one cluster left. So, we will get the following clusters . •Step -5:Once all the clusters are combined into one big cluster , develop the dendrogram to divide the clusters as per the problem . single link (min) complete link (max) average Cluster Distance Measures •Single link : smallest distance between an element in one cluster and an element in the other, i.e., d(Ci, Cj) = min{d( xip, xjq)} •Complete link : largest distance between an element in one cluster and an element in the other, i.e., d(Ci, Cj) = max{d( xip, xjq)} •Average : avg distance between elements in one cluster and elements in the other, i.e., d(Ci, Cj) = avg{d( xip, xjq)} d(C, C)=0 Cluster Distance Measures Example : Given a data set of five objects characterised by a single continuous feature, assume that there are two clusters: C 1: {a, b} and C 2: {c, d, e}. 1. Calculate the distance matrix . 2. Calculate three cluster distances between C 1 and C 2. a b c d e Feature 1 2 4 5 6 a b c d e a 01345 b 10234 c32012 d 43101 e 54210Single link Complete link Average 2 4}3, 2, 5, 4, min{3, e)}(b,d),(b,c),(b,e),(a,d),a,(,c)a,( min{)C,C(dist2 1 = == d d d d d d 5 4}3, 2, 5, 4, max{3, e)}(b,d),(b,c),(b,e),(a,d),a,(,c)a,( max{)C, dist(C2 1 = == d d d d d d 5.3621 6432543 6e)(b, d)(b, c)(b, e)(a, d)a,( c)a,()C, dist(C2 1 ==+++++=+++++=d d d d d d The dendrogram in Hierarchical clustering •The dendrogram is a tree-like structure that is mainly used to store each step as a memory that the HC algorithm performs . •In the dendrogram plot, the Y-axis shows the Euclidean distances between the data points, and the x-axis shows all the data points of the given dataset . •Result of hierarchical clustering can be represented as a binary tree: The root of the tree represents the entire collection Terminal nodes represent observations Each interior node represents a cluster Each subtree represents a partition The dendrogram in Hierarchical clustering •Problem: clustering analysis with agglomerative algorithm Example data matrix distance matrixEuclidean distance •Merge two closest clusters (iteration 1) Example •Update distance matrix (iteration 1) Example •Merge two closest clusters (iteration 2) Example •Update distance matrix (iteration 2) Example •Merge two closest clusters/update distance matrix (iteration 3) Example •Merge two closest clusters/update distance matrix (iteration 4) Example •Final result (meeting termination condition) Example •Dendrogram tree representation Key Concepts in Hierarchal Clustering 1.In the beginning we have 6 clusters: A, B, C, D, E and F 2.We merge clusters D and F into cluster (D, F) at distance 0.50 3.We merge cluster A and cluster B into (A, B) at distance 0.71 4.We merge clusters E and (D, F) into ((D, F), E) at distance 1.00 5.We merge clusters ((D, F), E) and C into (((D, F), E), C) at distance 1.41 6.We merge clusters (((D, F), E), C) and (A, B) into ((((D, F), E), C), (A, B)) at distance 2.50 7.The last cluster contain all the objects, thus conclude the computation 23456 object lifetime •Lifetime vs K-cluster Lifetime 23456 object lifetimeKey Concepts in Hierarchal Clustering •Lifetime The distance between that a cluster is created and that it disappears (merges with other clusters during clustering). e.g. lifetime of A, B, C, D, E and F are 0.71, 0.71, 1.41, 0.50, 1.00 and 0.50, respectively, the life time of (A, B) is 2.50 – 0.71 = 1.79, …… •K-cluster Lifetime The distance from that K clusters emerge to that K clusters vanish (due to the reduction to K-1 clusters). e.g. 5-cluster lifetime is 0.71 - 0.50 = 0.21 4-cluster lifetime is 1.00 - 0.71 = 0.29 3-cluster lifetime is 1.41 – 1.00 = 0.41 2-cluster lifetime is 2.50 – 1.41 = 1.09 Relevant Issues •How to determine the number of clusters –If the number of clusters known, termination condition is given! –The K-cluster lifetime as the range of threshold value on the dendrogram tree that leads to the identification of K clusters –Heuristic rule: cut a dendrogram tree with maximum life time to find a “proper” K •Major weakness of agglomerative clustering methods –Can never undo what was done previously –Sensitive to cluster distance measures and noise/outliers –Less efficient: O (n2 logn), where n is the number of total objects •There are several variants to overcome its weaknesses –BIRCH : scalable to a large data set –ROCK : clustering categorical data –CHAMELEON : hierarchical clustering using dynamic modelling

### Related Concepts
- [[Divisive]]
- [[Dendrogram]]
- [[DIANA]]
- [[Clustering Ensemble]]
- [[Hierarchical Clustering]]
- [[AGNES]]
- [[Agglomerative]]
