## Classic Model

### 1. Support Vector Machine[[Supervised Learning]]
- Where it comes from:![[Pasted image 20230702170546.png]]
- Soft Margin help with the sensitivity of support vectors
- Intuition:
	- Project low dimensional data to high dimensional space so that they can be separates into two groups by a support vector classifier
- Kernel function:
	- Systematically projections to higher dimensional space
	- Radial Kernel (RBF)
	- Polynomial Kernel
	- Kernel Trick:
		- Calculate the relationships between every pair of points as if they are in the higher dimension instead of doing the transformation
### 2.Logistics Regression[[Supervised Learning]]
- Comparison against linear regression
	- Binary v.s. regression
	- Logistics regression can be considered as regression model of log(odd) of event $y = \frac{1}{x}$ , with $odd = \frac{p}{1-p}$ 
	- Continus y v.s. discontinus y
	- Both can use Maximum likelihood estimation to estimate $\beta$ 
- Multiple Labels
	- If one sample only has one label
		- Softmax Regression
	- If one sample can have multiple label
		- Train k binary classifier, where i classifier is to classify if a sample belongs to class i or not.
### 3.Decision Tree[[Supervised Learning]]
- Comparison of different decision tree methods:
	- ![[Pasted image 20230702173806.png]]
- Pruning
	- Pre-pruning
		- Stop tree growth with certain depth
		- Stop tree growth with certain sample size
		- Stop tree growth with certain model improvement
	- Post pruning
		- REP, PEP, CVP, OPP
		- Cost Complexity Pruning