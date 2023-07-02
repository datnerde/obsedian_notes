## Model Evaluation

### 1.Limitation Of Metrics

- Accuracy
	- Cannot deal with unbalanced sample
	- We can use accuracy under each category
	- Accuracy = (TP + TN) / Total
- Recall & Precision
	- Precision = TP / (TP + FP)
	- Recall = TP / (TP + FN)
	- P-R (Precision-Recall) curve  
	![[Pasted image 20230630094036.png]]
	- F1 = (2 x precision x recall) / (precision + recall)
	- ROC/lin
- RMSE  
	![[Pasted image 20230630094116.png]]
	- Doesn't work well with outlier
		- If the outlier is noise, we shall remove it in data prep
		- If the outlier is not noise, we shall create better model to account for it
		- Map (Mean Absolute Percent Error)
			- ![[Pasted image 20230630094130.png]]

### 2.ROC Curve

- ROC = Receiver Operating Characteristic Curve
	- FPR = FP / N
	- TPR = TP / P = Recall  
	![[Pasted image 20230630094319.png]]
- AUC (Area Under Curve)
	- Range [0.5, 1]
	- The larger the better
- ROC will keep its shape when the balance of samples changes, compared to P-R curve

### 3.Cosine Distance
- Use case of distance measurement
	- Euclidean Distance focuses on difference in magnitude
	- Cosine Distance reflects difference directionally
### 4.A/B Testing
- Reasons for online A/B Testing
	- Offline testing doesn't remove the impact of overfitting
	- Offline testing doesn't mimic the condition of online engineering environment
	- Some metrics can only be calculated online
- How to conduct online A/B Testing: refer to  [[AB Testing]]
### 5. Model Evaluation
- Holdout
- Cross validation
	- k-fold
	- leave-one-out
- Bootstrap
	- when sample size is too small for data split
	- for sample size n, sampling data n times with repetition; data not sampled from n times will be used as validation set
	- when $n->\infty$, around $\frac{1}{e}$ = 36.8% samples don't get picked
### 6. Hyper-parameter tuning
- grid search
- random search
- bayesian optimization:[贝叶斯优化算法](https://www.cnblogs.com/marsggbo/p/9866764.html)
	- 具体来说，它学习目标函数形状的方法是，首先根据先验分布，假设一个搜集函数；然后，每一次使用新的采样点来测试目标函数时，利用这个信息来更新目标函数的先验分布；最后，算法测试由后验分布给出的全局最值最可能出现的位置的点。
### 7.Overfitting & Underfitting
- Overfitting: Perform well in training set but not prediction set
	- Get more data
	- Reduce model complexity
	- Regularization
	- Ensemble learning
- Underfitting: Perform bad in both training set and prediction set
	- Add new features
	- Add model complexity
	- Reduce regularization

#model_evaluation #distance_measure 
