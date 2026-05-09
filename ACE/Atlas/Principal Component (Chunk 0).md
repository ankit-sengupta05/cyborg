---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T17:36:25.088909'
id: 868151b9
links: []
modified: '2026-05-09T17:36:25.088909'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: Principal Component (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: fad4085aa2ae
source: WINSEM2025-26_CSE3008_ETH_AP2025264000479_2026-01-31_Reference-Material-I.pdf
page: 0
title: Principal Component (Chunk 0)
keywords: ['Principal Component Analysis']
created: 2026-05-09 23:06:25
tree_path: ML > Page 0 > Principal Component
---

Principal Component Analysis (PCA) Principal Component Analysis (PCA) •Principal component analysis (PCA) is a dimensionality reduction and machine learning method used to simplify a large data set into a smaller set while still maintaining significant patterns and trends . •Principal Component Analysis (PCA) is an unsupervised learning algorithm technique used to examine the interrelations among a set of variables . Principal Component Analysis (PCA) Example • Smaller data sets are easier to explore and visualize , and thus make analyzing data points much easier and faster for machine learning algorithms without extraneous variables to process . Principal Component Analysis (PCA) Principal Component Analysis (PCA) Why Do We Need PCA in Machine Learning? •Working with high-dimensional data will cause overfitting issues , and we will use dimensionality reduction to address them . • Increasing interpretability and minimizing information loss. •Aids in locating important characteristics . •Aids in the discovery of a linear combination of varied sequences . When should Principal Component Analysis be used in ML? •Whenever weneed toknow ourfeatures areindependent ofeach other •Whenever weneed fewer features from higher features Basic Terminologies of PCA in Machine Learning? •Variance : For calculating the variation of data distributed across the dimensionality of the graph •Covariance : Calculating dependencies and relationship between features . •Standardizing data: Scaling our dataset within a specific range for unbiased output . •Covariance matrix : Used for calculating interdependencies between the features or variables and also helps in reducing it to improve the performance . •EigenValues and EigenVectors : The eigenvectors aim to find the largest dataset variance to calculate the Principal Component . Eigenvalue means the magnitude of the Eigenvector . The eigenvalue indicates variance in a particular direction, whereas the eigenvector expands or contracts the X-Y (2D) graph without altering the direction . •Dimensionality Reduction : Transpose of original data and multiply it by transposing the derived feature vector . Reducing the features without losing information . Basic Terminologies of PCA in Machine Learning? •Covariance matrix : or How Does PCA Work? The steps involved for PCA in ML 1.Original Data 2.Normalize the original data (mean =0, variance =1) 3.Calculating covariance matrix 4.Calculating Eigen values, Eigen vectors, and normalized Eigenvectors 5.Calculating Principal Component (PC) 6.Plot the graph for orthogonality between PCs Example Consider the dataset Step 1: Calculate Mean: Step 2: Calculation of the covariance matrix: Feature Example 1 Example 2 Example 3 Example 4 X1 4 8 13 7 X2 11 4 5 14 Cov (X1,X2) Example Consider the dataset The covariance matrix is Feature Example 1 Example 2 Example 3 Example 4 X1 4 8 13 7 X2 11 4 5 14 Step 3: Eigenvalues of the covariance matrix: Solving the characteristic equation we get, Example Consider the dataset Feature Example 1 Example 2 Example 3 Example 4 X1 4 8 13 7 X2 11 4 5 14 Step 4: Compute eigenvectors •Tofind thefirst principal components, weneed only compute the eigenvector corresponding tothe largest eigenvalue . where t is any real number. •Taking t = 1, we get an eigenvector corresponding to λ1 as Example Consider the dataset Feature Example 1 Example 2 Example 3 Example 4 X1 4 8 13 7 X2 11 4 5 14 To find a unit eigenvector, we compute the length of λ1which is given by, The unit eigenvector e2 corresponding to the eigenvalue λ= λ2 can be Example Consider the dataset Feature Example 1 Example 2 Example 3 Example 4 X1 4 8 13 7 X2 11 4 5 14 Step 5: Computation of first principal components Let •Be the kth sample in the above Table (dataset) . The first principal component of this example is given by (here “T” denotes the transpose of the matrix) Example Consider the dataset Original Data pointsStep 6: Geometrical meaning of first principal components First, we shift the origin to the “center” and then change the directions of coordinate axes to the directions of the eigenvectors e1 and e2. Example Consider the dataset •The first principal components are the e1 -coordinates of the feet of perpendiculars , that is, the projections on the e1 -axis. •The projections of the data points on the e1-axis may be taken as approximations of the given data points hence we may replace the given data set with these points. Example 2

### Related Concepts
- [[Principal Component Analysis]]
