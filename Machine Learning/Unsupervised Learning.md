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
	* 