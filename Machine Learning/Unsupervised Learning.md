# K-mean Clustering
- ## Goal
	- Via iterations, find the combination of K clusters that minimize the cost function. In this case, we can represent the cost function as sum of square distance between point to cluster center of each cluster
	-  ![[Pasted image 20230712211017.png]]
* ## Process
	1. Data Preprocessing(e.g. standardize, normalize, outlier)
	2. Randomly select K cluster![[Pasted image 20230712211452.png]]
	3. Define cost function![[Pasted image 20230712211503.png]]
	4. Let t=0,1,2,... as iteration step, repeat the process until the cost function converges
		* Assign each sample $x_{i}$ to its nearest cluster
		* For each cluster $k$, recalculate the center
	* This is actually EM-Algorithm
* ## Disadvantages
	* Unstable result caused by initialization and outlier
	* Risk in local optimal solution
	* Cannot deal with unbalanced distribution
	* Sample can only be assigned to one group
* ## Advantages
	* Fast and Scalable
* ## Improvement
	* Data Normalisation / Standardization & Outlier 
	* Pick a Good K
		* Elbow Method / Gap Statistic
	* Kernel Trick
# K-means clustering Improved Method
* ## K-means++
	* Randomly pick the first center of a cluster
	* Assuming we have selected n initial cluster centers, when picking the n+1 center, centers that are further away fro from the previous selected centers have higher chances to get selected
	* It improves the drawbacks of initialization of K-means method
* ## ISODATA
	* Remove a group if there are no enough samples belonging to this group
	* Break down a group if there are many samples and dispersion under this group
	* It deals with the case that it is hard to estimate cluster number K when your data is high-dimensional and big. 
--------
# Gaussian Mixed Model
* ## Idea
	* Assuming dataset can be seen as generations from several Gaussian distributions, we estimate the probability of a dataset generated from these distributions.![[Pasted image 20230712213157.png]] You can also consider it as weighted probability of K Gaussian distributions
* ## Process
	1. Given a cluster number K
	2. Estimate the best Gaussian Mixed probability using EM algorithm
		1. E step: Given the current parameters, calculate probability of each point
		2. M step: Using the probability generated from E step, improve the parameters of Gaussian Mixed distributions
	3. When converging, we have our optimal models
# Comparison
- Both are clustering method
- Both need to specify K cluster number
- Both use EM algorithm to get the optimal model
- Both have the risk to converge in local optimal solution
- Gaussian Mixed Model can 
	- predict the probability of a sample belonging to a cluster
	- generate new samples
# Self-Organizing Map (SOM)
* ## Goal:
	* Can be used for clustering, visualizing high-dimensional data, data compression, and feature extractions
* ...
-------
# Evaluation of Clustering Methods
* 