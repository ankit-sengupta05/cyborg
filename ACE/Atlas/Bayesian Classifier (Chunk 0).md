---
aliases: []
area: ''
backlinks: []
created: '2026-05-09T17:37:01.659696'
id: ae989cf8
links: []
modified: '2026-05-09T17:37:01.659696'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: Bayesian Classifier (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: dafa2cdb5cfe
source: WINSEM2025-26_CSE3008_ETH_AP2025264000479_2026-03-20_Reference-Material-I.pptx
page: 0
title: Bayesian Classifier (Chunk 0)
keywords: ['Bayesian Classifier', 'Naive Bayes Classifier Algorithm', 'Naive Bayes algorithm', 'Bayesian classifier']
created: 2026-05-09 23:07:01
tree_path: ML > Page 0 > Bayesian Classifier
---

Bayesian Classifier Naïve Bayes Classifier Algorithm Naïve Bayes algorithm is a supervised learning algorithm, which is based on the Bayes theorem and used for solving classification problems. It is mainly used in text classification that includes a high-dimensional training dataset. It is a probabilistic classifier, which means it predicts on the basis of the probability of an object. Bayesian Classifier In many applications, the relationship between the attributes set and the class variable is non-deterministic. In other words, a test cannot be classified to a class label with certainty. In such a situation, the classification can be achieved probabilistically. The Bayesian classifier is an approach for modeling probabilistic relationships between the attribute set and the class variable. More precisely, the Bayesian classifier uses Bayes’ Theorem of Probability for classification. Before going to discuss the Bayesian classifier, we should have a quick look at the Theory of Probability and then Bayes’ Theorem. Recollect Prior and Posterior Probabilities Recollect Prior and Posterior Probabilities Naïve Bayesian Classifier Naïve Bayesian classifier calculates this posterior probability using Bayes’ theorem, which is as follows. Naïve Bayesian Classifier This principle is the basis of Naïve Bayes classification, where we assign a class label based on maximum posterior probability. Bayesian Classifier Solved Problems Naïve Bayesian Classifier Example: Working Steps of Naïve Bayes' Classifier Step 1: Calculate the prior probability for given class labels Step 2: Find the Likelihood probability with each attribute for each class Step 3: Put these values in Bayes Formula and calculate posterior probability. Step 4: See which class has a higher probability, given the input belongs to the higher probability class. Example Cont’d Learning Phase(frequency tables) P(Play=Yes) = 9/14 P(Play=No) = 5/14 Using the table of 14 examples we can calculate our overall probabilities and conditional probabilities. First, we estimated the probability of playing tennis: P(Play Tennis = Yes) = 9/14 = .64 P(Play Tennis = No) = 5/14 = .36 Then we estimate the conditional probabilities of the individual attributes. Remember this is the step in which we are assuming that the attributes are independent of each other: Outlook: P(Outlook = Sunny | Play Tennis = Yes) = 2/9 = .22 P(Outlook = Sunny | Play Tennis = No) = 3/5 = .6 P(Outlook = Overcast | Play Tennis = Yes) = 4/9 = .44 P(Outlook = Overcast | Play Tennis = No) = 0/5 = 0 P(Outlook = Rain | Play Tennis = Yes) = 3/9 = .33 P(Outlook = Rain | Play Tennis = No) = 2/5 = .4 Example Cont’d Example Cont’d Temperature P(Temperature = Hot | Play Tennis = Yes) = 2/9 = .22 P(Temperature = Hot | Play Tennis = No) = 2/5 = .40 P(Temperature = Mild | Play Tennis = Yes) = 4/9 = .44 P(Temperature = Mild | Play Tennis = No) = 2/5 = .40 P(Temperature = Cool | Play Tennis = Yes) = 3/9 = .33 P(Temperature = Cool | Play Tennis = No) = 1/5 = .20 Humidity P(Humidity = Hi | Play Tennis = Yes) = 3/9 = .33 P(Humidity = Hi | Play Tennis = No) = 4/5 = .80 P(Humidity = Normal | Play Tennis = Yes) = 6/9 = .66 P(Humidity = Normal | Play Tennis = No) = 1/5 = .20 Wind P(Wind = Weak | Play Tennis = Yes) = 6/9 = .66 P(Wind = Weak | Play Tennis = No) = 2/5 = .40 P(Wind = Strong | Play Tennis = Yes) = 3/9 = .33 P(Wind = Strong | Play Tennis = No) = 3/5 = .60 Example Cont’d Example Cont’d Car theft Example Data set Attributes are Color , Type , Origin, and the subject, stolen can be either yes or no. We want to classify a Red, Domestic,and SUV There is no example of a Red Domestic SUV in our data set Car theft Example Calculate the probabilities: P(Red|Yes), P(SUV|Yes), P(Domestic|Yes) , P(Red|No) , P(SUV|No), and P(Domestic|No) P(Stolen= Yes) = 5/10 = .5 P(Stolen= No) = 5/10 = .5 The example gets classified as ’NO’ Problem 3- for Naive Bayes Classification Classify from the following Data: Blood Pressure: High Wight: Above average Family History: Yes Age: 50+ Diabetes? Problem 3 Cont’d P(Diabetes=No) = 11/20=0.55 P(Diabetes=Yes) = 9/20 =0.45 Problem 3 Cont’d Classify from the following Data: Blood Pressure: High Wight: Above average Family History: Yes Age: 50+ Diabetes? Similarly, Problem 4 Air-Traffic Data Given this is the knowledge of data and classes, we are to find the most likely classification for any other unseen instance, for example: Problem 4 Cont’d Problem 4 Cont’d Instance: Case1: Class = On Time : 0.70 × 0.64 × 0.14 × 0.29 × 0.07 = 0.0013 Case2: Class = Late : 0.10 × 0.50 × 1.0 × 0.50 × 0.50 = 0.0125 Case3: Class = Very Late : 0.15 × 1.0 × 0.67 × 0.33 × 0.67 = 0.0222 Case4: Class = Cancelled : 0.05 × 0.0 × 0.0 × 1.0 × 1.0 = 0.0000 Case3 is the strongest; Hence correct classification is Very Late Problem 4 Cont’d Naïve Bayesian Classifier Pros and Cons The Naïve Bayes’ approach is a very popular one, which often works well. However, it has a number of potential problems It relies on all attributes being categorical. If the data is less, then it estimates poorly.

### Related Concepts
- [[Bayesian classifier]]
- [[Bayesian Classifier]]
- [[Naive Bayes Classifier Algorithm]]
- [[Naive Bayes algorithm]]
