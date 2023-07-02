## Classic Model

### 1. Support Vector Machine
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
### 2.Logistics Regression
- Comparison against linear regression
	- Binary v.s. regression
	- Logistics regression can be considered as regression model of log(odd) of event $y = \frac{1}{x}$ , with $odd = \frac{p}{1-p}$ 
	- Continus y v.s. discontinus y
	- Both can use Maximum likelihood estimation to estimate $\beta$ 
- Multiple Labels
	- Softmax Regression
		- 