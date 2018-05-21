=====================
ICGR Encoder/Decoder
=====================
Integer chaos game representation encoder/decoder in python. 

Based on: `Encoding DNA sequences by integer chaos game representation <https://arxiv.org/pdf/1712.04546.pdf>`_ by `Changchuan Yin <https://www.math.uic.edu/people/profile?netid=cyin1>`_.


Usage
-----
The script contains three main arguments.

1. -e / --encode (For encoding fasta sequence to icgr file)

```
-e 'fasta file path' # or --encode 'fasta file path'
```

2. -d / --decode (For decoding icgr data to fasta file)

```
-d 'icgr file path' # or --decode 'icgr file path'
```

3. -q / --quiet  (Anti-verbose mode will not print validity checks)


For example, to encode the fasta file with accession number: **M57671.1** found in the **test** folder. 

```
python icgr.py -e test/seq.fasta  
```
and with quiet mode: 

```
python icgr.py -e test/seq.fasta -q  
```
