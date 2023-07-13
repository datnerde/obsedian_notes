# K-mean Clustering
- Goal
	- Via iterations, find the combination of K clusters that minimize the cost function. In this case, we can represent the cost function as sum of square distance between point to cluster center of each cluster
	-  ![[Pasted image 20230712211017.png]]
* Process
	1. Data Preprocessing(e.g. standardize, normalize, outlier)
	2. Randomly select K cluster![[Pasted image 20230712211452.png]]
	3. Define cost function![[Pasted image 20230712211503.png]]
	4. Let t=0,1,2,... as iteration step, repeat the process until the cost function converges
		* Assign each sample $x_{i}$ to its nearest cluster
		* For each cluster $k$, recalculate the center
	* 