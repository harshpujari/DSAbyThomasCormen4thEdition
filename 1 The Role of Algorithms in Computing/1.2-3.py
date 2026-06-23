"""
We want the smallest integer $n$ such that

$100n^2 < 2^n$.

This means the quadratic-time algorithm is faster than the exponential-time algorithm.

Step 1: Test small values of $n$

- $n = 1$: $100(1)^2 = 100$, $2^1 = 2$  -> not true
- $n = 2$: $100(2)^2 = 400$, $2^2 = 4$  -> not true
- $n = 3$: $100(3)^2 = 900$, $2^3 = 8$  -> not true
- $n = 4$: $100(4)^2 = 1600$, $2^4 = 16$  -> not true
- $n = 5$: $100(5)^2 = 2500$, $2^5 = 32$  -> not true
- $n = 6$: $100(6)^2 = 3600$, $2^6 = 64$  -> not true
- $n = 7$: $100(7)^2 = 4900$, $2^7 = 128$  -> not true
- $n = 8$: $100(8)^2 = 6400$, $2^8 = 256$  -> not true
- $n = 9$: $100(9)^2 = 8100$, $2^9 = 512$  -> not true
- $n = 10$: $100(10)^2 = 10000$, $2^{10} = 1024$  -> not true
- $n = 11$: $100(11)^2 = 12100$, $2^{11} = 2048$  -> not true
- $n = 12$: $100(12)^2 = 14400$, $2^{12} = 4096$  -> not true
- $n = 13$: $100(13)^2 = 16900$, $2^{13} = 8192$  -> not true
- $n = 14$: $100(14)^2 = 19600$, $2^{14} = 16384$  -> not true
- $n = 15$: $100(15)^2 = 22500$, $2^{15} = 32768$  -> not true
- $n = 16$: $100(16)^2 = 25600$, $2^{16} = 65536$  -> not true
- $n = 17$: $100(17)^2 = 28900$, $2^{17} = 131072$  -> true

So the smallest value of $n$ is

$\boxed{17}$.

Explanation:
The algorithm with running time $100n^2$ grows quadratically, while the one with running time $2^n$ grows exponentially.
Exponential growth eventually becomes much larger than quadratic growth, so the quadratic algorithm becomes faster only for sufficiently large $n$.
Here, that crossover happens at $n = 17$.
"""
