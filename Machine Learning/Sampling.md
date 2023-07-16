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
- 