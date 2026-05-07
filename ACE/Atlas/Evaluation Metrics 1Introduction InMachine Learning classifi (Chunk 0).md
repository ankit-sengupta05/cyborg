---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:41:33.983755'
id: d3f45d77
links: []
modified: '2026-05-07T20:41:33.983755'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: Evaluation Metrics 1Introduction InMachine Learning classifi (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: 6030ee9ffb54
source: WINSEM2025-26_CSE3008_ETH_AP2025264000479_2026-03-11_Reference-Material-II.pdf
page: 0
title: Evaluation Metrics 1Introduction InMachine Learning classifi (Chunk 0)
keywords: ['Precision', 'Recall', 'F1-score', 'ROC analysis', 'Confusion matrix', 'True Positive (TP)', 'False Negative (FN)', 'False Positive (FP)', 'Precision', 'Recall']
created: 2026-05-08 02:11:33
tree_path: ML > Page 0 > Evaluation Metrics 1Introduction InMachine Learnin
---

Evaluation Metrics 1Introduction InMachine Learning classification problems, theperformance ofamodel isevaluated using several metrics such asPrecision, Recall, F1-score andROC analysis. These metrics arederived from theconfusion matrix. 2Class Evaluation Measures F o rabinary classification problem, theconfusion matrix consists of: •True Positive (TP) •True Negative (TN) •False Positive (FP) •False Negative (FN) 3Confusion Matrix andClass Evaluation Terms Inbinary classification, thepredicted class canbePositive orNegative, andtheactual class canalsobePositive orNegative. Theconfusion matrix isused toevaluate classifi- cation performance. 3.1 Confusion Matrix Actual /Predicted Positive Negative Positive True Positive (TP) False Negative (FN) Negative False Positive (FP) True Negative (TN) 3.2 True Positive (TP) True Positive isthenumber ofpositive instances correctly classified aspositive. Example: Apatient hasadisease andthemodel predicts disease. 3.3 True Negative (TN) True Negative isthenumber ofnegative instances correctly classified asnegative. Example: Ahealthy patient iscorrectly predicted ashealthy. 1 3.4 False Positive (FP) False Positive is the number of negative instances incorrectly classified as positive. This is also called a Type I error. Example:A healthy patient is incorrectly predicted as having a disease. 3.5 False Negative (FN) False Negative is the number of positive instances incorrectly classified as negative. This is also called a Type II error. Example:A patient with disease is incorrectly predicted as healthy. 3.6 Importance of Confusion Matrix Terms These values are used to compute evaluation metrics such as Accuracy, Precision, Recall, F1-score, and ROC curve. 3.7 Performance Metrics Accuracy=TP+TN TP+TN+FP+FN Precision=TP TP+FP Recall=TP TP+FN F1-score = 2·Precision·Recall Precision+Recall 4 ROC Curve The Receiver Operating Characteristic (ROC) curve plots: •True Positive Rate (TPR) on Y-axis •False Positive Rate (FPR) on X-axis TPR=TP TP+FN, FPR=FP FP+TN The Area Under Curve (AUC) measures classifier performance. A higher AUC indi- cates a better model. 2 5 Confusion Matrix Predicted Positive Predicted Negative Actual Positive True Positive (TP) False Negative (FN) Actual Negative False Positive (FP) True Negative (TN) TP: Correctly predicted positive instances TN: Correctly predicted negative instances FP: Incorrectly predicted positive instances FN: Incorrectly predicted negative instances 6 Precision Precision measures how many of the predicted positive instances are actually positive. Precision=TP TP+FP Example: IfTP= 40 andFP= 10 Precision=40 40 + 10=40 50= 0.8 7 Recall (Sensitivity) Recall measures how many of the actual positive instances are correctly identified. Recall=TP TP+FN Example: IfTP= 40 andFN= 20 Recall=40 40 + 20=40 60= 0.67 8 F1 Score F1 score is the harmonic mean of Precision and Recall. F1 =2×Precision×Recall Precision+Recall Example: If Precision = 0.8 and Recall = 0.67 F1 =2×0.8×0.67 0.8 + 0.67 F1 = 0.73 3 9 ROC Curve (Receiver Operating Characteristic) ROC curve is a graphical representation used to evaluate classification models. 9.1 True Positive Rate (TPR) TPR=TP TP+FN 9.2 False Positive Rate (FPR) FPR=FP FP+TN In the ROC curve: •X-axis represents False Positive Rate (FPR) •Y-axis represents True Positive Rate (TPR) 10 Interpretation of AUC AUC (Area Under Curve) represents the performance of the model. AUC Value Model Performance 0.9 – 1.0 Excellent 0.8 – 0.9 Good 0.7 – 0.8 Fair 0.5 Random Model 11 Example Problem Given the following confusion matrix: Predicted Yes Predicted No Actual Yes 30 10 Actual No 5 55 Find Precision, Recall and F1 Score. Solution Precision=30 30 + 5= 0.857 Recall=30 30 + 10= 0.75 F1 =2×0.857×0.75 0.857 + 0.75= 0.799 4 Exercise Consider the following confusion matrix obtained from a binary classification model. Predicted Positive Predicted Negative Actual Positive 45 15 Actual Negative 10 30 Calculate the following evaluation metrics: 1. Precision 2. Recall 3. F1-score 4. True Positive Rate (TPR) 5. False Positive Rate (FPR) 5

### Related Concepts
- [[True Positive (TP)]]
- [[False Positive (FP)]]
- [[ROC analysis]]
- [[Confusion matrix]]
- [[Recall]]
- [[F1-score]]
- [[False Negative (FN)]]
- [[Precision]]
