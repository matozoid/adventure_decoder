import sys

input_file = sys.argv[1]
file1_b = bytearray(open(input_file, 'rb').read())

size = len(file1_b)
xord_byte_array = bytearray(size)

for i in range(size):
    xord_byte_array[i] = file1_b[i] ^ 0xff

output_file = input_file + '.decoded'
open(output_file, 'wb').write(xord_byte_array)

print("[*] %s XOR $FF\n[*] Saved to %s." % (input_file, output_file))
