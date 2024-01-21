Some old text adventures "encrypt" all their text with "XOR $FF" encryption.

The xor.py tool xor's every byte in the input file and write the result to inputfile ".decoded".

The result can be inspected in an editor that doesn't mind a lot of garbage bytes.

Run it on the sample:
`python xor.py prisoner.bin` or 
`python3 xor.py prisoner.bin` or whatever.
I'm not a Python expert.