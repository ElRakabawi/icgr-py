# icgr-py
Integer chaos game representation in python. <br/>
Based on: [Encoding DNA sequences by integer chaos game
representation](https://arxiv.org/pdf/1712.04546.pdf) by [Changchuan Yin](https://www.math.uic.edu/people/profile?netid=cyin1).

Equation (1): 
* p1,x = α1,x
* p1,y = α1,y
* α1 = S(1), α1 ∈ {A, T, C, G}


Encryption Algorithm: <br/>
1. Get the nucleotide αn at position n from (n, X, Y ) based on
Equation (1).
2. Compute the x-coordinate at position i − 1 from that at
position i: pi−1,x = pi,x − 2
i−1αi,x.
3. Compute the y-coordinate at position i − 1 from that at
position i: pi−1,y = pi,y − 2
i−1αi,y.
4. Get the nucleotide αi−1 at position i − 1 from pi−1,x, pi−1,y
based on equation (3).
5. Repeat steps 2, 3 and 4 until i = 1.
6. Return the decoded nucleotide sequence of length n.
7. 

Decryption Algorithm: <br/>
1. Get the nucleotide αn at position n from (n, X, Y ) based on
Equation (3).
2. Compute the x-coordinate at position i − 1 from that at
position i: pi−1,x = pi,x − 2
i−1αi,x.
3. Compute the y-coordinate at position i − 1 from that at
position i: pi−1,y = pi,y − 2
i−1αi,y.
4. Get the nucleotide αi−1 at position i − 1 from pi−1,x, pi−1,y
based on equation (3).
5. Repeat steps 2, 3 and 4 until i = 1.
6. Return the decoded nucleotide sequence of length n.