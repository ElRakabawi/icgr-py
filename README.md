# ICGR Encoder/Decoder
#### Integer chaos game representation encoder/decoder in python. <br/>
Based on: [Encoding DNA sequences by integer chaos game
representation](https://arxiv.org/pdf/1712.04546.pdf) by [Changchuan Yin](https://www.math.uic.edu/people/profile?netid=cyin1).

## Use
The script contains three main arguments.
* -e / --encode (For encoding fasta sequence to icgr file)
 ```sh
python icgr.py -e 'fasta file path' 
```
* -d / --decode (For decoding icgr data to fasta file)
 ```sh
python icgr.py -d 'icgr file path' 
```
* -q / --quiet  (Anti-verbose mode will not print validity checks)


for example, to encode the fasta file with accession number: **M57671.1** found in the **test** folder. 
```sh
python icgr.py -e test/seq.fasta  
```
and with quiet mode: 

```sh
python icgr.py -e test/seq.fasta -q  
```
<br />

## Algorithm
Equation (1): 
* p1,x = α1,x
* p1,y = α1,y
* α1 = S(1), α1 ∈ {A, T, C, G}


#### Encryption Algorithm: <br/>
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

#### Decryption Algorithm: <br/>
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