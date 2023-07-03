## Dimensional Reduction
### 1.PCA
- Methodology
	1. Centralize data (deviation from the mean)
	2. Calculate the Covariance matrix
	3. Eigen decomposition of the covariance matrix to find the eigenvectors and eigenvalues (rank them from large to small)
	4. Select the first corresponding eigenvectors based on the eigenvalues (large to small) to form the projections to principle components
- Kernel PCA
	- works for complex dataset that needs non-linear dimensional reductions
### 2.LDA
- Linear Discriminant Analysis can be used for classification / supervised dimensional reduction
- Intuition:
	- Maximize inter-class distance while minimizing inner class distance
- 