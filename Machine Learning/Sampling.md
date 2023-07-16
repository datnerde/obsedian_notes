# Application in Machine Learning
* Mimic the random events to give a more intuitive understanding
* Use small samples (prior distribution) as a proxy of population's distribution, to describe the randomness of the event as a non-parametric models
* Resampling the existing dataset to get more information through Jack knife / Bootstrap methods to estimate variances etc.
* Mimic some complicated models to get a inference or empirical solutions
# Generate Uniformly distributed random numbers
- Linear Congruential Generator![[Pasted image 20230715132203.png]]
	- initial value $x_0$ is random seed
	- generate $x_{t+1}$ based on existing $x_t$
	- the above range is $[0,m-1]$,  we can divide $x_t$ by $m$ to get the range $[0,1]$
# Some general sampling methods
- ![[Pasted image 20230715180304.png]]
- ![[Pasted image 20230715180312.png]]
- Inverse Transform Sampling![[Pasted image 20230715185021.png]]
- Accept - reject Sampling![[Pasted image 20230715185214.png]]
- Adaptive Rejection Sampling
	- Use several functions to cover the target distribution instead of only one like accept-reject sampling![[Pasted image 20230715185508.png]]
- Importance Sampling![[Pasted image 20230715191913.png]]
# Markov Chain Monte Carlo (MCMC)
- Usage:
	- In high dimensional space, it is hard to find a good proxy distribution to sample, we use MCMC as an alternative
- Idea:
	- 针对待采样的目标分  布，构造一个马尔可夫链，使得该马尔可夫链的平稳分布就是目标分布；然后，  从任何一个初始状态出发，沿着马可夫链进行状态转移，最终得到的状态转移序列会收敛到目标分布，由此可以得到目标分布的一系列样本。
- Metropolis-Hastings Sampling / Gibbs Sampling
# Unbalanced Sample
- Over Sampling and Under Sampling
	- Over sampling may increase model complexity and overfitting
	- Under sampling may lose important information
- SMOTE - Remedy for Over Sampling![[Pasted image 20230715192826.png]]
	- This method could decrease the risk of overfitting
	- However, this method may increase the overlapping between two groups
		- Borderline - SMOTE
			- Only generate new sample for sample near borderline
		- ADASYN
			- Different new sample numbers for different class
- Informed Undersampling - Remedy for Under Sampling
	- Easy Ensemble Method
	- Balance Cascade Method
	- NearMiss / One-sided Selection
- We can also modify the target function / convert the problem to one-class learning & anomaly detection

