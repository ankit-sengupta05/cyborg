---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T17:36:03.150802'
id: 6124a272
links: []
modified: '2026-05-09T17:36:03.150802'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: Gradient-Based Optimization (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: 9f407670568e
source: WINSEM2025-26_CSE3008_ETH_AP2025264000479_2025-12-20_Reference-Material-I.pptx
page: 0
title: Gradient-Based Optimization (Chunk 0)
keywords: ['Gradient-Based Optimization', 'Optimization', 'Minimizing f(x)', 'Maximizing f(x)', 'Objective Function', 'Cost Function', 'Loss Function', 'Error Function', 'Convex Optimization', 'Linear Programming Problem', 'Convex Function', 'Machine Learning Models', 'Neural Networks']
created: 2026-05-09 23:06:03
tree_path: ML > Page 0 > Gradient-Based Optimization
---

Gradient-Based Optimization Gradient-Based Optimization Optimization refers to the task of either minimizing or maximizing some function f(x) by altering x. Optimization problems in terms of minimizing f (x) could be done. Maximization may be accomplished via a minimization algorithm by minimizing −f (x) The function we want to minimize or maximize is called the objective function or criterion. When we are minimizing it, we may also call it the cost function, loss function, or error function Value that minimizes or maximizes a function is denoted with a superscript for example, we might say x∗ = arg min f (x) Convex Optimization Convex optimization is a powerful tool for solving optimization problems in various fields such as finance, engineering, and machine learning. In a convex optimization problem, the goal is to find a point that maximizes or minimizes the objective function. Linear functions are convex, so linear programming problems are convex problems. A convex function is a function whose graph is always curved upwards, which means that the line segment connecting any two points on the graph is always above or on the graph itself. Convex optimization is critical in training machine learning models, which involves finding the optimal parameters that minimize a given loss function. In machine learning, convex optimization is used to solve many problems such as linear regression, logistic regression, support vector machines, and neural networks. Gradient Descent Gradient Descent is known as one of the most commonly used optimization algorithms to train machine learning models. Gradient descent is also used to train Neural Networks. It minimizes errors between actual and expected results. Gradient Descent Cont’d Gradient Descent Cont’d The Formula of the Gradient Descent Algorithm: Gradients are nothing but a vector whose entries are partial derivatives of a function. Different Types of Gradient Descent Algorithms Batch gradient descent: When the weight update is calculated based on all examples in the training dataset, it is called batch gradient descent. Stochastic gradient descent: When the weight update is calculated incrementally after each training example or a small group of training examples, it is called as stochastic gradient descent. Mini-batch gradient descent is a gradient descent modification that divides the training dataset into small batches that are used to compute model error and update model coefficients. Limitations For a good generalization we should have a large training set, which comes with a huge computational cost. i.e., as the training set grows to billions of examples, the time taken to take a single gradient step becomes long. Choosing Gradient Descent ? Batch Gradient Descent In batch gradient descent, we use all our training data in a single iteration of the algorithm. So, we first pass all the training data through the network and compute the gradient of the loss function for each sample. Then, we take the average of the gradients and update the parameters using the computed average. Batch Gradient Descent Cont’d Stochastic Gradient Descent SGD is a variant of the optimization algorithm that saves us both time and computing space while still looking for the best optimal solution Stochastic gradient descent is a variant of gradient descent. The process simply takes one random stochastic gradient descent example, iterates, then improves before moving to the next random example. However, because it takes and iterates one example at a time, it tends to result in more noise than we would normally like. Stochastic Gradient Descent Mini-Batch Descent Instead of going through the complete dataset or choosing one random parameter, Mini-batch gradient descent divides the entire dataset into randomly picked batches and optimizes it. The mini-batch is a fixed number of training examples that is less than the actual dataset. So, in each iteration, we train the network on a different group of samples until all samples of the dataset are used. Mini Batch Gradient Issue with GD is accidently getting stuck in local minima, where our loss can still be HUGE Global Minimum In the case of the linear regression model, there is only one minimum and it is the global minimum The local minimum reached depends on the initial coefficients taken into consideration. Here, point A, B are termed Local Minimum and point C is Global Minimum.

### Related Concepts
- [[Convex Optimization]]
- [[Optimization]]
- [[Convex Function]]
- [[Loss Function]]
- [[Error Function]]
- [[Machine Learning Models]]
- [[Objective Function]]
- [[Cost Function]]
- [[Linear Programming Problem]]
- [[Maximizing f(x)]]
- [[Minimizing f(x)]]
- [[Neural Networks]]
- [[Gradient-Based Optimization]]
