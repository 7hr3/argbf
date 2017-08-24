# argbf

Brute force programs that take passwords as arguments.

Mainly useful for CTF's.

root@kali:~# python argbf.py -h

usage: argbf.py [-h] [--wordlist= WORDLIST] [--inc= INC] prog [prog ...]

Brute force passwords as arguments.

positional arguments:
  prog                  A program to bruteforce.

optional arguments:

  -h, --help            show this help message and exit
  
  --wordlist= WORDLIST  Provide a wordlist.
  
  --inc= INC            Provide the answer for an incorrect password.
